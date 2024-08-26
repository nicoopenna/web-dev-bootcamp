from flask import Flask
from flask import render_template

app = Flask(__name__)

# define custom data structure with a class
class GalileanMoons:
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth


@app.route("/data-structures/")
def render_data_structures():

    # list operations
    movies = [
        "Leon the Professional",
        "The Usual Suspects",
        "A Beautiful Mind"
    ]

    # dictionary operations
    car = {
        "brand": "Tesla",
        "model": "Roadstar",
        "year": "2020",
    }

    # custom data structure operations
    moons = GalileanMoons("Io", "Europa", "Ganymede", "Callisto")

    kwargs = {
        "movies": movies,
        "car": car,
        "moons": moons,
    }

    return render_template("data_structures.html", **kwargs)

@app.route("/conditionals-basics/")
def render_conditionals_basics():
    company = "Microsoft"
    return render_template("conditionals_basics.html", company=company)

class User:
    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return f"User({self.username})"


@app.route("/conditionals-truthy/")
def render_conditionals_truthy():
    user = User("Adam")
    return render_template("conditionals_truthy.html", user=user)

@app.route("/for-loop/")
def render_loops_for():
    planets = [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupyter",
        "Saturn",
        "Uranus",
        "Neptune",
    ]
    return render_template("for_loop.html", planets=planets)

@app.route("/for-loop/dict/")
def render_loops_for_dict():
    cuisines = {
        "Italy": "Neapolitan Pizza",
        "France": "Baguette",
        "Spain": "Churros",
        "Japan": "Sushi",
        "India": "Dosa",
    }
    return render_template("for_loop_dict.html", cuisines=cuisines)

@app.route("/for-loop/conditionals/")
def render_for_loop_conditionals():
    user_os = [
        ("Miller", "Windows"),
        ("Bob", "MacOS"),
        ("Zach", "Linux"),
        ("Annie", "Linux"),
        ("Farah", "Windows"),
        ("George", "Windows"),
    ]

    return render_template("for_loop_conditionals.html", user_os=user_os)