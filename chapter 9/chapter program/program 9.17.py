def fact (num):
    f=1
    for i in range(1,num):
        f=f*i
        i+=1
    return f
den=int(input("Enter maximum value of denominator:"))
n=1
sum=0
while(n<=den):
    sum=sum+(1/fact(n))
    n+=1
print("Sum of series = ",sum)