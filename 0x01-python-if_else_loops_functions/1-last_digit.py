#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if (number < 0):
    ld = number % -10
else:
    ld = number % 10

if (ld == 0):
    print(f"Last digit of {number:d} is {ld :d} and is 0")

elif (ld > 5):
    print(f"Last digit of {number:d} is {ld :d} and is greater than 5")

else:
    print(f"Last digit of {number:d} is {ld : d} and is less than 6 and not 0")
