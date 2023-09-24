import requests
import json
import random

response = requests.get(
    "https://opentdb.com/api.php?amount=5&category=9&difficulty=easy&type=multiple"
)

json_data = response.json()

# json_data = json.dumps(data)

# json_data = {
#     "response_code": 0,
#     "results": [
#         {
#             "category": "General Knowledge",
#             "type": "multiple",
#             "difficulty": "easy",
#             "question": "Which sign of the zodiac is represented by the Crab?",
#             "correct_answer": "Cancer",
#             "incorrect_answers": ["Libra", "Virgo", "Sagittarius"],
#         },
#         {
#             "category": "General Knowledge",
#             "type": "multiple",
#             "difficulty": "easy",
#             "question": "What is the Spanish word for &quot;donkey&quot;?",
#             "correct_answer": "Burro",
#             "incorrect_answers": ["Caballo", "Toro", "Perro"],
#         },
#         {
#             "category": "General Knowledge",
#             "type": "multiple",
#             "difficulty": "easy",
#             "question": "Which candy is NOT made by Mars?",
#             "correct_answer": "Almond Joy",
#             "incorrect_answers": ["M&amp;M&#039;s", "Twix", "Snickers"],
#         },
#         {
#             "category": "General Knowledge",
#             "type": "multiple",
#             "difficulty": "easy",
#             "question": "The Flag of the European Union has how many stars on it?",
#             "correct_answer": "12",
#             "incorrect_answers": ["10", "14", "16"],
#         },
#         {
#             "category": "General Knowledge",
#             "type": "multiple",
#             "difficulty": "easy",
#             "question": "What is the closest planet to our solar system&#039;s sun?",
#             "correct_answer": "Mercury",
#             "incorrect_answers": ["Mars", "Jupiter", "Earth"],
#         },
#     ],
# }



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

# Question 1 - £100
data = json_data["results"][0]
question_one = data["incorrect_answers"]
correct_one = data["correct_answer"]
question_one.insert(random.randint(0, len(question_one)), data["correct_answer"])

if ready_to_start.lower() == "y":
    print(" ")
    print("For £100, Question 1:", json_data["results"][0]["question"])
    print(question_one)
    q1answer = input("The correct answer is: ")
else:
    exit_game()
if q1answer.title() == correct_one:
    congratulations(100)
else:
    exit_game()

# Question 2 - £200
data = json_data["results"][1]
question_two = data["incorrect_answers"]
correct_two = data["correct_answer"]
question_two.insert(random.randint(0, len(question_two)), data["correct_answer"])

if want_to_continue() == "y":
    print(" ")
    print("For £200, Question 2:", json_data["results"][1]["question"])
    print(question_two)
    q2answer = input("The correct answer is: ")
else:
    exit_game()
if q2answer.title() == correct_two:
    congratulations(200)
else:
    exit_game()

# Question 3 - £300
data = json_data["results"][2]
question_three = data["incorrect_answers"]
correct_three = data["correct_answer"]
question_three.insert(random.randint(0, len(question_three)), data["correct_answer"])

if want_to_continue() == "y":
    print(" ")
    print("For £300, Question 3:", json_data["results"][2]["question"])
    print(question_three)
    q3answer = input("The correct answer is: ")
else:
    exit_game()
if q3answer.title() == correct_three:
    congratulations(300)
else:
    exit_game()

# Question 4 - £500
data = json_data["results"][3]
question_four = data["incorrect_answers"]
correct_four = data["correct_answer"]
question_four.insert(random.randint(0, len(question_four)), data["correct_answer"])

if want_to_continue() == "y":
    print(" ")
    print("For £500, Question 4", json_data["results"][3]["question"])
    print(question_four)
    q4answer = input("The correct answer is: ")
else:
    exit_game()
if q4answer.title() == correct_four:
    congratulations(500)
else:
    exit_game()

# Question 5 - £1000
data = json_data["results"][4]
question_five = data["incorrect_answers"]
correct_five = data["correct_answer"]
question_five.insert(random.randint(0, len(question_five)), data["correct_answer"])

if want_to_continue() == "y":
    print(" ")
    print("For £1000, Question 5:", json_data["results"][4]["question"])
    print(question_five)
    q5answer = input("The correct answer is: ")
else:
    exit_game()
if q5answer.title() == correct_five:
    congratulations(1000)
else:
    exit_game()

# Question 6 - £2000
data = json_data["results"][0]
question_one = data["incorrect_answers"]
correct_one = data["correct_answer"]
question_one.insert(random.randint(0, len(question_one)), data["correct_answer"])

if want_to_continue() == "y":
    print(" ")
    print(
        "For £2000, Question 6:", json_data["results"][0]["question"]
    )
    print("a: 1492")
    print("b: 1620")
    print("c: 1776")
    print("d: 1812")
    q6answer = input("The correct answer is: ")
else:
    exit_game()
if q5answer.title() == "a":
    congratulations(2000)
else:
    exit_game()

# Question 7 - £4000
data = json_data["results"][0]
question_one = data["incorrect_answers"]
correct_one = data["correct_answer"]
question_one.insert(random.randint(0, len(question_one)), data["correct_answer"])

