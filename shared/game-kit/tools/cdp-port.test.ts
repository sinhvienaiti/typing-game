import { join } from "node:path";
import { describe, expect, it, vi } from "vitest";
// @ts-expect-error The JavaScript CLI helper is outside the TypeScript build.
import { portArg, readActivePort } from "./cdp-port.mjs";

const profile = join("profiles", "isolated-run");
const activeFile = join(profile, "DevToolsActivePort");
const missing = () => Object.assign(new Error("Missing file"), { code: "ENOENT" });
const clock = () => {
  let time = 0;
  return {
    now: () => time,
    sleep: vi.fn(async (ms: number) => { time += ms; }),
  };
};

describe("portArg", () => {
  it("lets Chrome allocate a port when CDP_PORT is absent", () => {
    expect(portArg({})).toEqual({ arg: "--remote-debugging-port=0", fixed: null });
  });

  it("treats an empty CDP_PORT as absent", () => {
    expect(portArg({ CDP_PORT: "" })).toEqual({ arg: "--remote-debugging-port=0", fixed: null });
  });

  it.each([1024, 9555, 65535])("uses the explicit port %i", (port) => {
    expect(portArg({ CDP_PORT: String(port) })).toEqual({
      arg: `--remote-debugging-port=${port}`, fixed: port,
    });
  });

  it.each(["abc", "80", "0", "1023", "65536", "-9555", "9555.5", "9e3", "0x2553", " "])(
    "rejects CDP_PORT=%s and includes the value", (value) => {
      expect(() => portArg({ CDP_PORT: value })).toThrow(value);
    },
  );
});

describe("readActivePort", () => {
  it("reads the first line from the profile's DevToolsActivePort", async () => {
    const readFile = vi.fn(async () => "9222\n/devtools/browser/abc");
    const timer = clock();
    await expect(readActivePort(profile, { readFile, ...timer })).resolves.toBe(9222);
    expect(readFile).toHaveBeenCalledExactlyOnceWith(activeFile, "utf8");
    expect(timer.sleep).not.toHaveBeenCalled();
  });

  it("retries two missing reads and sleeps exactly twice", async () => {
    const readFile = vi.fn()
      .mockRejectedValueOnce(missing())
      .mockRejectedValueOnce(missing())
      .mockResolvedValue("9555\n/devtools/browser/xyz");
    const timer = clock();
    await expect(readActivePort(profile, { readFile, ...timer })).resolves.toBe(9555);
    expect(readFile).toHaveBeenCalledTimes(3);
    expect(timer.sleep.mock.calls).toEqual([[50], [50]]);
    expect(timer.now()).toBe(100);
  });

  it("times out with the file path using only the fake clock", async () => {
    const readFile = vi.fn().mockRejectedValue(missing());
    const timer = clock();
    await expect(readActivePort(profile, {
      timeoutMs: 100, pollMs: 40, readFile, ...timer,
    })).rejects.toThrow(activeFile);
    expect(readFile).toHaveBeenCalledTimes(4);
    expect(timer.sleep.mock.calls).toEqual([[40], [40], [20]]);
    expect(timer.now()).toBe(100);
  });

  it.each(["abc", "0", "70000", "", "9222.5", "9e3"])(
    "rejects invalid first line %j immediately", async (line) => {
      const readFile = vi.fn(async () => `${line}\n/devtools/browser/abc`);
      const timer = clock();
      await expect(readActivePort(profile, { readFile, ...timer })).rejects.toThrow(activeFile);
      expect(readFile).toHaveBeenCalledTimes(1);
      expect(timer.sleep).not.toHaveBeenCalled();
    },
  );

  it.each([1, 65535])("accepts the active-port boundary %i with CRLF", async (port) => {
    await expect(readActivePort(profile, {
      readFile: async () => `${port}\r\n/devtools/browser/abc`, ...clock(),
    })).resolves.toBe(port);
  });

  it("propagates read failures other than a missing file", async () => {
    const error = Object.assign(new Error("Access denied"), { code: "EACCES" });
    const timer = clock();
    await expect(readActivePort(profile, {
      readFile: async () => { throw error; }, ...timer,
    })).rejects.toBe(error);
    expect(timer.sleep).not.toHaveBeenCalled();
  });
});
