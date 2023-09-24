import requests
import json
import random

response = requests.get(
    "https://opentdb.com/api.php?amount=15&category=9&difficulty=easy&type=multiple"
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
if q1answer == correct_one:
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
if q2answer == correct_two:
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
if q3answer == correct_three:
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
if q4answer == correct_four:
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
if q5answer == correct_five:
    congratulations(1000)
else:
    exit_game()


# Question 6 - £2000
data = json_data["results"][5]
question_six = data["incorrect_answers"]
correct_six = data["correct_answer"]
question_six.insert(random.randint(0, len(question_six)), data["correct_answer"])

if want_to_continue() == "y":
    print(" ")
    print("For £2000, Question 6:", json_data["results"][5]["question"])
    print(question_six)
    q6answer = input("The correct answer is: ")
else:
    exit_game()
if q6answer == correct_six:
    congratulations(2000)
else:
    exit_game()

# Question 7 - £4000
data = json_data["results"][6]
question_seven = data["incorrect_answers"]
correct_seven = data["correct_answer"]
question_one.insert(random.randint(0, len(question_seven)), data["correct_answer"])

if want_to_continue() == "y":
    print(" ")
    print("For £4000, Question 7:", json_data["results"][6]["question"])
    print(question_seven)
    q7answer = input("The correct answer is: ")
else:
    exit_game()
if q7answer.title() == correct_seven:
    congratulations(4000)
else:
    exit_game()

# Question 8 - £8000
data = json_data["results"][7]
question_eight = data["incorrect_answers"]
correct_eight = data["correct_answer"]
question_eight.insert(random.randint(0, len(question_eight)), data["correct_answer"])

if want_to_continue() == "y":
    print(" ")
    print("For £8000, Question 8:", json_data["results"][7]["question"])
    print(question_eight)
    q8answer = input("The correct answer is: ")
else:
    exit_game()
if q8answer.title() == correct_eight:
    congratulations(8000)
else:
    exit_game()

# Question 9 - £16000
data = json_data["results"][8]
question_nine = data["incorrect_answers"]
correct_nine = data["correct_answer"]
question_nine.insert(random.randint(0, len(question_nine)), data["correct_answer"])

if want_to_continue() == "y":
    print(" ")
    print("For £16,000, Qution 9:", json_data["results"][0]["question"])
    print(question_nine)
    q9answer = input("The correct answer is: ")
else:
    exit_game()
if q9answer.title() == correct_nine:
    congratulations(16000)
else:
    exit_game()

# Question 10 - £32000
data = json_data["results"][9]
question_ten = data["incorrect_answers"]
correct_ten = data["correct_answer"]
question_ten.insert(random.randint(0, len(question_ten)), data["correct_answer"])

if want_to_continue() == "y":
    print(" ")
    print("For £32,000, Question 10:", json_data["results"][9]["question"])
    print(question_ten)
    q10answer = input("The correct answer is: ")
else:
    exit_game()
if q10answer == correct_ten:
    congratulations(32000)
else:
    exit_game()

# Question 11 - £64000
data = json_data["results"][10]
question_eleven = data["incorrect_answers"]
correct_eleven = data["correct_answer"]
question_eleven.insert(random.randint(0, len(question_eleven)), data["correct_answer"])

if want_to_continue() == "y":
    print(" ")
    print("For £64,000, Question 11:", json_data["results"][0]["question"])
    print(question_eleven)
    q11answer = input("The correct answer is: ")
else:
    exit_game()
if q11answer == correct_eleven:
    congratulations(64000)
else:
    exit_game()

# Question 12 - £125000
data = json_data["results"][11]
question_twelve = data["incorrect_answers"]
correct_twelve = data["correct_answer"]
question_twelve.insert(random.randint(0, len(question_twelve)), data["correct_answer"])

if want_to_continue() == "y":
    print(" ")
    print("For £125,000, Question 12:", json_data["results"][11]["question"])
    print(question_twelve)
    q12answer = input("The correct answer is: ")
else:
    exit_game()
if q12answer == correct_twelve:
    congratulations(125000)
else:
    exit_game()

# Question 13 - £250000
data = json_data["results"][12]
question_thirteen = data["incorrect_answers"]
correct_thirteen = data["correct_answer"]
question_thirteen.insert(
    random.randint(0, len(question_thirteen)), data["correct_answer"]
)

if want_to_continue() == "y":
    print(" ")
    print("For £250,000, Question 13:", json_data["results"][12]["question"])
    print(question_thirteen)
    q13answer = input("The correct answer is: ")
else:
    exit_game()
if q13answer == correct_thirteen:
    congratulations(250000)
else:
    exit_game()

# Question 14 - £500000
data = json_data["results"][13]
question_fourteen = data["incorrect_answers"]
correct_fourteen = data["correct_answer"]
question_fourteen.insert(
    random.randint(0, len(question_fourteen)), data["correct_answer"]
)

if want_to_continue() == "y":
    print(" ")
    print("For £500,000, Question 14:", json_data["results"][13]["question"])
    print(question_fourteen)
    q14answer = input("The correct answer is: ")
else:
    exit_game()
if q14answer == correct_fourteen:
    congratulations(500000)
else:
    exit_game()

# Question 15 - £10000000
data = json_data["results"][14]
question_fifthteen = data["incorrect_answers"]
correct_fifthteen = data["correct_answer"]
question_fifthteen.insert(
    random.randint(0, len(question_fifthteen)), data["correct_answer"]
)

if want_to_continue() == "y":
    print(" ")
    print("THE MILLION POUND QUESTION!!")
    print("Question 15:", json_data["results"][14]["question"])
    print(question_fifthteen)
    q15answer = input("The correct answer is: ")
else:
    exit_game()
if q15answer == correct_fifthteen:
    print("AMAZING")
    print("YOU ARE NOW A MILLIONAIRE")
else:
    exit_game()
