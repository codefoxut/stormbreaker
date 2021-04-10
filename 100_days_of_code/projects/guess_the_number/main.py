"""

# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


"""
import random

from projects.guess_the_number.arts import logo


class GuessNumber:

    @staticmethod
    def check_answer(guess, the_number):
        if the_number > guess:
            print("Too low")
        elif the_number < guess:
            print("Too high")
        else:
            print(f"You got it. The answer is {the_number}")

    @staticmethod
    def set_difficulty():
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        return 7 if difficulty == 'hard' else 10

    def start(self):
        print(logo)
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")
        the_number = random.randint(1, 100)
        guesses = self.set_difficulty()
        continue_guessing = True
        while continue_guessing:
            print(f"You have {guesses} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            self.check_answer(guess, the_number)
            guesses -= 1
            if the_number == guess:
                break
            elif guesses == 0:
                print("You've run out of guesses, you lose.")
                break
            else:
                print("Guess again.")


if __name__ == '__main__':
    GuessNumber().start()
