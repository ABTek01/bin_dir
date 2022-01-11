#!/usr/bin/env python3
"""
convert greetings() function into function that records user
data and pass the function into programmer_type() function
as a parameter/argument to manage data.
"""


#application that determines what kind of programmer we are.

#function that captures and records user input.
def greetings():
    print('greetings, lets try to determine what kind of programmer your are...')
    print('please enter your favorite programming language here')

#check to see if language matches specific type of programmer type.
def programmer_type(language):

    #input() function allows user to enter data.
    language = input()
    type = ''
    if language == 'html' or language == 'css' or language == 'javascript':
        type = 'frontend engineer'
        print(f'you must be a {type}')
    elif language == 'java' or language == 'sql':
        engineer = 'engineer'
        type = f'backend {engineer}, or database {engineer}'
        print(f'you must be a {type}')
    elif language == 'python' or language == 'bash':
        type = 'automation engineer'
        print(f'you must be an {type}')
    elif language == 'shell scripting' or language == 'bash':
        type = 'systems administrator'
        print(f'you must be a {type} who automates regular system tasks')
    else:
        print(f'programmer type unidentified')

data = greetings()
#data contains a function and runs as an argument.
programmer_type(data)






    
    