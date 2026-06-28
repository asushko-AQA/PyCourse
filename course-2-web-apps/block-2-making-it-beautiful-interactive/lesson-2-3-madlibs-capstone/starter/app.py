# app.py
# Mad-Libs capstone — copy this folder to my_web_madlibs/ at project root

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def madlibs():
    story = ""
    if request.method == "POST":
        # TODO: Read noun, verb, adjective, place from request.form
        # TODO: Build a silly story string with f-strings
        pass
    return render_template("madlibs.html", story=story)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
