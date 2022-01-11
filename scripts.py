#!/usr/bin/env python3
#print() function/method used to log out code
#variables_use = underscores if they are 2 words <  or more.
#generic string concatenation is similar in js. 'string ' + 'value.'
#typecasting allows change of a datatype's type with type() function/method
#types; str(string), bool(boolean), int(integer), float(floating point number)
#arithmetic operators.
print('welcome to python 101') #way to output/run our code.
print('write code')
print('print code')

print('create hammer')
print('create nails')
print('use hammer on nails')

#python variables = ways to store data or some other functionality.
name = 'cyberman'
favorite_language = 'javaScript'
print('my alias is ' + name + ', my favorite programming language is ' + favorite_language)
#reassigning a variable with different data.
favorite_language = 'python'
print('yes my favorite language is a front end development langage, but I will learn ' + favorite_language)

#typecasting; changing the type of a value into another.
print(type(name))

firstnumber = 1
print(type(firstnumber))

firstfloat = 1.0
print(type(firstfloat))

boolean = True
print(type(boolean))#printing out boolean variable's type.

boolean = str(boolean)#setting boolean variable value to 'string'
print(type(boolean))#printing out boolean variable type 'string'.
print(boolean)

boolean = bool(boolean)#reverting boolean to a boolean.
print(type(boolean))#printing out boolean variable value type.
print(boolean)

int(firstfloat)#convert float to an integer.
print(firstfloat)

str(firstfloat)#convert integer to a string.
print(firstfloat)

#variables and datatypes exercise
item = 'computer software'
price = 99.99
print(item + ' is in our inventory, with a price of $' + str(price))

#setting price variable to an integer.
price = int(price)
print(type(price))
print(price)

#converting an integer variable to a string-float.
newnumber = 5
print('the new number is ' + str(float(newnumber)) + '.')

#arithmetic operators
print('#practicing basic arithmetic')

#iterating through a list/array of numbers.
languages = ['html','css','javaScript','jsx','python']
for language in languages:
	print('I use; ' + language + ' for programming and automation.')

newSkills = ['Front End Software Development', 'IT Support Specialist', 'Networking', 'Systems Administration']
for skill in newSkills:
	print('My skills are; ' + skill + ' as an IT professional.')

#why is python relevant to IT?
#easy to express data structures and algorithms, with easy syntax. 
#easy for scripting. available for download on a lot of os.

#loop that iterates and prints out 'string' a certain amount of times.
for i in range(1):
	print('It specialist; IT support, Networking, Sysadmin')


print('python; the general purpose scripting language')

#getting information from a user.
print( (((1 + 2) * 3)/4)**5 )

programmer_alias = 'cyberman'
print('my alias is; ' + programmer_alias)

#Data types; 
print(1 + 1)

#cannot add a number and a string unless we change its type(type casting).
print(type('a'))
print(type(2))
print(type(True))
print(type(3.9))

#calculate the average size of n file(s) sizes 
#then explicitly convert type so python can carry out an evaluation.
total = 2048 + 4347 + 97658 + 125 + 8
files = int(5)
average = total / files
print("The average size is:" + str(average))

#Implicit Conversion; is where the interpreter helps us out and automatically 
#converts one data type into another, without having to explicitly tell it to do so.

#Explicit Conversion; is where we manually convert from one 
#data type to another by calling the relevant function for the data type we want to convert to.

#functions
#define a function that prints out the number of seconds given the number of hours, minutes abd seconds.
def print_total_seconds(hours, minutes, seconds):
    	print(
			'given the amount of hours, minutes and seconds, there are a total of ' + str(int(hours + minutes + seconds)) + ' seconds.'
		)
print_total_seconds(3600, 120, 3)

#define a function that returns a string using named parameters.
def dept_message(first_name, department):
    print('Welcome ' + first_name + ' you are part of ' + department + '.')
dept_message('aaron', 'IT systems support')
dept_message('brad', 'frontend software engineering')

#return values 
#We use the 'return' keyword in a function, which tells the function to pass data back. 
#When we call the function, we can store the returned value in a variable. 
#define a function that calculates the area of different triangles (b*h)/2
def find_tri_area(base, height):
    	#return values live here.
    	return (base * height)/2
