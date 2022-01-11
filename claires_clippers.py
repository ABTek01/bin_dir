#!/usr/bin/env python3

print("python test code")

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]
#variable used to know how many prices to iterate through.
total_prices = 0

#loop that iterates each price and calculates the total amount of the prices list.
for price in prices:
  total_prices += price

print(F"last week's total number of hair cut prices: {total_prices}")

"""
calculating the average price within the price list.
"""
average_price = total_prices/len(prices)
print(F"last week's average hairuct price {average_price}")

#discounting current prices by 5 dollars; using list comprehension.
new_prices = [price - 5 for price in prices]
print(F"new price list: {new_prices}")

#determine total revennue
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

print(F"last week's total revenue: ${total_revenue} dollars.")

average_daily_revenue = total_revenue/7
print(F"last week's average daily revenue: ${average_daily_revenue} ")

cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]

print(F"cuts under $30 dollars list: {cuts_under_30}")
