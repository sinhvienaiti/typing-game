from pathlib import Path
import json


def replace_once(path: str, old: str, new: str, label: str) -> None:
    file = Path(path)
    text = file.read_text()
    if new in text:
        return
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: anchor count={count}")
    file.write_text(text.replace(old, new, 1))


main = "portal/src/main.ts"
replace_once(
    main,
    'import "./styles.css";\n',
    'import "./styles.css";\nimport { SpaceTypingAdmin } from "./admin/space-typing";\n',
    "admin import",
)
replace_once(
    main,
    'const learningMaintenance = new LearningMaintenancePage(navigate);\n',
    'const learningMaintenance = new LearningMaintenancePage(navigate);\nconst spaceTypingAdmin = new SpaceTypingAdmin(navigate);\n',
    "admin instance",
)
replace_once(
    main,
    '''    const active =\n      buttonPath === "/review"\n        ? path === "/review" || path.startsWith("/review/")\n        : path === buttonPath;\n''',
    '''    const active =\n      buttonPath === "/review"\n        ? path === "/review" || path.startsWith("/review/")\n        : buttonPath === "/admin/space-typing"\n          ? path === "/admin/space-typing" || path.startsWith("/admin/space-typing/")\n          : path === buttonPath;\n''',
    "admin nav state",
)
replace_once(
    main,
    'links.append(makeButton("Smart Review", "/review"));\n',
    'links.append(makeButton("Smart Review", "/review"));\nlinks.append(makeButton("Space Admin", "/admin/space-typing"));\n',
    "admin nav button",
)
replace_once(
    main,
    '''  const game = registry.games.find((item) => item.path === path);\n''',
    '''  if (path === "/admin/space-typing" || path.startsWith("/admin/space-typing/")) {\n    music.setKaraokeActive(false);\n    routeHost.replaceChildren(spaceTypingAdmin.render(path));\n    return;\n  }\n\n  const game = registry.games.find((item) => item.path === path);\n''',
    "admin route",
)

vite = Path("portal/vite.config.ts")
vite_text = vite.read_text()
if '"/api/admin"' not in vite_text:
    old = '''    hmr: {\n      host: "typing-game.local",\n      protocol: "wss",\n      clientPort: 443,\n    },\n'''
    new = '''    hmr: {\n      host: "typing-game.local",\n      protocol: "wss",\n      clientPort: 443,\n    },\n    proxy: {\n      "/api/admin": {\n        target: "http://127.0.0.1:3199",\n        changeOrigin: false,\n      },\n    },\n'''
    if vite_text.count(old) != 1:
        raise SystemExit("vite proxy anchor mismatch")
    vite.write_text(vite_text.replace(old, new, 1))

package_path = Path("package.json")
package = json.loads(package_path.read_text())
scripts = package["scripts"]
scripts["dev:admin"] = "node admin/server.mjs"
scripts["admin:test"] = "node --test admin/store.test.mjs"
scripts["admin:contract:validate"] = "node scripts/validate-space-admin-contract.mjs"
scripts["dev"] = (
    "bash scripts/cleanup-dev-ports.sh 3000 3001 3002 3003 3004 3100 3199 && "
    "concurrently -k -n admin,portal,monkeytype,shooter,recall,karaoke,space "
    '"pnpm dev:admin" "pnpm dev:portal" "pnpm dev:monkeytype:app" '
    '"pnpm dev:shooter:app" "pnpm dev:recall:app" "pnpm dev:karaoke:app" "pnpm dev:space:app"'
)
scripts["dev:space"] = (
    "bash scripts/cleanup-dev-ports.sh 3004 3100 3199 && "
    "concurrently -k -n admin,portal,space "
    '"pnpm dev:admin" "pnpm dev:portal" "pnpm dev:space:app"'
)
package_path.write_text(json.dumps(package, ensure_ascii=False, indent=2) + "\n")
