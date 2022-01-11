#!/usr/bin/env python3
#You are a student and you are trying to organize your subjects 
#and grades using Python.

last_semester_gradebook = [
 ["politics", 80], 
 ["latin", 96], 
 ["dance", 97], 
 ["architecture", 65]
]

# Your code below: 
subjects = [
  'physics',
  'calculus',
  'poetry',
  'history'
]

grades = [
  98,
  97,
  85,
  88
]

gradebook = [
  ['physics', 98],
  ['calculus', 97],
  ['poetry', 85],
  ['history', 88]
]
print(gradebook)

new_value = ['computer science', 100]

gradebook.append(new_value)
print(gradebook)


gradebook.append(['visual arts', 93])

print(gradebook)

#accessinf the last element in the list.
gradebook[-1][1] += 5
print(gradebook)

#removing an element from within a sublist of the two dimensional list.
gradebook[2].remove(85)
print(gradebook)

#adding an element within the two dimensional list.
gradebook[2].append('Pass')
print(gradebook)

full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)


