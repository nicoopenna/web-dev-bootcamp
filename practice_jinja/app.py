from flask import Flask, render_template, request


def create_app():
    app = Flask(__name__)
    @app.route("/todo")
    def todo():
        return render_template("home.html", todos=["Get milk", "Learn programming"])
    
    return app
