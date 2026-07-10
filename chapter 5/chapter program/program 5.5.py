a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))
if(a>b and a>c):
    print("1st number",a," is large")
elif(b>a and b>c):
    print("2nd number",b," is large")
else:
    print("3rd number",c," is large")