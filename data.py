import requests
import json
import random

response = requests.get(
    "https://opentdb.com/api.php?amount=5&category=9&difficulty=easy&type=multiple"
)

data = response.json()

# print(data)

convert = json.dumps(data)

print(convert)

# # quest_dict = []

# print(response.status_code)
# print(convert)

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

# print(json_data["results"])

# for question in json_data["results"]:
    # print("Question:", question["question"])
    # print("Correct Answer:", question["correct_answer"])
    # print("Incorrect Answers:", question["incorrect_answers"][0])
# print(json_data["results"][0]["incorrect_answers"][0])
# print(json_data["results"][0]["correct_answer"][0])

# incorrect_answers = json_data["results"][0]["incorrect_answers"]
# correct_answer = json_data["results"][0]["correct_answer"]
# random_index = random.randint(0, len(incorrect_answers))
# incorrect_answers.insert(random_index, correct_answer)

# print(incorrect_answers)