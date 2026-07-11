import streamlit as st

from pdf_loader import extract_text_from_pdf
from analyzer import analyze_resume

# --------------------------
# Page Config
# --------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# --------------------------
# Header
# --------------------------

st.title("📄 AI Resume Analyzer")
st.markdown(
    """
Upload your **Resume (PDF)** and receive AI-powered feedback on:

- 🎯 ATS Score
- 💪 Strengths
- ⚠ Weaknesses
- 🛠 Missing Skills
- 💡 Suggested Projects
- 📌 Resume Improvements
"""
)

uploaded_file = st.file_uploader(
    "Choose Resume",
    type=["pdf"]
)

# --------------------------
# No File Uploaded
# --------------------------

if uploaded_file is None:

    st.info("👆 Upload your resume to begin analysis.")

    st.stop()

# --------------------------
# Analyze Resume
# --------------------------

with st.spinner("🤖 AI is analyzing your resume..."):

    resume_text = extract_text_from_pdf(uploaded_file)

    result = analyze_resume(resume_text)

st.success("✅ Analysis Complete!")

st.divider()

# --------------------------
# Scores
# --------------------------

st.subheader("📊 Resume Scores")

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Overall Score",
        f"{result['overall_score']}/100"
    )

    st.progress(result["overall_score"] / 100)

with col2:

    st.metric(
        "ATS Score",
        f"{result['ats_score']}/100"
    )

    st.progress(result["ats_score"] / 100)

st.divider()

# --------------------------
# Strengths
# --------------------------

st.subheader("💪 Strengths")

for item in result["strengths"]:
    st.success(item)

# --------------------------
# Weaknesses
# --------------------------

st.subheader("⚠ Weaknesses")

for item in result["weaknesses"]:
    st.error(item)

# --------------------------
# Missing Skills
# --------------------------

st.subheader("🛠 Missing Skills")

for item in result["missing_skills"]:
    st.warning(item)

# --------------------------
# Suggested Projects
# --------------------------

st.subheader("💡 Suggested Projects")

for item in result["project_suggestions"]:
    st.info(item)

# --------------------------
# Resume Improvements
# --------------------------

st.subheader("📌 Resume Improvements")

for item in result["resume_improvements"]:
    st.info(item)

# --------------------------
# Final Verdict
# --------------------------

st.subheader("🎯 Final Verdict")

st.success(result["final_verdict"])