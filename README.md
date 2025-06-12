"""
# 📄 PDF Query Chatbot (Offline, Local LLM)

## Features
- Upload and process large PDFs (up to 50GB)
- Extract text using PyMuPDF
- Embed and chunk content
- Store and search with FAISS
- Answer using LLaMA 2 (local via llama.cpp)

## Setup Instructions

1. Clone the repo:
```bash
git clone https://github.com/yourname/pdf-chatbot.git
cd pdf-chatbot
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Download a local LLaMA GGUF model (7B recommended) and place it in `models/`

5. Run the app:
```bash
streamlit run app.py
```

## Notes
- No internet is required once setup is complete
- Uses only open-source tools and models
"""
