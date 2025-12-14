import streamlit as st
import ollama
import PyPDF2

# ----------------------------------
# Configuration
# ----------------------------------
MODEL_NAME = "llama3.2"

# ----------------------------------
# Session State Initialization
# ----------------------------------
if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""

# ----------------------------------
# Page Configuration
# ----------------------------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered"
)

st.title("📄 AI Resume Analyzer")
st.caption("Upload or paste your resume and get professional improvement suggestions")
st.markdown("---")

# ----------------------------------
# Helper: Extract text from PDF
# ----------------------------------
def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text.strip()

# ----------------------------------
# Resume Input Method
# ----------------------------------
resume_input_method = st.radio(
    "Choose resume input method:",
    ["Upload PDF Resume", "Paste Resume Text"],
    key="input_method"
)

# ----------------------------------
# Resume Input Handling (STATE ONLY)
# ----------------------------------
if resume_input_method == "Upload PDF Resume":
    uploaded_file = st.file_uploader(
        "📎 Upload your resume (PDF only)",
        type=["pdf"],
        key="pdf_uploader"
    )

    if uploaded_file is not None:
        st.session_state.resume_text = extract_text_from_pdf(uploaded_file)
        st.success("✅ Resume text extracted from PDF successfully!")

elif resume_input_method == "Paste Resume Text":
    st.session_state.resume_text = st.text_area(
        "📌 Paste your resume text",
        height=300,
        placeholder="Paste your complete resume content here...",
        key="resume_text_area"
    )

# ----------------------------------
# Job Role Input
# ----------------------------------
job_role = st.text_input(
    "🎯 Target Job Role",
    placeholder="e.g., Software Engineer, AI Engineer, Data Analyst"
)

# ----------------------------------
# Analyze Button
# ----------------------------------
analyze_btn = st.button("🔍 Analyze Resume")

# ----------------------------------
# AI Resume Analysis Logic
# ----------------------------------
def analyze_resume(resume, role):
    prompt = f"""
You are an experienced technical recruiter and ATS resume evaluator.

Analyze the following resume for the target job role: "{role}"

Resume:
\"\"\"
{resume}
\"\"\"

Respond STRICTLY in this format:

1. Resume Overview
2. Key Strengths
3. Weaknesses / Gaps
4. Missing or Weak Skills for the "{role}" role
5. Bullet Point Improvements
6. ATS & Formatting Suggestions
7. Final Actionable Recommendations

Be specific, honest, and professional.
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]

# ----------------------------------
# Output Section (STATE-BASED)
# ----------------------------------
if analyze_btn:
    if not st.session_state.resume_text.strip():
        st.warning("⚠️ Please upload a PDF or paste resume text.")
    elif not job_role.strip():
        st.warning("⚠️ Please enter a target job role.")
    else:
        with st.spinner("📊 Analyzing resume against industry standards..."):
            analysis = analyze_resume(
                st.session_state.resume_text,
                job_role
            )

        st.markdown("## 📑 Resume Analysis Report")
        st.markdown(analysis)
        st.success("✅ Resume analysis completed successfully")

# ----------------------------------
# Footer
# ----------------------------------
st.markdown("---")
st.caption("Built using Python, Streamlit, PyPDF2, and a local LLM via Ollama")
