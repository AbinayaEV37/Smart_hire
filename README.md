# Smart_hire 

Smart_hire is an AI-powered Recruitment Assistant that helps HR teams quickly analyze job descriptions, parse resumes, match candidates, and even schedule interviews — all with a friendly interface and automation under the hood.

---

## Features

-  Summarizes job descriptions
-  Parses candidate resumes
-  Matches resumes to job roles with skill & experience analysis
-  Sends interview invites via email
-  Uses SQLite for storing job/resume/match data

---

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

Python 
FastAPI 
Streamlit 
SQLite 
Uvicorn 
Requests, Pydantic, EmailUtils etc.


