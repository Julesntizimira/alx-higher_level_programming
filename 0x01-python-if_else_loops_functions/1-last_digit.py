#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number
if num < 0:
    num = num * -1
digit = num % 10
if number < 0:
    digit = digit * -1;
if digit > 5:
    print(f"Last digit of {number} is {digit} and is greater than 5")
elif digit == 0:
    print(f"Last digit of {number} is {digit} and is 0")
else:
    print(f"Last digit of {number} is {digit} and is less than 6 and not 0")
