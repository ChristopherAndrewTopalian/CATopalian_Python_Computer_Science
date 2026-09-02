# PYTHON CODE BOOK

---

## Section: 001_print

### `001_print.py`

```python
# print.py

print('Hi Everyone')

input('Press Enter to Exit')

'''
Hi Everyone
Press Enter to Exit
'''

# Dedicated to God the Father
# (c) Copyright 2000-2026 Christopher Andrew Topalian. All rights reserved.
# https://github.com/ChristopherAndrewTopalian
```

---

### `002_print_with_line_break.py`

```python
# print_with_line_break.py

print('Hi Everyone\nHappy Scripting')

input('Press Enter to Exit')

'''
Hi Everyone
Happy Scripting
Press Enter to Exit
'''

# Dedicated to God the Father
# (c) Copyright 2000-2026 Christopher Andrew Topalian. All rights reserved.
# https://github.com/ChristopherAndrewTopalian
```

---

### `003_print_with_multiple_line_breaks.py`

```python
# print_with_multiple_line_breaks.py

print('Hi Everyone\n\nHappy Scripting')

input('Press Enter to Exit')

'''
Hi Everyone

Happy Scripting
Press Enter to Exit
'''

# Dedicated to God the Father
# (c) Copyright 2000-2026 Christopher Andrew Topalian. All rights reserved.
# https://github.com/ChristopherAndrewTopalian
```

---

### `004_print_string_variable.py`

```python
# print_string_variable.py

numberOfPeople = 'Twenty'

print(numberOfPeople)

input('Press Enter to Exit')

####

'''
Twenty
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `005_print_integer_variable.py`

```python
# print_integer_variable.py

numberOfPeople = 20

print(numberOfPeople)

input('Press Enter to Exit')

####

'''
20
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `006_print_float_variable.py`

```python
# print_float_variable.py

numberOfPeople = 20.82

print(numberOfPeople)

input('Press Enter to Exit')

####

'''
20.82
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `007_print_dictionary_variable.py`

```python
# print_dictionary_variable.py

jane = {
    'name': 'Jane',
    'score': 98
}

print(jane)

input('Press Enter to Exit')

####

'''
{'name': 'Jane', 'score': 98}
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `008_print_list_of_dictionaries.py`

```python
# print_list_of_dictionaries.py

people = [
    {
        'name': 'Jane',
        'score': 95
    },
    {
        'name': 'Melissa',
        'score': 98
    },
    {
        'name': 'Tabitha',
        'score': 93
    }
]

####

print(people)

input('Press Enter to Exit')

####

'''
[{'name': 'Jane', 'score': 95}, {'name': 'Melissa', 'score': 98}, {'name': 
'Tabitha', 'score': 93}]
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `009_print_list.py`

```python
# print_list.py

people = [
    'Jane',
    'Tabitha',
    'Melissa'
]

####

print(people)

input('Press Enter to Exit')

####

'''
['Jane', 'Tabitha', 'Melissa']
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `010_repeat_print.py`

```python
# repeat_print.py

name = 'Jane'

def repeatPrint(whichMessage, whichAmount):
    for i in range(1, whichAmount + 1):
        print(whichMessage)

####

repeatPrint(name, 5)

input('Press Enter to Exit')

####

'''
Jane
Jane
Jane
Jane
Jane
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `011_print_separator.py`

```python
# print_separator.py

ourList = [ 1, 2, 3, 4, 5 ]

print(*ourList, sep="\n")

input("Press Enter to Exit")

####

'''
1
2
3
4
5
Press Enter to Exit
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `012_print_list_simple.py`

```python
# print_list.py

ourList = [1, 2, 3, 4, 5]

print(ourList)

input("Press Enter to Exit")

####

'''
[1, 2, 3, 4, 5]
Press Enter to Exit
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `013_text_multiline.py`

```python
# text_multiline.py

print('''hi
everyone''')

input("Press Enter to Exit")

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

## Section: 002_sleep

### `001_sleep_print.py`

```python
# sleep_print.py

import time

print('Count to 4')

time.sleep(4.0)

print('4 seconds passed')

input('Press Enter to Exit')

####

'''
Count to 4
4 seconds passed
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `002_sleep_print_if_else.py`

```python
# sleep_print_if_else.py

import time

print('Hi Friend')

time.sleep(3.0)

print('Is the sun shining?')

sunShining = input('y/n\n')

if (sunShining == 'y'):
    print('Nice that it is sunny out')
else:
    print('The sun will be there soon')

input('Press Enter to Exit')

####

'''
Hi Friend
Is the sun shining?
y/n

if y
Nice that it is sunny out

if n
The sun will be there soon
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `003_sleep_input_while.py`

```python
# sleep_input_while.py

import time

startCondition = input('Type 1 and press Enter\n')

while startCondition == '1':
    time.sleep(4.0)
    print('4 seconds passed')

input('Press Enter to Exit')

####

'''
Type 1 and press Enter
1
4 seconds passed
4 seconds passed
4 seconds passed
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `004_sleep_while_not_loop.py`

```python
# sleep_while_not_loop.py

import time

loopCondition = 0

print('Count to 4')

while loopCondition != 1:
    time.sleep(4.0)
    print('4 seconds passed')

####

input('Press Enter to Exit')

####

'''
Count to 4
4 seconds passed
4 seconds passed
4 seconds passed
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

## Section: 003_for

### `001_for_in_loop.py`

```python
# for_in_loop.py

ourNumbers = [
    4, 875, 23, 543, 12
]

for z in ourNumbers:
    print(z)

input('Press Enter to Exit')

####

'''
4
875
23 
543
12 
Press Enter to Exit

'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `002_for_in_range.py`

```python
# for_in_range.py

for z in range(5):
    print(z)

input('Press Enter to Exit')

####

'''
0
1
2
3
4
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `003_for_append_letters.py`

```python
# for_append_letters.py

name = 'Tabitha'

ourList = []

for z in name:
    ourList.append(z)

print(ourList)

input('Press Enter to Exit')

####

'''
['T', 'a', 'b', 'i', 't', 'h', 'a']
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `004_for_in_range_len.py`

```python
# for_in_range_len.py

ourNumbers = [
    4, 875, 23, 543, 12
]

for z in range(len(ourNumbers)):
    print(ourNumbers[z])

input('Press Enter to Exit')

####

'''
4
875
23 
543
12 
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `005_for_in_range_start_stop_step_reverse.py`

```python
# for_in_range_start_stop_step_reverse.py

# start, stop, step
for z in range(10, 0, -1):
    print(z)

input('Press Enter to Exit')

####

'''
10
9
8
7
6
5
4
3
2
1
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `006_for_in_range_start_stop_step.py`

```python
# for_in_range_start_stop_step.py

# start, stop, step
for z in range(1, 11, 2):
    print(z)

input('Press Enter to Exit')

####

'''
1
3
5
7
9
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `007_for_in_range_start_stop.py`

```python
# for_in_range_start_stop.py

# start, stop
for z in range(1, 11):
    print(z)

input('Press Enter to Exit')

####

'''
1
2
3
4
5
6
7
8
9
10
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `008_for_in_letters.py`

```python
# for_in_letters.py

name = 'Tabitha'

for z in name:
    print(z)

input('Press Enter to Exit')

####

'''
T
a
b
i
t
h
a
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `009_for_in_list_loop.py`

```python
# for_in_list_loop.py

names = ['Jane', 'Jennifer', 'Melissa', 'Tabitha']

for ourVariable in names:
    print(ourVariable)

input("Press Enter to Exit")

####

'''
Jane
Jennifer
Melissa
Tabitha
Press Enter to Exit
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `010_for_in_loop_2.py`

```python
# for_in_loop.py

for ourVariable in "Howdy":
    print(ourVariable)

input("Press Enter to Exit")

####

'''
H
o
w
d
y
Press Enter to Exit
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `011_for_in_list_loop_reversed.py`

```python
# for_in_list_loop_reversed.py

names = ['Jane', 'Jennifer', 'Melissa', 'Tabitha']

for ourVariable in reversed(names):
    print(ourVariable)

input("Press Enter to Exit")

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `012_for_in_list_loop_variable_reversed.py`

```python
# for_in_list_loop_variable_reversed.py

names = ['Jane', 'Jennifer', 'Melissa', 'Tabitha']

names = reversed(names)

for ourVariable in names:
    print(ourVariable)

input("Press Enter to Exit")

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

## Section: 003_while_loop

### `001_while_True.py`

```python
# while_True.py

while True:
    print('hi')

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `002_while_loop_if.py`

```python
# while_loop_if.py

counter = 0

while True:
    if (counter < 3):
        print('Hi')
        counter += 1

####

'''
Hi
Hi
Hi
'''

# Dedicated to God the Father
# (c) Copyright 2000-2026 Christopher Andrew Topalian. All rights reserved.
# https://github.com/ChristopherAndrewTopalian
```

---

## Section: 004_list

### `list_length.py`

```python
# list_length.py

people = [
    'Jane',
    'Tabitha'
]

numberOfPeople = len(people)

print(f'{numberOfPeople} people')

input('Press Enter to Exit')

####

'''
2
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `list_show_chosen_entry.py`

```python
# list_show_chosen_entry.py

ourList = [0, 1, 2, 3, 4, 5]

ourChoice = int(input('Enter 0 to 5: \n'))

#print('We chose:', ourList[ourChoice])
print(f'We chose: {ourList[ourChoice]}')

input('Press Enter to Exit')

####

'''
Enter 0 to 5: 
4
We chose: 4
'''

####

# we can alternatively use:
# print(f'We chose: {ourList[ourChoice]}')

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `list_show_first_entry.py`

```python
# list_show_first_entry.py

ourList = [0, 1, 2, 3, 4, 5]

print(ourList[0])

input('Press Enter to Exit')

####

'''
0
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

## Section: 001_count

### `001_list_count.py`

```python
# list_count.py

people = ['Melissa']

print(len(people))

input('Press Enter to Exit')

####

'''
1
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `002_list_count.py`

```python
# list_count.py

people = ['Melissa', 'Jennifer', 'Tabitha', 'Jane']

print(len(people))

input('Press Enter to Exit')

####

'''
4
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `003_list_count_variable.py`

```python
# list_count_variable.py

people = ['Melissa']

peopleAmount = len(people)

print(peopleAmount)

input('Press Enter to Exit')

####

'''
1
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `004_list_count_if_else.py`

