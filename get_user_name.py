#!/usr/bin/env python3
"""
function that creates a unique username
that concatenates first 3 letters of a user's first name
and the first 4 letters of the user's last name,
but if the first name is less than 3 letters
and the last name is less than 4 letters, full name
will be concatenated and returned
"""

def username_generator(first_name, last_name):
    first = first_name[:3]
    last = last_name[:4]
    if len(first_name) > 3 & len(last_name) > 4:
        return first_name + last_name
    else:
        return first + last
user_name = username_generator('aaron','bevans')
print(user_name)

"""
function that returns username but with each letter shifted
one place to the right.
"""

def password_generator(username):
    password = ''
    for i in range(0, len(username)):
        password += username[i - 1]
    return password
user_password = password_generator('cyberman')
print(user_password)
