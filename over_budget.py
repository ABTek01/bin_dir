#!/usr/bin/env python3
"""
Create a function called over_budget that has five parameters named 
budget, food_bill, electricity_bill, internet_bill, and rent.

The function should return True if budget is less than the sum of the 
other four parameters — you’ve gone over budget! Return False otherwise.

If we have gone over budget, we will return True. Otherwise we return False.
"""
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    
    if budget < food_bill + electricity_bill + internet_bill + rent:
        return str(True) + ': You went over your budget'
    else:
        return str(False) + ': You did not go over your budget'

print(over_budget(100, 20, 30, 10, 40)) #budget = 100, spent 100
print(over_budget(80, 20, 30, 10, 30)) #budget = 80, spent 90
