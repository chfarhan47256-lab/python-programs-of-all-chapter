def shape(num,ch):
    n=1
    
    while(n<=num):
        i=1
        while(i<=num):
            print(ch,end="")
            i+=1
        print()
        n+=1

num= int(input("Enter number:"))
ch=str(input("Enter character:"))
shape(num,ch)