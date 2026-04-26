import os
from flask import Flask, request, render_template
import PyPDF2

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

JOB_SKILLS = ["python", "sql", "machine learning", "data analysis", "flask"]

def extract_text(file_path):
    text = ""
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text.lower()

def analyze_resume(text):
    found = []
    missing = []

    for skill in JOB_SKILLS:
        if skill in text:
            found.append(skill)
        else:
            missing.append(skill)

    score = int((len(found) / len(JOB_SKILLS)) * 100)
    return score, found, missing

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    if "resume" not in request.files:
        return render_template("index.html", error="No file uploaded")

    file = request.files["resume"]

    if file.filename == "":
        return render_template("index.html", error="No file selected")

    if not file.filename.endswith(".pdf"):
        return render_template("index.html", error="Only PDF files allowed")

    path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(path)

    text = extract_text(path)
    score, found, missing = analyze_resume(text)

    return render_template("index.html",
                           score=score,
                           found=found,
                           missing=missing)

if __name__ == "__main__":
    app.run(debug=True)