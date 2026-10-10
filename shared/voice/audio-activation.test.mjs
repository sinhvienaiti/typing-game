import test from "node:test";
import assert from "node:assert/strict";
import { resumeVoiceAudio } from "../../portal/src/voice/audio-activation.mjs";

test("running capture resumes without leaving a preparation timeout", async (t) => {
  t.mock.timers.enable({ apis: ["setTimeout"] });
  let resumes = 0;
  const audio = {
    state: "suspended",
    resume() {
      resumes++;
      this.state = "running";
      return Promise.resolve();
    },
  };
  await resumeVoiceAudio(audio);
  t.mock.timers.tick(10000);
  assert.equal(resumes, 1);
});
test("a browser-blocked resume fails within ten seconds instead of waiting for the game watchdog", async (t) => {
  t.mock.timers.enable({ apis: ["setTimeout"] });
  let release;
  const audio = {
    state: "suspended",
    resume: () =>
      new Promise((resolve) => {
        release = resolve;
      }),
  };
  const outcome = assert.rejects(
    resumeVoiceAudio(audio),
    /Browser audio capture did not start/,
  );
  t.mock.timers.tick(10000);
  await outcome;
  audio.state = "running";
  release();
  await Promise.resolve();
});
test("a resolved resume with suspended audio cannot authorize microphone readiness", async () => {
  await assert.rejects(
    resumeVoiceAudio({ state: "suspended", resume: async () => {} }),
    /capture is suspended/,
  );
});
test("stop aborts blocked activation immediately and ignores a late resume", async (t) => {
  t.mock.timers.enable({ apis: ["setTimeout"] });
  const controller = new AbortController();
  let release;
  const audio = {
    state: "suspended",
    resume: () =>
      new Promise((resolve) => {
        release = resolve;
      }),
  };
  const outcome = assert.rejects(resumeVoiceAudio(audio, controller.signal), {
    name: "AbortError",
  });
  controller.abort();
  await outcome;
  t.mock.timers.tick(10000);
  audio.state = "running";
  release();
});
test("an already cancelled preparation never calls AudioContext.resume", async () => {
  const controller = new AbortController();
  controller.abort();
  let called = false;
  await assert.rejects(
    resumeVoiceAudio(
      {
        resume() {
          called = true;
        },
      },
      controller.signal,
    ),
    { name: "AbortError" },
  );
  assert.equal(called, false);
});
test("native resume rejection or synchronous exception is preserved", async () => {
  const error = new Error("Audio device unavailable");
  for (const resume of [
    () => Promise.reject(error),
    () => {
      throw error;
    },
  ])
    await assert.rejects(
      resumeVoiceAudio({ state: "suspended", resume }),
      (value) => value === error,
    );
});
