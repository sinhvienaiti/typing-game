from pathlib import Path

p = Path("admin/world-music-preview.test.mjs")
text = p.read_text()
old_policy = """      galaxies: {
        "2": {"""
new_policy = """      galaxies: {
        "3": {"""
old_assert = """  const world06Galaxy = galaxyPreview.worlds.find((world) => world.worldId === "world-06");
  assert.equal(world06Galaxy.states.normal.resolvedFrom, "galaxy-2.published.normal");
  assert.ok(world06Galaxy.states.normal.badges.includes("GALAXY FALLBACK"));"""
new_assert = """  const world11Galaxy = galaxyPreview.worlds.find((world) => world.worldId === "world-11");
  assert.equal(world11Galaxy.states.normal.resolvedFrom, "galaxy-3.published.normal");
  assert.ok(world11Galaxy.states.normal.badges.includes("GALAXY FALLBACK"));"""
if text.count(old_policy) != 1 or text.count(old_assert) != 1:
    raise SystemExit("Expected generated B04.2 Galaxy test shape not found exactly once.")
p.write_text(text.replace(old_policy, new_policy, 1).replace(old_assert, new_assert, 1))
print("Adjusted Galaxy fallback test to World 11 / Galaxy 3.")
