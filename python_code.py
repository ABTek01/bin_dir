#!/usr/bin/env python3
#conditional statements and control flow
user_name = ''

if user_name == 'cyberman':
  print('username is the primary user: ' + user_name)
else:
  print('username unidentifiable')



#relational operators II

# > greater than

# >= greater then or equal to

# < less than

# <= less than or equal to

#exercise; check to see if student has enough credits to graduate.

credits = 160

if credits >= 160:
   print('you have enough credits to graduate')


#boolean operators/logical operators; and, or, not

# and; combines two boolean expressions and evaluates as True if both components are True, but False otherwise.
# oranges are a fruits and carrots are a vegetable. 

#exercise; check if a student has enough credits and if his gpa is above a 2.0

gpa = 3.4

if credits >= 120 and gpa >= 2.0:
   print('congrats graduate!!')  


# or; combines two expressions into a larger expressions that is True if either components is True.
#only one component needs to be True for an or statement to be True.
# oranges are a fruits or apples are a vegetable.

#exercise; check if student has more than enough credits or has a gpa of 2.0 or above.

credits = 120
gpa = 1.9

if credits >= 120 or gpa >= 2.0:
   print('you have met at least one of the requirements')

# not; when applied to any boolean expression it reverses the boolean value.
# So if we have a True statement and apply a not operator we get a False statement.
# Oranges a not a fruit.

statement_one = not (2 * 2 == 5 - 1)

statement_two = not (7 * 7 == 49 > 0)

credits = 120
gpa = 1.8

if not credits >= 120:
  print("You do not have enough credits to graduate.")

if not gpa >= 2.0:
  print("Your GPA is not high enough to graduate.")

if not credits >= 120 and not gpa >= 2.0:
  print("You do not meet either requirement to graduate!")


#else statements; This prevents us from needing to write if statements for each possible condition,
#we can instead write a blanket else statement for all the times the condition is not met.

gpa = 1.9

if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
else:
  print("You do not meet the requirements to graduate.")


#else if(elif);We can use elif statements to control the order we want our program to check each of our conditional statements.

grade = 86

if grade >= 90:
  print("A")
elif grade >= 80:
  print("B")
elif grade >= 70:
  print("C")
elif grade >= 60:
  print("D")
else:
  print("F")


#strings & accessing different parts of a string.
first_string = 'python'
print(first_string[0])

# checking to see if the first letter of a string matches the last & check for empty string.
def first_and_last(string):
  if len(string) == 0:
    return True
  elif string[0] == string[-1]:
   print(True)
  else:
   print(False)
first_and_last('eye')
first_and_last('')

#finding the range of characters in a string.
string = 'cyberman'
#prints the whole string
print(string[:8])
print(string[0:])

#prints a range of the a string.
print(string[0:5])

#creating a new string & using string methods
my_new_string = 'this is a new string'
print(my_new_string.index('a'))

print('this' in my_new_string)
print('z' in my_new_string)

# function that loops through list of strings and and capitalizes the first letter.#

# The string method .lower() will return the string with all characters changed to lowercase.
# The inverse of this is the .upper() method, which will return the string all in uppercase.
# The .strip() method is used to remove surrounding whitespace from a string. 
# The methods .lstrip() and .rstrip() to remove whitespace only from the left or the right side of the string, respectively.
# The method .count() can be used to return the number of times a substring appears in a string.
# To check if a string ends with a given substring, you can use the method .endswith().
# The .isnumeric() method can check if a string is composed of only numbers.
# We can also use the join method to concatenate strings.

def initials(phrase):
    words = phrase.split()
    result = ""
    #looping through indexed string elements, within a range of a string length.
    for i in range(len(words)):
        result += words[i][0].upper()
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS

# formatting strings; using 'format()' method to store variables within a string.
# format() pattern 1.
eng_name = 'cyberman'
fav_num = len(eng_name) * 3
print('greetings, {} your favorite number is {}'.format(eng_name, fav_num))

def format_string(name, grade):
  print('{} received {}% on the python coding exam.'.format(name, grade))
  #return '{} received {}% on the python coding exam.'.format(name, grade)
  #print(format_string('cyberman', 90))
format_string('cyberman', 90)



#format pattern 2.
price = 7.5
prince_with_tax = 7.5 * 1.08
#use of '${:.2f} formats float number and 2 decimals within a string.
print('base price: ${:.2f}, Base Price With Tax: ${:.2f}'.format(price, prince_with_tax))

#use of '{:>3}' aligns string data 3 spaces to the right. '{:>6.2f}' aligns string data 6 spaces to the right and formats 
#float number by two decimals.

#writing python functions
def add_two(num):
    return num + 2
result = add_two(10)
print(result)

