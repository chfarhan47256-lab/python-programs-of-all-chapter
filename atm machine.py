def atm(ballence):
    n=4
    ch=1
    while(ch!=n):
        print("1 For check your Ballence")
        print("2 For Deposit amount")
        print("3 For Withdraw amount")
        print("4 For end program")
        ch = int(input("Enter your choice:"))
        if ch==1:
            print("Your Balnce is",ballence)
            print("         ----------------                ")
        elif ch==2:
            d_amount=int(input("Enter your total Deposit amount:"))
            if d_amount>0:
                print("Your total Ballence is ",ballence+d_amount)
                ballence+=d_amount
            else:
                print("Invalid Amount")
            print("         ----------------                ")
        elif ch==3:
            w_amount=int(input("Enter your Withdraw amount:"))
            if w_amount>0:
                if ballence>w_amount:
                    print("Your total ballenc after withdraw is ",ballence-w_amount)
                    ballence-=w_amount
                else:
                    print("Insufficient Balance")
            else:
                print("Invalid Amount")
            print("         ----------------                ")
        elif ch==4:
            print("Good bye")
            print("         ----------------                ")
        else :
            print("Invalid choice")
            print("         ----------------                ")

ballence=10000
atm(ballence)