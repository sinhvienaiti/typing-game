// Typing Feel start-up for admin/server.mjs: resolve the locations, open the
// store, run the start-up re-export (§3.12) and build the two route handlers.
// Never throws: a problem leaves Typing Feel answering 503 with the reason,
// while Space Typing, Media V2 and the rest of the shared Admin keep running.
import { resolve } from "node:path";
import { createTypingFeelHttpHandler, createTypingFeelRuntimeHandler } from "./http.mjs";
import { startTypingFeelJobs } from "./jobs.mjs";
import { resolveTypingFeelLocations } from "./locations.mjs";
import { TypingFeelService } from "./service.mjs";
import { TypingFeelRevisionStore } from "./store.mjs";

export async function startTypingFeel({ root, env = process.env, mediaStore, auditLog, onAuditError, logger = console }) {
  const locations = resolveTypingFeelLocations({ root, env });
  const typingFeel = { status: "unavailable", service: null, jobs: null, message: null, startup: null, locations };
  if (!locations.available) {
    typingFeel.message = locations.reason;
    logger.warn(locations.reason);
  } else if (resolve(root, mediaStore.rootDir) !== locations.dataDir) {
    // server.mjs reads TYPING_GAME_ADMIN_DATA_DIR itself; both must name the same Media V2 folder.
    typingFeel.message = "Typing Feel is off: the Media V2 folder of the server differs from the Typing Feel data folder.";
    logger.warn(typingFeel.message);
  } else {
    try {
      const store = new TypingFeelRevisionStore({ rootDir: locations.sharedDir });
      const service = new TypingFeelService({ store, mediaStore, publicDir: locations.publicDir, repoRoot: root });
      typingFeel.service = service;
      // Format jobs (G7, §3.9): one at a time, under the store's jobs/ folder; a job left running by a stopped service is marked interrupted.
      typingFeel.jobs = await startTypingFeelJobs({ store, service, mediaStore, repoRoot: root, env, logger });
      typingFeel.startup = await service.syncOnStartup();
      typingFeel.status = typingFeel.startup.status === "not-initialized" ? "not-initialized" : "available";
      if (typingFeel.startup.status === "error") logger.error(`Typing Feel start-up check failed; the published catalogue was left as it is: ${typingFeel.startup.problems.join(" ")}`);
      if (typingFeel.startup.status === "re-exported") logger.log(`Typing Feel: re-exported ${typingFeel.startup.activeRevision} (the catalogue on disk was ${typingFeel.startup.previousCatalogueRevision ?? "missing"}).`);
    } catch (error) {
      // An unexpected throw (an unreadable store, a disk error) leaves Typing Feel off,
      // as the Overview says, instead of editable with nothing on its pages.
      typingFeel.status = "failed";
      typingFeel.service = null;
      typingFeel.jobs = null;
      typingFeel.startup = null;
      const reason = (error instanceof Error ? error.message : String(error)).replace(/\.?\s*$/, ".");
      typingFeel.message = `Typing Feel failed to start: ${reason} Fix it, then restart the Admin service.`;
      logger.error(typingFeel.message, error?.stack ?? "");
    }
  }
  return {
    typingFeel,
    handleTypingFeelRequest: createTypingFeelHttpHandler({ typingFeel, auditLog, onAuditError }),
    handleTypingFeelRuntimeRequest: createTypingFeelRuntimeHandler({ typingFeel }),
  };
}
