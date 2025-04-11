# backend/scheduler/email_sender.py

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class EmailRequest(BaseModel):
    candidate_name: str
    candidate_email: str
    match_score: float
    interview_time: str

@router.post("/send_email")
async def send_email(request: EmailRequest):
    subject = "Interview Invitation"
    body = (
        f"Hi {request.candidate_name},\n\n"
        f"Congratulations! Based on your resume, you've been shortlisted with a match score of {request.match_score}%.\n"
        f"We would like to invite you to an interview on {request.interview_time}.\n\n"
        f"Best regards,\nRecruitment AI Team"
    )

    # Simulate sending email (print to console)
    print(f"\n Sending email to: {request.candidate_email}")
    print(f"Subject: {subject}")
    print(f"Body:\n{body}\n")

    return {"status": "success", "message": f"Email sent to {request.candidate_email}"}

