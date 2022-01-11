#!/usr/bin/env python3
"""
strings and conditionals pt.1
can iterate over strings to check for matching values.
"""
#write a function that checks for a matching str-char within a str input.

def check_for_match(word, letter):
    for i in word:
        if i == letter:
           print('linux systems')
        else:
           print('engineering')
check_for_match('engineering', 'e')

#write a function that checks for matching str-characters using 'in' keyword.

def letter_match(word, letter):
    if letter in word:
        print('confirmed')
    else:
        print('unidentified')
letter_match('linux systems engineering', 'i')

"""
strings and conditionals pt.2
can return boolean values when using 'in' keyword.
"""
"""
write a function that check if a string is within another string
but returns a list containing the exact letters.
"""

def common_letter(string_1, string_2):
    list = []
    #loop checks for every letter in first string
    for i in string_1:
    #condition checks if letters are within second string and not the empty list variable.
        if (i in string_1) and not (i in list):
   #condition is true, append each matching letter to empty list.
            list.append(i)
   #print the newly created list
    print(list)
common_letter('linux systems administrator', 'linux systems engineer')
