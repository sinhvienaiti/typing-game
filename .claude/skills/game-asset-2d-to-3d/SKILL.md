---
name: game-asset-2d-to-3d
description: Prepare and integrate Space Typing concepts, reference images, sprites, relief bundles, and authored GLB/glTF assets. Use for 2D-to-3D generation, Blender cleanup, animation, model optimization, or runtime asset validation.
---

# Space Typing asset pipeline

1. Identify destination mode and renderer before authoring: 2D Canvas, Duel relief/authored ship, bundled GLB, or separate Campaign 3D engine. Read relevant paths in [the asset map](references/asset-map.md); formats are not interchangeable.
2. Inspect source art and runtime assets. Define silhouette, views, scale, origin, sockets, clips, material/texture needs, quality tiers and fallback against the actual consumer. Keep provenance/license records with the asset.
3. For image-to-3D references, request views needed by the target generator. Keep the whole object in frame, intended bilateral symmetry, readable wings/appendages and consistent front/side/rear identity. Use orthographic references where required; avoid perspective distortion and ambiguous overlaps. Preserve intentionally asymmetric designs.
4. Use available image/3D generation skills or local authoring tools when appropriate. Check capability, credentials, cost and permission before paid/external generation; unavailable providers do not prevent preparing references or validating existing assets. Use Blender when installed and needed.
5. Clean geometry, normals, pivot, scale, materials, bones and clips; export to the project contract. Reuse preparation scripts, compression and quality tiers. Preserve source art and unrelated generated output.
6. Validate manifests, sockets/clips, textures, load failure and disposal. Render in the actual mode at representative quality levels, inspect multiple views/animation over time, then profile browser load/draw costs. A nice concept image or valid GLB header does not establish production readiness.

Coordinate Admin bindings with [admin-runtime-authoring](../admin-runtime-authoring/SKILL.md), performance with [game-performance-quality](../game-performance-quality/SKILL.md), and visual evidence with [space-typing-playtest](../space-typing-playtest/SKILL.md). Installed generic asset/Three.js skills supply techniques; project consumers decide contracts.
