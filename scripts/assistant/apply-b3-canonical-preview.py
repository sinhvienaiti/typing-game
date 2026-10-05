from pathlib import Path


def replace_once(path: str, old: str, new: str, label: str) -> None:
    file = Path(path)
    text = file.read_text()
    if new in text:
        return
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: anchor count={count}")
    file.write_text(text.replace(old, new, 1))


replace_once(
    "admin/server.mjs",
    'import { createDefaultSpaceTypingConfig } from "./default-config.mjs";\n',
    'import { createDefaultSpaceTypingConfig } from "./default-config.mjs";\nimport { runWorldMusicPreview, WorldMusicPreviewError } from "./world-music-preview.mjs";\n',
    "server preview import",
)
replace_once(
    "admin/server.mjs",
    '''    if (request.method === "POST" && url.pathname === "/api/admin/space-typing/revisions") {\n''',
    '''    if (request.method === "POST" && url.pathname === "/api/admin/space-typing/world-music/preview") {\n      const input = await body(request);\n      const activeConfig = await store.getRuntimeConfig();\n      const publishedPolicy = input.publishedPolicy ?? activeConfig.worldMusic?.publishedPolicy;\n      const preview = await runWorldMusicPreview({\n        rootDir: root,\n        contract,\n        publishedPolicy,\n        musicMode: input.musicMode ?? "map",\n      });\n      json(response, 200, preview);\n      return;\n    }\n    if (request.method === "POST" && url.pathname === "/api/admin/space-typing/revisions") {\n''',
    "server preview route",
)
replace_once(
    "admin/server.mjs",
    '''    if (error instanceof AdminValidationError) {\n      json(response, 400, { error: "validation", message: error.message });\n      return;\n    }\n    console.error(error);\n''',
    '''    if (error instanceof AdminValidationError) {\n      json(response, 400, { error: "validation", message: error.message });\n      return;\n    }\n    if (error instanceof WorldMusicPreviewError) {\n      json(response, 502, { error: "preview-error", message: error.message });\n      return;\n    }\n    console.error(error);\n''',
    "server preview error",
)

api = "portal/src/admin/api.ts"
replace_once(
    api,
    '''export type AdminStatePayload = {\n  state: {\n    version: number;\n    activeRevision: string;\n    generation: number;\n    updatedAt: string;\n  };\n  active: AdminRevision;\n  history: AdminRevision[];\n};\n''',
    '''export type AdminStatePayload = {\n  state: {\n    version: number;\n    activeRevision: string;\n    generation: number;\n    updatedAt: string;\n  };\n  active: AdminRevision;\n  history: AdminRevision[];\n};\n\nexport type WorldMusicPreviewState = {\n  state: "normal" | "mini" | "world" | "major";\n  trackIds: string[];\n  tracks: Array<{ id: string; title: string; playbackKind: "single" | "stems" }>;\n  trackCount: number;\n  selectionMode: "shuffle-bag" | "ordered";\n  resolvedFrom: string;\n  fallbackTrace: string[];\n  badges: string[];\n};\n\nexport type WorldMusicPreview = {\n  protocolVersion: 1;\n  configRevision: string;\n  manifestRevision: string;\n  musicMode: "map" | "random";\n  worlds: Array<{\n    worldId: string;\n    name: string;\n    galaxy: number;\n    stageRange: [number, number];\n    states: {\n      normal: WorldMusicPreviewState;\n      mini: WorldMusicPreviewState;\n      world: WorldMusicPreviewState;\n      major: WorldMusicPreviewState;\n    };\n  }>;\n};\n''',
    "api preview types",
)
replace_once(
    api,
    '''  createRevision(input: {\n''',
    '''  previewWorldMusic(input: {\n    publishedPolicy?: unknown;\n    musicMode?: "map" | "random";\n  } = {}): Promise<WorldMusicPreview> {\n    return this.request<WorldMusicPreview>("/api/admin/space-typing/world-music/preview", {\n      method: "POST",\n      body: JSON.stringify(input),\n    });\n  }\n\n  createRevision(input: {\n''',
    "api preview method",
)

