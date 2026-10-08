from flask import Flask, render_template, request

app = Flask(__name__)


# =========================================================
# CAREER DATABASE
# =========================================================

CAREERS = {

    "Software Engineer": {
        "description": "Design, develop and maintain software, websites and digital applications.",
        "skills": ["Programming", "Problem Solving", "Python", "Git & GitHub"],
        "fields": ["Web Development", "Mobile Development", "Software Engineering"],
        "education": "BS Software Engineering, BS Computer Science or related degree",
        "roadmap": [
            "Learn Programming Fundamentals",
            "Learn Python or another programming language",
            "Learn Git & GitHub",
            "Build software projects",
            "Apply for internships"
        ]
    },

    "Data Scientist": {
        "description": "Use data, mathematics and technology to discover useful information and solve real-world problems.",
        "skills": ["Python", "Statistics", "SQL", "Data Analysis"],
        "fields": ["Data Science", "Artificial Intelligence", "Data Analytics"],
        "education": "BS Data Science, Computer Science, Statistics or related degree",
        "roadmap": [
            "Learn Mathematics and Statistics",
            "Learn Python",
            "Learn SQL",
            "Practice Data Analysis",
            "Learn Machine Learning",
            "Build data projects"
        ]
    },

    "Doctor": {
        "description": "Diagnose, treat and help patients while working to improve human health.",
        "skills": ["Biology", "Communication", "Decision Making", "Problem Solving"],
        "fields": ["Medicine", "Surgery", "Healthcare"],
        "education": "MBBS followed by relevant specialization",
        "roadmap": [
            "Build strong Biology knowledge",
            "Complete medical education",
            "Complete clinical training",
            "Gain practical hospital experience",
            "Choose a medical specialization"
        ]
    },

    "Pharmacist": {
        "description": "Study medicines and help ensure their safe and effective use for patients.",
        "skills": ["Chemistry", "Biology", "Attention to Detail", "Communication"],
        "fields": ["Pharmacy", "Clinical Pharmacy", "Pharmaceutical Industry"],
        "education": "Doctor of Pharmacy (Pharm-D)",
        "roadmap": [
            "Study Chemistry and Biology",
            "Complete Pharm-D",
            "Gain practical pharmacy experience",
            "Learn medicine safety",
            "Explore clinical or industrial pharmacy"
        ]
    },

    "Lawyer": {
        "description": "Provide legal advice, represent clients and work with laws, regulations and legal documents.",
        "skills": ["Communication", "Research", "Critical Thinking", "Argumentation"],
        "fields": ["Corporate Law", "Criminal Law", "Civil Law"],
        "education": "LLB followed by required professional training",
        "roadmap": [
            "Improve communication skills",
            "Study legal concepts",
            "Complete LLB",
            "Gain legal internship experience",
            "Develop legal research skills"
        ]
    },

    "Business Manager": {
        "description": "Manage organizations, teams and projects while developing strategies for business growth.",
        "skills": ["Leadership", "Communication", "Management", "Marketing"],
        "fields": ["Business Management", "Marketing", "Entrepreneurship"],
        "education": "BBA, BS Management, MBA or related degree",
        "roadmap": [
            "Learn Business Fundamentals",
            "Develop Communication Skills",
            "Learn Marketing",
            "Develop Leadership Skills",
            "Work on business projects",
            "Gain practical experience"
        ]
    },

    "UI/UX Designer": {
        "description": "Design attractive, accessible and user-friendly digital products and experiences.",
        "skills": ["Creativity", "Figma", "Visual Design", "UX Research"],
        "fields": ["UI Design", "UX Design", "Product Design"],
        "education": "Degree or professional training in Design, Computer Science or related field",
        "roadmap": [
            "Learn Design Principles",
            "Learn Figma",
            "Study UX Research",
            "Create UI/UX projects",
            "Build a design portfolio"
        ]
    },

    "Teacher / Lecturer": {
        "description": "Educate students, develop their knowledge and help them achieve their academic goals.",
        "skills": ["Communication", "Teaching", "Leadership", "Patience"],
        "fields": ["School Education", "College Teaching", "University Education"],
        "education": "Relevant Bachelor's/Master's degree with required teaching qualification",
        "roadmap": [
            "Develop strong subject knowledge",
            "Improve communication skills",
            "Learn teaching methods",
            "Gain teaching experience",
            "Complete required qualifications"
        ]
    },

    "Journalist / Content Creator": {
        "description": "Research, create and communicate information through digital, print and media platforms.",
        "skills": ["Writing", "Communication", "Creativity", "Research"],
        "fields": ["Journalism", "Digital Media", "Content Creation"],
        "education": "BS Mass Communication, Journalism, Media Studies or related degree",
        "roadmap": [
            "Improve Writing Skills",
            "Learn Media Research",
            "Practice Content Creation",
            "Learn Digital Media Tools",
            "Build a professional portfolio"
        ]
    },

    "Scientist / Researcher": {
        "description": "Conduct research, perform experiments and develop knowledge in scientific fields.",
        "skills": ["Research", "Mathematics", "Critical Thinking", "Analysis"],
        "fields": ["Scientific Research", "Laboratories", "Academia"],
        "education": "Relevant Bachelor's degree followed by higher education and research",
        "roadmap": [
            "Build strong Science fundamentals",
            "Learn Research Methods",
            "Develop Analytical Skills",
            "Participate in research projects",
            "Pursue higher education"
        ]
    },

    "Engineer": {
        "description": "Use mathematics, science and technology to design and solve practical engineering problems.",
        "skills": ["Mathematics", "Problem Solving", "Technical Skills", "Critical Thinking"],
        "fields": ["Civil Engineering", "Electrical Engineering", "Mechanical Engineering"],
        "education": "Relevant BS Engineering degree",
        "roadmap": [
            "Build Mathematics and Physics skills",
            "Choose an engineering discipline",
            "Complete engineering degree",
            "Work on practical projects",
            "Gain industry experience"
        ]
    },

    "Agricultural Scientist": {
        "description": "Use science and technology to improve agriculture, crops, soil and food production.",
        "skills": ["Biology", "Research", "Science", "Problem Solving"],
        "fields": ["Agricultural Science", "Crop Science", "Food Production"],
        "education": "BS Agriculture, Agricultural Sciences or related degree",
        "roadmap": [
            "Study Biology and Agricultural Science",
            "Learn Crop and Soil Science",
            "Develop Research Skills",
            "Work on agricultural projects",
            "Gain field experience"
        ]
    }
}


