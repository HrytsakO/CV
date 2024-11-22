from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    name = "Oleksii Hrytsak"
    title = "Python Web Developer"
    email = "ohrytsak@icloud.com"
    phone = "+1-248-632-8863"
    github = "https://github.com/HrytsakO?tab=repositories"
    objective = "Entry-level Python Developer eager to apply skills in Flask, Django, and SQL to develop efficient web solutions. Committed to learning and growing within a collaborative environment."
    skills = ["Python", "SQL", "Flask", "Django", "Git", "MySQL", "Linux", "Problem-solving", "PyCharm"]
    experience = [
        {
            "role": "IT Assistant System Administrator",
            "company": "HardReset",
            "dates": "Jan 2022 - Mar 2022",
            "description": [
                "Supported daily IT operations, including server maintenance and network troubleshooting.",
                "Managed and optimized MySQL databases.",
                "Automated routine administrative tasks using Python scripts."
            ]
        }
    ]
    education = [
        {
            "degree": "Associate Degree in Computer Science",
            "institution": "Zespół Szkół Zawodowych Huty im. Tadeusza Sendzimira in Krakow city, Poland",
            "dates": "2019 - 2023"
        },
        {
            "degree": "Python Core Certificate",
            "institution": "SoftServe IT Academy Lviv city, Ukraine",
            "dates": "2021"
        }
    ]
    projects = [
        {
            "name": "Python Automation Suite",
            "description": "Organizes files in the current directory into folders based on their extensions; fetches the <title> tags from a given URL; sends an email via SMTP",
            "link": "https://github.com/HrytsakO/python-automation-suite"
        },
        {
            "name": "Calculator with UI",
            "description": "Just calculator with user-friendly interface",
            "link": "https://github.com/HrytsakO/Calculator-with-UI"
        },
        {
            "name": "Simple AI Project",
            "description": "The goal of this project is to build a Sentiment Analysis tool that can analyze text and determine whether the sentiment expressed is positive, negative, or neutral.",
            "link": "https://github.com/HrytsakO/AI-Project"
        },
        {
            "name": "Personal Expense Tracker",
            "description": "The expense tracker is a program that helps users log their daily expenses, categorize them, and track their spending over time.",
            "link": "https://github.com/HrytsakO/Personal-Expense-Tracker"
        }
    ]
    return render_template(
        "index.html",
        name=name,
        title=title,
        email=email,
        phone=phone,
        github=github,
        objective=objective,
        skills=skills,
        experience=experience,
        education=education,
        projects=projects,
    )

if __name__ == "__main__":
    app.run(debug=True)