# import requests
import json

# winnings = 0

# Gets the players name
start_game_name = input(
    "Welcome to Who Wants to be a Millionaire! Please enter a name and hit enter... "
)


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
if ready_to_start.lower() == "y":
    print(" ")
    print("For £100, Question 1: What is the capital of France?")
    print("a: Madrid")
    print("b: Berlin")
    print("c: Rome")
    print("d: Paris")
    q1answer = input("choose a, b, c or d: ")
else:
    exit_game()
if q1answer.lower() == "d":
    congratulations(100)
else:
    exit_game()

# Question 2 - £200
if want_to_continue() == "y":
    print(" ")
    print("For £200, Question 2: What is known as the Red Planet?")
    print("a: Venus")
    print("b: Mars")
    print("c: Jupiter")
    print("d: Saturn")
    q2answer = input("choose a, b, c or d: ")
else:
    exit_game()
if q2answer.lower() == "b":
    congratulations(200)
else:
    exit_game()

# Question 3 - £300
if want_to_continue() == "y":
    print(" ")
    print("For £300, Question 3: Who wrote the play 'Romeo and Juliet'?")
    print("a: Charles Dickens")
    print("b: William Shakespeare")
    print("c: Jane Austen")
    print("d: F.ScottFitzgerald")
    q3answer = input("choose a, b, c, or d: ")
else:
    exit_game()
if q3answer.lower() == "b":
    congratulations(300)
else:
    exit_game()

# Question 4 - £500
if want_to_continue() == "y":
    print(" ")
    print("For £500, Question 4: What is the chemical symbol for the element gold?")
    print("a: Go")
    print("b: Gd")
    print("c: Au")
    print("d: Ag")
    q4answer = input("choose a, b, c, d: ")
else:
    exit_game()
if q4answer == "c":
    congratulations(500)
else:
    exit_game()

# Question 5 - £1000
if want_to_continue() == "y":
    print(" ")
    print("For £1000, Question 5: What is the largest mammal in the world?")
    print("a: Elephant")
    print("b: Blue Whale")
    print("c: Giraffe")
    print("d: Hippopotamus")
    q5answer = input("choose a, b, c, d: ")
else:
    exit_game()
if q5answer == "b":
    congratulations(1000)
else:
    exit_game()

# Question 6 - £2000
if want_to_continue() == "y":
    print(" ")
    print(
        "For £2000, Question 6: In which year did Christopher Columbus first arrive in the Americas?"
    )
    print("a: 1492")
    print("b: 1620")
    print("c: 1776")
    print("d: 1812")
    q6answer = input("choose a, b, c, d: ")
else:
    exit_game()
if q5answer == "a":
    congratulations(2000)
else:
    exit_game()

# Question 7 - £4000
if want_to_continue() == "y":
    print(" ")
    print(
        "For £4000, Question 7: Which gas makes up the majority of Earth's atmosphere?"
    )
    print("a: Oxygen")
    print("b: Carbon Diaoxide")
    print("c: Nitrogen")
    print("d: Hydrogen")
    q5answer = input("choose a, b, c, d: ")
else:
    exit_game()
if q5answer == "c":
    congratulations(4000)
else:
    exit_game()

# Question 8 - £8000
if want_to_continue() == "y":
    print(" ")
    print(
        "For £8000, Question 8: Who was the first woman to fly solo across the Atlantic Ocean?"
    )
    print("a: Amelia Earhart")
    print("b: Marie Curie")
    print("c: Rosa Parks")
    print("d: Joan of Arc")
    q5answer = input("choose a, b, c, d: ")
else:
    exit_game()
if q5answer == "a":
    congratulations(8000)
else:
    exit_game()

# Question 9 - £16000
if want_to_continue() == "y":
    print(" ")
    print("For £16,000, Qution 9: What is the world's longest river?")
    print("a: Mississippi River")
    print("b: Nile River")
    print("c: Amazon River")
    print("d: Yangtze River")
    q5answer = input("choose a, b, c, d: ")
else:
    exit_game()
if q5answer == "b":
    congratulations(16000)
else:
    exit_game()

# Question 10 - £32000
if want_to_continue() == "y":
    print(" ")
    print(
        "For £32,000, Question 10: Which country is known as the Land of the Rising Sun?"
    )
    print("a: China")
    print("b: India")
    print("c: Japan")
    print("d: South Korea")
    q5answer = input("choose a, b, c, d: ")
else:
    exit_game()
if q5answer == "c":
    congratulations(32000)
else:
    exit_game()

# Question 11 - £64000
if want_to_continue() == "y":
    print(" ")
    print("For £64,000, Question 11: What is the chemical formula for water?")
    print("a: H2O")
    print("b: CO2")
    print("c: O2")
    print("d: NaCl")
    q5answer = input("choose a, b, c, d: ")
else:
    exit_game()
if q5answer == "a":
    congratulations(64000)
else:
    exit_game()

# Question 12 - £125000
if want_to_continue() == "y":
    print(" ")
    print("For £125,000, Question 12: Who painted the Mona Lisa?")
    print("a: Vincent van Gogh")
    print("b: Pablo Picasso")
    print("c: Leonardo da Vinci")
    print("d: Michelangelo")
    q5answer = input("choose a, b, c, d: ")
else:
    exit_game()
if q5answer == "c":
    congratulations(125000)
else:
    exit_game()

# Question 13 - £250000
if want_to_continue() == "y":
    print(" ")
    print("For £250,000, Question 13: What is the largest planet in our solar system?")
    print("a: Earth")
    print("b: Mars")
    print("c: Jupiter")
    print("d: Saturn")
    q5answer = input("choose a, b, c, d: ")
else:
    exit_game()
if q5answer == "c":
    congratulations(250000)
else:
    exit_game()

# Question 14 - £500000
if want_to_continue() == "y":
    print(" ")
    print(
        "For £500,000, Question 14: What is the process by which plants make their own food using sunlight?"
    )
    print("a: Respiration")
    print("b: Photosynthesis")
    print("c: Digestion")
    print("d: Fermentation")
    q5answer = input("choose a, b, c, d: ")
else:
    exit_game()
if q5answer == "b":
    congratulations(500000)
else:
    exit_game()

# Question 15 - £10000000
if want_to_continue() == "y":
    print(" ")
    print("THE MILLION POUND QUESTION!!")
    print("Question 15: In which year did the Titanic sink?")
    print("a: 1901")
    print("b: 1912")
    print("c: 1923")
    print("d: 1934")
    q5answer = input("choose a, b, c, d: ")
else:
    exit_game()
if q5answer == "b":
    print("AMAZING")
    print("YOU ARE NOW A MILLIONAIRE")
else:
    exit_game()

# print(ready_to_start)

# response = requests.get("https://google.com")

# data = response.json()

# convert = json.dumps(data)

# quest_dict = []

# print(response.status_code)
# print(convert)
