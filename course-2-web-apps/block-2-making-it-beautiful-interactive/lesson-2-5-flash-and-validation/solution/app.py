# app.py
# Form calculator capstone — copy this folder to my_web_calc/ at project root

from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "learning-flash-key"


@app.route("/", methods=["GET", "POST"])
def calc():
    total = None
    if request.method == "POST":
        raw_a = request.form.get("a", "").strip()
        raw_b = request.form.get("b", "").strip()
        if not raw_a or not raw_b:
            flash("Please enter both numbers.")
        else:
            try:
                num_a = int(raw_a)
                num_b = int(raw_b)
                total = num_a + num_b
            except ValueError:
                flash("Use whole numbers only (like 3 or 10).")
    return render_template("calc.html", total=total)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
