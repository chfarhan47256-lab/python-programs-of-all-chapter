def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    return a,b
a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c,d=swap(a,b)
print("Value of a and b before swapping...")
print("a=",a)
print("b=",b)
print("Value of a and b after swapping:")
print("a=",c)
print("b=",d)