```python
# list_count_if_elif_else.py

people = ['Melissa', 'Jennifer', 'Tabitha', 'Jane']

peopleAmount = len(people)

if (peopleAmount == 5):
    print('There are four people')

else:
    print('There are ' + str(peopleAmount) + ' people')

input('Press Enter to Exit')

####

'''
There are 4 people
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `005_list_of_dictionaries_len.py`

```python
# list_of_dictionaries_len.py

people = [
    {
        'name': 'Jane',
        'score': 95
    },
    {
        'name': 'Melissa',
        'score': 98
    },
    {
        'name': 'Tabitha',
        'score': 93
    }
]

print(len(people))

input('Press Enter to Exit')

####

'''
3
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

## Section: 002_sort

### `001_sort_list.py`

```python
# sort_list.py

names = ['Melissa', 'Jennifer', 'Tabitha', 'Jane']

names.sort()

for z in names:
    print(z)

input('Press Enter to Exit')

####

'''
Jane
Jennifer
Melissa
Tabitha
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `002_reverse_list.py`

```python
# reverse_list.py

names = ['Jane', 'Jennifer', 'Melissa', 'Tabitha']

names.reverse()

for z in names:
    print(z)

input('Press Enter to Exit')

####

'''
Tabitha
Melissa 
Jennifer
Jane
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `003_sort_list_append.py`

```python
# sort_list_append.py

names = ['Melissa', 'Jennifer', 'Tabitha', 'Jane']

names.sort()

theNames = []

for z in names:
    theNames.append(z)

print(theNames)

input('Press Enter to Exit')

####

'''
['Jane', 'Jennifer', 'Melissa', 'Tabitha']
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `004_reverse_list_append.py`

```python
# reverse_list_append.py

names = ['Melissa', 'Jennifer', 'Tabitha', 'Jane']

names.reverse()

theNames = []

for z in names:
    theNames.append(z)

print(theNames)

input('Press Enter to Exit')

####

'''
['Jane', 'Tabitha', 'Jennifer', 'Melissa']
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

## Section: 003_add

### `001_list_of_dictionaries_append_last.py`

```python
# list_of_dictionaries_append_last.py

people = []

jane = {
    'name': 'Jane',
    'score': 98
}

people.append(jane)

print(people)

input('Press Enter to Exit')

####

'''
[{'name': 'Jane', 'score': 98}]
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `002_list_of_dictionaries_append_last.py`

```python
# list_of_dictionaries_append_last_len.py

people = [
    {
        'name': 'Jane',
        'score': 95
    },
    {
        'name': 'Melissa',
        'score': 98
    },
    {
        'name': 'Tabitha',
        'score': 93
    }
]

jennifer = {
    'name': 'Jennifer',
    'score': 93
}

people.append(jennifer)

print(len(people))

print(people)

input('Press Enter to Exit')

####

'''
4
[{'name': 'Jane', 'score': 95}, {'name': 'Melissa', 'score': 98}, {'name': 'Tabitha', 'score': 93}, {'name': 'Jennifer', 'score': 93}]
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `003_list_of_dictionaries_insert_first.py`

```python
# list_of_dictionaries_insert_first.py

people = [
    {
        'name': 'Jane',
        'score': 95
    },
    {
        'name': 'Melissa',
        'score': 98
    },
    {
        'name': 'Tabitha',
        'score': 93
    }
]

jennifer = {
    'name': 'Jennifer',
    'score': 93
}

people.insert(0, jennifer)

print(len(people))

print(people)

input('Press Enter to Exit')

####

'''
4
[{'name': 'Jennifer', 'score': 93}, {'name': 'Jane', 'score': 95}, {'name': 'Melissa', 'score': 98}, {'name': 'Tabitha', 'score': 93}]
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `004_list_of_dictionaries_insert_input_object.py`

```python
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
```

---

## Section: 004_remove

### `001_list_of_dictionaries_pop_last.py`

```python
# list_of_dictionaries_pop_last.py

people = [
    {
        'name': 'Jane',
        'score': 95
    },
    {
        'name': 'Melissa',
        'score': 98
    },
    {
        'name': 'Tabitha',
        'score': 93
    }
]

# remove last entry from list
people.pop()

print(len(people))

print(people)

input('Press Enter to Exit')

####

'''
2
[{'name': 'Jane', 'score': 95}, {'name': 'Melissa', 'score': 98}]
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `002_list_of_dictionaries_pop_first.py`

```python
# list_of_dictionaries_pop_first.py

people = [
    {
        'name': 'Jane',
        'score': 95
    },
    {
        'name': 'Melissa',
        'score': 98
    },
    {
        'name': 'Tabitha',
        'score': 93
    }
]

# remove first entry from list
people.pop(0)

print(len(people))

print(people)

input('Press Enter to Exit')

####

'''
2
[{'name': 'Melissa', 'score': 98}, {'name': 'Tabitha', 'score': 93}]
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `003_list_of_dictionaries_remove_by_name.py`

```python
# list_of_dictionaries_remove_by_name.py

people = [
    {
        'name': 'Jane',
        'score': 95
    },
    {
        'name': 'Melissa',
        'score': 98
    },
    {
        'name': 'Tabitha',
        'score': 93
    }
]

for z in people:
    if z['name'] == 'Melissa':
        people.remove(z)
        break

print(len(people))

print(people)

input('Press Enter to Exit')

####

'''
2
[{'name': 'Jane', 'score': 95}, {'name': 'Tabitha', 'score': 93}]
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

## Section: 005_find

### `001_find_item_in_list.py`

```python
# find_item_in_list.py

ourNumbers = [
    4, 875, 23, 543, 12
]

numberToFind = 875

if (numberToFind in ourNumbers):
    print(f'Yes, {numberToFind} is there')
else:
    print(f'No, {numberToFind} is NOT there')

input('Press Enter to Exit')

####

'''
Yes, 875 is there
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

## Section: 005_info

### `001_getcwd.py`

```python
# getcwd.py

import os

print(os.getcwd())

input('Press Enter to Exit')

####

'''
D:\_1Code\_2PY\_0PY_Published\Python_Computer_Science\Python_Computer_Science\CATopalian_Python_Computer_Science
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `002_getcwd_variable.py`

```python
# getcwd_variable.py

import os

theCwd = os.getcwd()

print(theCwd)

input('Press Enter to Exit')

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `003_getuser.py`

```python
# getuser.py

import getpass

print(getpass.getuser())

input('Press Enter to Exit')

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `004_get_os_name.py`

```python
# get_os_name.py

import platform

osName = platform.system()

print(osName)

input('Press Enter to Exit')

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `005_get_os_name_if_elif_else.py`

```python
# get_os_name_if_elif_else.py

import platform

osName = platform.system()

# if os is windows
if osName == "Windows":
    print('Windows detected')

# if os is Linux
elif osName == "Linux":
    print('Linux detected')

# else os not known
else:
    print('os not known')

input('Press Enter to Exit')

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `006_get_bytes.py`

```python
# get_bytes.py

import os

fileName = 'get_bytes.py'

print(os.stat(fileName).st_size + 'bytes')

input('Press Enter to Exit')

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `007_get_last_modified_time.py`

```python
# get_last_modified_time.py

import os
import datetime as dt

fileName = 'get_stats.py'

lastModifiedTime = os.stat(fileName).st_atime 

mtime = dt.datetime.fromtimestamp(lastModifiedTime)

print(mtime)

input('Press Enter to Exit')

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `008_get_stats.py`

```python
# get_stats.py

import os

name = '008_get_stats.py'

print(os.stat(name))

input('Press Enter to Exit')

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `009_list_dir.py`

```python
# list_dir.py

import os

print(os.listdir())

input('Press Enter to Exit')

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `010_what_type_is_variable.py`

```python
# what_type_is_variable.py

import os

x = "Hi Everyone"

print(type(x))

input('Press Enter to Exit')

####

'''
<class 'str'>
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

## Section: 006_string

### `001_count_letters_a.py`

```python
# count_letters.py

name = 'Jane'

print(len(name))

input('Press Enter to Exit')

####

'''
4
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
```

---

### `001_count_letters_b.py`

```python
# countLetters.py

def countLetters(whichWord):
    length = len(whichWord)
    return length

####

print(countLetters('Jane'))

input('Press Enter to Exit')

####

'''
4
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
```

---

### `002_count_letters_variable.py`

```python
# count_letters_variable.py

name = 'Jane'

letterCount = len(name)

print(letterCount)

input('Press Enter to Exit')

####

'''
4
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
```

---

### `002_input_username.py`

```python
# input_username.py

userName = input('Enter Username: ')

print('Username is: ' + userName)

input('Press Enter to Exit')

####

'''
Username is: Christopher
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
```

---

### `002_input_username_b.py`

```python
# input_username_b.py

def inputName():
    userName = input('Enter Username: ')
    return userName

####

if __name__ == "__main__":
    print('Username is: ' + inputName())

    input('Press Enter to Exit')

####

'''
Username is: Christopher
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
```

---

### `003_reverse_string.py`

```python
# reverse_string.py

word = "kingdom"

# slicing, start, stop, step
reversedWord = word[::-1]

print(reversedWord)

input('Press Enter to Exit')

####

'''
modgnik
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `004_username_if_else.py`

```python
# username_if_else.py

userName = input("Enter Username: ")

if (userName == 'Christopher'):
    print('Hi Christopher')
else:
    print(f'Hi {userName}. Tell Christopher to sign in.')

input('Press Enter to Exit')

####

'''
Enter Username: Christopher
Hi Christopher

if user doesn't type Christopher, but instead, Jane

Hi Jane. Tell Christopher to sign in.
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `005_split_words.py`

```python
# split_words.py

words = 'Tabitha Lee'

splitWords = words.split()

for z in splitWords:
    print(z)

input('Press Enter to Exit')

####

'''
Tabitha
Lee
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `006_slice_start_stop.py`

```python
# slice_start_stop.py

people = ['Melissa', 'Jennifer', 'Tabitha', 'Jane']

# start is 0, stop is 2
print(people[0:2])

input('Press Enter to Exit')

####

'''
       0                1
['Melissa', 'Jennifer']
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `007_slice_start_stop_step_reverse.py`

```python
# slice_start_stop_step_reverse.py

people = ['Melissa', 'Jennifer', 'Tabitha', 'Jane']

# start, stop, step
print(people[3:1:-1])

input('Press Enter to Exit')

####

'''
['Jane', 'Tabitha']
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

## Section: 007_browser

### `001_open_webpage_in_browser.py`

```python
# open_webpage_in_browser.py

import webbrowser

webbrowser.open('https://github.com/ChristopherTopalian')

####

'''
Opens Default Web Browser to a Web Page.
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `002_open_webpage_input.py`

