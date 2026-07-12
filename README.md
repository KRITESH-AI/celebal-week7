# 📄 Document Question Answering System using Retrieval-Augmented Generation (RAG)

## 🚀 Live Demo

**Streamlit App:**  
https://kritesh-ai-celebal-week7-streamlit-app-zuvxol.streamlit.app/

## 📌 Overview

This project implements a **Retrieval-Augmented Generation (RAG)** based Document Question Answering system that enables users to ask questions over their own documents such as PDFs and text files.

Instead of relying solely on the language model's internal knowledge, the system retrieves the most relevant document chunks using semantic similarity search and generates grounded answers based on the retrieved context.

The application supports both a **Command Line Interface (CLI)** and an interactive **Streamlit Web Application**.

---

# 🚀 Features

- 📄 PDF Document Ingestion
- 📃 Text File Ingestion
- ✂️ Recursive Text Chunking
- 🧠 Sentence Transformer Embeddings
- 🔍 FAISS Vector Database
- 📐 Cosine Similarity Search
- 🎯 Semantic Retrieval
- 🤖 Grounded Answer Generation using FLAN-T5
- 🌐 Interactive Streamlit UI
- ⚙️ Configurable Top-K Retrieval
- 📚 Retrieved Context Visualization
- ✅ Similarity Threshold Filtering

---

# 🏗️ System Architecture

```
               Documents (PDF / TXT)
                        │
                        ▼
               Document Loader
                        │
                        ▼
               Text Chunking
                        │
                        ▼
         Sentence Transformer Embeddings
                        │
                        ▼
              FAISS Vector Database
                        │
                        ▼
                  User Question
                        │
                        ▼
                 Query Embedding
                        │
                        ▼
              Semantic Retrieval
                        │
                        ▼
              Relevant Context Chunks
                        │
                        ▼
              FLAN-T5 Language Model
                        │
                        ▼
                Grounded Final Answer
```

---

# 📂 Project Structure

```
Document-QA-RAG/

│
├── data/
│   ├── AI.pdf
│   ├── Resume.pdf
│   └── sample.txt
│
├── utils/
│   ├── loader.py
│   ├── chunker.py
│   ├── embeddings.py
│   ├── vectordb.py
│   ├── retriever.py
│   └── generator.py
│
├── vectorstore/
│
├── ingest.py
├── app.py
├── streamlit_app.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🧠 Technologies Used

- Python
- LangChain
- Sentence Transformers
- FAISS
- Hugging Face Transformers
- FLAN-T5 Base
- Streamlit
- PyMuPDF

---

# ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/KRITESH-AI/celebal-week7.git

cd Document-QA-RAG
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📥 Add Documents

Place your documents inside the **data/** folder.

Current sample documents:

- AI.pdf
- Resume.pdf
- sample.txt

Supported formats:

- PDF
- TXT

---

# 📦 Build the Vector Database

Run:

```bash
python ingest.py
```

This performs:

- Document Loading
- Text Chunking
- Embedding Generation
- FAISS Index Creation

---

# ▶️ Run the CLI Application

```bash
python app.py
```

### Example

```
Question:
What are the technical skills?

Answer:
Operation System Windows XP/7/8
Packages Python (basic level)
```

---

# 🌐 Run the Streamlit Application

```bash
streamlit run streamlit_app.py
```

Open your browser and visit:

```
http://localhost:8501
```

---

# 📊 System Configuration

| Component | Configuration |
|------------|--------------|
| Chunk Size | 500 |
| Chunk Overlap | 100 |
| Embedding Model | sentence-transformers/all-MiniLM-L6-v2 |
| Embedding Dimension | 384 |
| Vector Database | FAISS (IndexFlatIP) |
| Similarity Metric | Cosine Similarity |
| Language Model | google/flan-t5-base |
| Retrieval | Top-K Semantic Search |
| Threshold | Minimum Similarity Score |

---

# 🧪 Sample Questions

## 📄 Resume

- What are the technical skills?
- What are the strengths?
- What is the educational qualification?

## 🤖 AI Research Paper

- What is the paper about?
- Why are SLMs better for Agentic AI?
- What is LoRA?
- What is PEFT?
- What are AI Agents?

## 📃 Sample Text

- What is Retrieval-Augmented Generation?
- What are embeddings?
- What is FAISS?

## ❓ Out-of-Domain Question

- What is the capital of Japan?

**Expected Response**

```
I could not find the answer in the provided documents.
```

---

# 📈 Results

The system successfully:

- Retrieves semantically relevant document chunks.
- Generates grounded answers from the retrieved context.
- Prevents unsupported responses using a similarity threshold.
- Supports multiple document formats (PDF and TXT).
- Provides both CLI and Streamlit interfaces.

---

# 📚 Key Learnings

During this project, the following concepts were explored:

- Retrieval-Augmented Generation (RAG)
- Document Chunking
- Sentence Embeddings
- Vector Databases
- Semantic Search
- Cosine Similarity
- Prompt Engineering
- Large Language Models (LLMs)
- Context-Aware Question Answering

---

# 🔮 Future Improvements

Potential enhancements include:

- Hybrid Search (BM25 + Vector Search)
- Cross-Encoder Re-ranking
- LoRA / PEFT Fine-tuning
- Metadata-based Retrieval
- Multi-Document Ranking
- Conversational Memory
- Support for additional document formats

---

# 👨‍💻 Author

**Ritesh**

**Celebal Technologies Internship – Week 7 Assignment**

**Topic:** Retrieval-Augmented Generation (RAG)