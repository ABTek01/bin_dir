#!/usr/bin/env python3
"""
Create a function named twice_as_large() 
that has two parameters named num1 and num2.
Return True if num1 is more than double num2. Return False otherwise.
"""
def twice_as_large(num1, num2):
    if num1 > num2*2:
        return f'True: {num1} is greater than {num2*2}'
    else:
        return f'False: {num1} is not greater than {num2*2}'
print(twice_as_large(10, 5))
print(twice_as_large(11, 5))
