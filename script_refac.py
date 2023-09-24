import requests
import json
import random

response = requests.get(
    "https://opentdb.com/api.php?amount=15&category=9&difficulty=easy&type=multiple"
)

json_data_api = response.json()


# Gets the players name
start_game_name = input(
    "Welcome to Who Wants to be a Millionaire! Please enter a name and hit enter... "
).title()


# Game functions
def exit_game():
    print("Thanks for playing " + str(start_game_name) + "! Goodbye")
    exit()


def congratulations(winnings):
    print(" ")
    print("Correct, congratulations! You have won £{}!".format(winnings))


def want_to_continue():
    answer = input("Do you want to continue to the next question y/n? ")
    return answer


# Asks if they need instructions
instructions_needed = input(
    "Welcome, " + str(start_game_name) + "! Do you needs instructions, y/n? "
)
# Make sure they can use lower or uppercase
answer = instructions_needed.lower()

# Provides instructions or starts the game
if answer == "y":
    ready_to_start = input(
        """
Instructions: You will be asked 15 questions that will get increasingly difficult. Each question you get correct you will earn money, which will increase each with each question.
If you get a question wrong you will be out and lose all your money. Good luck, I hope you become a millionnaire!! Are you ready to begin (y/n)? 
          """
    )
else:
    ready_to_start = input("In that case are you ready to begin (y/n)? ")

import random

def ask_question(question_data, prize):
    question = question_data["question"]
    incorrect_answers = question_data["incorrect_answers"]
    correct_answer = question_data["correct_answer"]
    incorrect_answers.insert(random.randint(0, len(incorrect_answers)), correct_answer)

    print(" ")
    print(f"For £{prize}, Question:", question)
    print(incorrect_answers)
    user_answer = input("The correct answer is: ").title()

    if user_answer == correct_answer:
        print("Congratulations!")
        print(f"You've won £{prize}")
    else:
        exit_game()

def main():
    prize_values = [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 10000000]
    json_data = json_data_api  # Replace with your JSON data

    for i, prize in enumerate(prize_values, start=1):
        data = json_data["results"][i - 1]
        ask_question(data, prize)
        if i < len(prize_values) and want_to_continue() != "y":
            exit_game()

    print("AMAZING")
    print("YOU ARE NOW A MILLIONAIRE")

if __name__ == "__main__":
    main()
