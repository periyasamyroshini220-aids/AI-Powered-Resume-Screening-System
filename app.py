from flask import Flask, render_template, request
from PyPDF2 import PdfReader
import sqlite3
import re

app = Flask(__name__)

# -----------------------------
# DATABASE SETUP
# -----------------------------

conn = sqlite3.connect("resume.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS screening_results(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    candidate_name TEXT,
    skills_score INTEGER,
    experience_score INTEGER,
    education_score INTEGER,
    total_score INTEGER,
    status TEXT,
    reason TEXT
)
""")

conn.commit()
conn.close()

# -----------------------------
# HOME PAGE
# -----------------------------

@app.route('/')
def home():
    return render_template('index.html')


# -----------------------------
# ANALYZE RESUMES
# -----------------------------

@app.route('/predict', methods=['POST'])
def predict():

    job_description = request.form['job_description']

    resume_files = request.files.getlist('resume')

    # -----------------------------
    # Extract Requirements
    # -----------------------------

    skills = []
    experience = ""
    education = ""

    jd_lower = job_description.lower()

    skill_match = re.search(r"skills:(.*?)(experience:|education:|$)",
                            jd_lower,
                            re.DOTALL)

    if skill_match:
        skills_text = skill_match.group(1)
        skills = [s.strip() for s in skills_text.split(",") if s.strip()]

    exp_match = re.search(r"experience:(.*?)(education:|$)",
                          jd_lower,
                          re.DOTALL)

    if exp_match:
        experience = exp_match.group(1).strip()

    edu_match = re.search(r"education:(.*)$",
                          jd_lower,
                          re.DOTALL)

    if edu_match:
        education = edu_match.group(1).strip()

    results = []

    # -----------------------------
    # Process Each Resume
    # -----------------------------

    for index, resume_file in enumerate(resume_files, start=1):

        resume_text = ""

        try:

            pdf = PdfReader(resume_file)

            for page in pdf.pages:

                text = page.extract_text()

                if text:
                    resume_text += text

        except:
            continue

        resume_text = resume_text.lower()

        # -----------------------------
        # Skills Check
        # -----------------------------

        found = []
        missing = []

        for skill in skills:

            if skill in resume_text:
                found.append(skill)

            else:
                missing.append(skill)

        skills_score = int(
            (len(found) / len(skills)) * 60
        ) if skills else 0

        # -----------------------------
        # Experience Check
        # -----------------------------

        if experience and experience in resume_text:
            experience_score = 20
        else:
            experience_score = 0

        # -----------------------------
        # Education Check
        # -----------------------------

        if education and education in resume_text:
            education_score = 20
        else:
            education_score = 0

        # -----------------------------
        # Total Score
        # -----------------------------

        total_score = (
            skills_score +
            experience_score +
            education_score
        )

        # -----------------------------
        # Status
        # -----------------------------

        if total_score >= 80:
            status = "SELECTED ✅"
            reason = "You are the perfect match for this job."

        else:

            status = "NOT SELECTED ❌"

            reasons = []

            if missing:
                reasons.append(
                    "Missing Skills: " +
                    ", ".join(missing)
                )

            if experience_score == 0:
                reasons.append(
                    "Required Experience not found"
                )

            if education_score == 0:
                reasons.append(
                    "Required Education not found"
                )

            reason = " | ".join(reasons)

        # -----------------------------
        # Save To Database
        # -----------------------------

        conn = sqlite3.connect("resume.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO screening_results
        (
            candidate_name,
            skills_score,
            experience_score,
            education_score,
            total_score,
            status,
            reason
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            resume_file.filename,
            skills_score,
            experience_score,
            education_score,
            total_score,
            status,
            reason
        ))

        conn.commit()
        conn.close()

        # -----------------------------
        # Store Results
        # -----------------------------

        results.append({

            "id": index,

            "candidate_name": resume_file.filename,

            "skills_score": skills_score,

            "experience_score": experience_score,

            "education_score": education_score,

            "total_score": total_score,

            "status": status,

            "reason": reason

        })

    return render_template(
        "index.html",
        results=results
    )


# -----------------------------
# RUN APP
# -----------------------------

if __name__ == '__main__':
    app.run(debug=True)