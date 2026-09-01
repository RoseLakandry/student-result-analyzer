
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":

        name = request.form["name"]
        roll = request.form["roll"]

        marks = [
            int(request.form["sub1"]),
            int(request.form["sub2"]),
            int(request.form["sub3"]),
            int(request.form["sub4"]),
            int(request.form["sub5"])
        ]

        total = sum(marks)
        percentage = total / 5
        highest = max(marks)
        lowest = min(marks)

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

        if all(mark >= 35 for mark in marks):
            status = "PASS"
        else:
            status = "FAIL"

        result = {
            "name": name,
            "roll": roll,
            "total": total,
            "percentage": percentage,
            "highest": highest,
            "lowest": lowest,
            "grade": grade,
            "status": status
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
