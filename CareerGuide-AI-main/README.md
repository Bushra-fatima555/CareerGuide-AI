# 🚀 CareerGuide AI

## Smart Career Recommendation System

CareerGuide AI is a web-based career recommendation system developed using **Python and Flask**. It helps students explore suitable career options based on their educational background, interests, skills, preferred work style, career goals, and personal priorities.

The system uses a **weighted rule-based scoring algorithm** to analyze the user's answers and generate personalized career recommendations.

---

## 🎯 Project Objective

The main objective of CareerGuide AI is to help students make better career decisions by providing:

* Personalized career recommendations
* Top career matches with percentage scores
* Recommended skills
* Relevant career fields
* Suggested education
* Step-by-step career roadmap

---

## ✨ Main Features

### 🎓 Career Assessment

Students answer questions about their:

* Educational background
* Main interests
* Strongest skills
* Preferred work style
* Career goals
* Personal priorities

### 🧠 Smart Career Matching

The system applies a weighted scoring algorithm to compare the student's profile with different career paths.

### 🥇 Top Career Recommendation

The system displays the career with the highest compatibility score.

### 📊 Top 3 Matches

Students can view their three strongest career matches with percentage scores.

### 🛣️ Career Roadmap

The system provides a simple roadmap showing the recommended steps for entering the selected career.

### 💼 Career Information

Each recommendation includes:

* Required skills
* Career fields
* Educational requirements
* Career description

---

## 💻 Technologies Used

| Technology | Purpose                    |
| ---------- | -------------------------- |
| Python     | Backend programming        |
| Flask      | Web framework              |
| HTML       | Web page structure         |
| CSS        | User interface and styling |
| Jinja2     | Dynamic content rendering  |
| Git        | Version control            |
| GitHub     | Source code management     |

---

## 🏗️ Project Structure

```text
CareerGuide-AI/
│
├── app.py
│
├── requirements.txt
│
├── .gitignore
│
├── README.md
│
└── templates/
    │
    └── home.html
```

---

## ⚙️ How to Run the Project

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd CareerGuide-AI
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

### 5. Open the application

Open the following address in your browser:

```text
http://127.0.0.1:5000/
```

---

## 🧠 Recommendation Algorithm

CareerGuide AI uses a weighted scoring approach.

Different factors contribute different points to each career:

* Educational background
* Career interest
* Skills
* Work style
* Career goal
* Personal priority

The system calculates the total score for each career and sorts the careers according to their scores.

The highest-scoring career is shown as the **Best Career Match**, while the next two highest-scoring careers are displayed as alternative recommendations.

---

## 🧪 Testing

The system was tested using different student profiles.

| Test Case | Expected Career   | Result                  | Status |
| --------- | ----------------- | ----------------------- | ------ |
| TC-01     | Software Engineer | Software Engineer — 78% | ✅ PASS |
| TC-02     | Doctor            | Doctor — 98%            | ✅ PASS |
| TC-03     | Business Manager  | Business Manager — 93%  | ✅ PASS |
| TC-04     | UI/UX Designer    | UI/UX Designer — 93%    | ✅ PASS |
| TC-05     | Engineer          | Engineer — 93%          | ✅ PASS |

### Testing Summary

**5 out of 5 test cases passed successfully.**

**Test Pass Rate: 100%**

---

## 👥 Target Users

CareerGuide AI is designed for:

* School students
* College students
* University students
* Fresh graduates
* Students exploring different career options

The system is not limited to computer science or IT students.

---

## 🔮 Future Enhancements

Future versions can include:

* User login and registration
* Student profile management
* Database integration
* Machine Learning-based recommendations
* More career categories
* Career salary information
* Job and internship recommendations
* Admin dashboard
* Career assessment history
* Online deployment
* AI-powered career chatbot

---

## 📌 Project Type

**Software Construction and Development (SCD) Project**

### Project Name

**CareerGuide AI — Smart Career Recommendation System**

### Developed Using

**Python + Flask + HTML + CSS**

---

## 👩‍💻 Project Status

**Current Status: Functional Prototype**

The core career assessment, recommendation algorithm, result display, and testing have been successfully implemented.
