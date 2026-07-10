num = int(input("Enter number:"))
sume=0
sumo=0
n=1
while n<=num:
    if(n%2==0):
        sume=sume+n
    else:
        sumo=sumo+n
    n+=1
print("Sum of Even number ",sume)
print("Sum of odd number ",sumo)