# FizzBuzz in Python

# https://carpentries-incubator.github.io/python-intermediate-development/31-programming-paradigms/index.html#1-2-fizz-4-buzz--fizzbuzz

# The idea is to generate the sequence of integers, but replace multiples of
# three with “Fizz”, multiples of five with “Buzz”, and multiples of both
# with “FizzBuzz”.

# 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz


def fizz_buzz(n):
    for i in range(1, n+1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def accept_input():
    while True:
        try:
            n = int(input("Please enter a number: "))
            break
        except ValueError:
            print("That's not a number!")

    fizz_buzz(n)


__name__ == "__main__" and accept_input()
