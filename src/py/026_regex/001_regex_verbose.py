import re

# The re.VERBOSE flag lets us add spaces and comments to regex
word_pattern = re.compile(r"""
    \b      # Start at the boundary of a word
    \w+     # Match one or more alphanumeric characters (letters/numbers)
    \b      # End at the boundary of a word
""", re.VERBOSE)

text = "Hello world! This is a test."
words = word_pattern.findall(text)
print(words)

####

'''
['Hello', 'world', 'This', 'is', 'a', 'test']
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

