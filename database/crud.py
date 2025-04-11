# database/crud.py

from sqlalchemy.orm import Session
from database import models

def save_job_summary(db: Session, jd_text: str, summary: str):
    new_entry = models.JobSummary(jd_text=jd_text, summary=summary)
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

def get_all_summaries(db: Session):
    return db.query(models.JobSummary).all()
