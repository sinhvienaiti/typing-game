import test from "node:test";
import assert from "node:assert/strict";
import { evaluateEnglishAnswer, normalizeEnglishForGrading } from "./grading.mjs";

test("accepts second and third reviewed acceptedAnswers and safe contraction equivalents", () => {
  const item = {
    answerText: "I cannot go tomorrow.",
    acceptedAnswers: [
      "I cannot go tomorrow.",
      "I will not be able to go tomorrow.",
      "Tomorrow I cannot go.",
    ],
    gradingMode: "exact-normalized",
  };

  const r1 = evaluateEnglishAnswer(item, "I can't go tomorrow");
  assert.equal(r1.outcome, "correct");
  assert.equal(r1.matchedAnswer, "I cannot go tomorrow.");

  const r2 = evaluateEnglishAnswer(item, "i won't be able to go tomorrow.");
  assert.equal(r2.outcome, "correct");
  assert.equal(r2.matchedAnswer, "I will not be able to go tomorrow.");

  const r3 = evaluateEnglishAnswer(item, "  tomorrow i can't go! ");
  assert.equal(r3.outcome, "correct");
  assert.equal(r3.matchedAnswer, "Tomorrow I cannot go.");
});

test("enforces punctuation and capitalization when normalization flags require exactness", () => {
  const item = {
    answerText: "Are they leaving?",
    acceptedAnswers: ["Are they leaving?"],
    normalization: { caseSensitive: true, punctuationOptional: false },
  };

  assert.equal(evaluateEnglishAnswer(item, "Are they leaving?").outcome, "correct");

  const wrongPunct = evaluateEnglishAnswer(item, "Are they leaving.");
  assert.equal(wrongPunct.outcome, "incorrect");
  assert.equal(wrongPunct.reasonCode, "punctuation-mismatch");

  const wrongCase = evaluateEnglishAnswer(item, "are they leaving?");
  assert.equal(wrongCase.outcome, "incorrect");
  assert.equal(wrongCase.reasonCode, "capitalization-mismatch");
});

test("distinguishes less-suitable-context from arbitrary mismatch and keeps ungradable guided answers as needs-review", () => {
  const contextual = {
    answerText: "Could you resend the invoice?",
    acceptedAnswers: ["Could you resend the invoice?"],
    lessSuitableAlternatives: [
      { text: "Send me the bill now.", noteVi: "Câu đúng ngữ pháp nhưng quá cộc lốc trong ngữ cảnh công việc." },
    ],
    gradingMode: "exact-normalized",
  };
  const unfit = evaluateEnglishAnswer(contextual, "send me the bill now");
  assert.equal(unfit.outcome, "incorrect");
  assert.equal(unfit.reasonCode, "less-suitable-context");
  assert.match(unfit.note, /ngữ cảnh công việc/);

  const openPrompt = {
    answerText: "I'd appreciate it if you could double-check the report.",
    acceptedAnswers: ["I'd appreciate it if you could double-check the report."],
    gradingMode: "guided-self-check",
  };
  const openRes = evaluateEnglishAnswer(openPrompt, "Please verify the figures again when you have a moment.");
  assert.equal(openRes.outcome, "needs-review");
  assert.equal(openRes.autoGradable, false);
});

test("normalizeEnglishForGrading avoids conflating its vs it's incorrectly", () => {
  assert.notEqual(
    normalizeEnglishForGrading("Its color is blue."),
    normalizeEnglishForGrading("It's blue."),
  );
});
