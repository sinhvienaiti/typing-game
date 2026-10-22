// Source: games/space-typing/tests/shared-learning.test.ts (gameId passed explicitly)
import { describe, expect, it } from "vitest";
import {
  buildCombatLearningEvent,
  buildRecallLearningEvent,
  englishActivityEntries,
  parseEnglishActivityDataset,
  parseReviewDataset,
} from "./index";

const GAME = "dragon-hold";

describe("shared learning contract", () => {
  it("parses compatible vocabulary review datasets and preserves order", () => {
    expect(
      parseReviewDataset({
        version: 1,
        type: "typing-game:learning:v1:review-dataset",
        requestId: "review-1",
        goal: "mixed",
        items: [
          { entityType: "vocabulary", entityId: " Passport " },
          { entityType: "vocabulary", entityId: "AIRPORT" },
          { entityType: "vocabulary", entityId: "passport" },
        ],
      }),
    ).toEqual({
      version: 1,
      type: "typing-game:learning:v1:review-dataset",
      requestId: "review-1",
      goal: "mixed",
      entityIds: ["passport", "airport"],
    });
    expect(parseReviewDataset({ type: "other" })).toBeNull();
  });

  it("rejects unsupported goals and non-vocabulary items", () => {
    const base = { version: 1, type: "typing-game:learning:v1:review-dataset", requestId: "review-2" };
    expect(() => parseReviewDataset({ ...base, goal: "listening", items: [{ entityType: "vocabulary", entityId: "airport" }] })).toThrow(
      "goal is invalid",
    );
    expect(() => parseReviewDataset({ ...base, goal: "mixed", items: [{ entityType: "grammar", entityId: "time.present" }] })).toThrow(
      "vocabulary only",
    );
  });

  it("requires a gameId and stamps it on every event", () => {
    const entry = { id: "airport", en: "Airport", vi: "sân bay", ipa: "/ˈerˌpɔrt/" };
    expect(buildCombatLearningEvent({ gameId: GAME, entry, perfect: true, occurredAt: "2026-09-24T15:00:00.000Z" })).toEqual({
      version: 1,
      entityType: "vocabulary",
      entityId: "airport",
      gameId: GAME,
      activityType: "typing",
      result: "correct",
      occurredAt: "2026-09-24T15:00:00.000Z",
      hintUsed: false,
      replayUsed: false,
      expectedAnswer: "Airport",
    });
    expect(buildCombatLearningEvent({ gameId: GAME, entry, perfect: false })).toMatchObject({ result: "wrong", errorType: "spelling" });
    expect(() => buildCombatLearningEvent({ gameId: "", entry, perfect: true })).toThrow("gameId is required");
    expect(() => buildCombatLearningEvent({ gameId: "Space Typing", entry, perfect: true })).toThrow("gameId is required");
  });

  it("maps recall hints, replays, response time and failure state into one event", () => {
    const event = buildRecallLearningEvent({
      gameId: GAME,
      result: {
        entry: { id: "passport", en: "passport", vi: "hộ chiếu", ipa: "/ˈpæsˌpɔrt/" },
        completed: true,
        perfect: false,
        hintCount: 2,
        replayCount: 1,
        responseMs: 891.6,
      },
      occurredAt: "2026-09-24T15:00:00.000Z",
    });
    expect(event).toMatchObject({
      entityId: "passport",
      gameId: GAME,
      activityType: "recall",
      result: "wrong",
      responseMs: 892,
      hintUsed: true,
      replayUsed: true,
      errorType: "spelling",
    });
  });

  it("accepts English activities only for this game and keeps grammar identity", () => {
    const dataset = {
      version: 1,
      type: "typing-game:english-content:v1:activity-dataset",
      requestId: "rich-1",
      gameId: GAME,
      activity: "grammar-challenge",
      items: [
        {
          contentId: "gr.b1.second-conditional",
          entityType: "grammar",
          entityId: "gr.b1.second-conditional",
          promptText: "Complete the hypothetical sentence",
          answerText: "If I had more time, I would learn another language.",
        },
      ],
    };
    expect(() => parseEnglishActivityDataset(dataset, "space-typing")).toThrow("identity");
    const parsed = parseEnglishActivityDataset(dataset, GAME)!;
    const entry = englishActivityEntries(parsed)[0]!;
    expect(buildCombatLearningEvent({ gameId: GAME, entry, perfect: false, inputSource: "voice" })).toMatchObject({
      entityType: "grammar",
      entityId: "gr.b1.second-conditional",
      activityType: "speaking",
      result: "correct",
    });
    expect(() =>
      parseEnglishActivityDataset(
        { ...dataset, activity: "collocation", items: [{ ...dataset.items[0]!, entityId: "gr.a1.example" }] },
        GAME,
      ),
    ).toThrow("reserved");
  });
});