```python
# open_webpage_input.py

import webbrowser

url = input("Enter URL to Open: ")

webbrowser.open(url)

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `003_open_webpage_input_validation.py`

```python
# open_webpage_input_validation.py

import webbrowser

url = input("Enter URL to Open: ")

if url.startswith('http://') or url.startswith('https://'):
    webbrowser.open(url)
else:
    print("Enter a URL starting with 'http://' or 'https://'")

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `004_open_webpage_input_validation_error_handling.py`

```python
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
```

---

## Section: 008_make_html_file

### `001_write_custom_HTML.py`

```python
# write_custom_HTML.py

ourHTMLContent = """
<html>
<head>
<title> Our HTML Page </title>

<style>

body
{
    padding: 10px;
    background-color: rgb(30, 30, 30);
    font-family: Arial;
    font-size: 20px;
    color: rgb(255, 255, 255);
}

</style>

</head>

<body>

<div> Hi Everyone </div>

</body>

</html>

"""

with open('ourNewWebpage.html', 'w') as theFile:
    theFile.write(ourHTMLContent)

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `002_write_custom_HTML_PY_Date.py`

```python
# write_custom_HTML_PY_Date.py

import datetime as dt

currentDate = dt.datetime.now().strftime('%Y-%m-%d')

ourHTMLContent = f"""
<html>
<head>
<title> Our HTML Page </title>

<style>

body {{
    padding: 10px;
    background-color: rgb(30, 30, 30);
    font-family: Arial;
    font-size: 20px;
    color: rgb(255, 255, 255);
}}

</style>

</head>

<body>

<div> Current Date: {currentDate} </div>

<div> Hi Everyone </div>

</body>

</html>

"""

with open('ourNewWebpage.html', 'w') as theFile:
    theFile.write(ourHTMLContent)

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

## Section: 009_folder

### `001_make_new_folder_specified_path.py`

```python
# make_new_folder_specified_path.py

import os

# rename OurUsername to your username
thePath = r"C:\Users\OurUsername\Desktop\ourFolder"

if not os.path.exists(thePath):
    try:
        os.mkdir(thePath)
    except OSError as theError:
        print(f"Creation of the directory {thePath} failed: {theError}")
    else:
        print(f"Successfully created the directory {thePath}")
else:
    print(f"The directory {thePath} already exists.")

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `002_make_new_folder_username_concatenation.py`

```python
# make_new_folder_username_concatenation.py

import os
import getpass

# get current username
username = getpass.getuser()

thePath = "C:\\Users\\" + username + "\\Desktop\\ourFolder"

if not os.path.exists(thePath):
    try:
        os.mkdir(thePath)
    except OSError as theError:
        print("Creation of the directory " + thePath + " failed: " + str(theError))
    else:
        print("Successfully created the directory " + thePath)
else:
    print("The directory " + thePath + " already exists.")

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `003_make_new_folder_format_string.py`

```python
# make_new_folder_format_string.py

import os
import getpass

username = getpass.getuser()

thePath = r"C:\Users\{}\Desktop\ourFolder".format(username)

if not os.path.exists(thePath):
    try:
        os.mkdir(thePath)
    except OSError as theError:
        print(f"Creation of the directory {thePath} failed: {theError}")
    else:
        print(f"Successfully created the directory {thePath}")
else:
    print(f"The directory {thePath} already exists.")

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

## Section: 010_utility

### `001_prompt.py`

```python
# input.py

def ask_name():
    name = input("Enter Name: ")
    print("Hi " + name)

####

ask_name()

input('Press Enter to Exit')

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `eval.py`

```python
# eval.py

z = '4 + 5'

answer = eval(z)

print(answer)

input('Press Enter to Exit')

####

'''
9
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `get_keyword_list.py`

```python
# get_keyword_list.py

import keyword

keywordList = keyword.kwlist

print(keywordList)

input('Press Enter to Exit')

####

'''
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 
'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

## Section: 011_calendar

### `calendar_by_year_month.py`

```python
# calendar_by_year_month.py

import calendar

theYear = int(input("Enter Year: "))
theMonth = int(input("Enter Month: "))

print(calendar.month(theYear, theMonth))

input('Press Enter to Exit')

####

'''
Shows a calendar for the specified year and month
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `calendar_of_current_year_month.py`

```python
# calendar_of_current_year_month.py

import calendar as cal
import datetime as dt

theYear = dt.date.today().year
theMonth = dt.date.today().month

print(cal.month(theYear, theMonth))

input('Press Enter to Exit')

####

'''
Shows a calendar for the
current year and month
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `calendar_specified_year_month.py`

```python
# calendar_specified_year_month.py

import calendar

# specify year and month
year = 2029
month = 4

# show the calendar for April 2029
print(calendar.month(year, month))

input('Press Enter to Exit')

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

## Section: 012_datetime

### `clock.py`

```python
# clock.py

import time
import datetime as dt

def makeUpdatingClock():
    while True:
        print(dt.datetime.now().strftime("%I:%M:%S %p"), end = "\r")

        time.sleep(1)

####

makeUpdatingClock()

####

'''
03:25:52
'''

####

# The \r makes the cursor return
# to the beginning of the line,
# so the time gets overwritten
# every second instead of
# printing a new line.

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `date_time_ctime_24.py`

```python
# date_time_ctime_24.py

import time

# get current time in seconds since epoch
theSeconds = time.time()

# format seconds into a readable date time
theDateTime = time.ctime(theSeconds)

print(theDateTime)

input('Press Enter to Exit')

####

'''
Fri Oct 18 03:40:29 2024
'''

####

# time.time() returns the number
# of seconds that have passed
# since the Unix epoch (January 1, 1970)

# time.ctime(theSeconds) converts
# seconds into a human readable string,
# with a 24 hour format

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `time_update.py`

```python
# time_update.py

import time
from datetime import datetime as dt

def show_clock():
    while True:
        current_time = dt.now().strftime("%H:%M:%S")
        print(f"\r{current_time}", end="", flush=True)
        #print(current_time)
        time.sleep(1)

show_clock()

####

# Dedicated to God the Father
# (c) Copyright 2000-2026 Christopher Andrew Topalian. All rights reserved.
# https://github.com/ChristopherAndrewTopalian
```

---

## Section: date_if_day

### `date_if_day.py`

```python
# date_if_day.py

import datetime

def get_year():
    return datetime.datetime.now().year

def get_month():
    return datetime.datetime.now().month

def get_day_of_month():
    return datetime.datetime.now().day

def main():
    year = get_year()
    month = get_month()
    day_of_month = get_day_of_month()

    # Open a file for writing
    with open("output.txt", "w") as file:
        # Print to the console
        print(f"Year: {year}")
        print(f"Month: {month}")
        print(f"Day of Month: {day_of_month}")

        # Print to the file
        file.write(f"Year: {year}\n")
        file.write(f"Month: {month}\n")
        file.write(f"Day of Month: {day_of_month}\n")

        # Check if it is the 30th day
        day_alarm = 30

        if (day_of_month == day_alarm):
            print("It is the 30")
            file.write("It is the 30\n")
        else:
            print("It is NOT the 30")
            file.write("It is NOT the 30\n")

if __name__ == "__main__":
    main()

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

## Section: 013_random

### `001_random_integer_0_to_10.py`

```python
# random_integer_0_to_10.py

import random

# integer from 1 to 10
randomInteger = random.randint(1, 10)

print(randomInteger)

input('Press Enter to Exit')

####

'''
7
'''

####

# Dedicated to God the Father
# (c) Copyright 2000-2026 Christopher Andrew Topalian. All rights reserved.
# https://github.com/ChristopherAndrewTopalian
```

---

### `002_random_float_1_to_10.py.py`

```python
# random_float_1_to_10.py

import random

# Generate a random float between 1 and 10
random_float = random.uniform(1, 10)
print(random_float)

####

# Dedicated to God the Father
# (c) Copyright 2000-2026 Christopher Andrew Topalian. All rights reserved.
# https://github.com/ChristopherAndrewTopalian
```

---

### `003_random_float_1_to_10_round.py`

```python
# random_float_1_to_10_round.py

import random

# Generate a random float and round it to 2 decimal places
rounded_float = round(random.uniform(1, 10), 2)

print(rounded_float)

####

# Dedicated to God the Father
# (c) Copyright 2000-2026 Christopher Andrew Topalian. All rights reserved.
# https://github.com/ChristopherAndrewTopalian
```

---

### `004_random_float_0_to_1.py`

```python
# random_float_0_to_1.py

import random

# float from 0.0 to 1.0
randomFloat = random.random()

print(randomFloat)

input('Press Enter to Exit')

####

'''
0.5109827327232547
'''

####

# Dedicated to God the Father
# (c) Copyright 2000-2026 Christopher Andrew Topalian. All rights reserved.
# https://github.com/ChristopherAndrewTopalian
```

---

### `random_10_choice.py`

```python
# random_10_choice.py

from random import choice

for i in range(10):
   print(choice(("one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten")))

input("Press Enter to Exit")

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `random_10_choice_variable.py`

```python
# random_10_choice_variable.py

from random import choice

for i in range(10):
   #print(choice(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]))

   theChoices = choice(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"])

   print(theChoices)

input("Press Enter to Exit")

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `random_choice.py`

```python
# random_choice.py

import random

languages = ["JavaScript", "Python", "C"]

print(random.choice(languages))

input('Press Enter to Exit')

'''
Class: random
Function: choice()
Syntax: random.choice(seq)
Parameters:
    seq: A sequence (list, tuple, string) from which a random element will be chosen.
Returns:
    A randomly selected element from the non-empty sequence.
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

## Section: 014_convert

### `convert_float_to_integer.py`

```python
# convert_float_to_integer.py

theNumber = 22.74

convertedNumber = int(theNumber)

print(convertedNumber)

input('Press Enter to Exit')

####

'''
22
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `round.py`

```python
# round.py

theNumber = 12.52

convertedNumber = round(theNumber)

print(convertedNumber)

input('Press Enter to Exit')

####

'''
13
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `round_down_floor.py`

```python
# round_down_floor.py

import math

theNumber = 12.52

convertedNumber = math.floor(theNumber)

print(convertedNumber)

input('Press Enter to Exit')

####

