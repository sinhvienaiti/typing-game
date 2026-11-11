import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson } from "./english-content-core.mjs";
import { englishContentReviewSourceDigest } from "./english-review-core.mjs";

/**
 * Non-destructive validator for E11/E16 translation slices and review digests.
 * content/english/sentences/e11-translation-slice-*.json and
 * content/english/reviews/decisions.d/e11-translation-slice-*.json are hand-reviewed
 * and must never be overwritten by a script.
 */
const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const SENTENCES_DIR = path.join(ROOT, "content", "english", "sentences");
const DECISIONS_DIR = path.join(ROOT, "content", "english", "reviews", "decisions.d");

const FORBIDDEN_VARIANT_PATTERNS = [
  { name: "even although", rx: /\beven although\b/i },
  { name: "clause-final although", rx: /,\s*although(?:,|\s*[.?!]|$)|\balthough\s*[.?!]$/i },
  { name: "very ... that", rx: /\b(?:was|is|are|were|kept|found\s+it)\s+very\s+[a-z]+\s+that\b/i },
  { name: "very kind as to", rx: /\bvery\s+kind\s+as\s+to\b/i },
  { name: "nearly never", rx: /\bnearly\s+never\b/i },
  { name: "Could you stative/idiom", rx: /\bCould you\s+(?:like|mind|rather|prefer|marry|two\s+knock)\b/i },
  { name: "nor do I'd like", rx: /\bnor do I'd like\b/i },
  { name: "stranded contraction I'm who I'm", rx: /\bwho I'm\b/i },
  { name: "stranded contraction No, I'll not", rx: /\bNo,\s+I'll not\./i },
  { name: "mixed Maybe ... perhaps", rx: /\bMaybe\s+yes,\s+perhaps\s+not\b|\bPerhaps\s+yes,\s+maybe\s+not\b/i },
  { name: "uncontracted inverted Aux not Q", rx: /^(?:Why|How|What|Where|When|Who)\s+(?:is|are|was|were|do|does|did|can|could|would|should)\s+not\s+(?:this|that|these|those|Tom|anyone|anybody|any\s+of|the\s+|modern\s+)/ },
  { name: "uncontracted leading Is not Q", rx: /^Is not (?:Tom|that|this)\b/ },
  { name: "not really downtoner", rx: /\b(?:isn't|is\s+not|'m\s+not|am\s+not|aren't|are\s+not|wasn't|was\s+not|weren't|were\s+not|don't|do\s+not|doesn't|does\s+not|didn't|did\s+not|can't|cannot)\s+(?:seem\s+(?:to\s+be\s+)?|speak\s+\w+\s+|swim\s+|drive\s+|eat\s+|feel\s+|a\s+)?really\s+(?:good|well|busy|cold|tired|fast|happy|easy)\b/i },
  { name: "There is a lot/lots of plural", rx: /\bThere is\s+(?:a lot|lots) of mountains\b/ },
  { name: "lots of pain/garbage", rx: /\b(?:in lots of pain|ideas are lots of garbage|There(?:'s| is) lots of garbage)\b/i },
];

const ACTIVE_HAS_EXPANDED_TO_IS =
  /\b(?:He|he|She|she|It|it)\s+is\s+(?:never\s+(?:told\s+a\s+lie|lied\s+to|eaten\s+sushi|told\s+me)|always\s+been|already\s+(?:read\s+that\s+book|been)|become\s+necessary|just\s+stopped\s+raining|begun\s+to\s+rain|switched\s+the\s+(?:TV|television)\s+on)\b/;

async function main() {
  const sliceFiles = (await fs.readdir(SENTENCES_DIR))
    .filter((f) => /^e11-translation-slice-\d+\.json$/.test(f))
    .sort((a, b) => a.localeCompare(b, "en"));

  const errors = [];
  let totalRecords = 0;
  let multiVariantRecords = 0;

  for (const file of sliceFiles) {
    const sPath = path.join(SENTENCES_DIR, file);
    const dPath = path.join(DECISIONS_DIR, file);
    const [doc, dec] = await Promise.all([readJson(sPath), readJson(dPath)]);

    const decisionById = new Map((dec.decisions ?? []).map((d) => [d.recordId, d]));

    for (const r of doc.records ?? []) {
      if (r.type !== "translation") continue;
      totalRecords++;

      const prompt = typeof r.prompt === "string" ? r.prompt.trim() : "";
      if (!prompt || /^(?:Dịch sang|Dịch câu|Translate\b)/i.test(prompt) || /\[TODO|placeholder\]/i.test(prompt)) {
        errors.push(`${file} ${r.id}: invalid or placeholder Vietnamese prompt ${JSON.stringify(r.prompt)}`);
      }

      if (!Array.isArray(r.acceptedAnswers) || r.acceptedAnswers.length === 0) {
        errors.push(`${file} ${r.id}: acceptedAnswers must be a non-empty array`);
        continue;
      }

      if (r.acceptedAnswers.length > 1) multiVariantRecords++;

      const seen = new Set();
      for (const ans of r.acceptedAnswers) {
        if (typeof ans !== "string" || ans.trim() !== ans || ans.length === 0) {
          errors.push(`${file} ${r.id}: malformed answer variant ${JSON.stringify(ans)}`);
          continue;
        }
        if (seen.has(ans)) {
          errors.push(`${file} ${r.id}: duplicate acceptedAnswer ${JSON.stringify(ans)}`);
        }
        seen.add(ans);

        for (const { name, rx } of FORBIDDEN_VARIANT_PATTERNS) {
          if (rx.test(ans)) {
            errors.push(`${file} ${r.id}: forbidden E16 variant pattern (${name}) in ${JSON.stringify(ans)}`);
          }
        }
        if (ACTIVE_HAS_EXPANDED_TO_IS.test(ans)) {
          errors.push(`${file} ${r.id}: expanded 's->has misread as is in ${JSON.stringify(ans)}`);
        }
      }

      const decision = decisionById.get(r.id);
      if (!decision) {
        errors.push(`${file} ${r.id}: missing decision entry in ${dPath}`);
      } else {
        const expectedDigest = englishContentReviewSourceDigest(r);
        if (decision.sourceDigest !== expectedDigest) {
          errors.push(`${file} ${r.id}: sourceDigest mismatch (${decision.sourceDigest} !== ${expectedDigest})`);
        }
      }
    }
  }

  if (errors.length > 0) {
    for (const err of errors.slice(0, 50)) {
      console.error(`ERROR: ${err}`);
    }
    console.error(`Validation failed with ${errors.length} error(s) across ${sliceFiles.length} E11 translation slices.`);
    process.exitCode = 1;
    return;
  }

  console.log(
    JSON.stringify({
      status: "ok",
      slices: sliceFiles.length,
      totalRecords,
      multiVariantRecords,
    }),
  );
}

main().catch((err) => {
  console.error(err);
  process.exitCode = 1;
});
