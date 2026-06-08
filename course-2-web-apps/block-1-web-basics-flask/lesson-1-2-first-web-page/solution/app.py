# app.py
# Route Lab — your first web page with Flask

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Web World!"


if __name__ == "__main__":
    app.run(port=5000, debug=True)
