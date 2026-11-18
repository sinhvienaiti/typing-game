# Jade ring material (ticket 259, CX-C): ChatGPT run, 04/11/2026 (incomplete)

Chat: https://chatgpt.com/c/6aead1ae-67e4-83ec-983f-339fe8bb6531

Review count: FAIL (review 1; its corrected full version was still streaming at the 14:00 hard stop and is saved only in part). No PASS yet. Not forwarded to Gemini.

Saved verbatim by page JavaScript (innerText of each turn), not retyped. The first user turn below is the brief as sent; the brief file is also given in full first, because the page collapses long user bubbles.

## Brief as sent (verbatim)

```text
Role: you are the analyst for a game project (three.js r17x WebGL2, TypeScript, browser game "Tu Tien", xianxia flying swords). Research, analyse and propose a concrete, implementable solution. If you need clarifications, ask all of them in one message before you start; otherwise answer directly.

GOAL
Our signature sword "Clear Wind" (a Tripo GLB, 14,728 tris, base colour + ORM + normal 4096) renders its jade ring as chrome silver. The owner's approved concept image shows the ring as WHITE JADE with a PALE GOLD rim. Owner decision (final, do not reopen): make the ring white jade with a pale gold rim "as in the approved image", WITHOUT repainting the texture: a GEOMETRIC material mask in the sword's shader, then before/after images go to the owner. Only if he rejects it would the texture be repainted later.

APPROVED IMAGE (sampled by us from clearwind-src3q.v4-try1.png, sRGB): the ring is a thick flat disc (annulus) of white jade, open round hole; thin pale-gold lines run along the disc's inner (hole) edge and outer edge; a slim polished SILVER outer rim surrounds the disc; two pale green jade beads and white porcelain cloud brackets with pale-gold rims sit on the disc. White jade median #DFDDDF (p25 #D7D4D4, p90 #F5F4F7; saturation ~0.01, faintly cool). Pale gold median #D4B793 (p25 #CEAE89, p90 #EACB9D; hue ~33 deg, sat ~0.31). Beads: pale jade #C4E2CF.

CURRENT CODE (games/immortality-cultivation/src/view/skills/)
1) sword-material.ts, patchSwordMaterial(material: MeshStandardMaterial, opts {bladeFrom, jade:[r,g,b] linear <=0.86}) patches the weapon's own PBR material via onBeforeCompile; customProgramCacheKey "real-sword". Vertex: varying vSwP = position (the unit blade's local space: guard at y=0, tip at y=1, hilt y<0, pommel end pommelY ~ -0.61, blade flat faces +-Z, spine on x=0). Instanced attributes iFx (glow, flash, dissolve, seed) and iRim. Injections:
 - after <color_fragment>, chunk JADE:
   vec3 swC = diffuseColor.rgb;
   float swJade = smoothstep(0.07,0.17,(swC.g-swC.r)/max(swC.g,0.04)) * smoothstep(-0.05,0.0,swC.g-swC.b);  // hue mask: catches the pale green beads, NOT the chrome ring
   if (uSwMode > 0.5) diffuseColor.rgb *= uSwChar;   // Fire "furnace" mode darkens the body
 - after <emissivemap_fragment>, chunk EMIT: edge line (HDR, only blade), fresnel rim in skill colour, jade light swJadeE = swTint*uSwJade*swJade*(0.16+0.24*glow+0.4*flash) (Fire mode: swJadeE = uSwHeat*swJade*(...) embers, plus a heat band on the blade), hit flash += swC*min(flash,1.5)*0.55, dissolve edge.
 - replaces "vec3 outgoingLight = totalDiffuse + totalSpecular + totalEmissiveRadiance;" with OUTGOING: outgoingLight = (totalDiffuse+totalSpecular)*uSwLight + totalEmissiveRadiance; then subtracts the part of swJadeE that would push luminance over 0.95 (jade fills only headroom under bloom threshold 1.0, never blooms).
 - SWORD_LOOK uniforms shared by all swords: edge, mode (0 steel=Metal element, 1 furnace=Fire element), heat, char, heatFrom, time. SWORD_LIGHT gain.
2) blades.ts: guardBand(geometry) finds the run of heights round y=0 whose cross-section half-width > 2x the blade's width ("Clear Wind: its ring") -> [g0,g1]. auraAnchorsOf(...) returns AuraAnchors { profile, bladeFrom, guardFrom, ring: {y:(g0+g1)/2, r: guardHalf} | null, guardHalf (max |x| of vertices in the band), tasselFrom }. modelOf(geometry, material, jade, real, source, ring) computes guard, bladeFrom = max(0.01, g1+0.01), edgeField, patchSwordMaterial(material, {bladeFrom, jade}) and aura anchors. Two models share it: the full GLB (hero/lead swords) and a 3,200-tri textured LOD (mid swords), same UV map. overlayModel() clones the material and re-patches it. WeaponDef.motif {jade, ring?: boolean}; only Clear Wind has ring:true. AuraAnchors.ring is currently used only by aura layers, not by the material. NOTE: ring.r is guardHalf (max |x| in the band), which may include the cloud brackets sticking out; the hole's inner radius is not measured anywhere.
3) real-swords.ts: far swords (key 7 "river" of 88 swords, 35-130 px long) are impostors: an atlas baked in Blender from the same GLB under a fixed lookdev light (tLit, premultiplied, plus tMask: r = edge field, g = blade flag, a = coverage), 4 rows = rolls [0,30,60,90] deg round the long axis, cells 512x128, tip right. Meta (clear-wind-impostor.json): u0 .035, u1 .965, guardU .3111, bladeFromU .3886, ringU .31109, ringR .08008 (centre and outer radius along the cell, in u units; declared in SwordAtlasMeta but UNUSED), rollWidth [1,.8966,.5862,.3793]. Fragment: rows blended by vRoll; cellUv(row) = vec2(vUv.x, 1 - (row + 0.5 - vUv.y*0.5)/rows) so vUv.y in [-1,1] spans the cell height; col = c.rgb*uGain*uLight; furnace: col *= uChar, + heat band; flash; edge line. gl_FragColor = vec4(col*a, c.a*a). A second program FRAGMENT_HALO adds an analytic mantle around the sword.
4) Lab gate tools: src/lab/aura-gates.ts drawSwordMask renders blade red, guard band (ring + cloud guard) green, hilt blue. Scenario scripts/visual/scenarios/lab-element-parity.mjs captures fixed-clock frames (key 1 play + zoom camera, key 7, K5) for before/after pixel comparison; QS adds URL flags.

CONSTRAINTS
- Metal (steel mode) must stay pixel-identical OUTSIDE the ring region; Fire (furnace) likewise identical outside the ring. Inside the ring region only the material changes; geometry, silhouette and UVs untouched; the ring must keep >= 95 % of its pixels (no discard, no holes) at every frame.
- No bloom from the ring: anything emissive stays under luminance 0.95 (same headroom rule as swJadeE), no channel over 0.86; only the blade's edge line may bloom.
- Keep the pale gold far from coin gold #FFC83A and from the typing cyan #7FF5E0; white jade must read as jade (soft, slightly translucent, satin), not as chalk, plastic or chrome.
- The beads (hue mask) keep their pale jade light. The cloud brackets in the approved image are white porcelain with pale-gold rims: if your mask covers them, that is acceptable or even desired, say which.
- Zero allocation per frame; load-time measurements allowed; shader cost small (the river draws 88 swords at <= 11.5 ms p95 total frame).
- Far impostors cannot re-bake in this ticket unless you argue a re-bake is clearly better (the bake script scripts/models/blender/bake_sword_impostor.py exists and could also emit a ring mask channel); the worker is a code agent (Codex) without Blender UI; Blender CLI exists on the machine.
- Taste: anime/donghua xianxia, luxurious, radiant, never realism as the goal, never plain.

DELIVER
1) analysis: why the hue mask misses the chrome ring, what defines the ring geometrically on this mesh, risks (cloud brackets, collar, beads, the blade/tang near the ring, the LOD, the dissolve and flash paths, Fire mode).
2) the solution as ordered steps with reasons: (a) load-time measurement of the ring (centre y, outer radius, inner hole radius, the silver outer rim band) from the geometry, with the exact algorithm; (b) the exact GLSL for the geometric mask in vSwP space (radial bands: hole-edge gold line, white jade disc, outer gold line, silver rim kept or not; soft edges by fwidth), injected where (which three.js chunks: color_fragment, roughnessmap_fragment, metalnessmap_fragment, etc.), and the exact material values: albedo (linear), metalness, roughness for white jade and for pale gold, how the texture's detail is kept (luminance modulation), any wrap/translucency fake and its cap; (c) Fire mode behaviour inside the ring; (d) the impostor: the exact cell-space mask (u band, per-row ellipse with the roll, coverage, excluding the blade flag) and recolour formula; (e) uniforms/TS API changes (names), and how AuraAnchors/ringU/ringR feed them.
3) checks with numbers: ring pixel keep >= 95 %, outside-ring parity (exact or a tolerance you justify), colour check of the ring against the samples (e.g. OKLab distance), tsc/vitest, before/after captures.
4) what you are not sure about. Cite a source (three.js docs/source chunk names, PBR references) for every factual claim.
```

