export const GRADING_MODES = Object.freeze([
  "exact-normalized",
  "closed-choice",
  "guided-self-check",
]);

const CONTRACTION_EXPANSIONS = Object.freeze([
  [/\bcan't\b/gi, "cannot"],
  [/\bwon't\b/gi, "will not"],
  [/\bshan't\b/gi, "shall not"],
  [/\bdon't\b/gi, "do not"],
  [/\bdoesn't\b/gi, "does not"],
  [/\bdidn't\b/gi, "did not"],
  [/\bisn't\b/gi, "is not"],
  [/\baren't\b/gi, "are not"],
  [/\bwasn't\b/gi, "was not"],
  [/\bweren't\b/gi, "were not"],
  [/\bhaven't\b/gi, "have not"],
  [/\bhasn't\b/gi, "has not"],
  [/\bhadn't\b/gi, "had not"],
  [/\bcouldn't\b/gi, "could not"],
  [/\bshouldn't\b/gi, "should not"],
  [/\bwouldn't\b/gi, "would not"],
  [/\bmustn't\b/gi, "must not"],
  [/\bi'm\b/gi, "i am"],
  [/\byou're\b/gi, "you are"],
  [/\bwe're\b/gi, "we are"],
  [/\bthey're\b/gi, "they are"],
  [/\bi've\b/gi, "i have"],
  [/\byou've\b/gi, "you have"],
  [/\bwe've\b/gi, "we have"],
  [/\bthey've\b/gi, "they have"],
  [/\bi'll\b/gi, "i will"],
  [/\byou'll\b/gi, "you will"],
  [/\bhe'll\b/gi, "he will"],
  [/\bshe'll\b/gi, "she will"],
  [/\bit'll\b/gi, "it will"],
  [/\bwe'll\b/gi, "we will"],
  [/\bthey'll\b/gi, "they will"],
]);

function normalizeTypography(value) {
  return String(value ?? "")
    .normalize("NFC")
    .replace(/[\u2018\u2019]/g, "'")
    .replace(/[\u201C\u201D]/g, '"')
    .trim()
    .replace(/\s+/g, " ")
    .replace(/\s+([,.;:!?])/g, "$1");
}

function expandMeaningPreservingContractions(value) {
  let out = value;
  for (const [pattern, replacement] of CONTRACTION_EXPANSIONS) {
    out = out.replace(pattern, replacement);
  }
  return out;
}

export function normalizeEnglishForGrading(value, options = {}) {
  let text = normalizeTypography(value);
  if (text === "") return "";
  if (options.caseSensitive !== true) {
    text = text.toLocaleLowerCase("en-US");
  }
  if (options.contractionsEquivalent !== false) {
    text = expandMeaningPreservingContractions(text);
  }
  if (options.punctuationOptional !== false) {
    text = text.replace(/[.!?]+$/u, "").trim();
  }
  return text.replace(/\s+/g, " ");
}

function acceptedList(spec) {
  const raw = [];
  if (Array.isArray(spec?.acceptedAnswers)) {
    for (const candidate of spec.acceptedAnswers) {
      if (typeof candidate === "string" && candidate.trim() !== "") {
        raw.push(normalizeTypography(candidate));
      }
    }
  }
  if (typeof spec?.answerText === "string" && spec.answerText.trim() !== "") {
    const primary = normalizeTypography(spec.answerText);
    if (!raw.includes(primary)) raw.unshift(primary);
  }
  return raw;
}

/**
 * Evaluate a user answer against all accepted alternatives using bounded meaning-preserving normalization.
 * Never marks open / guided-self-check responses as incorrect.
 */
export function evaluateEnglishAnswer(item, userAnswer) {
  const mode = GRADING_MODES.includes(item?.gradingMode)
    ? item.gradingMode
    : "exact-normalized";
  const normalization = item?.normalization ?? {};
  const candidates = acceptedList(item);
  const rawInput = normalizeTypography(userAnswer);

  if (rawInput === "") {
    return {
      outcome: "incorrect",
      mode,
      normalizedInput: "",
      reasonCode: "empty-answer",
      acceptedAnswers: candidates,
      autoGradable: mode !== "guided-self-check",
    };
  }

  const normalizedInput = normalizeEnglishForGrading(rawInput, normalization);
  for (const candidate of candidates) {
    if (normalizeEnglishForGrading(candidate, normalization) === normalizedInput) {
      return {
        outcome: "correct",
        mode,
        matchedAnswer: candidate,
        normalizedInput,
        acceptedAnswers: candidates,
        autoGradable: true,
      };
    }
  }

  // Distinguish less-suitable context choices if explicitly recorded by contextual items
  if (Array.isArray(item?.lessSuitableAlternatives)) {
    for (const alt of item.lessSuitableAlternatives) {
      const altText = typeof alt === "string" ? alt : alt?.text;
      if (typeof altText === "string" && normalizeEnglishForGrading(altText, normalization) === normalizedInput) {
        return {
          outcome: "incorrect",
          mode,
          normalizedInput,
          reasonCode: "less-suitable-context",
          note: typeof alt === "object" && typeof alt?.noteVi === "string" ? alt.noteVi : undefined,
          acceptedAnswers: candidates,
          autoGradable: true,
        };
      }
    }
  }

  // Detect exact cause when caseSensitive and/or strict punctuation fail
  if (normalization.caseSensitive === true || normalization.punctuationOptional === false) {
    const looseInput = normalizeEnglishForGrading(rawInput, {
      caseSensitive: false,
      punctuationOptional: true,
      contractionsEquivalent: normalization.contractionsEquivalent !== false,
    });
    for (const candidate of candidates) {
      const looseCandidate = normalizeEnglishForGrading(candidate, {
        caseSensitive: false,
        punctuationOptional: true,
        contractionsEquivalent: normalization.contractionsEquivalent !== false,
      });
      if (looseCandidate === looseInput) {
        const sameIgnoringPunctOnly =
          normalizeEnglishForGrading(rawInput, { ...normalization, punctuationOptional: true }) ===
          normalizeEnglishForGrading(candidate, { ...normalization, punctuationOptional: true });
        const sameIgnoringCaseOnly =
          normalizeEnglishForGrading(rawInput, { ...normalization, caseSensitive: false }) ===
          normalizeEnglishForGrading(candidate, { ...normalization, caseSensitive: false });
        const reasonCode = sameIgnoringPunctOnly
          ? "punctuation-mismatch"
          : sameIgnoringCaseOnly
            ? "capitalization-mismatch"
            : "capitalization-and-punctuation-mismatch";
        return {
          outcome: "incorrect",
          mode,
          normalizedInput,
          reasonCode,
          acceptedAnswers: candidates,
          autoGradable: true,
        };
      }
    }
  }

  if (mode === "guided-self-check") {
    return {
      outcome: "needs-review",
      mode,
      normalizedInput,
      reasonCode: "open-response-needs-review",
      acceptedAnswers: candidates,
      autoGradable: false,
    };
  }

  return {
    outcome: "incorrect",
    mode,
    normalizedInput,
    reasonCode: mode === "closed-choice" ? "wrong-choice" : "answer-mismatch",
    acceptedAnswers: candidates,
    autoGradable: true,
  };
}
