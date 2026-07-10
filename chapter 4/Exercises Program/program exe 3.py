a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))
c = int(input("Enter value of c:"))
s=a+b+c
area=s*(s-a)*(s-b)*(s-c)
area= math.sqrt(area)
print("Area = ",area)