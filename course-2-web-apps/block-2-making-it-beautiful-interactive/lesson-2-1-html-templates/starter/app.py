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


# TODO: Add route "/about" — use render_template("about.html", page_title="About", ...)
# TODO: Add route "/jokes" — use render_template("jokes.html", page_title="Jokes", ...)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
