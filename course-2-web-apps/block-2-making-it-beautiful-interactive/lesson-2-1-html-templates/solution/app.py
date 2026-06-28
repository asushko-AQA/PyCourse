# app.py
# Studio Pages — HTML templates with a shared base layout

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "home.html",
        page_title="Home",
        headline="Welcome to My Studio",
    )


@app.route("/about")
def about():
    return render_template(
        "about.html",
        page_title="About",
        bio="I am learning Flask and building pages with templates!",
    )


@app.route("/jokes")
def jokes():
    return render_template(
        "jokes.html",
        page_title="Jokes",
        joke_setup="Why do programmers prefer dark mode?",
        joke_punchline="Because light attracts bugs!",
    )


if __name__ == "__main__":
    app.run(port=5000, debug=True)