## Turn 1 · user

````text
Role: you are the analyst for a game project (three.js r17x WebGL2, TypeScript, browser game "Tu Tien", xianxia flying swords). Research, analyse and propose a concrete, implementable solution. If you need clarifications, ask all of them in one message before you start; otherwise answer directly.

GOAL
Our signature sword "Clear Wind" (a Tripo GLB, 14,728 tris, base colour + ORM + normal 4096) renders its jade ring as chrome silver. The owner's approved concept image shows the ring as WHITE JADE with a PALE GOLD rim. Owner decision (final, do not reopen): make the ring white jade with a pale gold rim "as in the approved image", WITHOUT repainting the texture: a GEOMETRIC material mask in the sword's shader, then before/after images go to the owner. Only if he rejects it would the texture be repainted later.

APPROVED IMAGE (sampled by us from clearwind-src3q.v4-try1.png, sRGB): the ring is a thick flat disc (annulus) of white jade, open round hole; thin pale-gold lines run along the disc's inner (hole) edge and outer edge; a slim polished SILVER outer rim surrounds the disc; two pale green jade beads and white porcelain cloud brackets with pale-gold rims sit on the disc. White jade median #DFDDDF (p25 #D7D4D4, p90 #F5F4F7; saturation ~0.01, faintly cool). Pale gold median #D4B793 (p25 #CEAE89, p90 #EACB9D; hue ~33 deg, sat ~0.31). Beads: pale jade #C4E2CF.

CURRENT CODE (games/immortality-cultivation/src/view/skills/)
1) sword-material.ts, patchSwordMaterial(material: MeshStandardMaterial, opts {bladeFrom, jade:[r,g,b] linear <=0.86}) patches the weapon's own PBR material via onBeforeCompile; customProgramCacheKey "real-sword". Vertex: varying vSwP = position (the unit blade's local space: guard at y=0, tip at y=1, hilt y<0, pommel end pommelY ~ -0.61, blade flat faces +-Z, spine on x=0). Instanced attributes iFx (glow, flash, dissolve, seed) and iRim. Injections:
 - after <color_fragment>, chunk JADE:
   vec3 swC = diffuseColor.rgb;
   float swJade = smoothstep(0.07,0.17,(swC.g-swC.r)/max(swC.g,0.04)) * smoothstep(-0.05,0.0,swC.g-swC.b);  // hue mask: catches the pale green beads, NOT the chrome ring
   if (uSwMode > 0.5) diffuseColor.rgb *= uSwChar;   // Fire "furnace" mode darkens the body
 - after <emissivemap_fragment>, chunk EMIT: edge line (HDR, only blade), fresnel rim in skill colour, jade light swJadeE = swTint*uSwJade*swJade*(0.16+0.24*glow+0.4*flash) (Fire mode: swJadeE = uSwHeat*swJade*(...) embers, plus a heat band on the blade), hit flash += swC*min(flash,1.5)*0.55, dissolve edge.
 - replaces "vec3 outgoingLight = totalDiffuse + totalSpecular + totalEmissiveRadiance;" with OUTGOING: outgoingLight = (totalDiffuse+totalSpecular)*uSwLight + totalEmissiveRadiance; then subtracts the part of swJadeE that would push luminance over 0.95 (jade fills only headroom under bloom threshold 1.0, never blooms).
 - SWORD_LOOK uniforms shared by all swords: edge, mode (0 steel=Metal element, 1 furnace=Fire element), heat, char, heatFrom, time. SWORD_LIGHT gain.
2) blades.ts: guardBand(geometry) finds the run of heights round y=0 whose cross-section half-width > 2x the blade's width ("Clear Wind: its ring") -> [g0,g1]. auraAnchorsOf(...) returns AuraAnchors { profile, bladeFrom, guardFrom, ring: {y:(g0+g1)/2, r: guardHalf} | null, guardHalf (max |x| of vertices in the band), tasselFrom }. modelOf(geometry, material, jade, real, source, ring) computes guard, bladeFrom = max(0.01, g1+0.01), edgeField, patchSwordMaterial(material, {bladeFrom, jade}) and aura anchors. Two models share it: the full GLB (hero/lead swords) and a 3,200-tri textured LOD (mid swords), same UV map. overlayModel() clones the material and re-patches it. WeaponDef.motif {jade, ring?: boolean}; only Clear Wind has ring:true. AuraAnchors.ring is currently used only by aura layers, not by the material. NOTE: ring.r is guardHalf (max |x| in the band), which may include the cloud brackets sticking out; the hole's inner radius is not measured anywhere.
3) real-swords.ts: far swords (key 7 "river" of 88 swords, 35-130 px long) are impostors: an atlas baked in Blender from the same GLB under a fixed lookdev light (tLit, premultiplied, plus tMask: r = edge field, g = blade flag, a = coverage), 4 rows = rolls [0,30,60,90] deg round the long axis, cells 512x128, tip right. Meta (clear-wind-impostor.json): u0 .035, u1 .965, guardU .3111, bladeFromU .3886, ringU .31109, ringR .08008 (centre and outer radius along the cell, in u units; declared in SwordAtlasMeta but UNUSED), rollWidth [1,.8966,.5862,.3793]. Fragment: rows blended by vRoll; cellUv(row) = vec2(vUv.x, 1 - (row + 0.5 - vUv.y*0.5)/rows) so vUv.y in [-1,1] spans the cell height; col = c.rgb*uGain*uLight; furnace: col *= uChar, + heat band; flash; edge line. gl_FragColor = vec4(col*a, c.a*a). A second program FRAGMENT_HALO adds an analytic mantle around the sword.
4) Lab gate tools: src/lab/aura-gates.ts drawSwordMask renders blade red, guard band (ring + cloud guard) green, hilt blue. Scenario scripts/visual/scenarios/lab-element-parity.mjs captures fixed-clock frames (key 1 play + zoom camera, key 7, K5) for before/after pixel comparison; QS adds URL flags.

