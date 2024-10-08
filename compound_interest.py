def compound(p, r, t):
    amount = p * (pow((1 + r / 100), t))
    ci = amount - p

    print("Compound interest is", ci)


compound(50000, 5, 2)


# using loop
def compound_interest(principal, rate, time):
    Amount = principal
    for i in range(time):
        Amount = Amount * (1 + rate / 100)
    CI = Amount - principal
    print("Compound interest is", CI)


# Driver Code
compound_interest(1200, 5.4, 2)


# without using pow()
p = 1200
t = 2
r = 5.4
# calculates the compound interest
a = p * (1 + (r / 100)) ** t
ci = a - p

print(ci)
