def find_min(num):
    min=100000000
    for i in num:
        if(i<min):
            min=i
    return min
numbers = []
for i in range(0,10):
    num=int(input("Enter 10 number one by one:"))
    numbers.append(num)
print("Minimum number is =",find_min(numbers))