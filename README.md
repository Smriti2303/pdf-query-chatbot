Great! Below is a professional and attractive `README.md` file tailored to your **PDF Query Chatbot** project, including how to set it up, how to run it, and how to avoid GitHub large file issues.

---

### ✅ `README.md` (copy this into a file named `README.md` in your project root)

````markdown
# 🤖 PDF Query Chatbot (Offline)

A local AI chatbot that allows users to upload PDFs and ask questions based on the document content. Perfect for querying tenders, reports, contracts, or any official documents using LLM intelligence — all running **offline**.

---

## 🚀 Features

- 📄 PDF upload and text extraction
- 🧠 Embedding generation and vector search using FAISS
- 🤖 LLM-based question answering
- 🗂️ Folder and file organization UI
- 💻 Fully local — no internet or OpenAI API needed
- 🎨 Beautiful and interactive Streamlit frontend

---

## 📸 UI Preview

> ![screenshot](docs/demo.png) *(Add your own UI screenshot here)*

---

## 🧰 Tech Stack

- `Python 3.10+`
- `Streamlit`
- `FAISS` (Vector Search)
- `HuggingFace Embeddings`
- `LLaMA GGUF model (run locally)`
- `PyMuPDF` or `pdfminer.six` for PDF parsing

---

## 📦 Installation

Clone the repository and set up your virtual environment:

```bash
git clone https://github.com/Smriti2303/pdf-query-chatbot.git
cd pdf-query-chatbot

# Set up virtual environment
python -m venv venv
venv\Scripts\activate     # For Windows

# Install dependencies
pip install -r requirements.txt
````

---

## 🏃 Run the App

```bash
streamlit run app.py
```

Then open the app in your browser at [http://localhost:8501](http://localhost:8501)

---

## 📁 Folder Structure

```
pdf-query-chatbot/
│
├── app.py                  # Main Streamlit app
├── requirements.txt        # All dependencies
├── uploads/                # Store your PDFs here
├── models/                 # (Put your GGUF model here, but don't push it to GitHub)
├── embeddings/             # Embedding logic
├── faiss_index/            # FAISS index files
├── llm/                    # LLM response wrapper
├── .gitignore              # Ignore models, venv etc.
└── README.md               # You're here!
```

---

## ⚠️ GitHub File Size Limit

GitHub doesn't allow files larger than **100MB**. Our model file (e.g. `llama-2-7b-chat.gguf`) is \~460MB, so we **DO NOT PUSH** it.

To prevent pushing large models:

```bash
echo "models/*.gguf" >> .gitignore
```

If you accidentally committed it:

```bash
java -jar bfg-1.14.0.jar --delete-files llama-2-7b-chat.gguf
git reflog expire --expire=now --all
git gc --prune=now --aggressive
git push --force
```

---

## 🧠 Model Note

The model (`.gguf`) used for inference is assumed to be downloaded separately and placed in the `models/` folder.

We suggest using [llama.cpp](https://github.com/ggerganov/llama.cpp) or compatible GGUF models from Hugging Face.

---

## 🙋 How to Use

1. Upload your PDFs to `uploads/`
2. Choose the folder from the dropdown
3. Ask your question in the input box
4. Get instant responses based on the PDF content

---

## 💡 Future Enhancements

* 🔍 Keyword highlighting in PDF
* 📌 Chat history
* 🌐 Optional OpenAI API fallback

---

## 👩‍💻 Author

Made by [Smriti](https://github.com/Smriti2303)

---

## 📜 License

MIT License. Free for personal and commercial use.

````

---

### ✅ To Run Your Chatbot from GitHub

Now that your code is on GitHub:

1. Clone it on any machine:
   ```bash
   git clone https://github.com/Smriti2303/pdf-query-chatbot.git
   cd pdf-query-chatbot
````

2. Set up the virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate     # For Windows
   pip install -r requirements.txt
   ```

3. Download your model (`.gguf`) manually and place it in `models/`.

4. Run it:

   ```bash
   streamlit run app.py
   ```

---

Would you like me to also generate the `requirements.txt` file content for your chatbot?
