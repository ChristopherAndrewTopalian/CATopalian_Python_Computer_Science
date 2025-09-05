# or.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

def gateOr(a, b):
    if ((a == 1 and b == 0) or
        (a == 0 and b == 1) or
        (a == 1 and b == 1)):
        return "One or Both True"
    else:
        return "Choose the correct combination of 0 and 1"

####

def displayIt(a, b):
    print(gateOr(a, b))

    windll.user32.MessageBoxW(0,
    gateOr(a, b), 'OR Gate', 0)

####

displayIt(1, 1)

input('Press Enter to Exit')

####

# creates an OR gate

# OR GATE Truth Table
# A  B
# 0  0  =  0
# 0  1  =  1
# 1  0  =  1
# 1  1  =  1

# OR 0111

# Activates Only if One or Both True

# else if numbers other than 0 or 1 are chosen,
# the else statement will be activated

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

