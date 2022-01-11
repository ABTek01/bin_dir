#!/usr/bin/env python3
#ds that allows us to store multiple elements that is immutable

#tuple values cannot be changed
my_info = ('aaron', 30, 'python programmer')
print(my_info)

#unpacking tuples
name, age, occupation = my_info

#we can print out variables that contain tuple values
print(name)
print(age)
print(occupation)

#one element tuple
one_element_tuple = (1,)
print(one_element_tuple)

#situation to run tuples
#used to store data together that is not usually related

#use zip() method to convert lists into list of tuples.
#regula list

software_engineering = [
 'front-end web development',
 'mobile development',
 'back-end development',
 'systems administration'
]

#using zip() to convert list to a tuple-list.
manage_software_engineering = zip(software_engineering)
print(manage_software_engineering)

swe_list = list(manage_software_engineering)
print(swe_list)


