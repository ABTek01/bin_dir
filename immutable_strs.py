#!/usr/bin/env python3
"""
cannot change a string once it is created.
we create new strings when performing operations
on existing strings, which can be used create new strings,
"""

#change the first letter of a name using concatenation and slicing.
user_first_name = 'Baron'
new_first_letter = 'A'
edited_user_first_name = new_first_letter + user_first_name[1:]
print(f'user\'s first name is {edited_user_first_name}')

"""
escaping characters;
we need to use backslashes
to escape/add characters that have
special meanings in python, to not
end our newly created string or cause
the system to throw and error.
"""

string_sentence = 'I am a \"Linux Systems engineer\"'
print(string_sentence)

"""
iterating through strings
we can iterate through strings since strings
are essentailly lists.

we can iterate through strings using for and while 
loops.
"""

#a function that iterates over a string, using for_loop
engineer_type = 'linux systems engineer'
def eng_type_iterate(engineer_type):
    for letter in engineer_type:
        print(letter)
eng_type_iterate(engineer_type)

"""
write a function that will iterate through a 
string and find the character count of each character.
"""

def get_length(string):
    count = 0
    for i in string:
        count += 1
    return count
str_length = get_length('linux systems engineering')
print(str_length)