area_a = find_tri_area(10, 5)
area_b = find_tri_area(20, 10)
sum = area_a + area_b
print('The area of both triangles is:' + str(sum))

#principles of code reuse

#Use the get_seconds function to work out the amount of seconds in 2 hours and 30 minutes, 
#then add this number to the amount of seconds in 45 minutes and 15 seconds. Then print the result.
def get_seconds(hours, minutes, seconds):
      return 3600*hours + 60*minutes + seconds
#function takes a certain amount of parameters and arguments.
amount_a = get_seconds(2, 30, 0)
amount_b = get_seconds(0, 45, 15)
#variables containing two different function calls.
result = amount_a + amount_b
print(result)

#define a function that prints message but returns nothing.
def no_return_def(message):
    	print(message)
#read as a function call.
result = no_return_def('nothing returned...')
#return keyword is not used to nothing is returned.
print(result)
#None returned.
#None; a special data type in python used to indicate that things are empty or that they returned nothing.

#define a function that uses a return value.
def passback_my_data(fav_num):
    	return fav_num * 2
#stored function call within a variable to be return value later on.
my_fav_num_doubled = passback_my_data(12)
print(str(my_fav_num_doubled) + ' Kobe, The Black Mamba!!')


#principle of code reuse

#In this code, identify the repeated pattern and replace it with a function called month_days, 
#that receives the name of the month and the number of days in that month as parameters. 
#Adapt the rest of the code so that the result is the same. 
#Confirm your results by making a function call with the correct parameters for both months listed
june = 30
print('June has ' + str(june) + ' days.')
july = 31
print('July has ' + str(july) + ' days.')

#repeated lines of code are now reusable functions.
def month_days(month, days):
	print(str(month) + " has " + str(days) + " days.")
month_days('June', 30)
month_days('July', 31)

#practice quiz 
# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km
my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
round_trip = my_trip_km * 2

print("The round-trip in kilometers is " + str(round_trip))

#comparing things
a = 4
b = 5
#greater than operator
print(a > b)

#less than operator
print(a < b)

#equality operator
print(a == b)

#not equals operator
print(a != b)

#logical operators; used to evaluate to true or false logic, and help to write complex expressions.
#the 'and' operator needs both expressions to be true at the same time.

#'and'; true = both expressions needs to be true at the same time. 
print('Aaron' < 'Baron' and "Cameron" < "Fameron")
#python; alphebtical order increases number value e.g. A = 0, B = 1; A < B.
print('A' > 'B')
print('A' < 'B')



#'or'; expression will be true if either(one or the other) of the expressions are true, and
#false only when both expressions are false. 
a = 0
b = 1
c = 0
d = 1
print(a > b or c < d)
# true; because; one or the other expression is correct so the whole statement is TRUE.

#'not'; inverts(reverses) the value of the expressions that's in front of it.
print(not 'aaron' == 'aaron')
#false; because 'aaron' is 'aaron'

print(not 'aaron' == 'baron')
#true; because 'aaron' is not 'baron'

#branching with if statements.
#len(parameter/variable) checks for the lengths of a string.
def valid_username(username):
    if len(username) > 5:
    	print('username; ' + username + ' is valid. welcome; ' + username + '.') 
valid_username('cyberman')

def my_username(username):
    if username == 'cyberman':
    	print('username; ' + username)
my_username('cyberman')



#modulo %; The modulo operator is represented by the percentage sign and returns 
#the remainder of the integer division between two numbers. The integer division is an operation between integers 
#that yields two results which are both integers, the quotient and the remainder.
def greater_than_zero(number):
	if number > 0 and number % 2 == 1:
		print(str(number) + ' is greater than 0...')
	else:
		print(str(number) + ' is less than 0...')
greater_than_zero(5)

#we do not always need an else statement.
def is_even(number):
	if 5 % number == 0:
		print(str(number))
	else:
		print(str(False))
is_even(1)

def num_is_even(num):
    if 5 % num == 1:
    	print(str(True))
	return False
num_is_even(2)

number = 10
if number > 11: 
	print(0)
elif number != 10:
	print(1)
