ch = str(input("Enter character:"))
if(ch>='A' and ch<='Z'):
    print("You enter apper case letter")
elif(ch>='a' and ch<='z'):
    print("You enter lower case letter")
elif(ch>='1' and ch<='9'):
    print("You enter number")
else:
    print("You enter symbol")