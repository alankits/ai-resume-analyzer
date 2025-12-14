# 📄 AI Resume Analyzer & Builder

An AI-powered resume analysis tool that evaluates resumes against a target job role and provides actionable improvement suggestions using Generative AI.

---

## 🚀 Features
- Upload resume as **PDF** or paste resume text
- Role-based resume analysis
- Identifies strengths and weaknesses
- Detects missing or weak skills
- Provides ATS-focused suggestions
- Generates improved resume bullet points
- Handles non-readable PDFs gracefully

---

## 🧠 How It Works
1. User uploads a text-based PDF resume or pastes resume text
2. User enters a target job role
3. A local Large Language Model (LLaMA via Ollama) analyzes the resume
4. The system generates a structured resume analysis report

> Note: Some layout-based or scanned PDFs may not allow text extraction. In such cases, users are guided to paste resume text manually.

---

## 🛠 Tech Stack
- Python
- Streamlit
- Ollama (Local LLM)
- PyPDF2

---

## ▶ How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/ai-resume-analyzer.git
cd ai-resume-analyzer
