import assert from "node:assert/strict";
import test from "node:test";
import {
  QaSessionNotFoundError,
  QaSessionStore,
  QaSessionValidationError,
} from "./qa-sessions.mjs";

function fixture() {
  let now = Date.UTC(2026, 9, 5, 12);
  const store = new QaSessionStore({ now: () => now });
  return {
    store,
    now: () => now,
    advance: (ms) => { now += ms; },
  };
}

const request = {
  targetSessionId: "runtime-abc",
  environment: "development",
  ttlMs: 60_000,
  overrides: {
    stageAccess: { stage: 777, mode: "force" },
    shipPreview: "zenith",
    unlimitedWarp: true,
  },
};

test("issues a scoped bearer without exposing it through list", () => {
  const { store } = fixture();
  const issued = store.issue(request, "admin:test");
  assert.equal(typeof issued.bearer, "string");
  assert.ok(issued.bearer.length >= 32);
  assert.equal(issued.generation, 1);
  assert.deepEqual(issued.overrides, request.overrides);

  const [listed] = store.list();
  assert.equal(listed.id, issued.id);
  assert.equal("bearer" in listed, false);
  assert.equal(listed.consumeCount, 0);
});

test("consume requires id, bearer, target runtime and environment", () => {
  const { store } = fixture();
  const issued = store.issue(request, "admin:test");
  const consumed = store.consume({
    id: issued.id,
    bearer: issued.bearer,
    targetSessionId: request.targetSessionId,
    environment: request.environment,
  });
  assert.equal(consumed.gameId, "space-typing");
  assert.equal(consumed.targetSessionId, request.targetSessionId);
  assert.equal(consumed.actorId, "admin:test");
  assert.equal(store.list()[0].consumeCount, 1);

  assert.throws(() => store.consume({
    id: issued.id,
    bearer: issued.bearer,
    targetSessionId: "runtime-other",
    environment: request.environment,
  }), QaSessionNotFoundError);
  assert.throws(() => store.consume({
    id: issued.id,
    bearer: "x".repeat(64),
    targetSessionId: request.targetSessionId,
    environment: request.environment,
  }), QaSessionNotFoundError);
});

test("reconnect may re-exchange the same bound bearer until expiry", () => {
  const { store } = fixture();
  const issued = store.issue(request);
  const exchange = () => store.consume({
    id: issued.id,
    bearer: issued.bearer,
    targetSessionId: request.targetSessionId,
    environment: request.environment,
  });
  assert.equal(exchange().generation, 1);
  assert.equal(exchange().generation, 1);
  assert.equal(store.list()[0].consumeCount, 2);
});

test("new generation revokes an older capability for the same runtime", () => {
  const { store } = fixture();
  const first = store.issue(request);
  const second = store.issue(request);
  assert.equal(second.generation, 2);
  assert.equal(store.list().find((item) => item.id === first.id).revoked, true);
  assert.throws(() => store.consume({
    id: first.id,
    bearer: first.bearer,
    targetSessionId: request.targetSessionId,
    environment: request.environment,
  }), QaSessionNotFoundError);
});

test("expiry and explicit revoke fail closed", () => {
  const { store, advance } = fixture();
  const expired = store.issue(request);
  advance(60_000);
  assert.throws(() => store.consume({
    id: expired.id,
    bearer: expired.bearer,
    targetSessionId: request.targetSessionId,
    environment: request.environment,
  }), QaSessionNotFoundError);

  const live = store.issue({ ...request, targetSessionId: "runtime-2" });
  store.revoke(live.id);
  assert.throws(() => store.consume({
    id: live.id,
    bearer: live.bearer,
    targetSessionId: "runtime-2",
    environment: request.environment,
  }), QaSessionNotFoundError);
});

test("production, fake stages and unsafe TTL values are rejected", () => {
  const { store } = fixture();
  assert.throws(() => store.issue({ ...request, environment: "production" }), QaSessionValidationError);
  assert.throws(() => store.issue({ ...request, ttlMs: 1 }), QaSessionValidationError);
  assert.throws(() => store.issue({
    ...request,
    overrides: { stageAccess: { stage: 1001, mode: "force" } },
  }), QaSessionValidationError);
});
