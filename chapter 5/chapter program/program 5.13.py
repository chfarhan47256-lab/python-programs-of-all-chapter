unit=int(input("Enter total units:"))
if(unit<=300):
    bill=unit*2
elif(unit>300 and unit<=500):
    bill=unit*5
elif(unit>500):
    bill=unit*7
bill=bill+150
if(bill>2000):
    bill=bill+(bill*5/100)
print("YOur total bill of",unit,"unit is = Rs",bill)