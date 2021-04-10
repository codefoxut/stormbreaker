def odd_or_even():
    # 🚨 Don't change the code below 👇
    number = int(input("Which number do you want to check? "))
    # 🚨 Don't change the code above 👆

    # Write your code below this line 👇
    if number % 2 == 0:
        print("This is an even number.")
    else:
        print("This is an odd number.")


def bmi_calculator():
    # 🚨 Don't change the code below 👇
    height = float(input("enter your height in m: "))
    weight = float(input("enter your weight in kg: "))
    # 🚨 Don't change the code above 👆

    #  Write your code below this line 👇
    bmi = round(weight / (height ** 2), 2)

    if bmi < 18.5:
        print(f"Your bmi is {bmi}, You are underweight.")
    elif 18.5 <= bmi < 25:
        print(f"Your bmi is {bmi}, You have a normal weight")
    elif 25 <= bmi < 30:
        print(f"Your bmi is {bmi}, You are slightly overweight.")
    elif 30 <= bmi < 35:
        print(f"Your bmi is {bmi}, You are obese")
    else:
        print(f"Your bmi is {bmi}, You are clinically obese.")


def leap_year1():
    # 🚨 Don't change the code below 👇
    year = int(input("Which year do you want to check? "))
    # 🚨 Don't change the code above 👆

    # Write your code below this line 👇
    if year % 400 == 0:
        print(f"{year} is a Leap Year.")
    elif year % 100 != 0 and year % 4 == 0:
        print(f"{year} is a Leap Year.")
    else:
        print(f"{year} is not a Leap Year.")


def leap_year():
    # 🚨 Don't change the code below 👇
    year = int(input("Which year do you want to check? "))
    # 🚨 Don't change the code above 👆

    # Write your code below this line 👇
    if year % 4 != 0:
        print(f"{year} is not a Leap Year.")
    elif year % 100 == 0 and year % 400 != 0:
        print(f"{year} is not a Leap Year.")
    else:
        print(f"{year} is a Leap Year.")


def pizza_order():
    # 🚨 Don't change the code below 👇
    print("Welcome to Python Pizza Deliveries!")
    size = input("What size pizza do you want? S, M, or L ")
    add_pepperoni = input("Do you want pepperoni? Y or N ")
    extra_cheese = input("Do you want extra cheese? Y or N ")
    # 🚨 Don't change the code above 👆

    # Write your code below this line 👇
    if size == "S":
        bill = 15
    elif size == "M":
        bill = 20
    else:
        bill = 25

    if add_pepperoni == "Y":
        if size == "S":
            bill += 2
        else:
            bill += 3

    if extra_cheese == "Y":
        bill += 1

    print(f"Your final bill is: ${bill}")


def love_calculator():
    # 🚨 Don't change the code below 👇
    print("Welcome to the Love Calculator!")
    name1 = input("What is your name? \n")
    name2 = input("What is their name? \n")
    # 🚨 Don't change the code above 👆

    # Write your code below this line 👇
    names = name1.lower() + name2.lower()

    true_count, love_count = 0, 0
    for i in "true":
        true_count += names.count(i)
    for j in "love":
        love_count += names.count(j)

    love_score = int(str(true_count) + str(love_count))

    if love_score > 90 or love_score < 10:
        print(f"Your score is **{love_score}**, you go together like coke and mentos.")
    elif 40 < love_score < 50:
        print(f"Your score is **{love_score}**, you are alright together.")
    else:
        print(f"Your score is **{love_score}**")


def treasure_island():
    print(
        '''
    *******************************************************************************
              |                   |                  |                     |
     _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
              |                `"=._o`"=._      _`"=._                     |
     _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
              |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
     _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    '''
    )
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    left_or_right = input(
        "you are at the cross road. Where do you want to go? Type 'left' or 'right'\t"
    ).lower()
    if left_or_right == "left":
        swim_wait = input(
            "You came to a lake. There is an island in the middle of the lake. "
            "Type 'wait' to wait for a boat. Type 'swim' to swim across \t"
        ).lower()
        if swim_wait == "wait":
            door = input(
                "You arrived at the island unharmed. There is a house with 3 doors. one red, one yellow "
                "and one blue. Which color do you choose? \t"
            ).lower()
            if door == "red":
                print("You are burned by Fire. GAME OVER!")
            elif door == "blue":
                print("You are eaten by beast. GAME OVER!")
            elif door == "yellow":
                print("You Win!")
            else:
                print("GAME OVER!")
        else:
            print("You got attacked by trout. GAME OVER!")
    else:
        print("You fall into a hole. GAME OVER!")


if __name__ == "__main__":
    # odd_or_even()
    # bmi_calculator()
    # leap_year()
    # pizza_order()
    # love_calculator()
    treasure_island()
