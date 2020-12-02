from app import app
from datetime import datetime

from flask import render_template

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/about")
def about():
    return render_template("public/about.html")

@app.route("/jinja")
def jinja():
    my_html = "<h1>This is some HTML</h1>"
    suspicious = "<script>alert('NEVER TRUST USER INPUT!')</script>"

    # Strings
    my_name = "Pratyush"

    # Integers
    my_age = 30

    # Lists
    langs = ["Python", "JavaScript", "Java", "Ruby", "C", "Dart"]

    # Dictionaries
    friends = {
        "Abhipsha": 20,
        "Subha": 20,
        "Prapti": 20,
        "Sannath": 20,
        "Asutosh": 24
    }

    # Tuples
    colors = ("Red", "Blue")

    # Booleans
    cool = True

    # Classes
    class GitRemote:
        def __init__(self, name, description, domain):
            self.name = name
            self.description = description 
            self.domain = domain

        def pull(self):
            return f"Pulling repo '{self.name}'"

        def clone(self, repo):
            return f"Cloning into {repo}"

    my_remote = GitRemote(
        name="Learning Flask",
        description="Learn the Flask web framework for Python",
        domain="https://github.com/pranikz/flask-learn.git"

    
    )

    # Functions
    def repeat(x, qty=1):
        return x * qty

    return render_template(
        "public/jinja.html", my_name=my_name, my_age=my_age, langs=langs,
        friends=friends, colors=colors, cool=cool, GitRemote=GitRemote, 
        my_remote=my_remote, repeat=repeat
    )

    

    date1 = datetime.utcnow()

    return render_template(
    "public/jinja.html", my_name=my_name, my_age=my_age, langs=langs,
    friends=friends, colors=colors, cool=cool, GitRemote=GitRemote, 
    my_remote=my_remote, repeat=repeat, date=date1
)

@app.template_filter("clean_date")
def clean_date(dt):
    return dt.strftime("%d %b %Y")