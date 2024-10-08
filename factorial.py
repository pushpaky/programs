# using math function
import math
import numpy


def factorial(x):
    return (math.factorial(x))


num = 6
print(factorial(num))


# Factorial of a Number Using numpy.prod
x = 7
fact = numpy.prod([i for i in range(1, x + 1)])
print(fact)


# Factorial of a Number Using Recursive approach
def factorial(n):
    return 1 if (n == 0 or n == 1) else n * factorial(n - 1)


n = 4
print(factorial(n))


# Factorial of a Number Using Iterative approach
def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while n > 1:
            fact *= n
            n -= 1
        return fact


num = 5
print(factorial(num))


# Function to find factorial of given number
def factorial(n):

    res = 1

    for i in range(2, n + 1):
        res *= i
    return res


num = 5
print("Factorial of", num, "is", factorial(num))
