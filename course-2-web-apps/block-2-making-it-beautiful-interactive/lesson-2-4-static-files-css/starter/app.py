# app.py
# Studio Pages — static CSS with url_for

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "home.html",
        page_title="Home",
        headline="Welcome to My Styled Studio",
    )


# TODO: Add "/about" route with render_template("about.html", page_title="About", tagline="...")
# TODO: Link static/style.css in base.html using url_for('static', filename='style.css')


if __name__ == "__main__":
    app.run(port=5000, debug=True)
