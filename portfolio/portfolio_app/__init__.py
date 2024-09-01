from flask import Flask, render_template

app = Flask(__name__)
projects = [
    {
        "name": "Habit tracking app with Python and MongoDB",
        "thumb": "img/habit-tracking.png",
        "hero": "img/habit-tracking-hero.png",
        "categories": ["python", "web"],
        "slug": "habit-tracking",
        "prod": "https://udemy.com",
    },
    {
        "name": "Personal finance tracking app with React",
        "thumb": "img/personal-finance.png",
        "hero": "img/personal-finance.png",
        "categories": ["react", "javascript"],
        "slug": "personal-finance",
    },
    {
        "name": "REST API Documentation with Postman and Swagger",
        "thumb": "img/rest-api-docs.png",
        "hero": "img/rest-api-docs.png",
        "categories": ["writing"],
        "slug": "api-docs",
    },
]

contact_info = [
    {
        "name": "Github",
        "details": "nicoopenna",
        "icon": "img/github_logo.svg",
        "url": "https://github.com/nicoopenna",
    },
    {
        "name": "Linkedin",
        "details": "Nicolas Penna",
        "icon": "img/linkedin_logo.svg",
        "url": "https://www.linkedin.com/in/nico-penna/",
    },
    {
        "name": "Email",
        "details": "nicolas.penna16@gmail.com",
        "icon": "img/email_logo.svg",
        "url": "mailto:nicolas.penna16@gmail.com",
    },
]

@app.context_processor
def inject_contact_info():
    return dict(contact_info=contact_info)

@app.route("/")
def home():
    return render_template("home.html", projects=projects)


@app.route("/about")
def about():
    return render_template("about.html")
