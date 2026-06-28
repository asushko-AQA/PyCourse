# app.py
# Form calculator capstone — copy this folder to my_web_calc/ at project root

from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "learning-flash-key"


@app.route("/", methods=["GET", "POST"])
def calc():
    total = None
    if request.method == "POST":
        # TODO: Read a and b from request.form
        # TODO: flash("...") when fields are empty or not whole numbers
        # TODO: Set total = num_a + num_b when valid
        pass
    return render_template("calc.html", total=total)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