# =========================================================
# SCORING OPTIONS
# =========================================================

BACKGROUND_SCORES = {

    "computer": {
        "Software Engineer": 18,
        "Data Scientist": 15,
        "Engineer": 8
    },

    "medical": {
        "Doctor": 18,
        "Pharmacist": 17,
        "Scientist / Researcher": 5
    },

    "business": {
        "Business Manager": 18,
        "Lawyer": 5,
        "Journalist / Content Creator": 5
    },

    "arts": {
        "UI/UX Designer": 18,
        "Journalist / Content Creator": 15,
        "Business Manager": 5
    },

    "science": {
        "Scientist / Researcher": 18,
        "Data Scientist": 15,
        "Agricultural Scientist": 12,
        "Doctor": 8
    },

    "engineering": {
        "Engineer": 18,
        "Software Engineer": 10,
        "Data Scientist": 8
    },

    "humanities": {
        "Lawyer": 17,
        "Teacher / Lecturer": 15,
        "Journalist / Content Creator": 15,
        "Business Manager": 5
    },

    "agriculture": {
        "Agricultural Scientist": 20,
        "Scientist / Researcher": 10
    }
}


INTEREST_SCORES = {

    "technology": {
        "Software Engineer": 20,
        "Data Scientist": 17
    },

    "healthcare": {
        "Doctor": 20,
        "Pharmacist": 18
    },

    "law": {
        "Lawyer": 20
    },

    "business": {
        "Business Manager": 20
    },

    "design": {
        "UI/UX Designer": 20
    },

    "teaching": {
        "Teacher / Lecturer": 20
    },

    "media": {
        "Journalist / Content Creator": 20
    },

    "science": {
        "Scientist / Researcher": 20,
        "Data Scientist": 10
    },

    "engineering": {
        "Engineer": 20
    },

    "agriculture": {
        "Agricultural Scientist": 20
    }
}


SKILL_SCORES = {

    "programming": {
        "Software Engineer": 15,
        "Data Scientist": 12
    },

    "biology": {
        "Doctor": 15,
        "Pharmacist": 15,
        "Agricultural Scientist": 12
    },

    "communication": {
        "Lawyer": 15,
        "Teacher / Lecturer": 15,
        "Journalist / Content Creator": 15,
        "Business Manager": 12
    },

    "creativity": {
        "UI/UX Designer": 15,
        "Journalist / Content Creator": 12
    },

    "mathematics": {
        "Data Scientist": 15,
        "Engineer": 15,
        "Scientist / Researcher": 12
    },

    "leadership": {
        "Business Manager": 15,
        "Teacher / Lecturer": 12,
        "Lawyer": 8
    },

    "research": {
        "Scientist / Researcher": 15,
        "Journalist / Content Creator": 12,
        "Data Scientist": 10,
        "Agricultural Scientist": 10
    },

    "technical": {
        "Engineer": 15,
        "Software Engineer": 12
    }
}


