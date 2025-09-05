# py_logic_gate_function_008_converse_non_implication.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

def gateCni(a, b):
    if (a == 0 and b == 1):
        return "B True"
    else:
        return "Choose the correct combination of 0 and 1"

####

def displayIt(a, b):
    print(gateCni(a, b))

    windll.user32.MessageBoxW(0,
    gateCni(a, b), 'CNi Gate', 0)

####

displayIt(0, 1)

input('Press Enter to Exit')

####

# CONVERSE NON IMPLICATION GATE Truth Table
# A  B
# 0  0  =  0
# 0  1  =  1
# 1  0  =  0
# 1  1  =  0

# CNi 0100

# Activates Only if B True

# else if numbers other than 0 or 1 are chosen,
# the else statement will be activated

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

