#!/usr/bin/env python3
#In this project, we’ll build a program that will take the weight of
#a package and determine the cheapest way to ship that package using Sal’s Shippers.

weight = 41.5
ground_cost = ''

#ground shipping
if weight <= 2:
  ground_cost = weight * 1.50  + 20
elif weight <= 6:
  ground_cost = weight * 3.00 +  20
elif weight <= 10:
  ground_cost = weight * 4.00 + 20
else:
  ground_cost = weight * 4.75 + 20

print('cost of ground shipping: $' + str(ground_cost))

cost_ground_premium = 125.00

print('flat rate for premium ground shipping: $' + str(cost_ground_premium))



#drone shipping
if weight <= 2:
  drone_cost = weight * 4.50
elif weight <= 6:
  drone_cost = weight * 9.00
elif weight <= 10:
  drone_cost = weight * 12.00
else:
  drone_cost = weight * 14.25

print('going rate for dronw shipping: $' + str(drone_cost))

