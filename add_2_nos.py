import operator

num1 = 10
num2 = 20

sum = num1 + num2

print(sum)

# input data
num1 = int(input("Enter the 1st number"))
num2 = int(input("Enter the 2nd number"))

sum = num1 + num2

print("sum of", num1, "and", num2, "is", sum)


# using function
def add(a, b):
    return a+b


num1 = int(input("Enter the 1st number"))
num2 = int(input("Enter the 2nd number"))

sum = add(num1, num2)

print("sum of", num1, "and", num2, "is", sum)


# using operator add
num1 = 20
num2 = 30

sum = operator.add(num1, num2)
print(sum)


# using lambda function
# add_nos = lambda x, y: x + y

# num1 = 12
# num2 = 12

# sum = add_nos(num1, num2)
# print(sum)


# using recusion function
def add_nos_recursive(x, y):
    if y == 0:
        return x
    else:
        return add_nos_recursive(x + 1, y - 1)


num1 = 1
num2 = 2

sum = add_nos_recursive(num1, num2)
print(sum)
