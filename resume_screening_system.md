# AI Powered Resume Screening System

## Abstract

The AI Powered Resume Screening System is a web-based application designed to automate the resume screening process in recruitment. The system analyzes candidate resumes and compares them with job requirements such as skills, experience, and educational qualifications.

It generates a resume score, identifies missing requirements, and provides a selection status. This helps HR teams reduce manual effort, save time, and improve recruitment efficiency.

---

# Objectives

The main objectives of this project are:

* To automate the resume screening process.
* To reduce manual effort in recruitment.
* To compare candidate resumes with job requirements.
* To calculate resume scores automatically.
* To identify missing skills and qualifications.
* To improve candidate shortlisting efficiency.
* To assist HR teams in selecting suitable candidates.

---

# Requirement Analysis

## Inputs

### Required Skills

Skills expected by the company.

Example:

```text id="a1"
Python, Flask, SQL, Machine Learning
```

### Required Experience

Experience required for the job.

Example:

```text id="a2"
2 Years
```

### Required Education

Educational qualification required for the position.

Example:

```text id="a3"
BE Computer Science
```

### Resume PDF

Candidate uploads their resume in PDF format.

---

## Outputs

The system generates:

* Skills Match Score
* Experience Match Score
* Education Match Score
* Total Resume Score
* Selection Status
* Missing Skills Report

---

# Front End Details

## Technologies Used

### HTML

Used for creating the structure of web pages.

### CSS

Used for designing and styling the user interface.

## Front End Features

* Job Requirement Form
* Resume PDF Upload
* User-Friendly Interface
* Result Display Dashboard
* Resume Analysis Report

---

# Back End Details

## Technologies Used

### Python

Used for implementing the business logic and resume analysis process.

### Flask

Used as the backend framework to handle user requests and responses.

### PyPDF2

Used to extract text from uploaded PDF resumes.

## Backend Functions

* PDF Processing
* Resume Analysis
* Skills Matching
* Experience Verification
* Education Verification
* Resume Score Calculation
* Result Generation

---

# System Modules

## Module 1: Resume Upload Module

Allows candidates to upload resumes in PDF format.

### Input

Resume PDF

### Output

Uploaded Resume File

---

## Module 2: PDF Text Extraction Module

Extracts text from uploaded PDF files using PyPDF2.

### Input

PDF Resume

### Output

Resume Text

---

## Module 3: Skills Matching Module

Compares required skills with skills found in the resume.

### Output

Skills Match Score

---

## Module 4: Experience Verification Module

Checks whether the candidate satisfies the required experience criteria.

### Output

Experience Match Score

---

## Module 5: Education Verification Module

Verifies educational qualifications against company requirements.

### Output

Education Match Score

---

## Module 6: Resume Scoring Module

Calculates the overall candidate score.

### Score Distribution

| Category         | Marks |
| ---------------- | ----- |
| Skills Match     | 60    |
| Experience Match | 20    |
| Education Match  | 20    |
| Total Score      | 100   |

---

## Module 7: Result Generation Module

Generates the final screening result.

### Output

* Resume Score
* Selection Status
* Missing Skills Report

---

# Algorithm

### Step 1

Enter job requirements:

* Skills
* Experience
* Education

### Step 2

Upload candidate resume PDF.

### Step 3

Extract text from the PDF using PyPDF2.

### Step 4

Compare required skills with resume content.

### Step 5

Verify required experience.

### Step 6

Verify educational qualification.

### Step 7

Calculate the total resume score.

### Step 8

Generate final result.

---

# System Workflow

```text
Enter Job Requirements
          ↓
Upload Resume PDF
          ↓
Extract Resume Text
          ↓
Skills Matching
          ↓
Experience Verification
          ↓
Education Verification
          ↓
Score Calculation
          ↓
Result Generation
```

---

# Sample Output

```text
Skills Match      : 60%

Experience Match  : 20%

Education Match   : 20%

Total Resume Score: 100%

Status            : SELECTED

Missing Skills    : None
```

---

# Technologies Used

* HTML
* CSS
* Python
* Flask
* PyPDF2

---

# Future Enhancements

* AI-Based Resume Ranking
* NLP-Based Skill Extraction
* Multiple Resume Comparison
* Database Integration
* Recruiter Dashboard
* Downloadable Reports

---

# Conclusion

The AI Powered Resume Screening System automates the recruitment screening process by analyzing candidate resumes based on skills, experience, and educational qualifications. The system reduces manual effort, improves recruitment efficiency, and helps HR teams identify suitable candidates quickly and accurately.

---

## Developed By

**ROSHINI.P**