CONSTRAINTS
- Metal (steel mode) must stay pixel-identical OUTSIDE the ring region; Fire (furnace) likewise identical outside the ring. Inside the ring region only the material changes; geometry, silhouette and UVs untouched; the ring must keep >= 95 % of its pixels (no discard, no holes) at every frame.
- No bloom from the ring: anything emissive stays under luminance 0.95 (same headroom rule as swJadeE), no channel over 0.86; only the blade's edge line may bloom.
- Keep the pale gold far from coin gold #FFC83A and from the typing cyan #7FF5E0; white jade must read as jade (soft, slightly translucent, satin), not as chalk, plastic or chrome.
- The beads (hue mask) keep their pale jade light. The cloud brackets in the approved image are white porcelain with pale-gold rims: if your mask covers them, that is acceptable or even desired, say which.
- Zero allocation per frame; load-time measurements allowed; shader cost small (the river draws 88 swords at <= 11.5 ms p95 total frame).
- Far impostors cannot re-bake in this ticket unless you argue a re-bake is clearly better (the bake script scripts/models/blender/bake_sword_impostor.py exists and could also emit a ring mask channel); the worker is a code agent (Codex) without Blender UI; Blender CLI exists on the machine.
- Taste: anime/donghua xianxia, luxurious, radiant, never realism as the goal, never plain.

DELIVER
1) analysis: why the hue mask misses the chrome ring, what defines the ring geometrically on this mesh, risks (cloud brackets, collar, beads, the blade/tang near the ring, the LOD, the dissolve and flash paths, Fire mode).
2) the solution as ordered steps with reasons: (a) load-time measurement of the ring (centre y, outer radius, inner hole radius, the silver outer rim band) from the geometry, with the exact algorithm; (b) the exact GLSL for the geometric mask in vSwP space (radial bands: hole-edge gold line, white jade disc, outer gold line, silver rim kept or not; soft edges by fwidth), injected where (which three.js chunks: color_fragment, roughnessmap_fragment, metalnessmap_fragment, etc.), and the exact material values: albedo (linear), metalness, roughness for white jade and for pale gold, how the texture's detail is kept (luminance modulation), any wrap/translucency fake and its cap; (c) Fire mode behaviour inside the ring; (d) the impostor: the exact cell-space mask (u band, per-row ellipse with the roll, coverage, excluding the blade flag) and recolour formula; (e) uniforms/TS API changes (names), and how AuraAnchors/ringU/ringR feed them.
3) checks with numbers: ring pixel keep >= 95 %, outside-ring parity (exact or a tolerance you justify), colour check of the ring against the samples (e.g. OKLab distance), tsc/vitest, before/after captures.
4) what you are not sure about. Cite a source (three.js docs/source chunk names, PBR references) for every factual claim.
…
Show more
````

## Turn 2 · assistant (ChatGPT)

````text
ChatGPT said:
Clear Wind — White Jade Ring Shader Implementation

Project: Tu Tien · three.js r17x / WebGL2 / TypeScript
Scope: Clear Wind GLB, 3,200-triangle LOD, and far-sword impostors
Decision: Geometric shader mask. No texture repainting.

1. Analysis and architecture decision
1.1 Why the existing hue mask fails

The current shader identifies jade using:

glsl
float swJade =
    smoothstep(
        0.07, 0.17,
        (swC.g - swC.r) / max(swC.g, 0.04)
    ) *
    smoothstep(-0.05, 0.0, swC.g - swC.b);

This is a colour classifier, not a material classifier.

The pale-green beads have enough green dominance to activate swJade.

Chrome-silver pixels have approximately equal RGB channels, so their green dominance is close to zero.

White jade is nearly neutral too. Detecting it through green dominance would be unreliable even after recolouring.

Changing the hue thresholds globally would risk selecting blade steel, silver fittings, and other neutral surfaces.

Therefore, retain swJade for the existing green-bead illumination, and introduce a separate geometric mask, swRingMask, for the annulus.

The two masks must have different responsibilities.

1.2 What defines the ring geometrically?

The supplied coordinate system establishes:

Sword length along local Y.

Ring centre near the guard, y ≈ 0.

Ring positioned approximately in the local XY plane.

Front and back surfaces distinguished along Z.

A circular opening around the ring centre.

The primary ring coordinate is therefore:

𝑟
=
(
𝑥
−
𝑐
𝑥
)
2
+
(
𝑦
−
𝑐
𝑦
)
2
r=
(x−c
x
	​

)
2
+(y−c
y
	​

)
2
	​


where c_x and c_y are measured from the mesh.

The mask is an annular region between an inner hole radius and an outer radius, with an additional depth restriction where useful.

Important limitation: A purely radial shader mask cannot distinguish two different mesh surfaces occupying the same local XYZ region. This matters for cloud brackets, beads, and fittings attached to the ring.

The recommended implementation consequently uses:

Load-time geometric measurements.

A radial annular shader mask.

A conservative depth restriction.

Existing jade-colour recognition to protect the beads.

Explicit acceptance tests for adjacent fittings.

It does not replace the GLB, its vertices, its UV mapping, or its source textures.

1.3 Verified three.js integration points

I checked the actual three.js r170 shader source, rather than relying on newer documentation alone.

Shader insertion point

	

Purpose




After <color_fragment>

	

Compute geometric mask and replace base colour




After <roughnessmap_fragment>

	

Override roughnessFactor inside the ring




After <metalnessmap_fragment>

	

Override metalnessFactor inside the ring




After <emissivemap_fragment>

	

Preserve bead illumination; control ring-specific emission




Before <opaque_fragment>

	

Apply final ring HDR protection

In r170, the roughness and metalness chunks produce roughnessFactor and metalnessFactor. The physical lighting calculation subsequently consumes those variables. Therefore, overriding them after their respective chunks changes PBR behaviour without editing the underlying ORM texture. 
GitHub
+3

This is essential: changing only diffuseColor.rgb could make the ring lighter while leaving its chrome-like metalness and sharp specular reflections intact.

The proposed shader patch must change all three material properties together.

1.4 Material interpretation

The glTF metallic-roughness model distinguishes metal and dielectric surfaces. Metalness affects both diffuse response and specular colour, while roughness controls reflection sharpness. 
Khronos Registry
+1

For this ticket:

White jade: predominantly dielectric, satin rather than mirror-like.

Pale gold: a deliberately subdued metallic accent.

Silver rim: preserve the existing material.

Jade beads: preserve their current colour and illumination.

Cloud brackets: allow controlled white-jade/porcelain recolouring where the geometric mask overlaps, but preserve recognisable pale-gold edging.

The shader should create the approved luxury anime/donghua appearance through disciplined highlights and material separation, without adding a broad glowing aura around the ring.

2. Implementation plan
Step 1 — Measure the actual annulus at load time

Files: blades.ts, new helper ring-geometry.ts

Do not use guardHalf directly as the ring radius. It can include projecting cloud brackets. Likewise, ring.y is a useful starting estimate, not a verified ring centre.

