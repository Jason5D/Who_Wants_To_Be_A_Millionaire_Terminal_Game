<!-- # Who_Wants_To_Be_A_Millionaire_Terminal_Game -->

- I am building this game to learn about Python input() and API calls using Python

- I want to be able to enjoy this game myself or share it with my friends to play

1. Project Description

- This project will be created in a Python virtual environment to practice setting this up. I will need to download the request library using pip to call the API with the questions
- I will only need to use a GET request in this project
- I will be using this API website to generate increasingly difficult questions (https://opentdb.com/api_config.php)
- All this will be done in the terminal / cmd, using the input() method in Python

2. Installation Guide

- Python installation required
- This should run from one Python file
- Connection to the internet for the API call

3. Usage and Features

- It will be a set of 15 questions asked to the player
- They will be offered to type a choice of 4 answers
- If they get the question wrong they will lose and lose any money banked
- If they get a question right, they will bank the money for that question and move to the next question
- Before the next question is asked they can choose to exit the game with their current winnings
- After question 5, if they lose they will always bank the money up to question 5
- After question 10, if they lose they will always bank the money up to question 10
- The top prize will be £1 million
- Increments will be:
Q1 - £100
Q2 - £200
Q3 - £300
Q4 - £500
Q5 - £1000 bank
Q6 - £2000
Q7 - £4000
Q8 - £8000
Q9 - £16000
Q10 - £32000 bank
Q11 - £64000
Q12 - £125000
Q13 - £250000
Q14 - £500000
Q15 - £1000000 winner!

4. Technologies Used:

- Python
- Virtual Environment
- ipunt()
- requests
- terminal / cmd

5. Documentation and Code Structure

- Virtual environments https://docs.python.org/3/library/venv.html
- API https://opentdb.com/api_config.php
- https://www.dataquest.io/blog/python-api-tutorial/

6. Contributions

- Get in touch if you can help
- Future goal, is to maintain a leaderboard for whoever has played to see who can get the furthest!
- There is a slight issue with data from the API. Some data comes in corrupted so I will have to search for another api