# app.py
# Studio Pages — HTML forms with GET and POST

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


# TODO: Add route "/greet" (GET only) — read request.args.get("name") and show a greeting
# TODO: Add route "/message" (GET and POST) — read request.form.get("text") on POST


if __name__ == "__main__":
    app.run(port=5000, debug=True)
