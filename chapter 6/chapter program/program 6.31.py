num=int(input("Enter number:"))
max=0
min=100000
while(num>0):
    r=num%10
    if(r>max):
        max=r
    if(r<min):
        min=r
    num=num/10
    num=int(num)

print("Maximun = ",int(max))
print("Minimum = ",int(min))