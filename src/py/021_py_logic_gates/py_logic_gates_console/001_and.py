# gate_and.py

def gate_and(a, b):
    if a == 1 and b == 1:
        return "Both True"
    else:
        return "Choose the correct combination of 0 and 1"

####

def get_input():
    try:
        a = int(input("Enter 1 or 0 for input A: "))
        b = int(input("Enter 1 or 0 for input B: "))
        return a, b
    except ValueError:
        print("Invalid input. Please enter 0 or 1.")
        return get_input()

####

def display_it(a, b):
    result = gate_and(a, b)
    print(result)

####

if __name__ == "__main__":
    a, b = get_input()
    display_it(a, b)

    input('Press Enter to Exit')

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

