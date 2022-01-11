#!/usr/bin/env python3
#function that checks to see if the first and last letters in a string match
#also checks for empty strings.

def first_and_last(string):
   if len(string) == 0:
        print(False)
   elif string[0] == string[-1]:
        print(True)
   else:
        print(False)
first_and_last('erie')

