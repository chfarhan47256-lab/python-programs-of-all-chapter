num = int(input("Enter number:"))
n=num
sum = 0
while n!=0:
    r=n%10
    sum=sum+(r*r*r)
    n=n/10
    n=int(n) # line 7 n/10 is floating point number
if(sum==num):
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")