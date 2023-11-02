#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lasnum = abs(number) % 10
if number < 0:
    lasnum = -lasnum
if lasnum > 5:
    print("Last digit of", number, "is", lasnum, "and is greater than 5")
elif lasnum == 0:
    print("Last digit of", number, "is", lasnum, "and is 0")
else:
    print("Last digit of", number, "is", lasnum, "and is less than 6 and not 0")
~                           
