#!/usr/bin/env python3
#write a function that will return a number to the tenth power.
#function takes in one parameter as a number and raises that number to the 10th power.
def tent_power(num):
    num_to_the_tenth = num ** 10
    print(num_to_the_tenth)
tent_power(10)

#write a function that returns the square root of a number.
def square_rt(num):
    sqr_rt = round(num ** 0.5)
    print(sqr_rt)
square_rt(14)

#write a function that returns the win percentage of all played games.
def win_percent(wins, losses):
    wins_per = wins / (wins + losses) * 100
    print(wins_per)
win_percent(5, 5)
win_percent(10, 0)

#write a function that takes in two numbers and returns the average of the two numbers.
def average(num1, num2):
    avrg= (num1 + num2) / 2
    print(avrg)
average(1, 100)
average(5, 190)

#write a function that will return the remainder of two numbers.
def remainder(num1, num2):
    print((num1 * 2) % (num2 / 2))
remainder(5, 25)

#advance operations
#write a function that will print the first 3 multiples of a number then return the 3rd multiple of a number.
def multiple(num):
    print(num)
    print(num * 2)
    print(num * 3)
    return num * 3
multiple(3)


#write a function that returns the total tip of a meal.
def tip(total, percentage):
    total_tip = (total * percentage) / 100
    print('the total tip is ' + str(int(total_tip)) + ' dollars.')
tip(50, 8)


#write a function that will return an introduction starting with a last name.
def introduction(first_name, last_name):
    print(last_name + ', ' + first_name + ' ' + last_name)
introduction('Aaron', 'Bevans')


#write a function that calculates a dogs age in dog years within a string.
def dog_years(name, age):
    dog_years = age * 7
    print(f'{name}, you are {dog_years} in dog years.')
dog_years('pitbull', 7)

#write a function that will perform multiple operations on a various inputs.
def all_operations(a, b, c, d):
    val_a = a + b
    val_b = c - d
    val_c = val_a * val_b
    val_d = val_c % a
    print(val_a)
    print(val_b)
    print(val_c)
    print(val_d)
all_operations(1, 2, 3, 4)
all_operations(1, 1, 1, 1)



    








