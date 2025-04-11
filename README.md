# Smart_hire 

SmartHire is an AI-driven recruitment automation platform that streamlines the end-to-end hiring process using multiple intelligent agents. It leverages FastAPI, Streamlit, SQLite, and NLP to help organizations identify the right talent quickly and efficiently.

# Proposed Solution
* AI-Driven Automation:
SmartHire automates the hiring process using intelligent agents that summarize job descriptions, parse resumes, match candidates to job roles, and coordinate interviews—making recruitment faster and more efficient.

* Smart Matching & Skill Gap Handling:
The system uses NLP and AI scoring to match candidates with JDs based on skills, experience, and education. It detects skill gaps, recommends relevant courses, allows certificate uploads, and integrates MCQ-based assessments to ensure job readiness.

* Personalized Feedback & Interview Management:
Candidates receive real-time feedback—rejection reasons or improvement tips—and shortlisted applicants get email invites with the option to set interview reminders 4–5 hours before the scheduled time, ensuring a guided and transparent process.

---

# Features
- JD summarization with skill & experience extraction
- Resume parsing using NLP
- JD ↔ Resume matching with scoring
- Interview email scheduling
- Streamlit-based user interface
- SQLite-powered persistent storage
- Pre-assessment MCQ test mockup (via Figma UI)

##  Folder Structure

Smart_hire/
├── backend/
│   ├── main.py
│   ├── agents/
│   │   ├── job_summary_agent.py
│   │   ├── resume_parser.py
│   │   └── matcher.py
│   └── scheduler/
│       └── email_sender.py
├── database/
│   ├── models.py
│   └── crud.py
├── frontend/
│   └── app.py
├── db.sqlite         ← auto-generated after running
├── .gitignore
├── requirements.txt
└── README.md

---

##  How to Run

### Backend (FastAPI)
```bash
uvicorn backend.main:app --reload

Runs on: http://127.0.0.1:8000

You can view docs at: http://127.0.0.1:8000/docs

## Frontend (Streamlit)

streamlit run frontend/app.py

Tech Stack:

Backend: FastAPI
AI/NLP: spaCy, regex
Frontend: Streamlit (prototype)
Database: SQLite (via SQLAlchemy)
Email Integration: smtplib
Resume Parsing: custom rule-based NLP logic
Mobile UI: Figma(prototype)
