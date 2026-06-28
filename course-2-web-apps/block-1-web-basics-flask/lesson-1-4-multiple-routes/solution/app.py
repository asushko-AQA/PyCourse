# app.py
# Route Lab — mini-site plus URL calculator

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    links = (
        "<h1>My Flask Site</h1>"
        "<p>Welcome! Visit <a href='/about'>About</a> or <a href='/jokes'>Jokes</a>.</p>"
        "<p>Calculator: try <a href='/add/3/5'>/add/3/5</a> or <a href='/add/10/7'>/add/10/7</a></p>"
    )
    return links


@app.route("/about")
def about():
    return "<h1>About Me</h1><p>I am learning Flask and building web pages with Python!</p>"


@app.route("/jokes")
def jokes():
    return (
        "<h1>Jokes</h1>"
        "<p>Why do programmers prefer dark mode?</p>"
        "<p>Because light attracts bugs!</p>"
    )


@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    total = a + b
    return f"<h1>Calculator</h1><p>{a} + {b} = {total}</p>"


if __name__ == "__main__":
    app.run(port=5000, debug=True)
