from projects.quiz_game.question_model import Question


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        print(f"We have {len(self.question_list)} questions for you.")

    def ask_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text} (True/False)?: "
        )
        self.check_the_answer(user_answer, current_question.answer)

    def check_the_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
            guess = False
        print(f"The correct answer is {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def display_final_score(self):
        print(f"Your final score was: {self.score}/{self.question_number}")
