#!/usr/bin/env python3
# Little Cody is an interplanetary space boxer, 
# who is trying to win championship belts for various weight categories
# on other planets within the solar system.

# Write a space.py program that helps him keep track of his target weight by:
#1. Checks which number planet is equal to.
#2. It should then compute his weight on the destination planet.

#table of conversion
#1. Venus 0.91
#2. Mars 0.38
#3. Jupiter 2.34
#4. Saturn 1.06
#5. Uranus 0.92
#6. Neptune 1.19

planet = 3
weight = 210

if planet == 1:
 weight = weight * 0.91
elif planet == 2:
 weight = weight * 0.38
elif planet == 3:
 weight = weight * 2.34
elif planet == 4:
 weight = weight * 1.06
elif planet == 5:
 weight = weight * 0.92
elif planet == 6:
 weight = weight * 1.19 

print("Your weight on planet " + str(planet) + ": " + str(weight))