'''
12
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `round_up_ceil.py`

```python
# round_up_ceil.py

import math

theNumber = 12.52

convertedNumber = math.ceil(theNumber)

print(convertedNumber)

input('Press Enter to Exit')

####

'''
13
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

## Section: desktop_list_files

### `desktop_list_files.py`

```python
# desktop_list_files.py

import os
import getpass

# get current username
username = getpass.getuser()

thePath = "C:\\Users\\" + username + "\\Desktop"

print(thePath)

files = os.listdir(thePath)

print(files)

####

'''
for f in files:
    print(f)
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

## Section: desktop_path

### `desktop_path.py`

```python
# desktop_path.py

import os
import getpass

# get current username
username = getpass.getuser()

thePath = "C:\\Users\\" + username + "\\Desktop"

print(thePath)

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

## Section: 016_dir

### `current_working_directory.py`

```python
# current_working_directory.py

import os

nameOfFolder = os.getcwd()

print(nameOfFolder)

input("Press Enter to Exit")

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `get_file_path.py`

```python
# get_file_path.py

import pathlib

def getThisScriptFilePath():
    fileName = pathlib.Path(__file__).parent.resolve()

    return fileName

print(__file__)

input('Press Enter to Exit')

# returns for example:
# D:\_1Code\_2PY\_0\Topalian_Python_Date\py\path

# It does not include the file name itself, which in this case is getFilePath.py

# The special variable __file__ contains the path to the current file.
# From that we can get the directory using pathlib
# or we could alternatively use os.path module.

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
```

---

### `list_all_files_in_all_folders.py`

```python
# list_all_files_in_all_folders.py

import os

# get current working directory
currentFolder = os.getcwd()

# walk through all folders and subfolders
for dirpath, dirnames, filenames in os.walk(currentFolder):
    # check each file in current folder
    for file in filenames:
        print(file)

input('Press Enter to Exit')

####

'''
image_gallery.html
listdir.py
listdir_endswith.py
list_all_file_names_all_folders.py
list_image_file_names_all_folders_list.py
list_py_file_names_all_folders.py
list_py_file_names_all_folders_list.py
list_py_file_paths_all_folders.py
make_folder_if_not_already_made.py
notes.txt
001.jpg
002.jpg
008.jpg
008.png
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `list_all_files_paths_in_all_folders.py`

```python
# list_all_files_paths_in_all_folders.py

import os

# get current working directory
currentFolder = os.getcwd()

# walk through all folders and subfolders
for dirpath, dirnames, filenames in os.walk(currentFolder):
    # check each file in current folder
    for file in filenames:
        # print full path by joining directory path and file name
        fullPath = os.path.join(dirpath, file)
        print(fullPath)

####

input('Press Enter to Exit')

####

#D:\ourFolder\py\dir\image_gallery.html
#D:\ourFolder\py\dir\listdir.py
#D:\ourFolder\py\dir\listdir_endswith.py
#D:\ourFolder\py\dir\list_all_files_in_all_folders.py
#D:\ourFolder\py\dir\list_all_file_paths_in_all_folders.py
#D:\ourFolder\py\dir\list_image_file_names_all_folders_list.py
#D:\ourFolder\py\dir\list_py_file_names_all_folders.py
#D:\ourFolder\py\dir\list_py_file_names_all_folders_list.py
#D:\ourFolder\py\dir\list_py_file_paths_all_folders.py
#D:\ourFolder\py\dir\make_folder_if_not_already_made.py
#D:\ourFolder\py\dir\notes.txt
#D:\ourFolder\py\dir\New folder\001.jpg
#D:\ourFolder\py\dir\New folder\002.jpg
#D:\ourFolder\py\dir\New folder\008.jpg
#D:\ourFolder\py\dir\New folder\008.png

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `list_all_files_relative_paths_in_all_folders.py`

```python
# list_all_files_relative_paths_in_all_folders.py

import os

# get current working directory
currentFolder = os.getcwd()

# walk through all folders and subfolders
for dirpath, dirnames, filenames in os.walk(currentFolder):
    # check each file in current folder
    for file in filenames:
        # get full path
        fullPath = os.path.join(dirpath, file)
        
        # get relative path from currentFolder
        relativePath = os.path.relpath(fullPath, currentFolder)
        
        print(relativePath)

####

input('Press Enter to Exit')

####

# image_gallery.html
# listdir.py
# listdir_endswith.py
# list_all_files_in_all_folders.py
# list_all_files_relative_paths_in_all_folders.py
# list_all_file_paths_in_all_folders.py
# list_image_file_names_all_folders_list.py
# list_py_file_names_all_folders.py
# list_py_file_names_all_folders_list.py
# list_py_file_paths_all_folders.py
# make_folder_if_not_already_made.py
# notes.txt
# New folder\001.jpg
# New folder\002.jpg
# New folder\008.jpg
# New folder\008.png

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `list_image_file_names_all_folders_list.py`

```python
# list_image_file_names_all_folders_list.py

import os

currentFolder = os.getcwd()

imageFiles = []

for dirpath, dirnames, filenames in os.walk(currentFolder):
    for file in filenames:
        if file.endswith(('.jpg', '.png', '.jpeg', 'gif')):
            imageFiles.append(file)

####

print(imageFiles)

input('Press Enter to Exit')

####

'''
['001.jpg', '002.jpg', '007.jpg', '007.png', 'tree.gif']
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `list_py_file_names_all_folders.py`

```python
# list_py_file_names_all_folders.py

import os

# get current working directory
currentFolder = os.getcwd()

# walk through all folders and subfolders
for dirpath, dirnames, filenames in os.walk(currentFolder):
    # check each file in current folder
    for file in filenames:
        if file.endswith('.py'):
            print(file)

####

input('Press Enter to Exit')

####

'''
listdir.py
list_py_file_names_all_folders.py
listdir_endswith.py
test.py
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `list_py_file_names_all_folders_list.py`

```python
# list_py_file_names_all_folders_list.py

import os

currentFolder = os.getcwd()

pythonFiles = []

for dirpath, dirnames, filenames in os.walk(currentFolder):
    for file in filenames:
        if file.endswith('.py'):
            pythonFiles.append(file)

####

print(pythonFiles)

input('Press Enter to Exit')

####

'''
['listdir.py', 'listdir_endswith.py', 'list_py_file_names_all_folders.py', 'list_py_file_names_all_folders_list.py', 'list_py_file_paths_all_folders.py', 'test.py', 'notes.py']
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `list_py_file_paths_all_folders.py`

```python
# list_py_file_paths_all_folders.py

import os

currentFolder = os.getcwd()

for dirpath, dirnames, filenames in os.walk(currentFolder):
    for file in filenames:
        if file.endswith('.py'):
            print(os.path.join(dirpath, file))

####

input('Press Enter to Exit')

####

# D:\ourFolder\py\dir\listdir.py

#D:\ourFolder\py\dir\list_py_file_paths_all_folders.py

#D:\ourFolder\py\dir\listdir_endswith.py

#D:\ourFolder\py\dir\New folder\test.py

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `listdir.py`

```python
# listdir.py

import os

folderContents = os.listdir()

print(folderContents)

input('Press Enter to Exit')

####

'''
['output.txt', 'py', 'Python_Computer_Science.md']
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `listdir_endswith.py`

```python
# listdir_endswith.py

import os

folderContents = os.listdir('.')

for z in folderContents:
    if z.endswith('.py'):
        print(z)

####

input('Press Enter to Exit')

####

'''
listdir.py
listdir_endswith.py
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `make_folder_if_not_already_made.py`

```python
# make_folder_if_not_already_made.py

import os

folderName = "ourNewFolder"

# check if folder exists
if not os.path.exists(folderName):
    # create new folder
    os.makedirs(folderName)
    print(f"Folder '{folderName}' created.")
else:
    print(f"Folder '{folderName}' already exists.")

####

'''
Makes a new folder with a specified name if it doesn't already exist.
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `os_list_directory.py`

```python
# os_list_directory.py

import os

files = os.listdir('.')
print(files)

with open('check.txt', 'w') as ourFile:
    ourFile.write(str(files))

input("Press Enter to Exit")

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `os_path_dirname_listdir_realpath_print.py`

```python
# os_path_dirname_listdir_realpath_print.py

import os

path = os.path.dirname(os.path.realpath(__file__))

theData = os.listdir(path)

print(theData)

input('Press Enter to Exit')

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `os_path_dirname_listdir_realpath_write.py`

```python
# os_path_dirname_listdir_realpath_write.py

import os

path = os.path.dirname(os.path.realpath(__file__))

theData = os.listdir(path)

print(theData)

with open('theFiles.txt', 'w') as ourFile:
    ourFile.write(str(theData))

input('Press Enter to Exit')

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `pathlib_path_iterdir_append_fileNames.py`

```python
# pathlib_path_iterdir_append_fileNames.py

import pathlib

flist = [ ]

for thePath in pathlib.Path('.').iterdir():
    if thePath.is_file():
        print(thePath)
        flist.append(thePath)

input("Press Enter to Exit")

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

## Section: 017_startfile

### `startfile.py`

```python
# startfile.py

import os

os.startfile('testFile.odt')

####

'''
This opens the LibreOffice .odt file
named testFile.odt, that is located
in the same folder as this script.
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

## Section: 018_text

### `make_text_file_if_not_already_made.py`

```python
# make_text_file_if_not_already_made.py

import os

fileName = "ourNewFile.txt"

# check if file exists
if not os.path.exists(fileName):
    # create new file
    with open(fileName, 'w') as file:
        file.write("This is a new text file.\n")
    print(f"File '{fileName}' created.")
else:
    print(f"File '{fileName}' already exists.")

####

'''
Makes a new text file with a specified name if it doesn't already exist.
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

## Section: 019_math

### `abs.py`

```python
# abs.py

ourNumber = -5

print("Absolute value is ", abs(ourNumber))

input("Press Enter to Exit")

'''
Absolute value is  5
Press Enter to Exit
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `acos.py`

```python
# acos.py

import math

ourNumber = -1

print("Arc Cosine value is ", math.acos(ourNumber))

input("Press Enter to Exit")

'''
Arc Cosine value is  3.141592653589793
Press Enter to Exit
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `add.py`

```python
# add.py

def add_numbers(a, b):
    c = a + b
    return c

answer = str(add_numbers(8,8))

print(answer)

input("Press Enter to Exit")

'''
16
Press Enter to Exit
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `ceil.py`

```python
# math_ceil.js

import math

ourTitle = "Ceil App"

def ceil_to_string():
    ourText = math.ceil(4.25)
    answer = str(ourText)
    return answer

print(ceil_to_string())

input('Press Enter to Exit')

'''
5
Press Enter to Exit
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `division.py`

```python
# division.py

def ourFunction(a, b):
    c = a / b
    return c

answer = str(ourFunction(16,4))

print(answer)

input("Press Enter to Exit")

'''
4.0
Press Enter to Exit
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `exponent.py`

```python
# exponent.py

ourText = 8**2
ourTitle = "Power of App"

ourText = str(ourText)

print(ourText)

input("Press Enter to Exit")

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `floor.py`

```python
# floor.py

import ctypes
import math

ourTitle = "Floor App"

def ourFunction():
    ourText = math.floor(4.45)
    answer = str(ourText)
    return answer

print(ourFunction())

input("Press Enter to Exit")

'''
4
Press Enter to Exit
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `is_prime.py`

```python
# is_prime.py

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

####

if __name__ == "__main__":
    print(is_prime(5))

    input()

####

# True

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `multiplication.py`

```python
# multiplication.py

def ourFunction(a, b):
    c = a * b
    return c

answer = str(ourFunction(4,4))

print(answer)

input("Press Enter to Exit")

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `pi.py`

```python
# pi.py

import math

ourTitle = "Value of Pi"

def ourFunction():
    ourText = math.pi
    answer = str(ourText)
    return answer

print(ourFunction())

input("Press Enter to Exit")

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `pow.py`

```python
# pow.py

ourText = pow(8, 2)
ourTitle = "Power of App"

ourText = str(ourText)

print(ourText)

input("Press Enter to Exit")

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `round.py`

```python
# round.js

ourText = round(24.34, 1)
ourTitle = "Rounding App"

ourText = str(ourText)

print(ourText)

input("Press Enter to Exit")

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `sqrt.py`

```python
# sqrt.py

import math

ourText = math.sqrt(4)
ourTitle = "Square Root App"

ourText = str(ourText)

print(ourText)

input("Press Enter to Exit")

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `subtract.py`

```python
# subtract.py

def ourFunction(a, b):
    c = a - b
    return c

answer = str(ourFunction(30,20))

print(answer)

input("Press Enter to Exit")

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

## Section: screenshot

### `take_screenshot.py`

```python
# take_screenshot.py

# pip install Pillow

from PIL import ImageGrab

# capture the screen
ourImage = ImageGrab.grab()

# save screenshot as .png
ourImage.save('ourNewTexture.png')

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `take_screenshot_every_10s_autoname.py`

```python
# take_screenshot_every_10s_autoname.py

from PIL import ImageGrab
import time
from datetime import datetime

# start loop to take screenshot every 10 seconds
while True:
    # get current time for filename
    now = datetime.now()
    # e.g., 2025-06-09_13-45-12
    timestamp = now.strftime('%Y-%m-%d_%H-%M-%S')

    # capture the screen
    ourImage = ImageGrab.grab()

    # define filename
    filename = 'screenshot_' + timestamp + '.png'

    # save screenshot
    ourImage.save(filename)

    print('Saved:', filename)

    # wait 10 seconds
    time.sleep(10)

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `take_screenshot_every_10s_to_folder.py`

```python
# take_screenshot_every_10s_to_folder.py

from PIL import ImageGrab
import time
import os
from datetime import datetime

# define folder name
folderName = 'screenshots'

# create the folder if it doesn't exist
if not os.path.exists(folderName):
    # create the folder
    os.makedirs(folderName)
    print('Created folder: ' + folderName)

####

# start infinite screenshot loop
while True:
    # generate timestamp for filename
    now = datetime.now()
    timestamp = now.strftime('%Y-%m-%d_%H-%M-%S')

    # build full file path
    filename = folderName + '/screenshot_' + timestamp + '.png'

    # take screenshot
    ourImage = ImageGrab.grab()

    # save image
    ourImage.save(filename)

    print('Saved:', filename)

    # wait 10 seconds before next screenshot
    time.sleep(10)

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `take_screenshot_name_image.py`

```python
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
```

---

### `take_screenshot_name_image_png.py`

```python
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
```

---

## Section: py_logic_gates_MessageBoxW

### `001_and.py`

```python
# py_logic_gate_001_and.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

A = 1
B = 1

if (A == 1 and B == 1):
    print('Both True')

    windll.user32.MessageBoxW(0,
    'Both True', 'AND Gate', 0)

input('Press Enter to Exit')

####

# AND GATE Truth Table
# A  B
# 0  0  =  0
# 0  1  =  0
# 1  0  =  0
# 1  1  =  1

# AND 0001

# Activates Only if Both True

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `002_nand.py`

```python
# py_logic_gate_002_nand.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

A = 0
B = 0

if (A == 0 or B == 0):
    print('A True or B True or Both False')

    windll.user32.MessageBoxW(0,
    'A True or B True or Both False', 'NAND Gate', 0)

input('Press Enter to Exit')

####

# NAND GATE Truth Table
# A  B
# 0  0  =  1
# 0  1  =  1
# 1  0  =  1
# 1  1  =  0

# NAND 1110

# Activates Only if A True or B True,
# or Both False

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `003_or.py`

```python
# py_logic_gate_003_or.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

A = 1
B = 0

if (A == 1 or B == 1):
    print('One or Both True')

    windll.user32.MessageBoxW(0,
    'One or Both True', 'OR Gate', 0)

input('Press Enter to Exit')

####

# OR GATE Truth Table
# A  B
# 0  0  =  0
# 0  1  =  1
# 1  0  =  1
# 1  1  =  1

# OR 0111

# Activates Only if One or Both True

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `004_nor.py`

```python
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
```

---

### `005_xor.py`

```python
# py_logic_gate_005_xor.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

A = 1
B = 0

if ((A == 0 and B == 1) or
    (A == 1 and B == 0)):
    print('A True or B True')

    windll.user32.MessageBoxW(0,
    'A True or B True', 'XOR Gate', 0)

input('Press Enter to Exit')

####

# XOR GATE Truth Table
# A  B
# 0  0  =  0
# 0  1  =  1
# 1  0  =  1
# 1  1  =  0

# XOR 0110

# Activates Only if A True or B True

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `006_xnor.py`

```python
# py_logic_gate_006_xnor.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

A = 1
B = 1

if ((A == 0 and B == 0) or
    (A == 1 and B == 1)):
    print('Both True or Both False')

    windll.user32.MessageBoxW(0,
    'Both True or Both False', 'XNOR Gate', 0)

input('Press Enter to Exit')

####

# XNOR GATE Truth Table
# A  B
# 0  0  =  1
# 0  1  =  0
# 1  0  =  0
# 1  1  =  1

# XNOR 1001

# Activates Only if Both True
# or Both False

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `007_converse_implication.py`

```python
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
```

---

### `008_converse_non_implication.py`

```python
# py_logic_gate_008_converse_non_implication.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

A = 0
B = 1

if (A == 0 and B == 1):
    print('B True')

    windll.user32.MessageBoxW(0,
    'B True', 'CNi Gate', 0)

input('Press Enter to Exit')

####

# CONVERSE NON IMPLICATION GATE Truth Table
# A  B
# 0  0  =  0
# 0  1  =  1
# 1  0  =  0
# 1  1  =  0

# CNi 0100

# Activates Only if B True

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `009_material_implication.py`

```python
# py_logic_gate_009_material_implication.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

A = 0
B = 0

if (A == 0 or B == 1):
    print('Both True or Both False or B True')

    windll.user32.MessageBoxW(0,
    'Both True or Both False or B True', 'Mi Gate', 0)

input('Press Enter to Exit')

####

# MATERIAL IMPLICATION GATE Truth Table
# A  B
# 0  0  =  1
# 0  1  =  1
# 1  0  =  0
# 1  1  =  1

# Mi 1101

# Activates Only if Both True
# or Both False or B True

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `010_material_non_implication.py`

```python
# py_logic_gate_010_material_non_implication.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

A = 1
B = 0

if (A == 1 and B == 0):
    print('A True')

    windll.user32.MessageBoxW(0,
    'A True', 'MNi Gate', 0)

input('Press Enter to Exit')

####

# MATERIAL NON IMPLICATION GATE Truth Table
# A  B
# 0  0  =  0
# 0  1  =  0
# 1  0  =  1
# 1  1  =  0

# MNi 0010

# Activates Only if A True

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `011_right_projection.py`

```python
# py_logic_gate_011_right_projection.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

A = 1
B = 1

if (B == 1):
    print('Both True or B True')

    windll.user32.MessageBoxW(0,
    'Both True or B True', 'RP Gate', 0)

input('Press Enter to Exit')

####

# RIGHT PROJECTION GATE Truth Table
# A  B
# 0  0  =  0
# 0  1  =  1
# 1  0  =  0
# 1  1  =  1

# RP 0101

# Activates Only if Both True
# or B True

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `012_right_complementation.py`

```python
# py_logic_gate_012_right_complementation.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

A = 1
B = 0

if (B == 0):
    print('Both False or A True')

    windll.user32.MessageBoxW(0,
    'Both False or A True', 'RC Gate', 0)

input('Press Enter to Exit')

####

# RIGHT COMPLEMENTATION GATE Truth Table
# A  B
# 0  0  =  1
# 0  1  =  0
# 1  0  =  1
# 1  1  =  0

# RC 1010

# Activates Only if Both False
# or A True

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `013_left_projection.py`

```python
# py_logic_gate_013_left_projection.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

A = 1
B = 0

if (A == 1):
    print('Both True or A True')

    windll.user32.MessageBoxW(0,
    'Both True or A True', 'LP Gate', 0)

input('Press Enter to Exit')

####

# LEFT PROJECTION GATE Truth Table
# A  B
# 0  0  =  0
# 0  1  =  0
# 1  0  =  1
# 1  1  =  1

# LP 0011

# Activates Only if Both True
# or A True

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `014_left_complementation.py`

```python
# py_logic_gate_014_left_complementation.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

A = 0
B = 0

if (A == 0):
    print('Both False or B False')

    windll.user32.MessageBoxW(0,
    'Both False or B False', 'LC Gate', 0)

input('Press Enter to Exit')

####

# LEFT COMPLEMENTATION GATE Truth Table
# A  B
# 0  0  =  1
# 0  1  =  1
# 1  0  =  0
# 1  1  =  0

# LC 1100

# Activates Only if Both False
# or B True

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `015_contradiction.py`

```python
# py_logic_gate_015_contradiction.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

A = 0
B = 0

if ((A == 0 or A == 1) or
    (B == 0 or B == 1)):
    print("A or B is 0 or 1, Contradiction Gate Activated\nClosing App")

    windll.user32.MessageBoxW(0,
    'A or B is 0 or 1, Contradiction Gate Activated\nClosing App', 'Contradiction Gate', 0)

    quit()

input("Press Enter to Exit")

####

# CONTRADICTION GATE Truth Table
# A  B
# 0  0  =  0
# 0  1  =  0
# 1  0  =  0
# 1  1  =  0

# C 0000

# If A is 0 or 1 or B is 0 or 1
# meaning, any combination of 0 and 1
# activates the quit() function
# to represent the contradiction gate logically

# we could choose to not use the quit() function
# and instead just inform the person that
# the contradiction gate has been activated

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `016_tautology.py`

```python
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
```

---

## Section: py_logic_gates_console

### `001_and.py`

```python
# gate_and.py

def gate_and(a, b):
    if a == 1 and b == 1:
        return "Both True"
    else:
        return "Choose the correct combination of 0 and 1"

####

def get_input():
    try:
        a = int(input("Enter 1 or 0 for input A: "))
        b = int(input("Enter 1 or 0 for input B: "))
        return a, b
    except ValueError:
        print("Invalid input. Please enter 0 or 1.")
        return get_input()

####

def display_it(a, b):
    result = gate_and(a, b)
    print(result)

####

if __name__ == "__main__":
    a, b = get_input()
    display_it(a, b)

    input('Press Enter to Exit')

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

## Section: py_logic_gates_functions

### `001_and.py`

```python
# and.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

def gateAnd(a, b):
    if (a == 1 and b == 1):
        return "Both True"
    else:
        return "Choose the correct combination of 0 and 1"

def displayIt(a, b):
    print(gateAnd(a, b))

    windll.user32.MessageBoxW(0,
    gateAnd(a, b), 'AND Gate', 0)

####

displayIt(1, 1)

input('Press Enter to Exit')

####

# creates an AND gate

# AND GATE Truth Table
# A  B
# 0  0  =  0
# 0  1  =  0
# 1  0  =  0
# 1  1  =  1

# AND 0001

# Activates Only if Both True

# else if numbers other than 0 or 1 are chosen,
# the else statement will be activated

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `002_nand.py`

```python
# nand.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

def gateNand(a, b):
    if ((a == 0 and b == 0) or
        (a == 1 and b == 0) or
        (a == 0 and b == 1)):
        return "Both False or A True or B True"
    else:
        return "Choose the correct combination of 0 and 1"

def displayIt(a, b):
    print(gateNand(a, b))

    windll.user32.MessageBoxW(0,
    gateNand(a, b), 'NAND Gate', 0)

####

displayIt(0, 1)

input('Press Enter to Exit')

####

# creates a NAND gate

# NAND GATE Truth Table
# A  B
# 0  0  =  1
# 0  1  =  1
# 1  0  =  1
# 1  1  =  0

# NAND 1110

# Activates Only if Both False
# or A True or B True

# else if numbers other than 0 or 1 are chosen,
# the else statement will be activated

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `003_or.py`

```python
# or.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

def gateOr(a, b):
    if ((a == 1 and b == 0) or
        (a == 0 and b == 1) or
        (a == 1 and b == 1)):
        return "One or Both True"
    else:
        return "Choose the correct combination of 0 and 1"

####

def displayIt(a, b):
    print(gateOr(a, b))

    windll.user32.MessageBoxW(0,
    gateOr(a, b), 'OR Gate', 0)

####

displayIt(1, 1)

input('Press Enter to Exit')

####

# creates an OR gate

# OR GATE Truth Table
# A  B
# 0  0  =  0
# 0  1  =  1
# 1  0  =  1
# 1  1  =  1

# OR 0111

# Activates Only if One or Both True

# else if numbers other than 0 or 1 are chosen,
# the else statement will be activated

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `004_nor.py`

```python
# py_logic_gate_function_004_nor.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

def gateNor(a, b):
    if (a == 0 and b == 0):
        return "Both False"
    else:
        return "Choose the correct combination of 0 and 1"

####

def displayIt(a, b):
    print(gateNor(a, b))

    windll.user32.MessageBoxW(0,
    gateNor(a, b), 'NOR Gate', 0)

####

displayIt(0, 0)

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

# else if numbers other than 0 or 1 are chosen,
# the else statement will be activated

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `005_xor.py`

```python
# py_logic_gate_function_005_xor.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

def gateXor(a, b):
    if ((a == 1 and b == 0) or
        (a == 0 and b == 1)):
        return "A True or B True"
    else:
        return "Choose the correct combination of 0 and 1"

####

def displayIt(a, b):
    print(gateXor(a, b))

    windll.user32.MessageBoxW(0,
    gateXor(a, b), 'XOR Gate', 0)

####

displayIt(0, 1)

input('Press Enter to Exit')

####

# XOR GATE Truth Table
# A  B
# 0  0  =  0
# 0  1  =  1
# 1  0  =  1
# 1  1  =  0

# XOR 0110

# Activates Only if A True or B True

# else if numbers other than 0 or 1 are chosen,
# the else statement will be activated

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `006_xnor.py`

```python
# py_logic_gate_function_006_xnor.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

def gateXnor(a, b):
    if ((a == 0 and b == 0) or
        (a == 1 and b == 1)):
        return "Both False or Both True"
    else:
        return "Choose the correct combination of 0 and 1"

####

def displayIt(a, b):
    print(gateXnor(a, b))

    windll.user32.MessageBoxW(0,
    gateXnor(a, b), 'XNOR Gate', 0)

####

displayIt(0, 0)

input('Press Enter to Exit')

####

# XNOR GATE Truth Table
# A  B
# 0  0  =  1
# 0  1  =  0
# 1  0  =  0
# 1  1  =  1

# XNOR 1001

# Activates Only if Both False
# or Both True

# else if numbers other than 0 or 1 are chosen,
# the else statement will be activated

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `007_converse_implication.py`

```python
# py_logic_gate_function_007_converse_implication.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

def gateCi(a, b):
    if ((a == 0 and b == 0) or
        (a == 1 and b == 0) or
        (a == 1 and b == 1)):
        return "Both False or A True or Both True"
    else:
        return "Choose the correct combination of 0 and 1"

####

def displayIt(a, b):
    print(gateCi(a, b))

    windll.user32.MessageBoxW(0,
    gateCi(a, b), 'Ci Gate', 0)

####

displayIt(1, 1)

input('Press Enter to Exit')

####

# CONVERSE IMPLICATION GATE Truth Table
# A  B
# 0  0  =  1
# 0  1  =  0
# 1  0  =  1
# 1  1  =  1

# Ci 1011

# Activates Only if Both False
# or A True or Both True

# else if numbers other than 0 or 1 are chosen,
# the else statement will be activated

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `008_converse_non_implication.py`

```python
# py_logic_gate_function_008_converse_non_implication.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

def gateCni(a, b):
    if (a == 0 and b == 1):
        return "B True"
    else:
        return "Choose the correct combination of 0 and 1"

####

def displayIt(a, b):
    print(gateCni(a, b))

    windll.user32.MessageBoxW(0,
    gateCni(a, b), 'CNi Gate', 0)

####

displayIt(0, 1)

input('Press Enter to Exit')

####

# CONVERSE NON IMPLICATION GATE Truth Table
# A  B
# 0  0  =  0
# 0  1  =  1
# 1  0  =  0
# 1  1  =  0

# CNi 0100

# Activates Only if B True

# else if numbers other than 0 or 1 are chosen,
# the else statement will be activated

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `009_material_implication.py`

```python
# py_logic_gate_function_009_material_implication.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

def gateMi(a, b):
    if ((a == 0 and b == 0) or
        (a == 0 and b == 1) or
        (a == 1 and b == 1)):
        return "Both False or B True or Both True"
    else:
        return "Choose the correct combination of 0 and 1"

####

def displayIt(a, b):
    print(gateMi(a, b))

    windll.user32.MessageBoxW(0,
    gateMi(a, b), 'Mi Gate', 0)

####

displayIt(1, 1)

input('Press Enter to Exit')

####

# MATERIAL IMPLICATION GATE Truth Table
# A  B
# 0  0  =  1
# 0  1  =  1
# 1  0  =  0
# 1  1  =  1

# Mi 1101

# Activates Only if Both False
# or B True or Both True

# else if numbers other than 0 or 1 are chosen,
# the else statement will be activated

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `010_material_non_implication.py`

```python
# py_logic_gate_function_010_material_non_implication.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

def gateMni(a, b):
    if (a == 1 and b == 0):
        return "A True"
    else:
        return "Choose the correct combination of 0 and 1"

####

def displayIt(a, b):
    print(gateMni(a, b))

    windll.user32.MessageBoxW(0,
    gateMni(a, b), 'MNi Gate', 0)

####

displayIt(1, 0)

input('Press Enter to Exit')

####

# MATERIAL NON IMPLICATION GATE Truth Table
# A  B
# 0  0  =  0
# 0  1  =  0
# 1  0  =  1
# 1  1  =  0

# MNi 0010

# Activates Only if A True

# else if numbers other than 0 or 1 are chosen,
# the else statement will be activated

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `011_right_projection.py`

```python
# py_logic_gate_function_011_right_projection.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

def gateRp(a, b):
    if ((a == 0 and b == 1) or
        (a == 1 and b == 1)):
        return "B True or Both True"
    else:
        return "Choose the correct combination of 0 and 1"

####

def displayIt(a, b):
    print(gateRp(a, b))

    windll.user32.MessageBoxW(0,
    gateRp(a, b), 'RP Gate', 0)

####

displayIt(1, 1)

input('Press Enter to Exit')

####

# RIGHT PROJECTION GATE Truth Table
# A  B
# 0  0  =  0
# 0  1  =  1
# 1  0  =  0
# 1  1  =  1

# RP 0101

# Activates Only if B True
# or Both True

# else if numbers other than 0 or 1 are chosen,
# the else statement will be activated

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `012_right_complementation.py`

```python
# py_logic_gate_function_012_right_complementation.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

def gateRc(a, b):
    if ((a == 0 and b == 0) or
        (a == 1 and b == 0)):
        return "Both False or A True"
    else:
        return "Choose the correct combination of 0 and 1"

####

def displayIt(a, b):
    print(gateRc(a, b))

    windll.user32.MessageBoxW(0,
    gateRc(a, b), 'RC Gate', 0)

####

displayIt(1, 0)

input('Press Enter to Exit')

####

# RIGHT COMPLEMENTATION GATE Truth Table
# A  B
# 0  0  =  1
# 0  1  =  0
# 1  0  =  1
# 1  1  =  0

# RC 1010

# Activates Only if Both False
# or A True

# else if numbers other than 0 or 1 are chosen,
# the else statement will be activated

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `013_left_projection.py`

```python
# py_logic_gate_function_013_left_projection.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

def gateLp(a, b):
    if ((a == 1 and b == 0) or
        (a == 1 and b == 1)):
        return "A True or Both True"
    else:
        return "Choose the correct combination of 0 and 1"

####

def displayIt(a, b):
    print(gateLp(a, b))

    windll.user32.MessageBoxW(0,
    gateLp(a, b), 'LP Gate', 0)

####

displayIt(1, 1)

input('Press Enter to Exit')

####

# LEFT PROJECTION GATE Truth Table
# A  B
# 0  0  =  0
# 0  1  =  0
# 1  0  =  1
# 1  1  =  1

# LP 0011

# Activates Only if A True
# or Both True

# else if numbers other than 0 or 1 are chosen,
# the else statement will be activated

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `014_left_complementation.py`

```python
# py_logic_gate_function_014_left_complementation.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

def gateLc(a, b):
    if ((a == 0 and b == 0) or
        (a == 0 and b == 1)):
        return "Both False or B True"
    else:
        return "Choose the correct combination of 0 and 1"

####

def displayIt(a, b):
    print(gateLc(a, b))

    windll.user32.MessageBoxW(0,
    gateLc(a, b), 'LC Gate', 0)

####

displayIt(0, 1)

input('Press Enter to Exit')

####

# LEFT COMPLEMENTATION GATE Truth Table
# A  B
# 0  0  =  1
# 0  1  =  1
# 1  0  =  0
# 1  1  =  0

# LC 1100

# Activates Only if Both False
# or B True

# else if numbers other than 0 or 1 are chosen,
# the else statement will be activated

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `015_contradiction.py`

```python
# py_logic_gate_function_015_contradiction.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

def gateContradiction(a, b):
    if ((a == 0 and b == 0) or
        (a == 0 and b == 1) or
        (a == 1 and b == 0) or
        (a == 1 and b == 1)):
        return "One or Both False or True. Negative Message is placed here, or we can leave it blank"
    else:
        return "Choose the correct combination of 0 and 1"

####

def displayIt(a, b):
    print(gateContradiction(a, b))

    windll.user32.MessageBoxW(0,
    gateContradiction(a, b), 'CONTRADICTION Gate', 0)

####

displayIt(1, 1)

input('Press Enter to Exit')

####

# CONTRADICTION GATE Truth Table
# A  B
# 0  0  =  0
# 0  1  =  0
# 1  0  =  0
# 1  1  =  0

# C 0000

# Activates Only if One or Both False or True
# meaning, any combination of 0 and 1
# negative message is placed in the body of the if, or left blank

# else if numbers other than 0 or 1 are chosen,
# the else statement will be activated

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `016_tautology.py`

```python
# py_logic_gate_function_016_tautology.py
# creates a TAUTOLOGY gate

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

def gateTautology(a, b):
    if ((a == 0 and b == 0) or
        (a == 0 and b == 1) or
        (a == 1 and b == 0) or
        (a == 1 and b == 1)):
        return "One or Both False or True"
    else:
        return "Choose the correct combination of 0 and 1"

####

def displayIt(a, b):
    print(gateTautology(a, b))

    windll.user32.MessageBoxW(0,
    gateTautology(a, b), 'TAUTOLOGY Gate', 0)

####

displayIt(1, 1)

input('Press Enter to Exit')

####

# TAUTOLOGY GATE Truth Table
# A  B
# 0  0  =  1
# 0  1  =  1
# 1  0  =  1
# 1  1  =  1

# T 1111

# Activates Only if One or Both False or True
# meaning, any combination of 0 and 1 activates it

# else if numbers other than 0 or 1 are chosen,
# the else statement will be activated

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

## Section: py_logic_gates_pyside6

### `001_and.py`

```python
# and.py

import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox

def gate_and(a, b):
    if a == 1 and b == 1:
        return "Both True"
    else:
        return "Choose the correct combination of 0 and 1"

####

def display_it(label):
    result = gate_and(1, 1)  # simulate AND gate with (1, 1)
    label.setText(result)

    # show message box with the AND gate result
    QMessageBox.information(None, "AND Gate", result)

####

def start_app():
    # create the application
    app = QApplication(sys.argv)

    # create the main window
    window = QWidget()
    window.setWindowTitle("AND Gate")
    window.setGeometry(100, 100, 300, 200)

    # create layout and widgets
    layout = QVBoxLayout()
    
    label = QLabel("Press the button to see the AND gate result")
    layout.addWidget(label)

    button = QPushButton("Test AND Gate with (1, 1)")
    button.clicked.connect(lambda: display_it(label))
    layout.addWidget(button)

    # set layout to the window
    window.setLayout(layout)
    window.show()

    # execute the app
    sys.exit(app.exec())

####

if __name__ == "__main__":
    start_app()

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

## Section: 022_dictionary_of_dictionaries

### `001_dictionary_of_dictionaries.py`

```python
# dictionary_of_dictionaries.py

fleet = {
    "rover_01": {
        "type": "Scout",
        "speed": 15.5,
        "weapons": ["LiDAR", "Ultrasonic"],
    },
    "tank_01": {
        "type": "Heavy",
        "speed": 6.0,
        "weapons": ["120mm", "Smoke"],
    },
}

# INSTANT LOOKUP
print(fleet["rover_01"]["speed"])  # Output: 15.5

# DYNAMIC LOOKUP BY VARIABLE
active_id = "tank_01"
print(fleet[active_id]["type"])  # Output: Heavy

####

# Dedicated to God the Father
# (c) Copyright 2000-2026 Christopher Andrew Topalian. All rights reserved.
# https://github.com/ChristopherAndrewTopalian
```

---

### `002_dictionary_inputs.py`

```python
# dictionary_inputs.py

people = {}

person1 = input('Enter Name: ')

person2 = input('Enter Name: ')

people['team1'] = { 
    "seat1": person1, 
    "seat2": person2
}

print(people)

input('Press Enter to Exit')

####

# Dedicated to God the Father
# (c) Copyright 2000-2026 Christopher Andrew Topalian. All rights reserved.
# https://github.com/ChristopherAndrewTopalian
```

---

### `003_dictionary_of_dictionaries_lookup.py`

```python
# dictionary_of_dictionaries_lookup.py

fleet = {
    "rover_01": {
        "type": "Scout",
        "speed": 15.5,
        "weapons": ["LiDAR", "Ultrasonic"],
    },
    "tank_01": {
        "type": "Heavy",
        "speed": 6.0,
        "weapons": ["120mm", "Smoke"],
    },
}

# INSTANT LOOKUP
print(fleet["rover_01"]["speed"])  # Output: 15.5

# DYNAMIC LOOKUP BY VARIABLE
active_id = "tank_01"
print(fleet[active_id]["weapons"][1])  # Output: Heavy

####

# Dedicated to God the Father
# (c) Copyright 2000-2026 Christopher Andrew Topalian. All rights reserved.
# https://github.com/ChristopherAndrewTopalian
```

---

### `004_add_dictionary_to_dictionary.py`

```python
# add_dictionary_to_dictionary.py

world = {}

first_name = input("Enter First name: ")
last_name = input("Enter Last name: ")

name_dictionary = {
    "First name": first_name,
    "Last name": last_name
}

world[first_name] = name_dictionary

print(world)

####

'''
Enter First name: Christopher
Enter Last name: Topalian
{'Christopher': {'First name': 'Christopher', 'Last name': 'Topalian'}}
'''

'''
{
    'Christopher':
    {
        'First name': 'Christopher',
        'Last name': 'Topalian'
    }
}
'''

####

# Dedicated to God the Father
# (c) Copyright 2000-2026 Christopher Andrew Topalian. All rights reserved.
# https://github.com/ChristopherAndrewTopalian
```

---

### `005_dictionary_of_dictionaries_show_key.py`

```python
# dictionary_of_dictionaries_show_key.py

pokemon = {
    "pikachu":
    {
        "name": "Pikachu",
        "type": "Electric",
        "friend": "Ash"
    },

    "charazar":
    {
        "name": "Charazar",
        "type": "Fire",
        "friend": "Someone"
    }
}

print(pokemon["pikachu"])

'''
{'name': 'Pikachu', 'type': 'Electric', 'friend': 'Ash'}
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `006_dictionary_of_dictionaries_show_keys.py`

```python
# dictionary_of_dictionaries_show_keys.py

pokemon = {
    "pikachu":
    {
        "name": "Pikachu",
        "type": "Electric",
        "friend": "Ash"
    },

    "charizard":
    {
        "name": "Charizard",
        "type": "Fire",
    },

    "charmander":
    {
        "name": "Charmander",
        "type": "Fire",
    }
}

for key in pokemon:
    print(pokemon[key])

'''
{'name': 'Pikachu', 'type': 'Electric', 'friend': 'Ash'}
{'name': 'Charizard', 'type': 'Fire'}
{'name': 'Charmander', 'type': 'Fire'}
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `007_dictionary_of_dictionaries_sort_by_name.py.py`

```python
# dictionary_of_dictionaries_sort_by_name.py

pokemon = {
    "pikachu": {
        "name": "Pikachu",
        "type": "Electric",
        "friend": "Ash"
    },

    "charizard": {
        "name": "Charizard",
        "type": "Fire",
    },

    "charmander": {
        "name": "Charmander",
        "type": "Fire",
    }
}

# Sort by the inner 'name' key
sorted_pokemon = dict(sorted(
    pokemon.items(),
    key=lambda item: item[1]['name']
))

# Print the sorted dictionary
for key, data in sorted_pokemon.items():
    print(key, data)

'''
charizard {'name': 'Charizard', 'type': 'Fire'}
charmander {'name': 'Charmander', 'type': 'Fire'}
pikachu {'name': 'Pikachu', 'type': 'Electric', 'friend': 'Ash'}
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `008_dictionary_of_dictionaries_sort_by_key.py`

```python
# dictionary_of_dictionaries_sort_by_key.py

pokemon = {
    "pikachu": {
        "name": "Pikachu",
        "type": "Electric",
        "friend": "Ash"
    },

    "charizard": {
        "name": "Charizard",
        "type": "Fire",
    },

    "charmander": {
        "name": "Charmander",
        "type": "Fire",
    }
}

# Sort by the inner 'name' key
sorted_pokemon = dict(sorted(
    pokemon.items(),
    key=lambda item: item[1]['name']
))

print(sorted_pokemon)

'''
# Print the sorted dictionary
for key, data in sorted_pokemon.items():
    print(key, data)
'''

'''
{'charizard': {'name': 'Charizard', 'type': 'Fire'}, 'charmander': {'name': 'Charmander', 'type': 'Fire'}, 'pikachu': {'name': 'Pikachu', 'type': 'Electric', 'friend': 'Ash'}}
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

## Section: 023_class

### `001_class_show.py`

```python
# class_Pokemon.py

class Pokemon:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def showInfo(self):
        print("Name: " + self.name + "\n" + "Kind: " + self.kind)

    # This controls how the object looks when printed inside a dictionary or list
    def __repr__(self):
        return f"{self.name} ({self.kind} type)"

pikachu = Pokemon(
    "Pikachu",   #name
    "Electric"   #kind
)

ash_inventory = {}

# Add Pikachu using his name as the dictionary key
ash_inventory[pikachu.name] = pikachu

print("Ash's Inventory")
print(ash_inventory)

# You can now retrieve Pikachu out of the dictionary by name to call his methods
print("\nPulling from Inventory")
ash_inventory['Pikachu'].showInfo()

input("\nPress Enter to Exit")

'''
Name: Pikachu
Kind: Electric
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `002_class_pokemon_use_method.py`

```python
# class_pokemon_use_method.py