elif number >= 20 or number < 12:
	print(2)
else:
	print(3)


print('big' > 'small')
print(11 % 5)

def sum(x, y):
    		return(x+y)
print(sum(sum(1,2), sum(3,4)))

def check_math():
   print((10 >= 5*2) and (10 <= 5*2))
check_math()

#loops; while-loop & for-loop
#while loop runs as long as condition is true.

#break out of infinite while loops;
#1. think about what is needed for a loop to be successful.
#2. nest loop within body of if-state, or use a logic-op that both check that values are different than var that will cause infinite loop. 
#3. consider different values a var can take that helps make sure loop wont get stuck.
#5. use 'break' keyword;
#6. initialize vars
#7. make sure loop does not continue for ever.

def less_than_five(num):
	x = 0
	while x <= num:
		print('x = ' + str(x))
		x += 1
less_than_five(5)

def init(var):
    current = var
    while current > 0:
        current -= 1
        print(current)
    print('zero!!!')
init(25)

def print_prime_factors(number):
      # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor += 1
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT


def is_power_of_two(n):
# THIS QUESTION IS POORLY WRITTEN...
  # Check if the number can be divided by two without a remainder
  while n % 2 == 0:
    if n == 0:
      break;
    n = n / 2
  # If after dividing by two the number is 1, it's a power of two
  if n == 1:
    return True
  else:
    return False
  

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False

#Question 5
#The multiplication_table function prints the results of a number passed to it multiplied by 1 through 5. 
#An additional requirement is that the result is not to exceed 25, 
#which is done with the break statement. Fill in the blanks to complete the function to satisfy these conditions.

def multiplication_table(number):
    	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 5:
		result = multiplier * number
		# What is the additional condition to exit out of the loop?
		# if result is greater than 25 break/stop the loop.
		if result > 25:
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop 'multiplier', since we multiply number up until/including 5.
		multiplier += 1

multiplication_table(3) 
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5) 
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)	
# Should print: 8x1=8 8x2=16 8x3=24

#for-loops;
#for-loop; iterates over a sequence of values. 
#e.g. iterate over a sequence of numbers.
for variable in range(10):
    print(variable)
    
#1. in python, a range of numbers will start with the value 0 by default.
#2. the list of numbers generated will be one less than the given value.
#3. code in for-loop body will be executed on each value within range one at a time.
#4. can iterate through a sequence of any data types.

#Fill in the gaps of the sum_squares function, 
#so that it returns the sum of all the squares of numbers between 0 and x (not included). 
#Remember that you can use the range(x) function to generate a sequence of numbers from 0 to x (not included).
def square(n):
    return n * n

def sum_squares(x):
    sum = 0
    for n in range(x):
        #incrementing, summing through 'num.seq' and squaring every number within range(10)
        sum += square(n)
    return sum
print(sum_squares(10))

#when to use for-loops;
#when there is a sequence of elements to iterate.

#when to use while-loops;
#when you want to repeat an action until a condition changes.

def factorial(n):
    result = 1
    #iteration starts between 2, 4 - 1 = 3 + result = 4.
    for i in range(2, n + result):
        #result = 1, multiplies every number within that range.
        result *= i
    return result
print(factorial(4)) # should return 24
print(factorial(5)) # should return 120

#the range() function when passing one, two, or three parameters:


#One parameter will create a sequence, one-by-one, from zero to one less than the parameter.
#Two parameters will create a sequence, one-by-one, from the first parameter to one less than the second parameter.
#Three parameters will create a sequence starting with the first parameter and stopping before the second parameter, 
#...but this time increasing each step by the third parameter.

#nested for-loops within function that compares interpreted languages vs compiled.
language_types = [
    'javaScript',
    'python',
    'php',
    'c'
]
#nested for-loop used to iterate over a list of elements twice.
def compare_langs(langs):
    for interpreted in langs:
        for compiled in langs:
            if interpreted != compiled:
                print(interpreted + " vs " + compiled)
compare_langs(language_types)


# - Recursion; is the repeated application of the same procedure to a smaller problem.
# - Recursion lets us tackle complex problems by reducing the problem to a simpler one.#!/usr/bin/env python3
