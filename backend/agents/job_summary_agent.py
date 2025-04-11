# backend/agents/job_summary_agent.py

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from backend.db import SessionLocal
from database import crud
import re

router = APIRouter()

class JobDescriptionRequest(BaseModel):
    jd_text: str

KNOWN_SKILLS = {
    "python", "java", "sql", "excel", "fastapi", "django", "react",
    "javascript", "aws", "docker", "machine learning", "data analysis"
}

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/summarize")
async def summarize_job_description(request: JobDescriptionRequest, db: Session = Depends(get_db)):
    jd_text = request.jd_text

    # Extract skills
    skills = [skill for skill in KNOWN_SKILLS if skill in jd_text.lower()]

    # Extract experience (e.g. "3 years", "5+ years")
    exp_match = re.search(r"(\d+)\+?\s+years?", jd_text.lower())
    experience = int(exp_match.group(1)) if exp_match else None

    # Guess the role from first line or sentence
    role_line = jd_text.strip().split("\n")[0]
    role = role_line.strip()[:50]  # first 50 chars

    summary = f"This is a summary of the JD: {jd_text[:75]}..."

    #  Save to DB
    crud.save_job_summary(db, jd_text=jd_text, summary=summary)

    return {
        "summary": summary,
        "role": role,
        "experience_required": experience,
        "skills_required": skills
    }
