def multipal(a,b):
    if(b%a==0):
        return 1
    else:
        return 0
for i in range(1,5):
    a=int(input("Enter a number:"))
    b=int(input("Enter a number:"))
    re=multipal(a,b)
    if(re==1):
        print(b,"is multipal of",a)
    else:
        print(b,"Not multipal of",a)
        break