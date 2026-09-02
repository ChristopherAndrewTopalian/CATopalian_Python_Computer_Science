# Open the file once in 'a' (append) mode
with open('text001.txt', 'a') as file:
    print("Type your words (Type 'exit' to stop):")
    
    while True:
        words = input('> ')
        
        # Check if the user wants to stop
        if words.lower() == 'exit':
            print("Closing file...")
            break 
            
        # Write the word and a newline
        file.write(words + '\n')
        # file.flush() # Optional: forces the save to disk immediately

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

