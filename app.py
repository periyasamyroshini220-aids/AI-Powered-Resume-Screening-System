from flask import Flask, render_template, request
from PyPDF2 import PdfReader
import sqlite3
import re

app = Flask(__name__)

# -----------------------------
# INIT DATABASE
# -----------------------------
def init_db():
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

init_db()


# -----------------------------
# HOME PAGE
# -----------------------------
@app.route('/')
def home():
    return render_template("index.html")


# -----------------------------
# DASHBOARD (FIXED)
# -----------------------------
@app.route('/dashboard')
def dashboard():

    conn = sqlite3.connect("resume.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT candidate_name,
               skills_score,
               experience_score,
               education_score,
               total_score,
               status,
               reason
        FROM screening_results
        ORDER BY total_score DESC
    """)

    data = cursor.fetchall()
    conn.close()

    total = len(data)
    selected = len([d for d in data if d[5] == "SELECTED ✅"])
    rejected = total - selected

    return render_template(
        "dashboard.html",
        data=data,
        total=total,
        selected=selected,
        rejected=rejected
    )


# -----------------------------
# ANALYZE RESUMES
# -----------------------------
@app.route('/predict', methods=['POST'])
def predict():

    job_description = request.form['job_description']
    resume_files = request.files.getlist('resume')

    jd_lower = job_description.lower()

    # Extract JD requirements
    skills = []
    experience = ""
    education = ""

    skill_match = re.search(
        r"skills:(.*?)(experience:|education:|$)",
        jd_lower,
        re.DOTALL
    )
    if skill_match:
        skills = [s.strip() for s in skill_match.group(1).split(",") if s.strip()]

    exp_match = re.search(
        r"experience:(.*?)(education:|$)",
        jd_lower,
        re.DOTALL
    )
    if exp_match:
        experience = exp_match.group(1).strip()

    edu_match = re.search(
        r"education:(.*)$",
        jd_lower,
        re.DOTALL
    )
    if edu_match:
        education = edu_match.group(1).strip()

    results = []

    # -----------------------------
    # PROCESS RESUMES
    # -----------------------------
    for index, resume_file in enumerate(resume_files, start=1):

        text = ""

        try:
            pdf = PdfReader(resume_file)
            for page in pdf.pages:
                if page.extract_text():
                    text += page.extract_text()
        except:
            continue

        text = text.lower()

        found = []
        missing = []

        for skill in skills:
            if skill in text:
                found.append(skill)
            else:
                missing.append(skill)

        skills_score = int((len(found) / len(skills)) * 60) if skills else 0
        experience_score = 20 if experience and experience in text else 0
        education_score = 20 if education and education in text else 0

        total_score = skills_score + experience_score + education_score

        if total_score >= 80:
            status = "SELECTED ✅"
            reason = "Strong match for job requirements"
        else:
            status = "NOT SELECTED ❌"
            reason = "Missing Skills: " + ", ".join(missing)

        # Save to DB
        conn = sqlite3.connect("resume.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO screening_results (
            candidate_name,
            skills_score,
            experience_score,
            education_score,
            total_score,
            status,
            reason
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
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

    return render_template("index.html", results=results)


# -----------------------------
# RUN APP
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)