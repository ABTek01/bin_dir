#!/usr/bin/env python3
#list methods
"""
.count(); list method to count the number of occurrences
of an element in a list.

.insert(); list method to insert an element into a 
specific index of a list

.pop(); list method to remove and element form a 
specific index or from the end of a list.

range(); built-in python function to create a sequence of integers.

len(); built-in python function to get the length of a list.

.sort()/.sorted() - a method and built in function to sort a list.
"""

#list.insert(index, 'element')
language_list = [
    'python 3',
    'javaScript',
    'kotlin'
]

language_list.insert(1, 'bash')
language_list[1] = 'bash'
print(language_list)

#list.pop()
language_list.pop(2)
language_list.pop(2)

"""
language_list = [
'python 3',
'bash'
]
"""

#range()
my_range = range(5)
print(my_range)
range(0, 5)

#in order to use list object use; list()
print(list(my_range))
[0, 1, 2, 3, 4]

#using multiple input
range() 

#creates a list between 0 and 9, where the index
range(0, 10, 2); #counts by twos = [0, 2, 5, 6, 8] up until not including 10.

#a list with range(3, 10, 3) = [3, 6, 9]

#to find the number of items in a list use len()
new_list_len = [
    1, 2, 3, 4, 5
]

#prints out total number of elements within a list.
print(len(new_list_len)); 

long_range_list = range(0, 1000, 10)
len_of_long_range_list = len(long_range_list)
print(len_of_long_range_list)