WORK_STYLE_SCORES = {

    "problem_solving": {
        "Software Engineer": 12,
        "Engineer": 15,
        "Data Scientist": 12
    },

    "helping_people": {
        "Doctor": 15,
        "Pharmacist": 14,
        "Teacher / Lecturer": 14
    },

    "creative": {
        "UI/UX Designer": 15,
        "Journalist / Content Creator": 13
    },

    "leadership": {
        "Business Manager": 15,
        "Lawyer": 10,
        "Teacher / Lecturer": 10
    },

    "research": {
        "Scientist / Researcher": 15,
        "Data Scientist": 12,
        "Agricultural Scientist": 12
    },

    "communication": {
        "Lawyer": 15,
        "Teacher / Lecturer": 14,
        "Journalist / Content Creator": 14
    }
}


GOAL_SCORES = {

    "technology": {
        "Software Engineer": 20,
        "Data Scientist": 15
    },

    "medical": {
        "Doctor": 20,
        "Pharmacist": 18
    },

    "business": {
        "Business Manager": 20
    },

    "design": {
        "UI/UX Designer": 20
    },

    "law": {
        "Lawyer": 20
    },

    "education": {
        "Teacher / Lecturer": 20
    },

    "media": {
        "Journalist / Content Creator": 20
    },

    "research": {
        "Scientist / Researcher": 20,
        "Data Scientist": 10
    },

    "engineering": {
        "Engineer": 20
    },

    "agriculture": {
        "Agricultural Scientist": 20
    }
}


PRIORITY_SCORES = {

    "impact": {
        "Doctor": 5,
        "Teacher / Lecturer": 5,
        "Lawyer": 5,
        "Agricultural Scientist": 5
    },

    "income": {
        "Software Engineer": 5,
        "Doctor": 5,
        "Engineer": 5,
        "Business Manager": 5
    },

    "creativity": {
        "UI/UX Designer": 5,
        "Journalist / Content Creator": 5
    },

    "stability": {
        "Teacher / Lecturer": 5,
        "Doctor": 5,
        "Engineer": 5,
        "Pharmacist": 5
    },

    "innovation": {
        "Software Engineer": 5,
        "Data Scientist": 5,
        "Engineer": 5
    },

    "knowledge": {
        "Scientist / Researcher": 5,
        "Teacher / Lecturer": 5,
        "Data Scientist": 5
    }
}


# =========================================================
# CALCULATE CAREER SCORES
# =========================================================

def add_scores(scores, selected_value, score_map):

    selected_scores = score_map.get(
        selected_value,
        {}
    )

    for career, points in selected_scores.items():

        scores[career] += points


def calculate_scores(answers):

    scores = {
        career: 0
        for career in CAREERS
    }

    add_scores(
        scores,
        answers["background"],
        BACKGROUND_SCORES
    )

    add_scores(
        scores,
        answers["interest"],
        INTEREST_SCORES
    )

    add_scores(
        scores,
        answers["skill"],
        SKILL_SCORES
    )

    add_scores(
        scores,
        answers["work_style"],
        WORK_STYLE_SCORES
    )

    add_scores(
        scores,
        answers["goal"],
        GOAL_SCORES
    )

    add_scores(
        scores,
        answers["priority"],
        PRIORITY_SCORES
    )

    return scores


# =========================================================
# HOME
# =========================================================

@app.route("/")
def home():

    return render_template(
        "home.html"
    )


# =========================================================
# RECOMMENDATION
# =========================================================

@app.route(
    "/recommend",
    methods=["POST"]
)
def recommend():

    answers = {

        "background": request.form.get(
            "background",
            ""
        ),

        "interest": request.form.get(
            "interest",
            ""
        ),

        "skill": request.form.get(
            "skill",
            ""
        ),

        "work_style": request.form.get(
            "work_style",
            ""
        ),

        "goal": request.form.get(
            "goal",
            ""
        ),

        "priority": request.form.get(
            "confidence",
            ""
        )
    }


    scores = calculate_scores(
        answers
    )


    # -----------------------------------------------------
    # SORT CAREERS BY SCORE
    # -----------------------------------------------------

    sorted_careers = sorted(
        scores.items(),
        key=lambda item: item[1],
        reverse=True
    )


    # Top 3 careers
    top_careers = sorted_careers[:3]


    recommended_career = top_careers[0][0]

    recommended_score = top_careers[0][1]


    # Maximum possible score is approximately 100
    match_score = min(
        recommended_score,
        100
    )


    # Avoid an extremely low display
    if match_score < 40:
        match_score = 40


    career = CAREERS[
        recommended_career
    ]


    # -----------------------------------------------------
    # ALTERNATIVE CAREERS
    # -----------------------------------------------------

    alternatives = []

    for career_name, score in top_careers[1:]:

        alternatives.append({

            "name": career_name,

            "score": min(
                score,
                100
            )

        })


    return render_template(

        "home.html",

        result=True,

        career_name=recommended_career,

        match_score=match_score,

        description=career[
            "description"
        ],

        skills=career[
            "skills"
        ],

        fields=career[
            "fields"
        ],

        education=career[
            "education"
        ],

        roadmap=career[
            "roadmap"
        ],

        alternatives=alternatives

    )


# =========================================================
# RUN
# =========================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )