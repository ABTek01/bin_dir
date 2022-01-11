#!/usr/bin/env python3
"""
we can use negative numbers 
to access string indices
at the end of a string
"""
new_str = 'linux systems engineering'
new_str_len = len(new_str)
occupation_title = new_str[-11:]
print(occupation_title)
print(new_str_len)

system_os = new_str[:-20]
print(system_os)

