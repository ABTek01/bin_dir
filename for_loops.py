#!/usr/bin/env python3

"""
In programming, this process of using an initialization, 
repetitions, and an ending condition is called a loop.
In a loop, we perform a process of iteration (repeating tasks).
"""
var = "all about loops"
print(var)

"""
for-loops; In a for loop, we will know in advance 
how many times the loop will need to iterate because we will be working on 
a collection with a predefined length.
"""
#for-loop
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers_list:
    print(number + 1)
    
"""
for-loops using range();
using the range() method
we can iterate a certain amount
of times regardless of what is
in the list.
"""
#added a 1 to each iteration counting every element.
#computer reads it as 0-indexed, starting from 0.
#essentially adding 1 to each temporary variable iteration within loop
#changing its string-value not indexed-value.
#arbitrary list of numbers/items
for i in range(16):
    print('using range in a loop ' + str(i + 1) + ' times.')


#fizzbuzz; indexed from 0 to 15 == 16 ints, how computer reads 
#range() items.
for i in range(16):
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)

#program that appends a list to another.

language_list0 = ['bash', 'c', 'c#', 'dart', 'es6', 'fortran', 'golang']
language_list1 = ['haskell', 'html', 'java', 'javaScript', 'kotlin', 'lucid', 'python', 'ruby', 'scala']

for student in language_list0:
    language_list1.append(student)
sorted_languages = sorted(language_list1)
print(sorted_languages)
sorted_languages.insert(1, 'css')
print(sorted_languages)

#using break keyword to break out of loop when condition/code block is met.
programming_types = ['front end', 'back end', 'sysadmin', 'pen testing', 'automation scripting']
for type in programming_types:
    if type == 'automation scripting':
        print(F"I want to learn python to become great at {type}")
        break

#loop control; continue
#when the loop encounters a continue statement it 
#immediately skips the current iteration and moves onto the next element in the list
#continue keyword is usually coupled with an if/elif/else conditional.
#problem; skip any age that is less than the legal drinking age, which is 21.
ages = [19, 20, 31, 22, 21, 29, 17, 36]
for age in ages:
    if age < 21:
        continue
    print(age)



    