#!/usr/bin/python3
print("1", end="")
for i in range(2, 100):
    if i % 3 == 0 and i % 5 == 0:
        print(" FizzBuzz", end="")
    elif i % 3 == 0:
        print(" Fizz", end="")
    elif i % 5 == 0:
        print(" Buzz", end="")
    else:
        print(" {}".format(i), end="")
