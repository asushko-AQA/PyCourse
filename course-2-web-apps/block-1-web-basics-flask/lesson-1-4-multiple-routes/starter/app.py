# app.py
# Route Lab — mini-site plus URL calculator

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    links = (
        "<h1>My Flask Site</h1>"
        "<p>Welcome! Visit <a href='/about'>About</a> or <a href='/jokes'>Jokes</a>.</p>"
        "<p>Calculator: try <a href='/add/3/5'>/add/3/5</a></p>"
    )
    return links


# TODO: Add route "/about" — return a short About page with an <h1> title
# TODO: Add route "/jokes" — return one programming joke
# TODO: Add route "/add/<int:a>/<int:b>" — return the sum as plain text or simple HTML


if __name__ == "__main__":
    app.run(port=5000, debug=True)
