# Failures we hit

Each entry gives what happened, why it happened, and the rule that now prevents it.

1. **Prompts before research gave a villain-like hero, twice** (Last Line, 01/11/2026).
   - **What:** a dark full-face mask, two horn-like fins at the ears, smooth beige plates. The owner: "cái mặt nạ và 2c ở tai nhìn không kiểu sang trọng, hoàng gia chút nào".
   - **Why:** no research and no appeal checklist; the prompt listed parts, not a design idea.
   - **Rule:** research first; then check the silhouette for villain cues (closed dark face, horns or spikes at the head). Checklist items 1 and 6.

2. **Smooth toy plates.**
   - **What:** the owner: "phần giáp cũng cần được thiết kế để nhìn hiện đại hơn nữa, chứ hiện tại nhìn có vẻ khá là đơn giản".
   - **Rule:** modern layered construction, named premium materials, panel lines, trims and inset light. Checklist items 4 and 5.
   - **On the model side:** low face counts made earlier models look like plastic. Keep the face floors in `docs/games/MODEL_QUALITY.md`.

3. **A ring painted behind the head.**
   - **What:** the third try drew the halo straight into the character image. The owner found it strange and asked whether it could be handled another way.
   - **Rule:** no glow or halo baked into the picture by default. Split the radiance kit by the researched [pipeline decision](pipeline-decision.md). One image cannot carry the whole kit, and redrawing that image again and again is the wrong loop.

4. **Views of different designs.**
   - **What:** Firefly changed the helmet per view, and its "back" view was a front. (Its six-image landmark set also came out in five styles.)
   - **Rule:** a turnaround, then each view in one ChatGPT chat; a detail-list consistency check; consistency as a judging criterion ([views and sources](views-and-sources.md)).

5. **A back view that was a front.**
   - **Rule:** state what must and must not show in each view, and check "a back is a back" before judging.

6. **Graded on a big sheet, failed in the game** (31/10).
   - **What:** icons accepted on 256 px sheets read as smudges at 16–24 px in the game.
   - **Rule:** a check tile at the real on-screen size from the play camera; design hardest the side the camera sees.

7. **Self-grades run high.**
   - **What:** my own 8 became 7 and 7 from blind judges; a generator graded its own icons 10/10, and only 4 of 20 reached 8 at real size.
   - **Rule:** two blind judges with neutral labels; never accept a tool's or my own grade.

8. **Building on one design without showing options.**
   - **Rule:** two or three directions; the owner picks.

9. **Rerolling a prompt after it plateaued.**
   - **Rule:** after two rounds with no real gain, change approach in the same report: more research, better references, ready-made sources, another tool.

10. **Reserved colours ignored.**
    - **What:** the first hero prompts used white-gold, but gold marks enemy Pack Leaders in Last Line. The hero was corrected to ivory and graphite.
    - **Rule:** list the reserved colours before writing the colour script. Checklist item 8.

11. **Accepting ChatGPT's answer unchecked.**
    - **Rule:** verify each key claim at its source, mark it, and give my own view ([research lenses](research-lenses.md)).
