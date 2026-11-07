"""Reproduce the approved English-only snapshot from four checksum-pinned exports.

This does not download mutable exports, change the approved pin, or approve content.
Only --write can replace canonical shards, and only with bytes matching the pin.
"""
import argparse
import base64
import bz2
import collections
import gzip
import hashlib
import io
import json
from pathlib import Path
import re
import tarfile

ROOT = Path(__file__).resolve().parent.parent
PIN_PATH = ROOT / "content/english/sources/tatoeba-english-2026-10-31.json"
ACTION_TAGS = {"vulgar", "vulgarity", "profanity", "offensive", "duplicate", "needs context", "not a sentence", "archaic"}


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def verify_inputs(directory, inputs):
    for item in inputs:
        file = directory / item["filename"]
        digest = hashlib.file_digest(file.open("rb"), "sha256").hexdigest()
        if file.stat().st_size != item["bytes"] or digest != item["sha256"]:
            raise ValueError(f"Upstream checksum mismatch: {file.name}")


def archive_rows(file, member):
    with tarfile.open(file, "r:bz2") as archive:
        # Read the named member directly; never extract untrusted archive paths.
        stream = archive.extractfile(member)
        if stream is None:
            raise ValueError(f"Missing archive member: {member}")
        for line in stream:
            yield line.decode("utf8").rstrip("\n").split("\t")


def extract_rows(directory):
    native = {r[2] for r in archive_rows(directory / "user_languages.tar.bz2", "user_languages.csv")
              if len(r) >= 3 and r[0] == "eng" and r[1] == "5"}
    rows = {}
    counts = collections.Counter()
    with bz2.open(directory / "eng_sentences_detailed.tsv.bz2", "rt", encoding="utf8") as stream:
        for line in stream:
            fields = line.rstrip("\n").split("\t")
            if len(fields) != 6 or fields[1] != "eng":
                raise ValueError("Malformed English detailed sentence row")
            counts["englishRows"] += 1
            sid, _, text, owner, created, modified = fields
            if owner not in native:
                continue
            counts["nativeOwned"] += 1
            if not 5 <= len(re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", text)) <= 30 or len(text) > 300:
                continue
            if not re.fullmatch(r"[A-Z][\x20-\x7e]*[.?!]", text) or re.search(r"https?://|www\.|\d|[<>\[\]{}@#]", text):
                continue
            if int(sid) in rows:
                raise ValueError(f"Duplicate upstream sentence ID: {sid}")
            rows[int(sid)] = dict(id=int(sid), text=text, owner=owner, ownerEnglishLevel=5,
                                  created=created, modified=modified, positiveReviews=[], negativeReviews=[], actionTags=[])
    counts["structurallyEligibleNativeOwned"] = len(rows)
    with (directory / "users_sentences.csv").open(encoding="utf8") as stream:
        for line in stream:
            fields = line.rstrip("\n").split("\t")
            if len(fields) != 5:
                raise ValueError("Malformed sentence review row")
            user, sid, review, _, modified = fields
            row = rows.get(int(sid))
            if row is None or modified < row["modified"]:
                continue
            if review == "-1":
                row["negativeReviews"].append(dict(user=user, modified=modified))
            if review == "1" and user in native and user != row["owner"]:
                row["positiveReviews"].append(dict(user=user, englishLevel=5, modified=modified))
    for fields in archive_rows(directory / "tags.tar.bz2", "tags.csv"):
        if len(fields) != 2:
            raise ValueError("Malformed sentence tag row")
        row = rows.get(int(fields[0]))
        if row is not None and (fields[1].startswith("@") or fields[1].lower() in ACTION_TAGS):
            row["actionTags"].append(fields[1])
    eligible = [r for _, r in sorted(rows.items()) if r["positiveReviews"] and not r["negativeReviews"] and not r["actionTags"]]
    for row in eligible:
        row["positiveReviews"].sort(key=lambda r: r["user"])
        if len({r["user"] for r in row["positiveReviews"]}) != len(row["positiveReviews"]):
            raise ValueError(f"Duplicate positive reviewer: {row['id']}")
    counts["sourceEvidenceCandidates"] = len(eligible)
    counts["twoOrMoreIndependentPositiveRatings"] = sum(len(r["positiveReviews"]) >= 2 for r in eligible)
    return eligible, dict(counts)


def encode_shards(rows):
    shards = []
    for offset in range(0, len(rows), 25000):
        group = rows[offset:offset + 25000]
        raw = ("\n".join(json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":")) for row in group) + "\n").encode("utf8")
        buffer = io.BytesIO()
        with gzip.GzipFile(filename="", fileobj=buffer, mode="wb", mtime=0, compresslevel=9) as compressor:
            compressor.write(raw)
        compressed = buffer.getvalue()
        descriptor = dict(path=f"content/english/sources/tatoeba-english-2026-10-31/{offset // 25000:03}.jsonl.gz.b64",
                          count=len(group), contentBytes=len(raw), contentSha256=sha256(raw),
                          compressedBytes=len(compressed), compressedSha256=sha256(compressed))
        shards.append((descriptor, base64.encodebytes(compressed)))
    return shards


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, default=ROOT / ".cache/english-content/tatoeba-english-intake")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    pin = json.loads(PIN_PATH.read_text())
    verify_inputs(args.input_dir, pin["upstreamInputs"])
    rows, analysis = extract_rows(args.input_dir)
    encoded = encode_shards(rows)
    if [desc for desc, _ in encoded] != pin["canonicalShards"] or analysis != pin["sourceAnalysis"]:
        raise ValueError("Extraction differs from approved canonical snapshot; refusing to replace it")
    for descriptor, data in encoded:
        file = ROOT / descriptor["path"]
        if args.write:
            file.parent.mkdir(parents=True, exist_ok=True)
            file.write_bytes(data)
        elif file.read_bytes() != data:
            raise ValueError(f"Canonical bytes differ: {file.name}")
    print(json.dumps(dict(status="PASS", candidates=len(rows), canonicalShards=len(encoded), publicationApproved=False)))


if __name__ == "__main__":
    main()
