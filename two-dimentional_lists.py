#!/usr/bin/env python3
# 2-dimensional; lists can contain other lists.
double_dem_list = [['cyberman', 'python3'], ['programmer1','ruby'], ['alpha_hacker','bash']]

#accessing 2d lists.
primary_hacker = double_dem_list[0][1]
print(primary_hacker)

secondary_hacker = double_dem_list[1][1]
print(secondary_hacker)

tertiary_hacker = double_dem_list[2][1]
print(tertiary_hacker)


#accessing 2d list values using negative numbers.
primary_hacker = double_dem_list[-3][-1]
print(primary_hacker)

primary_hacker = double_dem_list[-3][0]
print(primary_hacker)

#modifying 2d list elements/values
print(double_dem_list)


#modifying 2d list elements/values using list methods; .append()
double_dem_list[1].remove('ruby')
print(double_dem_list)

#modifying 2d list elements/values using list methods; .append()
double_dem_list[0].append('bash scripting')
print(double_dem_list)

double_dem_list.append(['linux', ['systems administration','hacking', 'pen test']])
print(double_dem_list)

#modifying a list by adding elements/list items to the end using '+' operator.
new_systems_tools_list = double_dem_list + ['hack the fucking system!!']
print(new_systems_tools_list)
#modifying a list by removing the first duplicate element with .remove()







