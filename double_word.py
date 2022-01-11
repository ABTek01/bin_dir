#!/usr/bin/env python3
# function that doubles a word by multiplying the word by two, and concats the words new total length at the
# end of the string.

def double_word(word):
 return word * 2 + str(len(word) * 2)
print(double_word('python'))
print(double_word('code'))
print(double_word('automation'))

