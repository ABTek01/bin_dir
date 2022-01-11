#!/usr/bin/env python3
#list comprehension
"""
Python list comprehensions provide a concise way 
for creating lists. It consists of brackets containing 
an expression followed by a for clause, 
then zero or more for or if clauses: 
[EXPRESSION for ITEM in LIST <if CONDITIONAL>].

The expressions can be anything - any kind of object 
can go into a list.

A list comprehension always returns a list.
"""
#problem; scaling up grades on an exam.
grades = [90, 87, 56, 72, 100, 49, 89]
scaled_grades = [grade + 10 for grade in grades]
print(scaled_grades)

#using if/else conditional statements and loops in list comprehension.
#problem;
values = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
values_managed = [
    num * 2 if num % 5 == 0 else num * 0 for num in values
]
print(values_managed)


#problem; used list comprehensions to convert numbers using exponents.
single_digits = list(range(0, 10))
squares = []
for digit in single_digits:
  squares.append(digit ** 2)
  print(digit)
print(squares)

cubes = [digit ** 3 for digit in single_digits]
print(cubes)

