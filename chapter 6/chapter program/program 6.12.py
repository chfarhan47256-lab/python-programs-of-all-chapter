num = 0
max=0
min=100000000
sum=0
n=0
while(num>=0):
    num=int(input("Enter positive number:"))
    if(num<0):
        break
    n+=1
    sum =sum+num
    if (num>max):
        max=num
    if(num<min):
        min=num
avg = sum/n
print("You enter total ",n," number")
print("Average =",f"{avg:.4}")
print("Maximum = ",max)
print("Minimum = ",min)