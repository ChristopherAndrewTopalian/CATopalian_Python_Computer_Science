# list_of_dictionaries_append_object_input.py

people = [
    {
        'nameFirst': 'Jane',
        'nameLast': 'Grace'
    },
    {
        'nameFirst': 'Melissa',
        'nameLast': 'Angelo'
    },
    {
        'nameFirst': 'Tabitha',
        'nameLast': 'Portman'
    }
]

def main():
    firstName = input('First Name: ')
    lastName = input('Last Name: ')

    newPerson = {
        'nameFirst': firstName,
        'nameLast': lastName
    }

    # add object to end of the list
    people.append(newPerson)

    listLength = len(people)

    print(listLength)

    print(people)

    with open("output.txt", "w") as file:
        print(f"First Name: {people[listLength-1]['nameFirst']}")

        print(f"Last Name: {people[listLength-1]['nameLast']}")

        ##

        file.write(f"First Name: {people[listLength-1]['nameFirst']}\n")

        file.write(f"Last Name: {people[listLength-1]['nameLast']}\n")

    ##

    with open("output.html", "w") as file:
        htmlString = f'''
        <html>
        <head>
        <title> Our Webpage </title>
        
        <style>

        body
        {{
            background-color: rgb(30, 30, 30);
            font-size: 20px;
            color: rgb(255, 255, 255);   
        }}

        </style>
        </head>
        <body>
        <div>First Name: {people[listLength-1]['nameFirst']} </div>
        <div>Last Name: {people[listLength-1]['nameLast']} </div>

        </body>
        </html>
        '''

        file.write(htmlString)
        
        #file.write("First Name: " + people[listLength-1]['nameFirst'] + "\n")

        #file.write("Last Name: " + people[listLength-1]['nameLast'] + "\n")

main()

input('Press Enter to Exit')

####

# add object to list at specified position
# people.insert(0, newPerson)

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

