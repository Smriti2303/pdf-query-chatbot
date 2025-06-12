import streamlit as st
from pdf_processor.extract_text import extract_text_from_pdf
from embeddings.embedder import generate_embeddings
from faiss_index.vector_store import create_or_update_index, search_index
from llm.llama_infer import get_llm_response
import os

# Setup
st.set_page_config(page_title="PDF Chatbot", page_icon="📚", layout="centered")
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Title Section
st.markdown("<h1 style='text-align: center;'>🤖 PDF Chatbot Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Ask questions from your uploaded documents – fast, offline, and smart!</p>", unsafe_allow_html=True)
st.divider()

# Icons Row
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("📄 PDFs Loaded", len(os.listdir(UPLOAD_DIR)))
with col2:
    st.metric("🧠 Model", "LLaMA (Offline)")
with col3:
    st.metric("⚡ Speed Tip", "Keep files small for faster answers")

# Folder/File Selector
folders = [f.name for f in os.scandir(UPLOAD_DIR) if f.is_dir()]
pdfs_in_root = [f for f in os.listdir(UPLOAD_DIR) if f.endswith(".pdf")]

if not folders and not pdfs_in_root:
    st.warning("📂 No PDFs or folders with PDFs found in 'uploads/'. Please add some.")
    st.stop()

options = ["📁 Root Folder"] + folders if pdfs_in_root else folders
selected = st.selectbox("Select PDF Source Location:", options)

folder_path = UPLOAD_DIR if selected == "📁 Root Folder" else os.path.join(UPLOAD_DIR, selected)
existing_pdfs = [f for f in os.listdir(folder_path) if f.endswith(".pdf")]

if not existing_pdfs:
    st.warning("❌ No PDFs found in selected location.")
    st.stop()

# PDF Indexing Section
with st.spinner("🔍 Reading and indexing selected documents..."):
    all_chunks, all_embeddings = [], []
    for pdf_file in existing_pdfs:
        file_path = os.path.join(folder_path, pdf_file)
        texts = extract_text_from_pdf(file_path)
        chunks, embeddings = generate_embeddings(texts)
        all_chunks.extend(chunks)
        all_embeddings.extend(embeddings)
    create_or_update_index(all_embeddings, all_chunks)

st.success(f"✅ Indexed {len(existing_pdfs)} PDF(s) from '{selected}'")

st.divider()

# Question Area
st.markdown("### 📝 Ask Your Question Below")

question = st.text_input("🔎 What do you want to know?", placeholder="e.g. What are the eligibility criteria?")
if question:
    with st.spinner("🧠 Thinking..."):
        context_chunks = search_index(question, top_k=5)
        context_text = "\n\n".join(context_chunks)

        prompt = f"""
You are an expert assistant. Based on the following document content, answer the user's question in detail.

Context:
{context_text}

Question: {question}

Answer:"""

        answer = get_llm_response(question, context_text)
        st.markdown("### 💡 Answer")
        st.write(answer)

# Help & Info
with st.expander("📘 How to Use"):
    st.markdown("""
    1. Place your PDFs inside the `uploads/` folder or within subfolders.
    2. Select a folder or root location from the dropdown.
    3. Enter your query in the input box.
    4. Get a smart answer extracted from your documents!
    """)

with st.expander("⚙️ Technical Info"):
    st.markdown("""
    - Embedding Model: Sentence Transformer
    - Vector Store: FAISS (offline)
    - LLM: Local LLaMA (via llama.cpp or similar)
    - UI: Built with Streamlit
    """)

st.caption("by Smriti Mahajan.")