Use a geometry-driven fitting pass once per model, before calling patchSwordMaterial().

Required output

TypeScript
interface SwordRingGeometry {
  cx: number;
  cy: number;
  innerR: number;
  outerR: number;
  innerGoldEnd: number;
  outerGoldStart: number;
  silverStart: number;
  zMin: number;
  zMax: number;
  confidence: number;
}

All coordinates are in the same local space as vSwP. Radii are model-local lengths, not pixels or UV values.

Exact fitting procedure

Prepare triangle data. Read position, normal where available, and index from the normalized BufferGeometry. If the geometry is non-indexed, process each consecutive triangle. Compute geometric face normals from triangle edges; do not depend solely on imported smoothed vertex normals.

Define the search neighbourhood. Let R0 = auraAnchors.ring.r and Y0 = auraAnchors.ring.y. Consider guard-region triangles whose projected XY bounding boxes intersect the disc centred at (0,Y0) with radius 1.25 * R0. Retain sufficiently front/back-facing candidates with abs(faceNormal.z) >= 0.55 and projected area greater than 1e-8 * R0². This reduces contributions from tangs and thin, nearly edge-on geometry. The thresholds are proposed fitting parameters, not properties guaranteed by Tripo.

Find the centre. Evaluate candidate centres (cx,cy) with cx from -0.10R0 to +0.10R0 and cy from Y0-0.15R0 to Y0+0.15R0, both in increments of 0.02R0. Include the initial centre exactly. The limited search assumes the ring is centred near the established guard anchor.

Collect radial intersections. For each candidate centre, cast 256 evenly spaced radial half-lines in the XY plane. Intersect each half-line with the projected triangles. Each triangle supplies an interval of radial distances. Sort and merge intervals with endpoint tolerance 1e-4 * R0.

Identify the recurring annular band. For each angle, consider intervals with inner distance in [0.12R0, 0.85R0], outer distance in [0.35R0, 1.25R0], and positive width at least 0.08R0. Choose the interval minimizing distance to the median inner/outer boundaries of the other angles, iterating median selection until unchanged or for at most eight iterations. Missing intervals count as failures. This rejects most isolated beads, collar projections, and bracket overhangs because they do not form a continuous circular band.

Score the centre. Among candidate centres, prefer the one with the lowest

Plain text
score =
    MAD(innerDistances) / R0
  + MAD(outerDistances) / R0
  + 2 * missingAngleFraction

where MAD is the median absolute deviation. Break ties by smallest distance to (0,Y0), then cx, then cy. Set innerR and outerR to the median fitted boundary distances.

Verify the fit. Require at least 90% valid angles, innerR < outerR, both boundary MAD values below 0.06R0, and fewer than 5% of sampled interior-ring points falling on a projected gap. Otherwise fail the automated fit rather than quietly selecting guardHalf.

Measure depth. Take triangle samples falling within the fitted annular region, at least 5% of the annulus width away from both radial edges. Among front/back-facing samples, use the 10th and 90th percentiles of interpolated local Z; expand by 0.05R0 on each side to establish zMin and zMax. Validate that these bounds encompass both visible faces and the bevel.

Find the silver perimeter. In the outermost 15% of the fitted radius, examine face-normal changes by radial position. If an approximately circular transition from disc face to bevel occurs across at least 75% of valid angular samples, take its median radius as silverStart.

Handle an indistinguishable perimeter. If no consistent geometric bevel or ridge exists, assign silverStart = 0.94 * outerR. This is an explicit design fallback, not a claimed geometric measurement. A material boundary painted solely into a texture cannot be recovered reliably from geometry alone.

For a missing or unreliable automatic fit, let the worker supply a versioned, Clear-Wind-specific measurement record after inspecting the geometry and debug renders. These values remain geometric measurements/constants; they are not texture edits.

Why not automatically cut a new hole? The approved requirement prohibits modifying geometry or discarding pixels. If the LOD has filled its hole during simplification, the material shader cannot legitimately recreate that opening.

Ring proportions

Use the measured radii to define the decorative bands:

Region

	

Proposed boundaries




Inner hole

	

r < innerR




Inner pale-gold line

	

innerR to innerR + 0.020 * outerR




White jade body

	

End of inner gold to start of outer gold




Outer pale-gold line

	

silverStart - 0.025 * outerR to silverStart




Polished silver outer rim

	

silverStart to outerR

Validate:

Plain text
0 < innerR
innerR < innerGoldEnd
innerGoldEnd < outerGoldStart
outerGoldStart < silverStart
silverStart < outerR

If a measured ring is too narrow for these proportions, scale both gold-line widths down proportionally until each occupies no more than 15% of the annulus thickness.

The result preserves the desired hierarchy:

Schematic of the radial material layout, not a rendering of the actual GLB. The original geometry determines the hole and outer silhouette.

Step 2 — Introduce the ring GLSL

File: sword-material.ts

The recommended mask computes its radial coordinate using vSwP.xy, and a depth window using vSwP.z.

Declare the following uniforms and helper once in the fragment-shader header:

glsl
#ifdef SW_CLEAR_WIND_RING

// cx, cy, innerR, outerR
uniform vec4 uSwRingA;

// innerGoldEnd, outerGoldStart, silverStart
uniform vec3 uSwRingB;

// zMin, zMax
uniform vec2 uSwRingZ;

uniform vec3 uSwRingJadeColor;
uniform vec3 uSwRingGoldColor;

// Used after color_fragment; unchanged elsewhere.
float swRingProtected = 0.0;
float swRingJadeWeight = 0.0;
float swRingGoldWeight = 0.0;

// fwidth supplies a screen-space antialiasing scale.
float swBand(float x, float lo, float hi, float w) {
    return smoothstep(lo, lo + w, x) *
           (1.0 - smoothstep(hi - w, hi, x));
}

#endif

fwidth is supported by the WebGL2 fragment shader and is commonly used to anti-alias procedural edges. 
MDN
+1

Within the existing chunk inserted immediately after <color_fragment>, compute the original hue mask first, then the new geometric material weights:

glsl
#ifdef SW_CLEAR_WIND_RING

vec2 swOffset = vSwP.xy - uSwRingA.xy;
float swR = length(swOffset);
float swOuterR = uSwRingA.w;

float swInnerGoldEnd = uSwRingB.x;
float swOuterGoldStart = uSwRingB.y;
float swSilverStart = uSwRingB.z;

float swMinLine = min(
    swInnerGoldEnd - uSwRingA.z,
    swSilverStart - swOuterGoldStart
);

float swAA = min(
    max(fwidth(swR), 1e-6 * swOuterR),
    0.24 * swMinLine
);

float swZAA = max(fwidth(vSwP.z), 1e-6 * swOuterR);
swZAA = min(swZAA, 0.24 * (uSwRingZ.y - uSwRingZ.x));

float swDisc = swBand(
    swR, uSwRingA.z, swOuterR, swAA
);

float swDepth = swBand(
    vSwP.z, uSwRingZ.x, uSwRingZ.y, swZAA
);

// Protect the existing bead material.
float swBeadKeep = 1.0 - swJade;

swRingProtected = swDisc * swDepth;

// Radial material ownership.
float swHoleGold = 1.0 - smoothstep(
    swInnerGoldEnd - swAA,
    swInnerGoldEnd + swAA,
    swR
);

