import faiss
import numpy as np
from embeddings.embedder import model
import os
import pickle

INDEX_FILE = "faiss_index/index.faiss"
META_FILE = "faiss_index/meta.pkl"
os.makedirs("faiss_index", exist_ok=True)

def create_or_update_index(embeddings, chunks):
    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    faiss.write_index(index, INDEX_FILE)
    with open(META_FILE, "wb") as f:
        pickle.dump(chunks, f)

def search_index(query, top_k=10):
    if not os.path.exists(INDEX_FILE) or not os.path.exists(META_FILE):
        raise ValueError("Index or metadata file not found. Please index documents first.")

    index = faiss.read_index(INDEX_FILE)
    with open(META_FILE, "rb") as f:
        chunks = pickle.load(f)

    query_vec = model.encode([query])
    D, I = index.search(np.array(query_vec), top_k)
    results = []
    for i in I[0]:
        if i < len(chunks):
            results.append(chunks[i])
    return results
