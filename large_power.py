#!/usr/bin/env python3
"""
1.Define the function to accept two input parameters called base and exponent
2.Calculate the result of base to the power of exponent
3.Use an if statement to test if the result is greater than 5000. If it is then return True. Otherwise, return False
"""
def large_power(base, exponent):
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False
print(large_power(2, 13))
print(large_power(2, 12))



