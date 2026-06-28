# app.py
# Mad-Libs capstone — copy this folder to my_web_madlibs/ at project root

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def madlibs():
    story = ""
    if request.method == "POST":
        noun = request.form.get("noun", "something").strip() or "something"
        verb = request.form.get("verb", "move").strip() or "move"
        adjective = request.form.get("adjective", "silly").strip() or "silly"
        place = request.form.get("place", "somewhere").strip() or "somewhere"
        story = (
            f"One sunny day, a {adjective} {noun} decided to {verb} "
            f"all the way to {place}. The crowd cheered. The end!"
        )
    return render_template("madlibs.html", story=story)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
