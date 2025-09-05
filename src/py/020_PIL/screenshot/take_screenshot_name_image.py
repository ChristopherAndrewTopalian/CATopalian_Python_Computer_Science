# take_screenshot_name_image.py

from PIL import ImageGrab

# capture the screen
ourImage = ImageGrab.grab()

# ask user to name the image
# with file type included
question = "Name of Image with Extension: "

nameOfImage = input(question)

# save screenshot
ourImage.save(nameOfImage)

####

'''
takes a screenshot of the entire screen
and asks the user to name the image
with the file extension type included
in the name. It then saves the image
with the name and type specified.

For example:
001.jpg
or
002.png
or
003.gif
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

