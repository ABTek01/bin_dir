#!/usr/bin/env python3
#We’ve decided to pursue the dream of small-business ownership and open up a furniture store called Lovely Loveseats for Neat Suites on Fleet Street.
#We’re going to build a system to help speed up the process of creating receipts for your customers.
#We will be storing the names and prices of a furniture store’s catalog in variables.
#Process the total price and item list of customers, printing them to the output terminal.

lovely_loveseat_description = '''
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.'''
print(lovely_loveseat_description)

lovely_loveseat_price = 254.00
print(lovely_loveseat_price)

stylish_settee_description = '''
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
'''
print(stylish_settee_description)

stylish_settee_price = 180.50
print(stylish_settee_price)

luxurious_lamp_description = ''' Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.'''

luxurious_lamp_price = 52.15

sales_tax = .088

customer_one_total = 0

customer_one_itemization = ''

customer_one_total

customer_one_itemization += lovely_loveseat_description

customer_one_total += luxurious_lamp_price

customer_one_itemization +=  luxurious_lamp_description

customer_one_tax = customer_one_total * sales_tax

customer_one_total += customer_one_tax

print('Customer One Items:')
print(customer_one_itemization)
print('Customer One Total:')
print(round(float(customer_one_total)))

