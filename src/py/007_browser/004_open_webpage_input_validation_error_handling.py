# open_webpage_input_validation_error_handling.py

import webbrowser

url = input("Enter URL to Open: ")

if url.startswith('http://') or url.startswith('https://'):
    try:
        webbrowser.open(url)
        print("Web page opened successfully.")
    except Exception as e:
        print("An error occurred:", e)
else:
    print("Enter a URL starting with 'http://' or 'https://'")

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

