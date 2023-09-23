import requests
import json

# Gets the players name
start_game_name = input(
    "Welcome to Who Wants to be a Millionaire! Please enter a name and hit enter... "
)
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

# Give player a chance to exit game or start game
if ready_to_start == "n":
    print("Thanks for playing " + str(start_game_name) + "! Goodbye")
    exit()
else:
    print("Question 1: Does a cat have a: 1, b: 2, c: 3, d: 4, legs?")
    input("choose a, b, c or d: ")
    





print(ready_to_start)

response = requests.get("https://google.com")

# data = response.json()

# convert = json.dumps(data)

# quest_dict = []

print(response.status_code)
# print(convert)
