def even_odd(num):
    if(num%2==0):
        print(num,"is Number even")
    else:
        print(num,"is Number odd")
def prime_or_not(num):
    if num <= 1:
        print(num, "is not prime")
        return
    for i in range(2,num):
        if(num%i==0):
            print(num,"is not prime number")
            return
    print(num, "is prime number")
num=int(input("Enter number:"))
even_odd(num)
prime_or_not(num)