if want_to_continue() == "y":
    print(" ")
    print(
        "For £4000, Question 7:", json_data["results"][0]["question"]
    )
    print("a: Oxygen")
    print("b: Carbon Diaoxide")
    print("c: Nitrogen")
    print("d: Hydrogen")
    q5answer = input("The correct answer is: ")
else:
    exit_game()
if q5answer.title() == "c":
    congratulations(4000)
else:
    exit_game()

# Question 8 - £8000
data = json_data["results"][0]
question_one = data["incorrect_answers"]
correct_one = data["correct_answer"]
question_one.insert(random.randint(0, len(question_one)), data["correct_answer"])

if want_to_continue() == "y":
    print(" ")
    print(
        "For £8000, Question 8:", json_data["results"][0]["question"]
    )
    print("a: Amelia Earhart")
    print("b: Marie Curie")
    print("c: Rosa Parks")
    print("d: Joan of Arc")
    q5answer = input("The correct answer is: ")
else:
    exit_game()
if q5answer.title() == "a":
    congratulations(8000)
else:
    exit_game()

# Question 9 - £16000
data = json_data["results"][0]
question_one = data["incorrect_answers"]
correct_one = data["correct_answer"]
question_one.insert(random.randint(0, len(question_one)), data["correct_answer"])

if want_to_continue() == "y":
    print(" ")
    print("For £16,000, Qution 9:", json_data["results"][0]["question"])
    print("a: Mississippi River")
    print("b: Nile River")
    print("c: Amazon River")
    print("d: Yangtze River")
    q5answer = input("The correct answer is: ")
else:
    exit_game()
if q5answer.title() == "b":
    congratulations(16000)
else:
    exit_game()

# Question 10 - £32000
data = json_data["results"][0]
question_one = data["incorrect_answers"]
correct_one = data["correct_answer"]
question_one.insert(random.randint(0, len(question_one)), data["correct_answer"])

if want_to_continue() == "y":
    print(" ")
    print(
        "For £32,000, Question 10:", json_data["results"][0]["question"]
    )
    print("a: China")
    print("b: India")
    print("c: Japan")
    print("d: South Korea")
    q5answer = input("The correct answer is: ")
else:
    exit_game()
if q5answer == "c":
    congratulations(32000)
else:
    exit_game()

# Question 11 - £64000
data = json_data["results"][0]
question_one = data["incorrect_answers"]
correct_one = data["correct_answer"]
question_one.insert(random.randint(0, len(question_one)), data["correct_answer"])

if want_to_continue() == "y":
    print(" ")
    print("For £64,000, Question 11:", json_data["results"][0]["question"])
    print("a: H2O")
    print("b: CO2")
    print("c: O2")
    print("d: NaCl")
    q5answer = input("The correct answer is: ")
else:
    exit_game()
if q5answer == "a":
    congratulations(64000)
else:
    exit_game()

# Question 12 - £125000
data = json_data["results"][0]
question_one = data["incorrect_answers"]
correct_one = data["correct_answer"]
question_one.insert(random.randint(0, len(question_one)), data["correct_answer"])

if want_to_continue() == "y":
    print(" ")
    print("For £125,000, Question 12:", json_data["results"][0]["question"])
    print("a: Vincent van Gogh")
    print("b: Pablo Picasso")
    print("c: Leonardo da Vinci")
    print("d: Michelangelo")
    q5answer = input("The correct answer is: ")
else:
    exit_game()
if q5answer == "c":
    congratulations(125000)
else:
    exit_game()

# Question 13 - £250000
data = json_data["results"][0]
question_one = data["incorrect_answers"]
correct_one = data["correct_answer"]
question_one.insert(random.randint(0, len(question_one)), data["correct_answer"])

if want_to_continue() == "y":
    print(" ")
    print("For £250,000, Question 13:", json_data["results"][0]["question"])
    print("a: Earth")
    print("b: Mars")
    print("c: Jupiter")
    print("d: Saturn")
    q5answer = input("The correct answer is: ")
else:
    exit_game()
if q5answer == "c":
    congratulations(250000)
else:
    exit_game()

# Question 14 - £500000
data = json_data["results"][0]
question_one = data["incorrect_answers"]
correct_one = data["correct_answer"]
question_one.insert(random.randint(0, len(question_one)), data["correct_answer"])

if want_to_continue() == "y":
    print(" ")
    print(
        "For £500,000, Question 14:", json_data["results"][0]["question"]
    )
    print("a: Respiration")
    print("b: Photosynthesis")
    print("c: Digestion")
    print("d: Fermentation")
    q5answer = input("The correct answer is: ")
else:
    exit_game()
if q5answer == "b":
    congratulations(500000)
else:
    exit_game()

# Question 15 - £10000000
data = json_data["results"][0]
question_one = data["incorrect_answers"]
correct_one = data["correct_answer"]
question_one.insert(random.randint(0, len(question_one)), data["correct_answer"])

if want_to_continue() == "y":
    print(" ")
    print("THE MILLION POUND QUESTION!!")
    print("Question 15:", json_data["results"][0]["question"])
    print("a: 1901")
    print("b: 1912")
    print("c: 1923")
    print("d: 1934")
    q5answer = input("The correct answer is: ")
else:
    exit_game()
if q5answer == "b":
    print("AMAZING")
    print("YOU ARE NOW A MILLIONAIRE")
else:
    exit_game()


