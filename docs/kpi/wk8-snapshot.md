```markdown
# wk8-snapshot.md — Post-ingestion baseline

**Date:** YYYY-MM-DD
**Vector store:** Qdrant Cloud
**Collection:** capstone_chunks_v2 (N points, 1536 dim, cosine)
**Chunking strategy:** recursive (or structure-aware where possible)
**PII scrubbing:** regex + Presidio hybrid

## Headline numbers

| Metric | W7 (capstone_chunks) | W8 (capstone_chunks_v2) | Delta |
|---|---|---|---|
| Cost per query | $0.000XXX | $0.000XXX | ~0 (same models) |
| Latency p50 (ms) | XXX | XXX | ~0 (Qdrant handles both) |
| Retrieval hit rate | XX% | XX% | +Y pp (better chunks) |
| Grounded response rate | XX% | XX% | +Y pp (less garbage in chunks) |
| PII items scrubbed | 0 | N | ← new capability |

## Operational deltas

| Property | W7 | W8 |
|---|---|---|
| Metadata fields per chunk | 3 | 9 |
| Filtered retrieval possible | no | yes |
| PII risk | leak-prone | scrubbed at ingest |

## Method
- Same 20 golden-set questions from W5
- W7 baseline from wk7-snapshot.md
- W8 numbers from a fresh run against capstone_chunks_v2

## Interpretation
[why did hit rate move? Was it chunking or metadata? Anything surprising?]
```
