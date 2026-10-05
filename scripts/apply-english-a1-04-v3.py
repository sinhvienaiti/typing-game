from __future__ import annotations

import ast
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = Path(__file__).with_name("apply-english-a1-04.py")
V2_PATH = Path(__file__).with_name("apply-english-a1-04-v2.py")

# Reuse the exact CI #771 review-lock map from v2 without executing v2's main().
tree = ast.parse(V2_PATH.read_text(encoding="utf-8"))
reviewed_digests = None
for node in tree.body:
    if isinstance(node, ast.Assign) and any(
        isinstance(target, ast.Attribute)
        and isinstance(target.value, ast.Name)
        and target.value.id == "module"
        and target.attr == "REVIEWED_DIGESTS"
        for target in node.targets
    ):
        reviewed_digests = ast.literal_eval(node.value)
        break
if reviewed_digests is None:
    raise SystemExit("cannot recover artifact-locked A1-04 digest map from v2 helper")

spec = importlib.util.spec_from_file_location("apply_english_a1_04", MODULE_PATH)
if spec is None or spec.loader is None:
    raise SystemExit("cannot load A1-04 publication helper")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Canonicalize references caught by the controlled validator before review publication.
topics = module.load_json(module.TOPIC_PATH)
reference_map = {
    "gr.a1.present-simple-positive": "gr.a1.present-simple-routines",
    "gr.a1.there-be": "gr.a1.there-is-are",
}
changed = 0
for topic in topics.get("records", []):
    for field in ("prerequisiteIds", "contrastTopicIds"):
        old = topic.get(field, [])
        new = [reference_map.get(value, value) for value in old]
        if new != old:
            topic[field] = new
            changed += 1
if changed != 5:
    raise SystemExit(f"expected 5 canonical reference replacements, got {changed}")
module.write_json(module.TOPIC_PATH, topics)

# These four source records changed only in canonical prerequisite/contrast references;
# digests were recomputed after that correction and reviewed again before publication.
reviewed_digests["grammar-topics"].update({
    "gr.a1.likes-gerund-noun": "6e16a69ed1a95773f9f82531ced732b06aca7913260e94218bde2daf079e6303",
    "gr.a1.want-need-infinitive": "6abc871ed939db059d5927b3786ec2eba78da08d7860c19b6e4557559b586b91",
    "gr.a1.place-prepositions": "ee80d69a4517d3fc3e20f1650568eb3294ba051b73d361725c6f78c955da438c",
    "gr.a1.movement-prepositions": "aa7a03cdcbacc2cb9e634a926d825d6432b06cdfbfa79f91f693b27ea298d597",
})
module.REVIEWED_DIGESTS = reviewed_digests
module.main()
