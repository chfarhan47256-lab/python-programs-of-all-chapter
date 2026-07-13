def factriol(num):
    n=1
    f=1
    while(n<=num):
        f=f*n
        n+=1
    print("Factriol of",num,"=",f)
num =int(input("Enter number:"))
factriol(num)