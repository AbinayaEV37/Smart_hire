# backend/agents/matcher.py

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

class MatchRequest(BaseModel):
    resume_skills: List[str]
    resume_experience: Optional[int] = None
    jd_skills: List[str]
    jd_experience_required: Optional[int] = None

@router.post("/match_resume")
async def match_resume(request: MatchRequest):
    resume_skills = set([s.lower() for s in request.resume_skills])
    jd_skills = set([s.lower() for s in request.jd_skills])

    # Skill Matching
    common_skills = resume_skills.intersection(jd_skills)
    skill_match_score = (len(common_skills) / len(jd_skills)) * 100 if jd_skills else 0

    # Experience Match (bonus 20% if experience >= required)
    experience_score = 0
    if request.jd_experience_required and request.resume_experience:
        if request.resume_experience >= request.jd_experience_required:
            experience_score = 20

    # Final Score (skill match + experience bonus)
    total_score = min(100, round(skill_match_score + experience_score))

    return {
        "match_score": total_score,
        "common_skills": list(common_skills),
        "experience_bonus": experience_score
    }
