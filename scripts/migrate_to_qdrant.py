import json
from pathlib import Path

import importlib

# 1. Import the folder/package dynamically using a string
my_package = importlib.import_module("src.rag.qdrant_store")
from my_package import (
    load_store, ensure_collection, upsert_chunks, collection_size,
)

INDEX_PATH = Path("data/embeddings.json")

ROOT_DIR = Path(__file__).resolve().parent.parent
print(ROOT_DIR)
if str(ROOT_DIR) not in sys.path:
     sys.path.insert(0, str(ROOT_DIR))

print(f"Loading embeddings from {INDEX_PATH}...")
with INDEX_PATH.open() as f:
    index = json.load(f)  # list of {chunk_id, source_id, text, vector}
print(f"  {len(index)} chunks loaded from JSON")

# Separate chunks from vectors
chunks = [{k: c[k] for k in ("chunk_id", "source_id", "text")} for c in index]
vectors = [c["vector"] for c in index]

# Push to Qdrant
print("Connecting to Qdrant...")
store = load_store()
ensure_collection(store)

print(f"Upserting {len(chunks)} points into '{store.collection}'...")
upsert_chunks(store, chunks, vectors)

# Confirm
n = collection_size(store)
print(f"Done. Collection now has {n} points.")