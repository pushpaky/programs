def interest(p, t, r):
    print("the principal is:", p)
    print("the time period is:", t)
    print("the rate of interest is:", r)

    simple_interest = (p * t * r) / 100
    print("the simple interest is:", simple_interest)
    return simple_interest


p = int(input("Enter the principal: "))
t = int(input("Enter the time period: "))
r = int(input("Enter the rate of interest: "))
interest(p, t, r)
