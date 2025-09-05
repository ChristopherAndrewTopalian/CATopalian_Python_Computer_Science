# take_screenshot_name_image_png.py

from PIL import ImageGrab

# capture the screen
ourImage = ImageGrab.grab()

# ask user to name the image
nameOfImage = input('Name of Image: ')

# save screenshot
ourImage.save(nameOfImage + '.png')

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

