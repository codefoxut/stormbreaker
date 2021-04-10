def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                flag = True
            else:
                flag = False
        else:
            flag = True
    else:
        flag = False
    return flag


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap(year):
        days = 29
    else:
        days = month_days[month - 1]
    return days


def check_days_in_month():
    # 🚨 Do NOT change any of the code below
    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))
    days = days_in_month(year, month)
    print(days)


if __name__ == "__main__":
    check_days_in_month()
