num=int(input("Enter number:"))
n=1
sum=0
mid=num/2
while (n<=int(mid)):
    if(num%n==0):
        sum=sum+n
    n+=1
if(sum==num):
    print(num," is perfect number")