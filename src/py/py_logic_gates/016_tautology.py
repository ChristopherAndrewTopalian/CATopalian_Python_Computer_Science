# py_logic_gate_016_tautology.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

A = 0
B = 0

if ((A == 0 or A == 1) or
    (B == 0 or B == 1)):
    print('A or B is 0 or 1')

    windll.user32.MessageBoxW(0,
    'A or B is 0 or 1', 'Tautology Gate', 0)

input('Press Enter to Exit')

####

# TAUTOLOGY GATE Truth Table
# A  B
# 0  0  =  1
# 0  1  =  1
# 1  0  =  1
# 1  1  =  1

# T 1111

# Activates if A is 0 or 1 or B is 0 or 1
# meaning, any combination of 0 and 1 activates it

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

