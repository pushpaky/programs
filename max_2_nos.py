def maximunn(a, b):
    if a >= b:
        return a
    else:
        return b


a = 12
b = 15

result = maximunn(a, b)
print(result)

# using max() function
x = 12
y = 20

maximum = max(x, y)
print(maximum)

# using ternary operator
a = 10
b = 5

print(a if a >= b else b)


# using lambda function
# a = 20
# b = 1

# maximum = lambda a, b: a if a > b else b

# print(maximum)

# using list comprehension
a = 100
b = 200

x = [a if a > b else b]
print(x)

# using sort()
a = 45
b = 50

x = [a, b]
x.sort()
print(x[-1])
