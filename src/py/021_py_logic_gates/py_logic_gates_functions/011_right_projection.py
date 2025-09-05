# py_logic_gate_function_011_right_projection.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

def gateRp(a, b):
    if ((a == 0 and b == 1) or
        (a == 1 and b == 1)):
        return "B True or Both True"
    else:
        return "Choose the correct combination of 0 and 1"

####

def displayIt(a, b):
    print(gateRp(a, b))

    windll.user32.MessageBoxW(0,
    gateRp(a, b), 'RP Gate', 0)

####

displayIt(1, 1)

input('Press Enter to Exit')

####

# RIGHT PROJECTION GATE Truth Table
# A  B
# 0  0  =  0
# 0  1  =  1
# 1  0  =  0
# 1  1  =  1

# RP 0101

# Activates Only if B True
# or Both True

# else if numbers other than 0 or 1 are chosen,
# the else statement will be activated

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

