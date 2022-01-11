#!/usr/bin/env python3
#introduction to strings.
#strings can be treated as lists because each character is 0 indexed.
fav_string_word = 'triumphant'
print(fav_string_word)

#can access individual letters using square brackets as we do in lists.
first_letter = fav_string_word[0]
print(first_letter)

#return a portion of a string/slice a string.
sliced = fav_string_word[:3]
print(sliced)

eng_alias = 'cyberman'
engineer_type = 'software engineer'
def return_alias(alias, eng):
    user_name = alias[:2] + eng[-9:-5]
    print(user_name)
return_alias(eng_alias, engineer_type)

    
#getting length of a string, & index of string characters.

string_val = 'linux systems engineering'

#using len(); function to find length of string.

length_of_string = len(string_val)
print(length_of_string)

#find the index of the last string character, return is within a string.

last_char = string_val[len(string_val) - 1]
print(f'the last indexed character of the string_val variable is {last_char}')  

#can slice the last several characters of s atring using len():
#function that finds the first four letters of the string
"""
find the first characters of a string 
using string[:string_length-n] where n is the 
amount of characters youd like to omit. 
"""
systems_alias = 'cyberman'
def find_alias(alias):
    alias_length = len(alias)
    alias_title = alias[:alias_length-3]
    print(alias_title)
find_alias(systems_alias)

"""
function that returns a concatenated string using
the first three letters of a fist name and a last name 
"""
def username_fun(first,last):
    first_len = len(first)
    last_len = len(last)
    user_name = first[:first_len-4] + last[:last_len-3]
    return(user_name)
abev_user_name = username_fun('aaron', 'bevans')
print(abev_user_name)




