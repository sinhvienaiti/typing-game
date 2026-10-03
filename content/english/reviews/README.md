# English-content editorial review ledger

`decisions.json` is intentionally empty until an editor makes explicit review
decisions.

Every decision is bound to:

- batch ID + record-set ID + stable record ID;
- SHA-256 of the exact source record being reviewed;
- the quality checks the reviewer is changing;
- an explicit target quality state;
- reviewer identity and review timestamp.

A stale digest is a hard failure. Publication is also a hard failure while any
required or existing check is `pending` or `fail`.

The source authoring/review-queue files remain immutable inputs. Publication
overlays accepted decisions at build time, which keeps review history separate
from imported/generated source content.
