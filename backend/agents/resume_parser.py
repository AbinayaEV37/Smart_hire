# backend/agents/resume_parser.py

from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, List
import re

router = APIRouter()

class ResumeRequest(BaseModel):
    resume_text: str

# Predefined skills (you can expand this)
KNOWN_SKILLS = {
    "python", "java", "c++", "sql", "excel", "fastapi", "django",
    "react", "javascript", "aws", "docker", "machine learning"
}

@router.post("/parse_resume")
async def parse_resume(request: ResumeRequest):
    text = request.resume_text
    lines = text.splitlines()

    # --- Name extraction: assume first non-empty line is name ---
    name = None
    for line in lines:
        if line.strip():
            name = line.strip()
            break

    # --- Email extraction ---
    email_match = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    email = email_match.group(0) if email_match else None

    # --- Experience extraction ---
    exp_match = re.search(r"(\d+)\s+years?", text.lower())
    experience = int(exp_match.group(1)) if exp_match else None

    # --- Skills extraction ---
    skills_found = [skill for skill in KNOWN_SKILLS if skill.lower() in text.lower()]

    return {
        "name": name,
        "email": email,
        "experience": experience,
        "skills": skills_found
    }
