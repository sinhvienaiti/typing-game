import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const read = (path) => readFile(resolve(root, path), "utf8");
const [history, security, api] = await Promise.all([
  read("portal/src/admin/space-typing-history-phase-b.ts"),
  read("admin/admin-security.mjs"),
  read("portal/src/admin/api.ts"),
]);

assert(history.includes("Administrator Activity"), "A14 must surface attributed administrator activity.");
assert(history.includes("Review Changes"), "A14 must provide an administrator-facing change review surface.");
assert(history.includes("businessPath"), "A14 must translate raw config paths into business/domain labels.");
assert(history.includes("friendlyValue"), "A14 must render before/after values in human-readable form.");
assert(history.includes("→"), "A14 modified values must be shown as before → after.");
assert(history.includes("Advanced · raw revision and path diff"), "Raw revision/path evidence must live under Advanced disclosure.");
assert(history.includes("api.getAudit(100)"), "A14 activity must use the canonical audit endpoint.");
assert(history.includes("api.validateRevision(revision)"), "A14 must retain server-side validation before pointer mutation.");
assert(history.includes("api.publish(revision, latest.state.activeRevision)"), "A14 publish must remain expected-active CAS protected.");
assert(history.includes("api.rollback(revision, latest.state.activeRevision)"), "A14 rollback must remain expected-active CAS protected.");
assert(history.includes("rollbackEligible"), "A14 must preserve canonical rollback eligibility.");
assert(history.includes("publishable"), "A14 must preserve canonical publish eligibility.");
assert(!history.includes("Config Diff\", \"Compare immutable config snapshots"), "Raw config diff must no longer be the primary compare workflow.");
assert(security.includes("actorDisplayName"), "Audit events must retain actor display attribution.");
assert(security.includes('result: "attempt"'), "Mutations must retain durable pre-mutation audit attempt records.");
assert(security.includes('result: "success"'), "Mutations must retain success audit records.");
assert(api.includes("getAudit(limit = 8)"), "Portal API must retain audit history access.");
assert(api.includes("publish(revision: string, expectedActiveRevision: string)"), "Portal publish API must require expected active revision.");
assert(api.includes("rollback(targetRevision: string, expectedActiveRevision: string)"), "Portal rollback API must require expected active revision.");

console.log("Space Typing Admin A14 validation passed: attributed activity, human-readable compare, Advanced raw evidence and CAS-safe publish/rollback are preserved.");
