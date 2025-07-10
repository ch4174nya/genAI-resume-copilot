# 📄 GenAI Resume Copilot

A GenAI-powered app that:
- Extracts and analyzes resume content (from a PDF)
- Suggests suitable job roles 
- Improves individual bullet points
- Provides overall feedback on the resume

### Tech Stack 
- Streamlit for UI
- OpenAI GPT-4o-mini for LLM-powered reasoning
- PyMuPDF for PDF parsing

### 🚀 Features
- 📥 Upload your resume (PDF)
- 🤖 GPT-powered job role suggestions
- ✍️ Resume bullet rewriter
- 🧠 Skill and structure feedback

### ▶️ Live Demo
[Try it here](https://genai-resume-copilot-aaz7xhssqfnn3auazspr4u.streamlit.app/)

### 📸 Screenshot

![demo](demo.gif)

### 📂 Run Locally

```bash
git clone https://github.com/ch4174nya/genai-resume-copilot
cd genai-resume-copilot
pip install -r requirements.txt
streamlit run app.py
```

### 💡 Future Ideas

- Save feedback history
- Role-specific tailoring (e.g., PM, DevOps)