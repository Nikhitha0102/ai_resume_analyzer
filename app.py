from flask import Flask, request, jsonify
from flask_cors import CORS
import PyPDF2
app = Flask(__name__)
CORS(app)
# -----------------------------
# Extract text from PDF
# -----------------------------
def extract_text(file):
    reader = PyPDF2.PdfReader(file)
    text = ""

    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()

    return text
# -----------------------------
# Skill list
# -----------------------------
skills_list = [
    "python", "java", "sql", "machine learning",
    "data analysis", "html", "css", "javascript",
    "flask", "react", "node", "c++", "excel", "power bi",
    "deep learning", "algorithms"
]
# -----------------------------
# Extract skills
# -----------------------------
def extract_skills(text):
    found_skills = []
    text = text.lower()

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills
# -----------------------------
# Calculate score
# -----------------------------
def calculate_score(skills):
    return len(skills) * 10
# -----------------------------
# Job Roles (NEW)
# -----------------------------
job_roles = {
    "data_analyst": ["python", "sql", "excel", "power bi"],
    "software_engineer": ["java", "c++", "algorithms"],
    "ml_engineer": ["python", "machine learning", "deep learning"],
    "web_developer": ["html", "css", "javascript", "react"]
}
# -----------------------------
# Suggestions (SMART)
# -----------------------------
def generate_suggestions(skills, job_skills):
    suggestions = []

    for skill in job_skills:
        if skill not in skills:
            suggestions.append(f"Learn {skill}")

    return suggestions
# -----------------------------
# Job Matching
# -----------------------------
def match_job(skills, job_skills):
    if len(job_skills) == 0:
        return [], 0
    matched = []
    for skill in skills:
        if skill in job_skills:
            matched.append(skill)

    match_percentage = (len(matched) / len(job_skills)) * 100

    return matched, round(match_percentage, 2)
# -----------------------------
# Home Route
# -----------------------------
@app.route('/')
def home():
    return "✅ Resume Analyzer API is running"
# -----------------------------
# Upload API
# -----------------------------
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files['file']
    # Get selected job role
    job_role = request.form.get("job_role")
    job_skills = job_roles.get(job_role, [])
    # Extract text
    text = extract_text(file)

    # Extract skills
    skills = extract_skills(text)

    # Score
    score = calculate_score(skills)

    # Matching
    matched, match_percent = match_job(skills, job_skills)

    # Suggestions
    suggestions = generate_suggestions(skills, job_skills)

    return jsonify({
        "message": "Resume uploaded successfully",
        "selected_job": job_role,
        "skills": skills,
        "score": score,
        "job_match": match_percent,
        "matched_skills": matched,
        "suggestions": suggestions,
        "preview": text[:300]
    })


# -----------------------------
# Run server
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True)