# split_without_punctuation.py

import re

text = "Hi, everyone! Python is very fun."
# Matches any sequence of alphanumeric characters

words = re.findall(r'\w+', text)

print(words)

'''
['Hi', 'everyone', 'Python', 'is', 'very', 'fun']
'''

'''
When our sentence has punctuation signs, but we only want the words, we use the Regular Expression re.findall(r'\w+', text)
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

