🚀 AI Resume Analyzer & Job Matcher

📌 Project Overview

The AI Resume Analyzer & Job Matcher is a full-stack web application that analyzes resumes (PDF), extracts skills, calculates ATS score, and matches the resume with a given job description using NLP techniques.

It also provides:

- Job recommendations
- Missing skills
- Resume improvement suggestions

---

🎯 Key Features

✔ Resume Parsing (PDF)
✔ Skill Extraction
✔ ATS Score Calculation
✔ Job Description Matching (AI-based)
✔ Job Recommendations
✔ Resume Improvement Suggestions
✔ Interactive Dashboard UI

---

🛠️ Tech Stack

🔹 Backend

- Python
- Flask
- Flask-CORS
- PyPDF2
- Scikit-learn (TF-IDF, Cosine Similarity)

🔹 Frontend

- HTML
- CSS
- JavaScript

🔹 Tools

- Postman (API testing)
- GitHub (version control)
- Render / Netlify (deployment)

---

⚙️ How the Project Works

Step 1: Resume Upload

User uploads a PDF resume through the UI.

Step 2: Text Extraction

The backend extracts text using PyPDF2.

Step 3: Skill Extraction

The system scans resume text and identifies skills from a predefined list.

Step 4: ATS Score Calculation

The resume is scored based on:

- Skills present
- Resume length
- Sections (Education, Experience)
- Contact details

Step 5: Job Description Matching

User pastes a job description.
The system uses:

- TF-IDF Vectorization
- Cosine Similarity

to calculate how well the resume matches the job.

Step 6: Job Recommendation

Based on extracted skills, suitable job roles are suggested.

Step 7: Suggestions & Issues

The system identifies:

- Missing skills
- Resume weaknesses (e.g., missing experience section)

---

🧠 AI Concept Used

- TF-IDF (Text Feature Extraction)
- Cosine Similarity (Text Matching)

These are used to compare resume content with job descriptions.

---

📊 Output Includes

- ATS Score (Resume Quality)
- Job Match Percentage
- Extracted Skills
- Matched Skills
- Missing Skills
- Recommended Jobs
- Resume Issues

---

🖥️ Project Structure

Resume-Analyzer/
│
├── app.py              # Backend Flask API
├── index.html          # Frontend UI
├── requirements.txt    # Dependencies
└── README.md           # Documentation

---

▶️ How to Run the Project

Step 1: Clone Repository

git clone https://github.com/your-username/ai-resume-analyzer.git
cd ai-resume-analyzer

Step 2: Install Dependencies

pip install -r requirements.txt

Step 3: Run Backend

python app.py

Step 4: Open Frontend

- Open "index.html" in browser

---

🌍 Deployment

- Backend deployed using Render
- Frontend deployed using Netlify

---

💡 Future Enhancements

- User Login System
- Database Integration (MongoDB/MySQL)
- Resume Upload History
- PDF Report Generation
- AI-based Resume Feedback (Deep Learning)
- React Frontend

---

👩‍💻 Author

Manjula Jadav
📍 Hyderabad, India
📧 pkethavath31@gmail.com
🔗 GitHub: https://github.com/Nikhitha0102

---

⭐ Conclusion

This project demonstrates the integration of:

- Full-stack development
- NLP techniques
- Real-world problem solving (job matching)

It helps users improve resumes and align them with job requirements effectively.
