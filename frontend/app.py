import streamlit as st
import requests

st.set_page_config(page_title="Recruitment AI", layout="centered")
st.title("🤖 Recruitment AI System")

backend_url = "http://127.0.0.1:8000"

# --- JD Section ---
st.header("📄 Job Description")
jd_text = st.text_area("Paste the job description here:")

if st.button("Summarize JD"):
    if jd_text.strip():
        response = requests.post(f"{backend_url}/summarize", json={"jd_text": jd_text})
        if response.status_code == 200:
            jd_result = response.json()
            st.success("✅ JD Summary Generated")
            st.write("**Summary:**", jd_result["summary"])
            st.write("**Role:**", jd_result["role"])
            st.write("**Experience Required:**", jd_result["experience_required"])
            st.write("**Skills Required:**", jd_result["skills_required"])
        else:
            st.error("❌ Failed to summarize job description.")
    else:
        st.warning("Please paste a job description.")

# --- Resume Section ---
st.header("📄 Candidate Resume")
resume_text = st.text_area("Paste the candidate's resume text here:")

if st.button("Parse Resume"):
    if resume_text.strip():
        response = requests.post(f"{backend_url}/parse_resume", json={"resume_text": resume_text})
        if response.status_code == 200:
            resume_result = response.json()
            st.success("✅ Resume Parsed")
            st.write("**Name:**", resume_result.get("name"))
            st.write("**Email:**", resume_result.get("email"))
            st.write("**Experience:**", resume_result.get("experience"))
            st.write("**Skills:**", resume_result.get("skills"))
        else:
            st.error("❌ Failed to parse resume.")
    else:
        st.warning("Please paste a resume.")

# --- Matcher Section ---
st.header("🎯 Match Resume to Job")
if st.button("Match Resume"):
    if jd_text.strip() and resume_text.strip():
        jd_response = requests.post(f"{backend_url}/summarize", json={"jd_text": jd_text})
        resume_response = requests.post(f"{backend_url}/parse_resume", json={"resume_text": resume_text})

        if jd_response.status_code == 200 and resume_response.status_code == 200:
            jd_data = jd_response.json()
            resume_data = resume_response.json()

            match_payload = {
                "resume_skills": resume_data.get("skills", []),
                "resume_experience": resume_data.get("experience"),
                "jd_skills": jd_data.get("skills_required", []),
                "jd_experience_required": jd_data.get("experience_required")
            }

            match_response = requests.post(f"{backend_url}/match_resume", json=match_payload)

            if match_response.status_code == 200:
                match_result = match_response.json()
                st.success(f"✅ Match Score: {match_result['match_score']}%")
                st.write("🎯 Common Skills:", match_result["common_skills"])
                st.write("🎁 Experience Bonus:", match_result["experience_bonus"])
            else:
                st.error("❌ Match API failed.")
        else:
            st.error("❌ JD or Resume parsing failed.")
    else:
        st.warning("Paste both JD and resume before matching.")

# --- Email Sender ---
st.header("✉️ Send Interview Invite")
with st.form("email_form"):
    name = st.text_input("Candidate Name")
    email = st.text_input("Candidate Email")
    time = st.text_input("Interview Time", placeholder="e.g., Monday 10 AM")
    send_button = st.form_submit_button("Send Email")

    if send_button:
        score = match_result["match_score"] if "match_result" in locals() else 0
        response = requests.post(f"{backend_url}/send_email", json={
            "candidate_name": name,
            "candidate_email": email,
            "match_score": score,
            "interview_time": time
        })
        if response.status_code == 200:
            st.success(response.json()["message"])
        else:
            st.error("Failed to send email.")
