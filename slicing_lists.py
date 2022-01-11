#!/usr/bin/env python3
#slicing lists 1
#extracting a portion of a list
#[beginning_index:second_to_last_index]

numbers_list = [0, 1, 2, 3, 4, 5, 6]
middle_numbers = numbers_list[2:5]
print(middle_numbers)

#slicing lists 2
#using negative index values
first_two = numbers_list[:-5]
first_two = numbers_list[:2]
print(first_two)
#prints [0,1]

