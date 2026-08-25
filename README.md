# EchoAssist: Chat and Voice-Enabled RAG Assistant for IITK Student Services

EchoAssist is an intelligent Retrieval-Augmented Generation (RAG) assistant equipped with both textual chat and voice interactive capabilities, designed to streamline student services, queries, campus guidelines, and academic information for IIT Kanpur (IITK).

## 🌟 Key Features
- **Multimodal Interaction:** Supports both text-based conversational queries and real-time Voice-to-Text (STT) / Text-to-Voice (TTS) input/output.
- **RAG Architecture:** High-precision information retrieval over IITK student handbooks, academic regulations, mess rules, and campus services documentation.
- **Vector Search Engine:** FAISS / ChromaDB vector embeddings for fast semantic document retrieval.
- **Interactive UI:** Web dashboard powered by Streamlit and FastAPI backend server.

## 🚀 Tech Stack
- **Frameworks:** LangChain, FastAPI, Streamlit, PyTorch
- **Vector Store & Embeddings:** ChromaDB / FAISS, HuggingFace SentenceTransformers
- **Voice Processing:** OpenAI Whisper / SpeechRecognition (STT), gTTS / pyttsx3 (TTS)
- **LLM Integration:** OpenAI GPT-4 / Ollama Llama 3 / Mistral

## 📁 Repository Structure
```
EchoAssist/
├── backend/
│   ├── __init__.py
│   ├── document_processor.py   # PDF & Text parsing engine
│   ├── vector_store.py         # FAISS / ChromaDB vector indexing
│   ├── rag_chain.py            # LangChain RAG pipeline
│   └── voice_engine.py         # STT & TTS voice handling
├── frontend/
│   ├── app.py                  # Streamlit Chat & Voice UI
├── data/                       # IITK Student guidelines & manuals
├── notebooks/                  # RAG evaluation & experimentation
├── tests/                      # Unit tests for RAG pipeline
├── config.py                   # System configuration & environment vars
├── requirements.txt            # Dependency manifest
└── README.md                   # Project documentation
```

## 🛠️ Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Devashishpandey1103/EchoAssist-Chat-and-Voice-Enabled-RAG-Assistant-for-IITK-Student-Services.git
cd EchoAssist-Chat-and-Voice-Enabled-RAG-Assistant-for-IITK-Student-Services
```

### 2. Set Up Environment & Install Dependencies
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Run the Backend & Frontend Application
```bash
# Start FastAPI backend server
python backend/rag_chain.py

# Start Streamlit voice & chat web app
streamlit run frontend/app.py
```

---
*Developed for IITK Student Services Automation & Modern AI Portfolio.*
