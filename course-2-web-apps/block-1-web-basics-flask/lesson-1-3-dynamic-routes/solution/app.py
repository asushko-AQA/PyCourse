# app.py
# Route Lab — dynamic routes with URL variables

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to Dynamic Routes! Try /hello/YourName"


@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {name}!"


if __name__ == "__main__":
    app.run(port=5000, debug=True)
