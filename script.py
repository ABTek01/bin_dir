#!/usr/bin/env python3
#function that converts fahrenheit to celsius
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

#function now lives within a variable that will be returned
f100_in_celsius = f_to_c(100)

#function that converts celsius to fahrenheit
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

#function now lives within a variable that will be returned
c0_in_fahrenheit = c_to_f(0)

print(c0_in_fahrenheit)

#100f to c is 37.77777, rounded is 38
print(round(f100_in_celsius))