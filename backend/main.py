from fastapi import FastAPI
from backend.agents.job_summary_agent import router as jd_summarizer_router
from backend.agents.resume_parser import router as resume_parser_router
from backend.agents.matcher import router as matcher_router
from backend.scheduler.email_sender import router as email_router
app = FastAPI(
    title="Recruitment AI System",
    version="0.1.0"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Recruitment AI System"}

# Include all agent routers
app.include_router(jd_summarizer_router)
app.include_router(resume_parser_router)
app.include_router(matcher_router)
app.include_router(email_router)
