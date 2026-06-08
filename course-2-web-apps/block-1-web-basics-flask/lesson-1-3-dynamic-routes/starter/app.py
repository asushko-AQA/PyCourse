# app.py
# Route Lab — dynamic routes with URL variables

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to Dynamic Routes! Try /hello/YourName"


# TODO: Add a route "/hello/<name>" that greets the visitor by name
# Hint: def hello(name): return f"Hello, {name}!"


if __name__ == "__main__":
    app.run(port=5000, debug=True)