class Pokemon:
    def __init__(this, name, kind):
        this.name = name
        this.kind = kind

    def showInfo(this):
        print("Name: " + this.name + "\n" + "Kind: " + this.kind)

pikachu = Pokemon(
"Pikachu",   #name
"Electric"     #kind
)

pikachu.showInfo()

input("Press Enter to Exit")

'''
Name: Pikachu
Kind: Electric
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `find_path_of_class.py`

```python
# find_path_of_class.py

import inspect

print(inspect.getfile(inspect))
input('Press Enter to Exit')

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
```

---

### `find_path_of_class_and_open.py`

```python
# find_path_of_class_and_open.py

import datetime
import inspect
import os

# Get the file path of the datetime module
datetime_path = inspect.getfile(datetime)
print(f"Path of datetime module: {datetime_path}")

# Check if the path is a file and readable
if os.path.isfile(datetime_path):
    with open(datetime_path, 'r') as file:
        content = file.read()
        print("Content of the datetime module:")
        print(content)
else:
    print("The datetime module is a built-in module and does not have a .py file.")

input('Press Enter to Exit')

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
```

---

### `find_path_of_class_and_open_file.py`

```python
# find_path_of_class_and_open_file.py

import datetime
import inspect
import os
import subprocess
import platform

def open_module_in_editor(module):
    try:
        # Get the file path of the module
        module_path = inspect.getfile(module)
        print(f"Path of the module: {module_path}")

        # Check if the path is a file and readable
        if os.path.isfile(module_path):
            # Open the file in the default editor based on the operating system
            if platform.system() == 'Windows':
                os.startfile(module_path)
            elif platform.system() == 'Darwin':  # macOS
                subprocess.call(('open', module_path))
            else:  # Linux and other Unix-like systems
                subprocess.call(('xdg-open', module_path))
        else:
            print(f"{module.__name__} is a built-in module and does not have a .py file.")
    except TypeError:
        print(f"{module.__name__} is a built-in module and does not have a .py file.")

# Example usage
open_module_in_editor(datetime)

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
```

---

### `find_path_of_class_and_open_file_2.py`

```python
# find_path_of_class_and_open_file_2.py

import datetime
import inspect
import os
import subprocess
import platform

def open_module_in_editor(module):
    try:
        # Get the file path of the module
        module_path = inspect.getfile(module)
        print(f"Path of the module: {module_path}")

        # Check if the path is a file and readable
        if os.path.isfile(module_path):
            editor = "code"  # Replace with your preferred editor's command
            # Open the file in the specified editor based on the operating system
            if platform.system() == 'Windows':
                f = open(module_path, "r")
                print(f.read()) 
                #subprocess.call([editor, module_path])
            elif platform.system() == 'Darwin':  # macOS
                subprocess.call([editor, module_path])
            else:  # Linux and other Unix-like systems
                subprocess.call([editor, module_path])
        else:
            print(f"{module.__name__} is a built-in module and does not have a .py file.")
    except TypeError:
        print(f"{module.__name__} is a built-in module and does not have a .py file.")

# Example usage
open_module_in_editor(datetime)

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
```

---

## Section: 024_file

### `append_to_file.py`

```python
# append_to_file.py

with open("myscripts.txt", "a") as file:
    file.write("This line is being added to the end.\n")

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `append_to_file_input.py`

```python
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
```

---

### `append_to_file_input_ensure_write.py`

```python
import os

with open('text001.txt', 'a') as file:
    while True:
        words = input('Enter words (or "exit"): ')
        if words.lower() == 'exit': break
        
        file.write(words + '\n')
        
        # Force the data out of Python's buffer
        file.flush()
        # Force the OS to write to the physical disk
        os.fsync(file.fileno())

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `open_readline_for_correct.py`

```python
# open_readline_for_correct.py

import os

file_path = os.path.join('C:' + os.sep, 'Users', 'ourUserName', 'Desktop', 'testFile.txt')

with open(file_path, 'r') as theData:
    for line in theData:
        print(line, end='')

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `open_readline_for_correct_path.py`

```python
from pathlib import Path

file_path = Path('C:/') / 'Users' / 'ourUserName' / 'Desktop' / 'testFile.txt'

with open(file_path, 'r') as theData:
    for line in theData:
        print(line, end='')

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `open_readline_for_correct_path_getpass.py`

```python
# open_readline_for_correct_path_getpass.py

from pathlib import Path
import getpass

username = getpass.getuser()

file_path = Path('C:/') / 'Users' / username / 'Desktop' / 'testFile.txt'

with open(file_path, 'r') as theData:
    for line in theData:
        print(line, end='')

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `path.py`

```python
# path.py

import os

def get_file_path(file_name):
    # Get the absolute path of the file
    absolute_path = os.path.abspath(file_name)
    return absolute_path

# Example usage
file_name = 'example_file.py'

file_path = get_file_path(file_name)

print(f"The absolute path of the file is: {file_path}")

input('Press Enter to Exit')

"""
    Get the absolute path of a file.
    
    Parameters:
    file_name (str): The name or relative path of the file.
    
    Returns:
    str: The absolute path of the file.
"""

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

## Section: windows_only

### `os_startfile.py`

```python
# os_startfile.py

import os

os.startfile('C:/Users/ourUserName/Desktop/testFile.odt')

# This version only works on Windows.
# As we see, we are using a / forward slash.
# The / forward slash only works on Windows.
# To make a cross platform version,
# we must use os.path.join instead,
# alternatively we could use the Path library

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

## Section: wrong_ways

### `open_readline.py`

```python
# open_readline.py

theData = open('C:/Users/energy/Desktop/testFile.txt', 'r')

firstline = theData.readline()

secondline = theData.readline()

print(firstline)

print(secondline)

theData.close()

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `open_readline_for.py`

```python
# open_readline_for.py

theData = open('C:/Users/energy/Desktop/testFile.txt', 'r')

for line in theData:
    print (line, end = '')

theData.close()

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

## Section: 025_list_of_dictionaries

### `list_of_dictionaries_show_all.py`

```python
# list_of_dictionaries_show_all.py

people = [
    { 
        'firstName' : 'John', 
        'lastName' : 'Rambo', 
        'dob' : '3-1-1977', 
        'weight' : '170'
    },
    { 
        'firstName' : 'Jesse', 
        'lastName' : 'Tomson', 
        'dob' : '1-8-1978', 
        'weight' : '185'
    }
]

print(people)

input("Press Enter to Exit")

'''
[{'firstName': 'John', 'lastName': 'Rambo', 'dob': '3-1-1977', 'weight': '170'}, {'firstName': 'Jesse', 'lastName': 'Tomson', 'dob': '1-8-1978', 'weight': '185'}]
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `list_of_dictionaries_show_all_json.py`

```python
# list_of_dictionaries_show_all_json.py

import json

people = [
    { 
        'firstName' : 'John', 
        'lastName' : 'Rambo', 
        'dob' : '3-1-1977', 
        'weight' : '170'
    },
    { 
        'firstName' : 'Jesse', 
        'lastName' : 'Tomson', 
        'dob' : '1-8-1978', 
        'weight' : '185'
    }
]

print(json.dumps(people, indent=4))

input("Press Enter to Exit")

'''
[
    {
        "firstName": "John",
        "lastName": "Rambo",
        "dob": "3-1-1977",
        "weight": "170"
    },
    {
        "firstName": "Jesse",
        "lastName": "Tomson",
        "dob": "1-8-1978",
        "weight": "185"
    }
]
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `list_of_dictionaries_show_all_pprint.py`

```python
# list_of_dictionaries_show_all_pprint.py

from pprint import pprint

people = [
    { 
        'firstName' : 'John', 
        'lastName' : 'Rambo', 
        'dob' : '3-1-1977', 
        'weight' : '170'
    },
    { 
        'firstName' : 'Jesse', 
        'lastName' : 'Tomson', 
        'dob' : '1-8-1978', 
        'weight' : '185'
    }
]

pprint(people)

input("Press Enter to Exit")

'''
[{'dob': '3-1-1977', 'firstName': 'John', 'lastName': 'Rambo', 'weight': '170'},
 {'dob': '1-8-1978',
  'firstName': 'Jesse',
  'lastName': 'Tomson',
  'weight': '185'}]
'''

'''
Notice it alphabetized the keys within each dictionary (dob before firstName) — that's pprint's default sorting behavior, not something you controlled. If you want to preserve your original key order, add sort_dicts=False: pprint(people, sort_dicts=False).
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---

### `list_of_dictionaries_show_first_person.py`

```python
# list_of_dictionaries_show_first_person.py

people = [
    { 
        'firstName' : 'John', 
        'lastName' : 'Rambo', 
        'dob' : '3-1-1977', 
        'weight' : '170'
    },
    { 
        'firstName' : 'Jesse', 
        'lastName' : 'Tomson', 
        'dob' : '1-8-1978', 
        'weight' : '185'
    }
]

print (people[1])

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

---