float swSilver = smoothstep(
    swSilverStart - swAA,
    swSilverStart + swAA,
    swR
);

float swOuterGold = smoothstep(
    swOuterGoldStart - swAA,
    swOuterGoldStart + swAA,
    swR
) * (1.0 - swSilver);

float swWhite = max(
    0.0,
    1.0 - swHoleGold - swOuterGold - swSilver
);

swRingJadeWeight =
    swRingProtected * swBeadKeep * swWhite;

swRingGoldWeight =
    swRingProtected * swBeadKeep *
    (swHoleGold + swOuterGold);

float swChange = clamp(
    swRingJadeWeight + swRingGoldWeight,
    0.0, 1.0
);

// swC was captured before applying the furnace char.
float swY = dot(
    swC,
    vec3(0.2126, 0.7152, 0.0722)
);

// Retain modest baked surface variation.
float swJadeDetail =
    clamp(1.0 + 0.22 * (swY - 0.55), 0.90, 1.10);

float swGoldDetail =
    clamp(1.0 + 0.10 * (swY - 0.55), 0.94, 1.05);

vec3 swWhiteColor =
    uSwRingJadeColor * swJadeDetail;

vec3 swGoldColor =
    uSwRingGoldColor * swGoldDetail;

// The original colour remains unchanged where mask == 0.
diffuseColor.rgb =
    diffuseColor.rgb * (1.0 - swChange) +
    swWhiteColor * swRingJadeWeight +
    swGoldColor * swRingGoldWeight;

#endif

This code assumes swC and swJade already exist in the preceding part of the project’s existing JADE insertion.

Integration detail: The existing Fire uSwChar multiplication should execute after this recolouring, with a ring exemption described in Step 4. Do not leave the old unconditional multiplication ahead of the new code.

The mask is zero outside the fitted radial/depth region, so the existing colour is preserved there. The band boundaries are antialiased inward, rather than expanding onto neighbouring geometry.

One qualification: this procedural mask respects geometry in coordinate space, but it is not a semantic component selector. Any cloud surface within the same fitted volume can also be recoloured. That is acceptable for porcelain-like brackets; unwanted collar or blade contamination is not.

Step 3 — Override the actual PBR properties
Material constants

Use these as the initial production values. They are art-direction choices, not scientifically measured jade or gold properties.

White jade

#DFDDDF · sRGB

Pale gold

#D4B793 · sRGB

Property	White jade	Pale gold
Linear albedo R	0.73791	0.65837
Linear albedo G	0.72306	0.47353
Linear albedo B	0.73791	0.29177
Metalness	0.00	0.72
Roughness	0.58	0.32

The linear albedo numbers are the sRGB-transfer conversions of the approved median colours. three.js performs material lighting in Linear-sRGB; supplying the hex values directly as GLSL floats would be incorrect. 
Three.js
+1

After <roughnessmap_fragment>, insert:

glsl
#ifdef SW_CLEAR_WIND_RING
float swMaterialWeight =
    swRingJadeWeight + swRingGoldWeight;

roughnessFactor =
    roughnessFactor * (1.0 - swMaterialWeight)
    + 0.58 * swRingJadeWeight
    + 0.32 * swRingGoldWeight;
#endif

After <metalnessmap_fragment>:

glsl
#ifdef SW_CLEAR_WIND_RING
metalnessFactor =
    metalnessFactor * (1.0 - swMaterialWeight)
    + 0.00 * swRingJadeWeight
    + 0.72 * swRingGoldWeight;
#endif

These override the sampled ORM properties only inside the recoloured bands. Outside, the original maps retain their complete effect.

Keep some normal-map detail

Preserve the existing normal texture. If the current chrome bake produces excessively sharp-looking surface relief, reduce the normal-map perturbation only on the jade.

Immediately after <normal_fragment_maps>:

glsl
#ifdef SW_CLEAR_WIND_RING
normal = normalize(mix(
    normal,
    nonPerturbedNormal,
    0.15 * swRingJadeWeight
));
#endif

In r170, nonPerturbedNormal is computed before the normal-map perturbation, making this interpolation possible without changing UVs or textures. 
GitHub
+1

The 15% reduction is a starting value. It retains most surface detail while letting roughness control the satin appearance.

Subtle jade translucency approximation

Do not introduce transmission, refraction, screen-space distortion, or an additional rendering pass.

For a minimal, stylistic suggestion of luminous jade, add a small grazing-angle fill after <emissivemap_fragment> and before lighting accumulation:

glsl
#ifdef SW_CLEAR_WIND_RING
float swFacing = clamp(
    dot(
        normalize(normal),
        normalize(vViewPosition)
    ),
    0.0, 1.0
);

float swWrap =
    0.018 *
    pow(1.0 - swFacing, 2.0) *
    swRingJadeWeight;

totalEmissiveRadiance +=
    vec3(0.80, 0.84, 0.86) * swWrap;
#endif

Maximum added channel contribution is under 0.016 linear. It is a fake translucency cue, not actual subsurface scattering.

The approved look should come primarily from the PBR albedo and roughness. If this fill looks milky or self-illuminated, set the coefficient to zero.

Step 4 — Preserve the Fire and flash paths

The white-jade annulus must remain white jade in both Metal and Fire modes. Fire may animate the steel blade and its surrounding aura, but it must not turn this distinctive fitting into charcoal or orange-hot metal.

Replace the existing unconditional furnace multiplication with:

glsl
if (uSwMode > 0.5) {
#ifdef SW_CLEAR_WIND_RING
    diffuseColor.rgb *= mix(
        uSwChar,
        vec3(1.0),
        swRingProtected
    );
#else
    diffuseColor.rgb *= uSwChar;
#endif
}

Expected behaviour:

Surface

	

Metal

	

Fire




Blade

	

Existing steel

	

Existing furnace




White-jade annulus

	

White jade

	

White jade




Gold lines

	

Pale gold

	

Pale gold




Silver perimeter

	

Existing polished silver

	

Protected from furnace char




Green beads

	

Existing bead illumination

	

Existing bead illumination retained




Everything else

	

Unchanged

	

Unchanged

For the existing EMIT injection:

Leave swJadeE operational for the pale-green beads.

Multiply the broad skill-coloured Fresnel contribution by 1.0 - swRingProtected.

Apply the same exemption to any blade heat-band term that can overlap the annulus.

Keep the existing blade-edge HDR line unchanged outside the ring.

Use the recoloured surface, rather than the old silver swC, as the hit-flash base inside the protected region.

For the last point:

glsl
vec3 swFlashBase = swC;
#ifdef SW_CLEAR_WIND_RING
swFlashBase = mix(
    swC, diffuseColor.rgb, swRingProtected
);
#endif

Then substitute swFlashBase only in the existing hit-flash colour contribution. Keep the flash timing and multiplier unchanged.

Hard protection against ring bloom

The existing swJadeE headroom calculation controls one emissive contribution, but it does not cap specular reflection or all flash paths.

For a strict guarantee, add a final check immediately before <opaque_fragment>:

glsl
#ifdef SW_CLEAR_WIND_RING
if (swRingProtected > 0.0) {
    outgoingLight = min(
        outgoingLight,
        vec3(0.86)
    );
}
#endif

This is in linear scene space, before the standard tone-mapping and output-colour-space chunks. The r170 source confirms that ordering. 
GitHub
+2

