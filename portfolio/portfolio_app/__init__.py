from flask import Flask, render_template, abort

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

slug_to_project = {project["slug"]: project for project in projects}

@app.context_processor
def inject_contact_info():
    return dict(contact_info=contact_info)

@app.route("/")
def home():
    return render_template("home.html", projects=projects)


@app.route("/about")
def about():
    return render_template("about.html")

# Two ways to do this:
# - either store everything about a project in Python and populate a generic `project.html` template.
# - or as done here, have separate templates for each project
# At the end of the day, we have to write the project info somewhere, and HTML is a great tool for that.
# This allows each project to be slightly different as we choose,
# And with Jinja2 we can always reuse parts of the code as macros (more on that, later!)
@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"project_{slug}.html", project=slug_to_project[slug])