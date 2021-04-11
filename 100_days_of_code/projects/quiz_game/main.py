import random

import requests

from projects.quiz_game.quiz_brain import QuizBrain
from question_model import Question
from data import question_data
from html import unescape


class QuizGame:
    def __init__(self):
        quiz = input("Fetch questions from internet, Type 'y' or 'n': ")
        question_bank = (
            self.fetch_live_questions() if quiz == "y" else self.populate_questions()
        )
        self.quiz_brain = QuizBrain(question_bank)

    @staticmethod
    def fetch_live_questions():
        number_of_questions = random.randint(10, 28)
        params = f"amount={number_of_questions}&category=9&difficulty=easy&type=boolean"
        resp = requests.get(f"https://opentdb.com/api.php?{params}")
        data = resp.json()
        question_bank = []
        for x in data["results"]:
            question_bank.append(
                Question(text=unescape(x["question"]), answer=x["correct_answer"])
            )
        return question_bank

    @staticmethod
    def populate_questions():
        question_bank = []
        for q in question_data:
            question_bank.append(Question(**q))
        return question_bank

    def start(self):
        while self.quiz_brain.still_has_question():
            self.quiz_brain.ask_question()

        print("You've completed the quiz.")
        self.quiz_brain.display_final_score()


if __name__ == "__main__":
    QuizGame().start()
