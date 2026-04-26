# 🚀 Smart Resume Analyzer

An AI-powered web application that analyzes resumes and provides a skill-based evaluation with improvement suggestions.

---

## 📌 Features

* 📄 Upload PDF resumes
* 🔍 Extract text using PyPDF2
* 🧠 Analyze skills based on predefined job requirements
* 📊 Generate resume score (%)
* ✅ Show **matched skills**
* ❌ Show **missing skills**
* 🎨 Modern UI using HTML + CSS
* ⚡ Built with Flask (Python backend)

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS
* **Backend:** Python (Flask)
* **Libraries:**

  * PyPDF2
  * NumPy (optional)
* **Database:** (optional upgrade) SQLite

---

## 📁 Project Structure

```
resume_analyzer/
│── app.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── uploads/
```

---

## ⚙️ Installation & Setup


### 2️⃣ Install Dependencies

```
pip install flask PyPDF2
```

### 3️⃣ Run Application

```
python app.py
```

### 4️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

---

##  How It Works

1. Upload your resume (PDF)
2. Application extracts text
3. Matches skills with job requirements
4. Displays:

   * Resume Score
   * Skills Found
   * Missing Skills

---

##  Example Output

* Score: **60%**
* Skills Found: Python, SQL
* Missing Skills: Machine Learning, Flask

---

##  Limitations

* Works best with text-based PDFs
* Keyword-based matching (basic NLP)
* No support for scanned/image resumes

