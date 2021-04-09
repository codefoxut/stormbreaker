import random


def average_height():
    # 🚨 Don't change the code below 👇
    student_heights: list = input("Input a list of student heights ").split()
    for n in range(0, len(student_heights)):
        student_heights[n] = int(student_heights[n])
    # 🚨 Don't change the code above 👆

    # Write your code below this row 👇
    count, sum_of_heights = 0, 0
    for i in student_heights:
        count += 1
        sum_of_heights += i
    avg = round(sum_of_heights / count)
    print(avg)


def high_score():
    # 🚨 Don't change the code below 👇
    student_scores: list = input("Input a list of student scores ").split()
    for n in range(0, len(student_scores)):
        student_scores[n] = int(student_scores[n])
    print(student_scores)
    # 🚨 Don't change the code above 👆

    # Write your code below this row 👇
    h_score = 0
    for i in student_scores:
        if i > h_score:
            h_score = i
    print(h_score)


def add_even_numbers():
    sum_of_evens = 0
    for i in range(0, 101, 2):
        sum_of_evens += i
    print(sum_of_evens)


def fizz_buzz_game():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

class PasswordGenerator:
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    def easy_password(self):
        print("Welcome to the PyPassword Generator!")
        nr_letters = int(input("How many letters would you like in your password?\n"))
        nr_symbols = int(input(f"How many symbols would you like?\n"))
        nr_numbers = int(input(f"How many numbers would you like?\n"))

        # Eazy Level - Order not randomised:
        # e.g. 4 letter, 2 symbol, 2 number = JduE&!91
        password = ''
        for _ in range(int(nr_letters)):
            password += self.letters[random.randint(0, len(self.letters) - 1)]

        for _ in range(int(nr_symbols)):
            password += self.symbols[random.randint(0, len(self.symbols) - 1)]

        for _ in range(int(nr_numbers)):
            password += self.numbers[random.randint(0, len(self.numbers) - 1)]

        print(password)

    def hard_password(self):
        print("Welcome to the PyPassword Generator!")
        nr_letters = int(input("How many letters would you like in your password?\n"))
        nr_symbols = int(input(f"How many symbols would you like?\n"))
        nr_numbers = int(input(f"How many numbers would you like?\n"))

        # Hard Level - Order of characters randomised:
        # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
        choose_count = [nr_letters, nr_symbols, nr_numbers]
        password = ''
        while choose_count[0] + choose_count[1] + choose_count[2] > 0:
            ty = random.randint(0, 2)
            if choose_count[ty] > 0:
                if ty == 0:
                    password += self.letters[random.randint(0, len(self.letters) - 1)]
                elif ty == 1:
                    password += self.symbols[random.randint(0, len(self.symbols) - 1)]
                else:
                    password += self.numbers[random.randint(0, len(self.numbers) - 1)]
                choose_count[ty] -= 1

        print(password)


if __name__ == '__main__':
    # average_height()
    # high_score()
    # add_even_numbers()
    # fizz_buzz_game()
    # PasswordGenerator().easy_password()
    PasswordGenerator().hard_password()
