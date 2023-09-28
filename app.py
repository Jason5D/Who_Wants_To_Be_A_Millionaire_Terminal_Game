from flask import Flask, render_template, request, redirect, url_for
import json
import random
import requests

app = Flask(__name__)

response = requests.get(
    "https://opentdb.com/api.php?amount=15&category=9&difficulty=easy&type=multiple"
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/question/<int:question_number>", methods=["GET", "POST"])
def ask_question(question_number):
    prize = prize_values[question_number - 1]
    data = json_data_api["results"][question_number - 1]

    if request.method == "POST":
        user_answer = request.form.get("user_answer")
        correct_answer = data["correct_answer"]

        if user_answer == correct_answer:
            next_question_number = question_number + 1
            if next_question_number <= len(prize_values):
                return render_template(
                    "congratulations.html",
                    prize=prize,
                    next_question_number=next_question_number,
                )
            else:
                return render_template("game_over.html")
        else:
            return render_template("game_over.html")

    return render_template("question.html", question_data=data, prize=prize)


if __name__ == "__main__":
    prize_values = [
        100,
        200,
        300,
        500,
        1000,
        2000,
        4000,
        8000,
        16000,
        32000,
        64000,
        125000,
        250000,
        500000,
        10000000,
    ]
    app.run(debug=True)