ui = "portal/src/admin/space-typing.ts"
replace_once(
    ui,
    '''  type SpaceTypingAdminConfig,\n} from "./api";\n''',
    '''  type SpaceTypingAdminConfig,\n  type WorldMusicPreview,\n} from "./api";\n''',
    "ui preview type import",
)
replace_once(
    ui,
    '''      } else if (path === "/admin/space-typing/world-music") {\n        this.renderWorldMusic(panel, state);\n''',
    '''      } else if (path === "/admin/space-typing/world-music") {\n        const preview = await this.api.previewWorldMusic();\n        this.renderWorldMusic(panel, state, preview);\n''',
    "ui load preview",
)
replace_once(
    ui,
    '''.st-world strong{font-size:13px}.st-world small{display:block;color:#8faabb;margin-top:5px}.st-history''',
    '''.st-world strong{font-size:13px}.st-world small{display:block;color:#8faabb;margin-top:5px}.st-world-badges{display:flex;gap:4px;flex-wrap:wrap;margin-top:8px}.st-world-source{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:10px;color:#7fa2b8;margin-top:7px;overflow-wrap:anywhere}.st-history''',
    "ui world styles",
)
old_method = '''  private renderWorldMusic(panel: HTMLElement, state: AdminStatePayload): void {\n    panel.replaceChildren(this.renderHeader("World Music", "10 Galaxy groups × 5 Worlds. Canonical resolver badges arrive from child preview data in B3.2."));\n    const note = document.createElement("div");\n    note.className = "st-admin-note";\n    note.textContent = `Active policy: ${state.active.config.worldMusic.policyRevision}. This page intentionally does not infer READY/FALLBACK badges without canonical resolver traces.`;\n    panel.append(note);\n    const list = document.createElement("div");\n    list.className = "st-galaxy-list";\n    for (let galaxy = 1; galaxy <= contract.worldMusic.galaxyCount; galaxy += 1) {\n      const section = document.createElement("section");\n      section.className = "st-galaxy";\n      const title = document.createElement("h3");\n      title.textContent = `Galaxy ${String(galaxy).padStart(2, "0")}`;\n      const worlds = document.createElement("div");\n      worlds.className = "st-world-grid";\n      for (let offset = 1; offset <= contract.worldMusic.worldsPerGalaxy; offset += 1) {\n        const worldNumber = (galaxy - 1) * contract.worldMusic.worldsPerGalaxy + offset;\n        const worldId = `world-${String(worldNumber).padStart(2, "0")}`;\n        const card = document.createElement("div");\n        card.className = "st-world";\n        const strong = document.createElement("strong");\n        strong.textContent = worldId;\n        const mode = document.createElement("small");\n        mode.textContent = Object.hasOwn(state.active.config.worldMusic.assignments, worldId)\n          ? "Published override present"\n          : "No Admin override";\n        card.append(strong, mode);\n        worlds.append(card);\n      }\n      section.append(title, worlds);\n      list.append(section);\n    }\n    panel.append(list);\n  }\n'''
new_method = '''  private renderWorldMusic(\n    panel: HTMLElement,\n    state: AdminStatePayload,\n    preview: WorldMusicPreview,\n  ): void {\n    panel.replaceChildren(this.renderHeader("World Music", "Canonical resolver preview for all 50 Worlds — no UI-side fallback guessing."));\n    const note = document.createElement("div");\n    note.className = "st-admin-note";\n    note.textContent = `Config ${preview.configRevision} · manifest ${preview.manifestRevision} · mode ${preview.musicMode} · active revision ${state.state.activeRevision}`;\n    panel.append(note);\n    const list = document.createElement("div");\n    list.className = "st-galaxy-list";\n    for (let galaxy = 1; galaxy <= contract.worldMusic.galaxyCount; galaxy += 1) {\n      const section = document.createElement("section");\n      section.className = "st-galaxy";\n      const title = document.createElement("h3");\n      title.textContent = `Galaxy ${String(galaxy).padStart(2, "0")}`;\n      const worlds = document.createElement("div");\n      worlds.className = "st-world-grid";\n      for (const world of preview.worlds.filter((item) => item.galaxy === galaxy)) {\n        const card = document.createElement("div");\n        card.className = "st-world";\n        const strong = document.createElement("strong");\n        strong.textContent = `${world.worldId} · ${world.name}`;\n        const range = document.createElement("small");\n        range.textContent = `Stages ${world.stageRange[0]}–${world.stageRange[1]} · normal ${world.states.normal.trackCount} · boss ${world.states.world.trackCount}`;\n        const badges = document.createElement("div");\n        badges.className = "st-world-badges";\n        for (const badge of [...new Set([...world.states.normal.badges, ...world.states.world.badges])]) {\n          const chip = document.createElement("span");\n          chip.className = "st-badge";\n          chip.textContent = badge;\n          badges.append(chip);\n        }\n        const source = document.createElement("div");\n        source.className = "st-world-source";\n        source.textContent = `normal: ${world.states.normal.resolvedFrom} · boss: ${world.states.world.resolvedFrom}`;\n        source.title = [...world.states.normal.fallbackTrace, ...world.states.world.fallbackTrace].join("\\n");\n        card.append(strong, range, badges, source);\n        worlds.append(card);\n      }\n      section.append(title, worlds);\n      list.append(section);\n    }\n    panel.append(list);\n  }\n'''
replace_once(ui, old_method, new_method, "ui world canonical preview")

workflow = ".github/workflows/admin-ci.yml"
replace_once(
    workflow,
    '''          node --check admin/server.mjs\n          node --check admin/store.test.mjs\n''',
    '''          node --check admin/server.mjs\n          node --check admin/world-music-preview.mjs\n          node --check admin/world-music-preview.test.mjs\n          node --check admin/store.test.mjs\n''',
    "ci preview syntax",
)
replace_once(
    workflow,
    '''      - name: Test Space Typing\n        run: pnpm --dir games/space-typing test\n''',
    '''      - name: Test canonical World Music Admin preview bridge\n        run: node --test admin/world-music-preview.test.mjs\n\n      - name: Test Space Typing\n        run: pnpm --dir games/space-typing test\n''',
    "ci preview integration",
)
