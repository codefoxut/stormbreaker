def grade_student():
    """grading assignment.

    Notes:
        Scores 91 - 100: Grade = "Outstanding"
        Scores 81 - 90: Grade = "Exceeds Expectations"
        Scores 71 - 80: Grade = "Acceptable"
        Scores 70 or lower: Grade = "Fail"

    """
    student_scores = {
        "Harry": 81,
        "Ron": 78,
        "Hermione": 99,
        "Draco": 74,
        "Neville": 62,
    }
    # 🚨 Don't change the code above 👆

    # TODO-1: Create an empty dictionary called student_grades.
    student_grades = {}

    # TODO-2: Write your code below to add the grades to student_grades.👇
    for key, val in student_scores.items():
        if val > 90:
            g = "Outstanding"
        elif 90 >= val > 80:
            g = "Exceeds Expectations"
        elif 80 >= val > 70:
            g = "Acceptable"
        else:
            g = "Fail"
        student_grades[key] = g

    # 🚨 Don't change the code below 👇
    print(student_grades)


def update_travel_log():
    travel_log = [
        {
            "country": "France",
            "visits": 12,
            "cities": ["Paris", "Lille", "Dijon"]
        },
        {
            "country": "Germany",
            "visits": 5,
            "cities": ["Berlin", "Hamburg", "Stuttgart"]
        },
    ]
    # 🚨 Do NOT change the code above

    # TODO: Write the function that will allow new countries
    # to be added to the travel_log. 👇
    def add_new_country(country, visits, cities):
        item = {
             "country": country,
            "visits": visits,
            "cities": cities
        }
        travel_log.append(item)

    # 🚨 Do not change the code below
    add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
    print(travel_log)


if __name__ == "__main__":
    grade_student()
    update_travel_log()
