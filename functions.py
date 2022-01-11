#!/usr/bin/env python3

#python functions
#code written before a function call will run before the function is executed.
print('python functions are straight forward.')
def greeting_fun():
    print('hello, world! with python3!')

#un-indented code before function call.
print('un-indented code will run before the function runs, because it\'s written before the function execution.')

#python function calls only run after they are defined.
greeting_fun()

#function parameters and arguments
#parameters; variables/data the function can act upon and return data from.
#arguments; data that lives inside parameters that will be used by function code.

def systems_admin_skills(first_language, second_language, lang_use, title):
    print("my primary coding language is " + first_language + ".")
    print("my secondary coding language is " + second_language + ".")
    print('I use both ' + first_language + ' and ' + second_language + ' for ' + lang_use + ' as a ' + title + '.')
    print('\n')
print('--initialized--')
systems_admin_skills('python3', 'bash', 'systems automation', 'linux systems administrator')

print('\n')

#function that calculates the total cost of a trip.
def vacation_expenses():
    print('my next vacation, and expenses.')
vacation_expenses()
    
#TYPES OF ARGUMENTS
#default valued arguments.
#positional arguments; match the parameters in order.
#keyword arguments/can be out of order/assigned specific values.
print('\n')

#function; using various parameters and arguments for tasks at work.
#arguments/parameters;default parameters
def work_duties(task, os, work_location='intel laboratories'):
    print('daily task consists of ' + task)
    print('\n')
    for system in os:
        print('I work with a lot of ' + system + '.')
    print('our technologies are located within ' + work_location)
print('function defined')
work_duties('computer hardware', ['linux', 'windows'])

#built-in vs user-defined-functions
#built-in function; max()
def find_max_price(list_of_prices):
    max_price = max(list_of_prices)
    print('the max price within the list of prices is ' + str(max_price))
find_max_price([20.00, 45.73, 23.75, 110.50])

#keyword arguments/mix-match
def manage_tech(os, first_lang, second_lang='bash'):
    print(f'I use {second_lang} for systems automation')
    print(f'I use {first_lang} for web/software development within {os}')
manage_tech('macos', second_lang='python3', first_lang='javascript')
manage_tech('linux', 'python3')

#variable accessibility
universal_data = 'python3 globally accessible variable'

def defined_function_A():
    print('printing universal data')
    
def defined_function_B():
    print(f'this variable contains a {universal_data}')

defined_function_A()
defined_function_B()


#returned function value;
"""
When there is a result from 
a function that is stored in a variable
"""

#write a function that uses a returned function value.
#budgeting update application
current_budget = 5000
car_payment = 340.00
phone_bill = 160.00
rent = 1000

def monthly_bills(budget, expense_a, expense_b, expense_c):
    return budget - (expense_a + expense_b + expense_c)
budget_update = monthly_bills(current_budget, car_payment, phone_bill, rent)
print('\n')
print(f"your current budget is; ${str(budget_update)}.")

#calculate expenses based on hourly wage.


#return multiple values from a function
def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  #ordered variables
  return first, second, third

#considered actions outside of function.
#ordered variables set to function call returns function-data code block.
most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()

#printing out variables that all contain a function call.
#printing out return data in order.
print(most_popular1)
print(most_popular2)
print(most_popular3)




