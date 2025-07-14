# 📄 GenAI Resume Copilot

A multi-page AI-powered app that helps jobseekers improve and align their resumes using GPT-4 + RAG techniques.

### 🚀 Features
- Extracts and analyzes resume content (from a PDF)
- Suggests suitable job roles 
- Improves individual bullet points
- Provides overall feedback on the resume
- Compares resume with a job description

### Tech Stack 
- Streamlit for UI
- OpenAI GPT-4o-mini for LLM-powered reasoning
- PyMuPDF for PDF parsing
- SentenceTransformers for embeddings
- FAISS for vector DB and similarity search 
- RAG orchestration via custom-module `rag_compare/`
- Folder Structure:
```
    resume-copilot/
    ├── app.py
    ├── resume_parser.py
    ├── feedback_engine.py
    ├── role_matcher.py
    ├── rag_compare/
    │   ├── __init__.py
    │   ├── chunker.py
    │   ├── embedder.py
    │   ├── faiss_utils.py
    │   └── comparator.py
    ├── requirements.txt
    └── README.md
```
    

### ▶️ Live Demo
[Try it here](https://genai-resume-copilot-aaz7xhssqfnn3auazspr4u.streamlit.app/)

### 📸 Screenshot

<!-- ![demo](demo_2.gif) -->
<p align="center">
<img src="demo.gif" width="80%">
</p>

### 📂 Run Locally

```bash
git clone https://github.com/ch4174nya/genai-resume-copilot
cd genai-resume-copilot
pip install -r requirements.txt
streamlit run app.py
```

### 💡 Future Ideas

- Export feedback 
- Role-specific tailoring (e.g., PM, DevOps)
- User login and saving history