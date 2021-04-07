
def band_name_generator():
    # 1. Create a greeting for your program.
    print("Welcome to Band-name-generator!!!")

    # 2. Ask the user for the city that they grew up in.
    city = input("Which is the city where you grew up?\n")

    # 3. Ask the user for the name of a pet.
    pet = input("What is the name of your favourite pet?\n")

    # 4. Combine the name of their city and pet and show them their band name.
    print(f"The name of your band is {city} {pet}")

    # 5. Make sure the input cursor shows on a new line, see the example at:
    #   https://band-name-generator-end.appbrewery.repl.run/


def bmi_calculator():
    # 🚨 Don't change the code below 👇
    height = input("enter your height in m: ")
    weight = input("enter your weight in kg: ")
    # 🚨 Don't change the code above 👆

    # Write your code below this line 👇
    bmi = float(weight) / (float(height) ** 2)
    print(int(bmi))


def life_in_weeks():
    # 🚨 Don't change the code below 👇
    age = input("What is your current age(in years?\n")
    # 🚨 Don't change the code above 👆

    # Write your code below this line 👇
    total_age = 90
    current_age_int = int(float(age))
    remaining_years = total_age - current_age_int
    remaining_months = remaining_years * 12
    remaining_weeks = remaining_years * 52
    remaining_days = remaining_years * 365
    print(f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left.")


def tip_calculator():
    print("Welcome to Tip Calculator")
    bill_amount = input("What was your total bill?  \n")
    tip_percent = input("What percentage tip would you like to give? 10, 12 or 15? ")
    num_of_people = input("How many people slit the bill? \n")

    bill_amount_float = float(bill_amount)
    tip_percent_float = float(tip_percent)
    num_of_people = int(num_of_people)

    tip_amount = round(bill_amount_float * (100 + tip_percent_float) / (100 * num_of_people), 2)

    print(f"Each person should pay: ${tip_amount}")


if __name__ == '__main__':
    # band_name_generator()
    # bmi_calculator()
    # life_in_weeks()
    tip_calculator()
