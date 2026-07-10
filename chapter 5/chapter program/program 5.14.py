r=int(input("Enter radius:"))
ch=int(input("Enter 1 for area or 2 for cricumfrance:"))
if(ch==1):
    area=r*r*3.141
    print("Area = ",f"{area:.3}")
elif(ch==2):
    cri=2*r*3.141
    print("Cricumfrance = ",cri)
else:
    print("Wrong choice")