This guarantees that no protected ring fragment exceeds 0.86 in any linear RGB channel at this point. Consequently, its luminance cannot exceed 0.86, safely below the bloom threshold of 1.0.

It does not guarantee that other rendered layers composited on top of the ring are below the threshold. Test them separately.

Dissolve rule: Do not add alpha fading, alpha testing, or discard to the new ring shader. If the existing dissolve path can discard ring fragments, exempt the protected annular region from that discard before it executes. Preserve the original dissolve condition everywhere else.

This is necessary to satisfy the requirement that the ring retain at least 95% of its visible pixels even during dissolve frames. It also means the protected fitting may outlive a dissolving blade; that visual consequence should be included in the owner's comparison captures.

Step 5 — Implement the far-impostor treatment

Files: real-swords.ts, clear-wind-impostor.json

I recommend keeping the current atlas for the first implementation. A shader-side correction is cheaper to integrate and can be evaluated at the actual 35–130 px sword sizes before committing to an offline re-bake.

However, the impostor cannot use vSwP. It needs an ellipse in atlas-cell coordinates.

Coordinate calculation

The provided metadata gives:

Plain text
ringU = 0.31109
ringR = 0.08008
cellWidth = 512
cellHeight = 128

A circular front-facing ring has an expected vertical radius, in normalized cell coordinates, of:

𝑟
𝑣
=
0.08008
512
128
=
0.32032
r
v
	​

=0.08008
128
512
	​

=0.32032

For each roll row, scale that vertical radius using its existing rollWidth value.

glsl
float swCellV = 0.5 + 0.5 * vUv.y;

vec2 swEllipse = vec2(
    (vUv.x - uSwRingU) / uSwRingR,
    (swCellV - 0.5) /
        (uSwRingR * 4.0 * rollWidth)
);

float swEllipseR = length(swEllipse);

Here, uSwRingU = 0.31109, uSwRingR = 0.08008, and rollWidth is the value for the row currently being sampled. Do not interpolate a single ellipse after blending the two rows.

The existing row widths are:

Roll

	

Width scale




0°

	

1.0000




30°

	

0.8966




60°

	

0.5862




90°

	

0.3793

These are measured atlas values, not theoretical cosine values. Preserve them.

Annular masking and recolouring

For each row sample, define:

glsl
float ri = uSwRingInnerRatio;
float rs = uSwRingSilverRatio;

float aa = min(
    max(fwidth(swEllipseR), 1e-4),
    0.004
);

float disc = swBand(
    swEllipseR, ri, 1.0, aa
);

float innerGoldEnd =
    ri + uSwRingInnerGoldRatio;

float outerGoldStart =
    rs - uSwRingOuterGoldRatio;

float innerGold = 1.0 - smoothstep(
    innerGoldEnd - aa,
    innerGoldEnd + aa,
    swEllipseR
);

float silver = smoothstep(
    rs - aa,
    rs + aa,
    swEllipseR
);

float outerGold = smoothstep(
    outerGoldStart - aa,
    outerGoldStart + aa,
    swEllipseR
) * (1.0 - silver);

float white = max(
    0.0,
    1.0 - innerGold - outerGold - silver
);

// tMask.g is the blade classification.
float guardOnly = 1.0 - smoothstep(
    0.25, 0.75, maskSample.g
);

float coverage = step(1e-5, c.a);
float ring = disc * guardOnly * coverage;

vec3 originalStraight =
    c.rgb / max(c.a, 1e-5);

float jadeHue =
    smoothstep(
        0.07, 0.17,
        (originalStraight.g - originalStraight.r) /
            max(originalStraight.g, 0.04)
    ) *
    smoothstep(
        -0.05, 0.0,
        originalStraight.g - originalStraight.b
    );

float beadKeep = 1.0 - jadeHue;

float jadeWeight = ring * white * beadKeep;
float goldWeight = ring *
    (innerGold + outerGold) * beadKeep;

float amount = min(
    jadeWeight + goldWeight, 1.0
);

float luma = dot(
    originalStraight,
    vec3(0.2126, 0.7152, 0.0722)
);

float detail = clamp(
    1.0 + 0.22 * (luma - 0.55),
    0.90, 1.10
);

// c.rgb assumed premultiplied as specified.
c.rgb =
    c.rgb * (1.0 - amount)
    + c.a * uSwRingJadeColor *
        detail * jadeWeight
    + c.a * uSwRingGoldColor *
        detail * goldWeight;

The variables c and maskSample represent the existing tLit and tMask samples for the current row.

Use the same band ratios as the 3D model:

Plain text
uSwRingInnerRatio     = innerR / outerR
uSwRingSilverRatio    = silverStart / outerR
uSwRingInnerGoldRatio = innerGoldWidth / outerR
uSwRingOuterGoldRatio = outerGoldWidth / outerR

The colours use the same linear albedo values as the GLB material.

Apply the modified sample before the current uGain, uLight, flash, and furnace operations. Exempt the projected ring from uChar, heat coloration, and the existing non-blade flash emission wherever those operations could cause bloom.

After the existing brightness operations, apply the same protected-region cap of 0.86 linear RGB. Keep the current coverage and premultiplied-alpha expression unchanged.

The tMask.g exclusion is important: an ellipse alone could recolour part of the blade or tang in a roll-dependent projection.

Row blending

The proper sampling order is:

Plain text
sample row 0
→ compute row 0 geometric mask
→ recolour row 0

sample row 1
→ compute row 1 geometric mask
→ recolour row 1

blend corrected rows by existing vRoll
→ existing gain, flash and final alpha

This avoids a recoloured ellipse drifting across two differently projected sprite rows.

Re-bake decision

A pre-baked tLit atlas cannot fully reproduce a new PBR material because the original chrome reflections are already encoded in its RGB values. Recolouring can change hue and contrast, but cannot recover the lighting response of rough jade.

The shader treatment is nevertheless a reasonable first choice at the supplied impostor sizes.

Re-bake through the existing Blender CLI only if:

The ring still appears chrome-like after recolouring.

The ellipse visibly covers the hole or the blade.

Gold lines shimmer or produce unacceptable roll transitions.

Row-specific geometry cannot be matched accurately enough.

If triggered, use the Blender script to apply the same geometry-based ring assignment at bake time and regenerate tLit, optionally adding an independent ring mask channel. Do not repaint the base-colour texture. A re-bake would be an offline output regeneration, not a reversal of the owner's material decision.

Step 6 — TypeScript API and integration

Recommended API:

TypeScript
interface SwordRingOptions {
  geometry: SwordRingGeometry;
  jadeColorLinear: readonly [number, number, number];
  goldColorLinear: readonly [number, number, number];
}

interface SwordMaterialOptions {
  bladeFrom: number;
  jade: readonly [number, number, number];
  ring?: SwordRingOptions;
}

interface RingAtlasMeta {
  ringU: number;
  ringR: number;
  ringInnerRatio: number;
  ringSilverRatio: number;
  ringInnerGoldRatio: number;
  ringOuterGoldRatio: number;
}

Implementation sequence:

In blades.ts, compute SwordRingGeometry only when WeaponDef.motif.ring === true.

Perform separate measurements for the full GLB and 3,200-triangle LOD.

Extend AuraAnchors.ring with the measured geometry, while retaining y and r for backward compatibility. Keep the aura's existing outer reach if its visual anchoring depends on bracket overhang.

Pass the measured ring and linear colours to patchSwordMaterial().

