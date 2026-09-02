# date_if_day.py

import datetime

def get_year():
    return datetime.datetime.now().year

def get_month():
    return datetime.datetime.now().month

def get_day_of_month():
    return datetime.datetime.now().day

def main():
    year = get_year()
    month = get_month()
    day_of_month = get_day_of_month()

    # Open a file for writing
    with open("output.txt", "w") as file:
        # Print to the console
        print(f"Year: {year}")
        print(f"Month: {month}")
        print(f"Day of Month: {day_of_month}")

        # Print to the file
        file.write(f"Year: {year}\n")
        file.write(f"Month: {month}\n")
        file.write(f"Day of Month: {day_of_month}\n")

        # Check if it is the 30th day
        day_alarm = 30

        if (day_of_month == day_alarm):
            print("It is the 30")
            file.write("It is the 30\n")
        else:
            print("It is NOT the 30")
            file.write("It is NOT the 30\n")

if __name__ == "__main__":
    main()

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

