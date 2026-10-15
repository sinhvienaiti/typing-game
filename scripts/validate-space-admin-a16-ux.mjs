import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const read = (path) => readFile(resolve(root, path), "utf8");
const [studio, previewCss, remediationCss, v2Css] = await Promise.all([
  read("portal/src/admin/v2/preview/production-preview-studio.ts"),
  read("portal/src/admin/v2/preview/production-preview-a16.css"),
  read("portal/src/admin/space-typing-remediation.css"),
  read("portal/src/admin/v2/admin-v2.css"),
]);

assert(studio.includes('root.setAttribute("role", "region")'), "A16 production preview must expose a keyboard/focusable region.");
assert(studio.includes('statusHost.setAttribute("aria-live", "polite")'), "A16 production preview lifecycle must be announced accessibly.");
assert(studio.includes('root.addEventListener("keydown", onKeyDown)'), "A16 production preview must expose keyboard controls.");
assert(studio.includes('document.addEventListener("fullscreenchange", onFullscreenChange)'), "A16 fullscreen UI must track browser fullscreen state.");
assert(studio.includes('document.removeEventListener("fullscreenchange", onFullscreenChange)'), "A16 fullscreen listeners must be cleaned up.");
assert(studio.includes("actionGeneration += 1"), "A16 async preview actions must be invalidated during teardown.");
assert(studio.includes('document.fullscreenElement === root'), "A16 teardown/fullscreen state must target the actual preview root.");
assert(previewCss.includes("aspect-ratio:16/9"), "A16 preview must have a stable desktop aspect ratio.");
assert(previewCss.includes("@media(max-width:760px)"), "A16 preview must adapt below tablet width.");
assert(previewCss.includes(":fullscreen"), "A16 preview must provide intentional fullscreen layout.");
assert(previewCss.includes("contain:layout paint"), "A16 preview viewport must contain layout/paint work.");
assert(remediationCss.includes("overscroll-behavior:contain"), "A16 list/diff surfaces must keep scroll containment.");
assert(remediationCss.includes(".st-admin-btn:focus-visible"), "A16 shared administrator actions must retain focus-visible styling.");
assert(remediationCss.includes("max-height:min(68vh,760px)"), "A16 revision lists must remain scalable/scrollable.");
assert(v2Css.includes("prefers-reduced-motion:reduce"), "A16 design system must respect reduced-motion preference.");
assert(v2Css.includes("st-admin-v2-empty-state"), "A16 design system must retain explicit empty-state primitives.");
assert(v2Css.includes("st-admin-v2-error-state"), "A16 design system must retain explicit error-state primitives.");
assert(v2Css.includes("st-admin-v2-skeleton"), "A16 design system must retain explicit loading-state primitives.");

console.log("Space Typing Admin A16 validation passed: responsive/focus/loading/error foundations plus keyboard/fullscreen/teardown-safe production previews are present.");