Add a compiled ring shader variant only for Clear Wind.

Reapply the patch explicitly in overlayModel() after cloning the material.

Pass dimensionless geometric ratios to the impostor shader, using existing ringU, ringR, and rollWidth.

Do not change the shader behaviour of other weapons.

Use a cache key such as:

TypeScript
material.customProgramCacheKey = () =>
  ring ? "real-sword:ring-v1" : "real-sword:base-v1";

Geometry measurements belong in material-specific uniforms, not in the global SWORD_LOOK object shared between different weapon models. The two shader variants may share compiled code where appropriate, but must not share incorrect geometry measurements.

The three.js documentation explicitly covers onBeforeCompile and customProgramCacheKey for shader customization and program reuse. 
Three.js Docs

Create the uniform vectors and arrays once at model initialization. No allocations, texture creation, geometry traversal, or material recompilation may occur during gameplay frames.

3. Acceptance and verification
3.1 Automated gates

Gate

	

Required result




Geometry fitting

	

≥90% valid angles; boundary MAD < 6% of R0




Ring coverage

	

≥95% of reference ring pixels retained at every tested frame




New holes/discards

	

Zero introduced




Outside parity, pre-postprocessing

	

Exact shader output where the mask has zero support, allowing ≤1/255 readback quantization




Outside parity, final frame

	

Review only expected bloom/AA spill around the ring; no unrelated changes




Ring HDR

	

RGB channels ≤0.86 before tone mapping




Ring bloom

	

No ring-generated pixels above threshold 1.0




Runtime allocations

	

Zero new allocations per frame




Performance

	

River scene p95 ≤11.5 ms, with ≤0.3 ms p95 regression as a secondary target




Compilation

	

TypeScript, Vitest, and WebGL shader compilation pass

One distinction matters: even when a material change is perfectly confined to the annulus, postprocessing such as bloom can affect nearby screen pixels. Therefore, enforce exact outside-mask parity on the pre-postprocessing render, and assess the final composited image separately.

3.2 Colour validation

Use the approved sampled medians as the initial reference:

Material

	

Reference median

	

Suggested OKLab median-distance target




White jade

	

#DFDDDF

	

ΔOKLab ≤0.035




Pale gold

	

#D4B793

	

ΔOKLab ≤0.045




Pale-green beads

	

#C4E2CF

	

No meaningful change from baseline

Use the Euclidean distance in the OKLab L,a,b space, after converting captured sRGB colours correctly. The published transformation is available in Björn Ottosson's original specification. 
bottosson.github.io

These distances are proposed image-acceptance tolerances, not official perceptual thresholds. Compare median colours within clearly classified central jade/gold pixels, excluding anti-aliased edges, specular hotspots, and overlapping beads.

There is an important numerical incompatibility between the strict channel cap and the brightest approved samples. A linear channel of 0.86 corresponds to approximately sRGB #EFEFEF before tone mapping, whereas the approved p90 jade sample #F5F4F7 is brighter. The shader therefore cannot reproduce the complete approved p90 range under the strict cap.

Prioritize the owner's median colour, luxurious shading, and no-bloom requirement. Do not weaken the fixed cap merely to match the brightest concept-image pixels.

3.3 Required tests

Use src/lab/aura-gates.ts to add a separate ring-debug mode; the existing guard-band green mask is too broad because it includes cloud brackets.

Test the radial fitting and GLSL masks against synthetic indexed and non-indexed annuli, including shifted centres, bevels, cloud-like protrusions, and an unrelated central tang. Include a flat ring with no identifiable silver bevel to verify the explicit fallback.

For shader testing, assert that every expected #include replacement occurs exactly once. Compile and render every affected shader variant in a WebGL2 context; string tests alone cannot establish GLSL validity.

Run the repository's TypeScript and Vitest checks, for example npx tsc --noEmit and npx vitest run if those match the project configuration.

3.4 Before/after capture matrix

Extend scripts/visual/scenarios/lab-element-parity.mjs using its existing fixed-clock capture process.

Required owner review board

Scene	View	State
Hero Clear Wind	Close-up	Metal, idle
Hero Clear Wind	Close-up	Fire, active
Lead swords	Game camera	Metal, flash
LOD swords	Normal + zoom	Metal / Fire
Key 7 river	Game camera	0°, 30°, 60°, 90°
Dissolve	Close-up	Start / middle / end

For each scene, capture baseline and modified frames with identical clock, camera, seed, lighting, effect state, and renderer settings. Include a ring-only mask and a difference image alongside the beauty comparison.

For coverage testing, render the annulus in a controlled isolated pass so occlusion by other swords does not create false failures. Count surviving alpha-covered pixels against the fully opaque geometric reference at every sampled frame.

The owner-facing board should make it easy to answer three visual questions: does the annulus unmistakably read as white jade, do the gold and silver details remain refined, and does it still belong to the same premium Clear Wind sword?

4. Uncertainties and risks

The main unresolved issue is the actual Tripo topology. The GLB and LOD were not attached here, so the proposed fitting thresholds, depth bounds, and band positions are implementation candidates, not measured results. In particular, I cannot verify that the hole is unobstructed or that the silver perimeter has a separate geometric ridge.

The second risk is overlapping components. A radial mask plus depth restriction may still affect a collar or cloud surface at the same local coordinates. If this happens, the worker should first refine the fitted region or use an asset-specific geometric measurement. A semantic separation cannot always be achieved from position alone without an additional attribute, material partition, or geometry change.

The third risk is impostor fidelity. Roll-dependent ellipses are approximations, and the baked chrome lighting may prevent a convincing satin appearance. This is the strongest reason to allow an offline CLI re-bake later if the first owner comparison fails.

The fourth risk is the existing dissolve implementation. Its exact source was not supplied. Any discard, alpha-test, or coverage-changing operation must be inspected before promising the 95% visibility guarantee.

Finally, the actual installed three.js revision must be checked. The chunk ordering and variable names above were verified against r170. The project description says r17x, which is not enough to guarantee that a different installed revision has identical shader source.

5. Verified technical references

These are the principal sources behind the implementation:

three.js r170 — meshphysical shader — authoritative insertion order for colour, ORM, normal maps, lighting and final output.

three.js r170 — roughness chunk and metalness chunk — exact PBR factor variables.

three.js Material documentation — shader patching and program-cache keys.

three.js colour management — Linear-sRGB working values and texture colour spaces.

Khronos glTF PBR reference — metallic-roughness material interpretation.

MDN — shader derivatives — fwidth and WebGL2 support.

OKLab original reference — colour-distance calculations.

Final implementation decision

Implement the geometric annulus measurement and Clear-Wind-only shader variant first. Override albedo, metalness and roughness; preserve the beads, cloud detail where possible, existing alpha coverage, and all non-ring shader paths. Add the analytical ellipse treatment to the current impostor atlas without requiring an immediate re-bake.

Acceptance is determined by the fixed-clock before/after captures and the owner's approval. If the geometry cannot be fitted cleanly, use explicit asset-specific measurements rather than a dangerously broad mask. If the far atlas cannot lose its baked chrome appearance convincingly, regenerate that atlas through Blender CLI without repainting the source texture.

No GLB-specific measurements, compiled shader tests, frame captures, or performance benchmarks have been executed here; those remain verification work for Codex against the actual project.
````

## Turn 3 · user

