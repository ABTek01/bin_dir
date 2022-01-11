#!/usr/bin/env python3
#python lists are ordered lists of data that can store any data type.

my_empty_list = []

#built in functionality to create, manipulate, and even delete data.

#list method form; list_name.method(); some methods require input value
#data value goes in-between parenthesis of the method list_name.method(input_data).

# .append() method; allows new elements to be appended/added to the 
# end of a list.

numbers_list = [0, 1, 2, 3, 4, 5]
new_number = 3 + 3 
numbers_list.append(new_number)
print(numbers_list)

# growing a list with plus (+) operator; allows us to add
# elements to the end of a list without modifying the original list.

new_numbers_list = numbers_list + [7]
print(new_numbers_list)


# accessing List Elements; call the location of an element in a list its index.
# python lists are zero-indexed. e.g. starting at 0, rather than 1.


# 0 = 'aaron', 1 = 'angelica', 2 = 'avrie', 3 = 'amari'
names = ['aaron', 'angelica', 'avrie', 'amari']

#prints out 'aaron'
print(names[0])

first_list_name = names[0]
print(first_list_name)

# accessing list elements; negative index;
# we can select the last element on a list using -1, -2, -3 etc...

last_list_element = names[-1]
print(last_list_element)


#modifying list elements; replacing a list element.
animals = []


#shrinking a list; name_of_list.remove(data_value)
#shrinking a list with two identical elements within it will remove the first instance.

my_new_list = [1, 2, 1, 3, 4, 4, 5]
my_new_list.remove(1)

#first item in the list will be removed.
print(my_new_list)
