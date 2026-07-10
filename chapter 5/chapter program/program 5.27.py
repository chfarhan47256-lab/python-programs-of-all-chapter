a = float(input("Enter value of a:"))
op = str(input("Enter opreator:"))
b = float(input("Enter value of b:"))
match op:
    case '+':
        print("Sum =",a+b)
    case '-':
        print("Diffrence = ",a-b)
    case '*':
        print("Multiplication = ",a*b)
    case '%':
        print("Modules = ",a%b)
    case '/':
        if(b==0):
            print("Division by 0")
        else:
            print("division = ",a/b)
    case _:
        print("Invalid ")