````text
Review your latest full answer above against the brief, the facts and the constraints. It FAILS only for a real defect: a wrong fact or source, a step that would not work, a missing step the goal needs, a contradiction with the constraints or the owner's decisions, or a part too vague for a worker to execute. Wording, style and optional extra ideas are not defects.
If it is correct and accurate, answer with exactly one line: VERDICT: PASS (you may add one line "Optional:" with ideas that do not change the verdict)
Otherwise answer: VERDICT: FAIL, then list each defect, then give the corrected FULL analysis and solution (not a diff).
````

## Turn 4 · assistant (ChatGPT) [INCOMPLETE: still streaming when saved at 13:50:58]

````text
ChatGPT said:
VERDICT: FAIL

The overall approach is consistent with the owner's decision, but the previous design has implementation defects that prevent it from being handed to Codex as written.

Defects

1. The geometric fitting algorithm is not reliable enough. Merging all projected triangle intervals can fill the ring's hole with triangles belonging to the collar, tang or cloud brackets. The proposed centre search and confidence score do not resolve overlapping geometry. The fitted radii could therefore describe the guard assembly rather than the annulus.

2. The silver-rim detection is under-specified. Detecting a face-normal transition does not necessarily identify the material boundary. A geometrically smooth rim with a texture-defined silver border needs an explicitly defined fallback and validation.

3. The shader variant is not actually enabled. The GLSL uses #ifdef SW_CLEAR_WIND_RING, but the TypeScript implementation never defines that macro. Changing customProgramCacheKey() alone does not enable conditional GLSL. Consequently, Codex could implement the stated code and obtain no ring recolouring.

4. The material mask can affect unrelated fittings. The radial/depth test can select blade, tang, collar, cloud or bead surfaces occupying the same region. Protecting only the original green hue mask is insufficient to guarantee that non-ring steel remains unchanged.

5. The original normal-map modification is not justified. Reducing mapped normals by 15% may erase engraved detail on precisely the surfaces where the owner wants luxury. It also introduces an unnecessary extra variable into the first material comparison.

6. The Fire integration is incomplete. The proposed instructions do not precisely resolve every affected path: furnace char, blade heat, skill Fresnel, hit flash, existing bead emission and the shared outgoing-light gain. The bead colour and emission also need an explicit rule in Fire mode.

7. The dissolve instruction can violate the existing animation. Exempting the ring from an existing dissolve may leave a floating annulus after the sword disappears. It contradicts the requirement to change material appearance without redesigning the dissolve. Coverage must be tested against the original frame's intended visibility.

8. The impostor ellipse is not sufficiently grounded. rollWidth describes the supplied atlas's projected width; it has not been established as the ring's projected minor-axis scale. The assumption that every row's ring centre is at vertical UV 0.5 is also unverified. The proposed mask may recolour the blade or empty space, especially at 60° and 90°.

9. The impostor coverage and premultiplication handling are incomplete. The previous code uses c.a for coverage without incorporating the authoritative tMask.a, and does not specify precisely where the ring brightness clamp occurs relative to gain, flash, row blending and the final premultiplied output.

10. The ring no-bloom guarantee is incomplete across rendering paths. Clamping one PBR material before <opaque_fragment> does not constrain an independent impostor program or a separately drawn halo. The earlier design also conflates the material-changed region with the broader ring-protection region.

11. The colour acceptance test needs a defined rendering pipeline. Directly comparing shaded gameplay pixels against concept-image median colours without controlling lighting, tone mapping and exposure can reject a correct albedo or accept an incorrect material.

12. Several integration and test steps are too vague for an implementation agent. In particular, the prior answer lacks concrete fallback semantics, shader injection validation, uniform ownership, coordinate-normalization checks and failure behaviour when the geometry cannot be isolated.

These are implementation defects, not objections to the approved geometric-mask approach.

Corrected full analysis and solution
1. Fixed decisions and technical basis

The implementation must deliver a white-jade annulus with two thin pale-gold borders and a preserved polished-silver perimeter. The source base-colour, ORM and normal textures remain unchanged. No vertices, indices, UV coordinates or visible silhouettes are modified.

The three representations must be treated independently:

Representation

	

Material correction

	

Geometry data




Full GLB, 14,728 triangles

	

PBR shader override

	

Full-resolution annulus measurement




Textured LOD, 3,200 triangles

	

Same PBR override

	

Independently measured LOD




Key 7 impostors, 88 swords

	

Linear-colour correction of tLit

	

Projected, roll-specific ellipse

Only Clear Wind receives this feature.

Verified three.js facts

The r170 meshphysical shader evaluates base colour, alpha handling, roughness and metalness before lighting. Its physical material then uses the resulting diffuseColor, roughnessFactor and metalnessFactor. 
GitHub
+3

The relevant source also confirms that normal and nonPerturbedNormal exist after the normal chunks, and that outgoingLight is finalized before <opaque_fragment>, tone mapping and output colour conversion. 
GitHub
+3

These facts support a PBR material override without rebuilding the material system.

Why the original hue test is insufficient

The existing swJade test responds to a positive green-minus-red difference. White jade and chrome silver are both nearly neutral; neither is reliably identifiable by that test. The green beads are a different material and should keep their established hue-based handling.

Use two independent classifications:

swJade: existing pale-green bead classification.

swRingJade / swRingGold: geometric annular material classification.

Do not alter the original swJade thresholds merely to find the silver ring.
````

## Check table (Claude, 04/11/2026, partial: the run stopped at the 14:00 hard stop)

| Claim | Source | Status | Note |
|---|---|---|---|
| The ring needs geometric masking because the hue mask only catches green-over-red texels | `src/view/skills/sword-material.ts` chunk `JADE` | Verified | The formula needs (g − r)/g ≥ 0.07; a grey chrome texel gives ~0 |
| `roughnessFactor` and `metalnessFactor` exist after `roughnessmap_fragment` / `metalnessmap_fragment`, both before `lights_physical_fragment` | `node_modules/three/src/renderers/shaders/ShaderLib/meshphysical.glsl.js` lines 173–186; `ShaderChunk/roughnessmap_fragment.glsl.js`, `metalnessmap_fragment.glsl.js` (three 0.170.0) | Verified | Injecting after `metalnessmap_fragment` can override both and `diffuseColor` |
| White jade #DFDDDF → linear (0.738, 0.723, 0.738); pale gold #D4B793 → linear (0.658, 0.474, 0.292) | sRGB transfer function, computed by Claude | Verified | Matches the numbers in ChatGPT's material table (0.73791 / 0.65837, 0.72306 / 0.47353) |
| Impostor vertical ring radius = ringR × cellW / cellH = 0.32032 (of the half cell) at broadside | `clear-wind-impostor.json` (ringR 0.08008, cells 512 × 128) | Verified arithmetic | Whether `rollWidth` (blade width per row) or cos(roll) should scale it for the disc is open |
| Ring fit by radial intervals, centre search and MAD scoring; fail loudly instead of falling back to `guardHalf` | ChatGPT proposal | Unverified | Not yet reviewed against the GLB; Claude's draft uses an occupancy raster and flood fill |
| Gold line widths 0.020 / 0.025 × outerR; measured `silverStart` | ChatGPT proposal | Unverified | Art-direction values; to be judged on the before/after images |
| Fire: the ring is protected from `char`; beads keep their light | ChatGPT proposal, Claude's draft | Agreed, unverified in render | |
