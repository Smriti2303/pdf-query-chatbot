from sentence_transformers import SentenceTransformer
from tqdm import tqdm
import numpy as np

def chunk_text(text, max_length=500):
    """Split text into smaller chunks."""
    words = text.split()
    chunks = [" ".join(words[i:i+max_length]) for i in range(0, len(words), max_length)]
    return chunks

model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embeddings(text):
    chunks = chunk_text(text)
    embeddings = model.encode(chunks, show_progress_bar=True)
    return chunks, embeddings