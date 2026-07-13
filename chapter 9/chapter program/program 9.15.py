def square (a):
    return a*a
def cube (b):
    return b*b*b
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
sum=square(a)+cube(b)
print("Sum of its cube and square =", sum)