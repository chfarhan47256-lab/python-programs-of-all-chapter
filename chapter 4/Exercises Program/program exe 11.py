num = int(input("Enter 3 digit number:"))
a=num%10
num=num/10
b=num%10
num=num/10
c=num%10
print("One by one")
print(int(c))
print(int(b))
print(int(a))