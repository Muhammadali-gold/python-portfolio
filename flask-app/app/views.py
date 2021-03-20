from app import app

from flask import render_template

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello")
def indexhello():
    return "Hello world"

@app.route("/about")
def about():
    return "All about Flask"   

@app.route("/abouth")
def abouth():
    return "<h1 style='color: red;'>I'm a red H1 heading!</h1>"     

@app.route("/aboutk")
def aboutk():
    return """
    <h1 style='color: red;'>I'm a red H1 heading!</h1>
    <p>This is a lovely little paragraph</p>
    <code>Flask is <em>awesome</em></code>
    """    