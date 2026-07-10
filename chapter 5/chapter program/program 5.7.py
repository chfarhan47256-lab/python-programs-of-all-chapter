a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))
d=int(input("Enter 4th number:"))
e=int(input("Enter 5th number:"))
max=min=a
if(b>max):
    max=b
if(c>max):
    max=c
if(d>max):
    max=d
if(e>max):
    max=d
if(b<min):
    min=b
if(c<min):
    min=c
if(d<min):
    min=d
if(e<min):
    min=e
print(max," Is large number")
print(min," Is small number")