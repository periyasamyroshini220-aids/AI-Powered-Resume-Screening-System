from flask import Flask, render_template, request
from PyPDF2 import PdfReader

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    skills = request.form['skills']
    experience = request.form['experience']
    education = request.form['education']

    resume_file = request.files['resume']

    # Extract text from PDF
    resume_text = ""

    if resume_file:
        pdf = PdfReader(resume_file)

        for page in pdf.pages:
            text = page.extract_text()
            if text:
                resume_text += text

    resume_text = resume_text.lower()

    required_skills = [
        skill.strip().lower()
        for skill in skills.split(",")
        if skill.strip()
    ]

    found = []
    missing = []

    for skill in required_skills:
        if skill in resume_text:
            found.append(skill)
        else:
            missing.append(skill)

    # Skills Score (60 Marks)
    skills_score = (
        int((len(found) / len(required_skills)) * 60)
        if required_skills else 0
    )

    # Experience Score (20 Marks)
    experience_score = 20 if experience.lower() in resume_text else 0

    # Education Score (20 Marks)
    education_score = 20 if education.lower() in resume_text else 0

    total_score = (
        skills_score +
        experience_score +
        education_score
    )

    # Status
    if total_score >= 80:
        status = "SELECTED ✅"
    else:
        status = "NOT SELECTED ❌"

    # Reason Generation
    reasons = []

    if missing:
        reasons.append(
            "Missing Skills: " + ", ".join(missing)
        )

    if experience_score == 0:
        reasons.append(
            f"Required Experience not found: {experience}"
        )

    if education_score == 0:
        reasons.append(
            f"Required Education not found: {education}"
        )

    if total_score == 100:
        reason = "Perfect Match for this Job."
    else:
        reason = " | ".join(reasons)

    return render_template(
        "index.html",
        skills_score=skills_score,
        experience_score=experience_score,
        education_score=education_score,
        prediction=f"Total Resume Score: {total_score}%",
        reason=reason,
        status=status,
        found=found,
        missing=missing
    )

if __name__ == '__main__':
    app.run(debug=True)
