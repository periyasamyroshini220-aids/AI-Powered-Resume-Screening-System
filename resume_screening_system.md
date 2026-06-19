# AI-POWERED RESUME SCREENING SYSTEM

## Abstract

The Sample AI-Powered Resume Screening System is a web-based recruitment application developed to automate the process of candidate evaluation and resume screening. The system enables recruiters to upload multiple resumes in PDF format and compare them against a job description.

The application extracts text from resumes, identifies matching skills and qualifications, calculates a suitability score, ranks candidates based on their performance, and automatically identifies the best candidate. This reduces manual screening effort, improves hiring efficiency, and supports faster recruitment decisions.

## Objectives

* Automate the resume screening process.
* Compare candidate resumes with job descriptions.
* Analyze multiple resumes simultaneously.
* Calculate candidate suitability scores automatically.
* Rank candidates based on performance.
* Identify the best candidate for a job role.
* Reduce recruitment time and manual effort.
* Improve hiring accuracy and efficiency.

## Requirement Analysis

### Inputs

#### Job Description

Recruiters provide job requirements such as:

* Required Skills
* Technologies
* Experience
* Educational Qualification

Example:

Skills: Python, Flask, SQL, Machine Learning

Experience: 2 Years

Education: BE Computer Science

#### Candidate Resumes

Multiple candidate resumes are uploaded in PDF format.

Examples:

* Arun_Kumar_Resume.pdf
* Priya_Sharma_Resume.pdf
* Rahul_Resume.pdf
* Karthik_Resume.pdf
* Sneha_Reddy_Resume.pdf

### Outputs

The system generates:

* Skills Match Score
* Experience Match Score
* Education Match Score
* Total Score Percentage
* Candidate Ranking
* Selection Status
* Best Candidate Recommendation
* Dashboard Reports

## Front End Details

### Technologies Used

* HTML
* CSS

### Features

* Multiple Resume Upload
* Job Description Input Form
* Resume Analysis Results
* Candidate Ranking Table
* Dashboard Interface
* Candidate Status Display

## Back End Details

### Technologies Used

* Python
* Flask
* PyPDF2
* SQLite

### Backend Functions

* Resume PDF Processing
* Text Extraction
* Keyword Matching
* Skills Analysis
* Score Calculation
* Candidate Ranking
* Database Storage
* Dashboard Generation

## Database Details

### Database Name

resume.db

### Table Name

screening_results

### Fields

| Field Name       | Type    | Description            |
| ---------------- | ------- | ---------------------- |
| id               | INTEGER | Primary Key            |
| candidate_name   | TEXT    | Candidate Resume Name  |
| skills_score     | INTEGER | Skills Match Score     |
| experience_score | INTEGER | Experience Match Score |
| education_score  | INTEGER | Education Match Score  |
| total_score      | INTEGER | Total Score            |
| status           | TEXT    | Selection Status       |
| reason           | TEXT    | Screening Feedback     |

## System Modules

### Module 1: Resume Upload Module

Uploads multiple candidate resumes.

### Module 2: Job Description Module

Accepts recruiter requirements.

### Module 3: Resume Extraction Module

Extracts text from PDF resumes.

### Module 4: Skill Matching Module

Compares resume skills with job requirements.

### Module 5: Score Calculation Module

Calculates candidate score.

Formula:

Total Score = Skills Score + Experience Score + Education Score

### Module 6: Ranking Module

Ranks candidates based on total score.

### Module 7: Database Storage Module

Stores candidate screening results.

### Module 8: Dashboard Module

Displays rankings, scores, and candidate status.

## Algorithm

Step 1: Enter Job Description.

Step 2: Upload Multiple Resume PDFs.

Step 3: Extract Resume Text.

Step 4: Convert Text to Lowercase.

Step 5: Extract Skills, Experience, and Education Requirements.

Step 6: Compare Resume Content with Job Description.

Step 7: Calculate Individual Scores.

Step 8: Calculate Total Score.

Step 9: Generate Selection Status.

Step 10: Store Results in SQLite Database.

Step 11: Rank Candidates by Score.

Step 12: Identify Best Candidate.

Step 13: Display Dashboard Results.

## System Workflow

Job Description
↓
Upload Resumes
↓
Extract Resume Text
↓
Skill Matching
↓
Score Calculation
↓
Candidate Ranking
↓
Store Results
↓
Select Best Candidate
↓
Display Dashboard

## Sample Output

| Candidate Name | Total Score | Status         |
| -------------- | ----------- | -------------- |
| Arun Kumar     | 100%        | SELECTED ✅     |
| Priya Sharma   | 85%         | SELECTED ✅     |
| Rahul          | 80%         | SELECTED ✅     |
| Karthik        | 80%         | SELECTED ✅     |
| Sneha Reddy    | 70%         | NOT SELECTED ❌ |
| Vignesh        | 0%          | NOT SELECTED ❌ |

### Top Candidate

Arun Kumar – 100%

## Technologies Used

* HTML
* CSS
* Python
* Flask
* SQLite
* PyPDF2
* Regular Expressions (re)

## Future Enhancements

* NLP-Based Resume Analysis
* AI Skill Recommendation
* Resume Classification
* Candidate Performance Prediction
* Recruiter Analytics Dashboard
* Excel/PDF Report Generation
* Email Notifications

## Conclusion

The Sample AI-Powered Resume Screening System automates the recruitment process by analyzing multiple resumes, calculating candidate scores, ranking applicants, and identifying the most suitable candidate. The system minimizes manual effort, improves recruitment efficiency, and provides a structured hiring workflow for organizations.

## Developed By

ROSHINI.P
