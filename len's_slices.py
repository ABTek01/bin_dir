#use your knowledge of Python lists to organize some of your sales data.

# Your code below:
toppings = [
  "pepperoni",
  "pineapple",
  "cheese",
  "sausage",
  "olives",
  "anchovies",
  "mushrooms"
]

prices = [
  2, 6, 1, 3, 2, 7, 2
]

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

num_pizzas = len(toppings)
print(num_pizzas)

#string interpelation.
print(f"We sell {num_pizzas} different kinds of pizza!")

pizza_and_prices = [
  [2, "pepperoni"],
  [6, "pineapple"],
  [1, "cheese"],
  [3, "sausage"],
  [2, "olives"],
  [7, "anchovies"],
  [2, "mushrooms"]
]
print(pizza_and_prices)

#sorting and printing pizza prices
pizza_and_prices.sort()
print(pizza_and_prices)

#cheepest pizza
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)

priciest_pizza = pizza_and_prices[-1]
print(f"the most expensive pizza is {priciest_pizza}")

pizza_and_prices.pop(-1)
print(pizza_and_prices)

#appending a new list to existing list
pizza_and_prices.append([2.5, "peppers"])
print(pizza_and_prices)

pizza_and_prices.sort()
print(pizza_and_prices)

#printing three cheapest pizza prices
three_cheapest = pizza_and_prices[:3]
print(f"The three cheapest pizzas prices and toppings are; {three_cheapest}")

























