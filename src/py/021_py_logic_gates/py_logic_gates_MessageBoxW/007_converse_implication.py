# py_logic_gate_007_converse_implication.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

A = 0
B = 0

if (A == 1 or B == 0):
    print('Both True or Both False or A True')

    windll.user32.MessageBoxW(0,
    'Both True or Both False or A True', 'Ci Gate', 0)

input('Press Enter to Exit')

####

# CONVERSE IMPLICATION GATE Truth Table
# A  B
# 0  0  =  1
# 0  1  =  0
# 1  0  =  1
# 1  1  =  1

# Ci 1011

# Activates Only if Both True
# or Both False or A True

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

