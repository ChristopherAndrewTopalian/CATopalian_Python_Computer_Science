# py_logic_gate_function_004_nor.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

def gateNor(a, b):
    if (a == 0 and b == 0):
        return "Both False"
    else:
        return "Choose the correct combination of 0 and 1"

####

def displayIt(a, b):
    print(gateNor(a, b))

    windll.user32.MessageBoxW(0,
    gateNor(a, b), 'NOR Gate', 0)

####

displayIt(0, 0)

input('Press Enter to Exit')

####

# NOR GATE Truth Table
# A  B
# 0  0  =  1
# 0  1  =  0
# 1  0  =  0
# 1  1  =  0

# NOR 1000

# Activates Only if Both False

# else if numbers other than 0 or 1 are chosen,
# the else statement will be activated

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

