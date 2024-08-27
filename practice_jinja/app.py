from flask import Flask, render_template, request


def create_app():
    app = Flask(__name__)
    todos = [
        ("Get milk", False),
        ("Learn Programming", True)
    ]
    @app.route("/todo")
    def todo():
        return render_template("home.html", todos=todos)
    
    return app
