import random


def coin_toss():
    item = random.randint(0, 1)
    print(item)
    if item == 0:
        print("HEADS")
    else:
        print("TAILS")


def banker_roulette():
    # Split string method
    names_string = input("Give me everybody's names, separated by a comma. ")
    names = names_string.split(", ")
    # 🚨 Don't change the code above 👆

    # Write your code below this line 👇
    item = random.randint(0, len(names) - 1)
    print(f"{names[item]} is going to buy the meal today!")


def treasure_map():
    # 🚨 Don't change the code below 👇
    row1 = ["⬜️", "⬜️", "⬜️"]
    row2 = ["⬜️", "⬜️", "⬜️"]
    row3 = ["⬜️", "⬜️", "⬜️"]
    map = [row1, row2, row3]
    print(f"{row1}\n{row2}\n{row3}")
    position = input("Where do you want to put the treasure? ")
    # 🚨 Don't change the code above 👆

    # Write your code below this row 👇
    col = int(position[0]) - 1
    row = int(position[1]) - 1

    map[row][col] = 'X'
    # Write your code above this row 👆

    # 🚨 Don't change the code below 👇
    print(f"{row1}\n{row2}\n{row3}")


def rock_paper_scissors():
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
    rps = [rock, paper, scissors]
    user = input("What do you choose? Type 1 for Rock, 2 for Paper or 3 for Scissors. \t")
    print("\n")
    if int(user) > 3 or int(user) < 1:
        print("You chose an invalid number, You LOSE!!")
        return 
    print(rps[int(user) - 1])
    comp = random.randint(1, 3)
    print("Computer chose:")
    print(rps[comp - 1])
    if (
            user == '1' and comp == 2
            or user == '2' and comp == 3
            or user == '3' and comp == 1
    ):
        print("YOU LOSE!!")
    elif int(user) == comp:
        print("DRAW!!")
    else:
        print("YOU WIN!!")


if __name__ == '__main__':
    # coin_toss()
    # banker_roulette()
    # treasure_map()
    rock_paper_scissors()
