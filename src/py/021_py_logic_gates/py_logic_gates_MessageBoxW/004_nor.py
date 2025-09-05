# py_logic_gate_004_nor.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

A = 0
B = 0

if (A == 0 and B == 0):
    print('Both False')

    windll.user32.MessageBoxW(0,
    'Both False', 'NOR Gate', 0)

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

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

