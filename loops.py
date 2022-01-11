#!/usr/bin/env python3

"""
In programming, this process of using an initialization, 
repetitions, and an ending condition is called a loop.
In a loop, we perform a process of iteration (repeating tasks).
"""
var = "all about loops"
print(var)

"""
for-loops; In a for loop, we will know in advance 
how many times the loop will need to iterate because we will be working on 
a collection with a predefined length.
"""

#for-loop
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers_list:
    print(number + 1)

"""
for-loops using range();
using the range() method
we can iterate a certain amount
of times regardless of what is
in the list.
"""
#added a 1 to each iteration counting every element.
#computer reads it as 0-indexed, starting from 0.
#essentially adding 1 to each temporary variable iteration within loop
#changing its string-value not indexed-value.
#arbitrary list of numbers/items
for i in range(16):
    print('using range in a loop ' + str(i + 1) + ' times.')


#fizzbuzz; indexed from 0 to 15 == 16 ints, how computer reads 
#range() items.
for i in range(16):
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)

"""
go through the lists of data that have 
been collected in the past couple of weeks.
You will be calculating some important 
metrics that Carly can use to plan out the 
operation of the business for the rest of the month.
"""
