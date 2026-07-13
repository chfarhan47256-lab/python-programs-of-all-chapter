def cal (a,b,ch):
    match ch:
        case '+':
            print(a,"+",b,"=",a+b)
        case '-':
            print(a,"-",b,"=",a-b)
        case '*':
            print(a,"*",b,"=",a*b)
        case '/':
            print(a,"/",b,"=",a/b)
        case '%':
            print(a,"%",b,"=",a%b)
        case _:
            print("Invalid")
    
a =int(input("Enter value of a:"))
ch=input("Enter opreater:")
b= int(input("Enter value of b:"))
cal(a,b,ch)
