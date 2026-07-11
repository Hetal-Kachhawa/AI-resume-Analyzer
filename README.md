# AI Resume Analyzer

AI Resume Analyzer is a web application that analyzes PDF resumes using a Large Language Model (Mistral AI). The application provides ATS-oriented feedback, identifies strengths and weaknesses, suggests missing technical skills, recommends projects to improve the resume, and gives actionable improvement suggestions.

# live demo link - https://ai-resume-analyzer-sjouhr8wzpqvbmk42eawb9.streamlit.app/
---

## Features

- Upload resumes in PDF format
- AI-powered resume analysis using Mistral AI
- Overall Resume Score
- ATS Compatibility Score
- Resume Strengths
- Resume Weaknesses
- Missing Technical Skills
- Suggested Projects
- Resume Improvement Recommendations
- Final Hiring Verdict

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Streamlit | Web Interface |
| LangChain | LLM Orchestration |
| Mistral AI | Resume Analysis |
| PyPDF | PDF Text Extraction |
| python-dotenv | Environment Variable Management |

---

## Project Structure

resume-analyzer/
│
├── app.py
├── analyzer.py
├── config.py
├── pdf_loader.py
├── prompts.py
├── requirements.txt
├── .env
└── README.md

---

## How It Works

1. Upload a PDF resume.
2. Extract text from the PDF.
3. Send the extracted resume to Mistral AI using LangChain.
4. Generate structured resume feedback.
5. Display the analysis in an interactive Streamlit dashboard.

---

## Example Output

The application generates:

- Overall Resume Score
- ATS Score
- Strengths
- Weaknesses
- Missing Skills
- Suggested Projects
- Resume Improvements
- Final Hiring Recommendation

---

## Future Improvements

- Job Description Matching
- Resume Keyword Optimization
- Multi-language Resume Support
- Downloadable PDF Report
- Interview Question Generator
- Resume Version Comparison

