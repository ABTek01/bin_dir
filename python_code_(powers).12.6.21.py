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





