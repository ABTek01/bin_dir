#!/usr/bin/env python3
#counting in a list; list.count(); counts the amount of
#occurrences of a list element there are.

letters_list = ['a', 'a', 'b', 'c', 'c', 'd']
doubles = letters_list.count('a', 'c')


#sort through a list using list.sort(), does not return a value.
#if we try to store it in a variable it will return None.

number_order = [0, 2, 3, 5, 6, 1, 3, 6, 6, 77, 890776, 1000000, 44, 21, 2345, 6]
number_order.sort()
print(number_order)

#.sort() in reverse
number_order.sort(reverse=True)
print(number_order)

#used sorted(); sorted(list) to sort out a list. 
#sorted() does not mutate a list.

