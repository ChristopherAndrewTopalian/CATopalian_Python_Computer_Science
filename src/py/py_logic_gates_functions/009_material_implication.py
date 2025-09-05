# py_logic_gate_function_009_material_implication.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

def gateMi(a, b):
    if ((a == 0 and b == 0) or
        (a == 0 and b == 1) or
        (a == 1 and b == 1)):
        return "Both False or B True or Both True"
    else:
        return "Choose the correct combination of 0 and 1"

####

def displayIt(a, b):
    print(gateMi(a, b))

    windll.user32.MessageBoxW(0,
    gateMi(a, b), 'Mi Gate', 0)

####

displayIt(1, 1)

input('Press Enter to Exit')

####

# MATERIAL IMPLICATION GATE Truth Table
# A  B
# 0  0  =  1
# 0  1  =  1
# 1  0  =  0
# 1  1  =  1

# Mi 1101

# Activates Only if Both False
# or B True or Both True

# else if numbers other than 0 or 1 are chosen,
# the else statement will be activated

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

