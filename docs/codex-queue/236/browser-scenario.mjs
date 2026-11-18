// Chạy từ gốc worktree bằng tools/audio-lab/board/tools/cdp-run.mjs.
// Cần Admin 3199 và Vite 3100 đã chạy; không dùng profile Chrome của chủ dự án.
import { writeFileSync, mkdirSync } from "node:fs";
import { resolve } from "node:path";

const routes = [
  ["/admin", "/admin/shared", "All games / Overview"],
  ["/admin/shared", "/admin/shared", "All games / Overview"],
  ["/admin/shared/learning-content", "/admin/shared/learning-content", "All games / Learning Content"],
  ["/admin/space-typing", "/admin/space-typing", "Space Typing / Overview"],
  ["/admin/space-typing/ships", "/admin/space-typing/ships", "Space Typing / Ships"],
  ["/admin/media", "/admin/media", "Administration / Media Library"],
  ["/admin/roles", "/admin/roles", "Administration / Roles & Permissions"],
  ["/admin/space-typing/media", "/admin/media", "Administration / Media Library"],
  ["/admin/space-typing/roles", "/admin/roles", "Administration / Roles & Permissions"],
  ["/admin/space-typing/typing-content", "/admin/shared/learning-content", "All games / Learning Content"],
];

export default async function (page) {
  const origin = "http://127.0.0.1:3100";
  const mode = process.env.SPACE_MISSING === "1" ? "missing" : "present";
  const out = resolve("tmp/236");
  mkdirSync(out, { recursive: true });
  const records = [];
  for (const [width, height] of [[1280, 800], [1920, 1080]]) {
    await page.viewport(width, height, 1);
    for (const [index, [opened, expectedURL, expectedBreadcrumb]] of routes.entries()) {
      const logStart = page.logs.length;
      const exceptionStart = page.exceptions.length;
      await page.goto(origin + opened, { settle: 1800 });
      const state = await page.eval(`({ finalURL: location.pathname, title: document.title, heading: document.querySelector('.st-admin-content h1')?.textContent ?? null, breadcrumb: document.querySelector('.st-admin-breadcrumb')?.textContent?.trim() ?? null, missingSpace: document.querySelector('.st-admin-content')?.textContent?.includes('Space Typing is not checked out'), horizontalOverflow: document.documentElement.scrollWidth > innerWidth })`);
      const screenshot = `${out}/${mode}-${width}-${String(index).padStart(2, "0")}.png`;
      await page.shot(screenshot);
      records.push({ opened, width, height, ...state, consoleErrors: page.logs.slice(logStart), exceptions: page.exceptions.slice(exceptionStart), screenshot,
        pass: state.finalURL === expectedURL && state.breadcrumb === expectedBreadcrumb && !state.horizontalOverflow && (mode !== "missing" || !opened.startsWith("/admin/space-typing") || expectedURL.startsWith("/admin/shared") || expectedURL === "/admin/media" || expectedURL === "/admin/roles" || state.missingSpace) });
    }
  }
  // Thử chuyển khu bằng chuột và mở bảng lệnh bằng phím thật qua CDP.
  await page.goto(origin + "/admin/shared", { settle: 800 });
  await page.click('.st-admin-area-selector button:nth-child(2)', { fallback: false });
  await page.sleep(800);
  const switchToSpace = await page.eval('location.pathname === "/admin/space-typing"');
  await page.click('.st-admin-command', { fallback: false });
  await page.typeKeys("Learning Content");
  await page.key("ArrowDown");
  await page.key("Enter");
  await page.sleep(800);
  const commandToShared = await page.eval('location.pathname === "/admin/shared/learning-content"');
  const result = { status: "executed", mode, records, interactions: { switchToSpace, commandToShared }, logs: page.logs, exceptions: page.exceptions };
  writeFileSync(resolve(`docs/codex-queue/236/browser-${mode}.json`), JSON.stringify(result, null, 2));
  if (records.some((record) => !record.pass) || !switchToSpace || !commandToShared || page.exceptions.length) throw new Error("Browser acceptance failed; inspect JSON and captures.");
  return result;
}
