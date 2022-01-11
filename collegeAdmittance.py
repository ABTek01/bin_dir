#!/usr/bin/env python3
credits = 120
gpa = 3.5

if credits >= 120 and gpa >= 2.0:
    print('you have enough credits and a high enough gpa to go to college')

if not credits >= 120:
    print('you do not have enough credits to graduate')

if not gpa >= 2.0:
    print('you do not have a high enough gpa to graduate')


if not credits >= 120 and not gpa >= 2.0:
    print('you do not have enough credits or a high enough gpa to graduate')

