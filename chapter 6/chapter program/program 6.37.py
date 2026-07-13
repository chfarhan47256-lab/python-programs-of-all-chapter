num =int(input("Enter number:"))
n=1
p=1
while(n<=num/2):
    if(num%n==0):
        p=0
        break
    n+=1
if(p==1):
    print("Prime number")
else :
    print("Not prime number")

