# database/models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class JobSummary(Base):
    __tablename__ = "job_summaries"
    
    id = Column(Integer, primary_key=True, index=True)
    jd_text = Column(String)
    summary = Column(String)
