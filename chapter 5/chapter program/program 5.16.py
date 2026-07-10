call = int(input("Enter total no of calls:"))
if(call<=100):
    bill=200
elif(call>100 and call<=150):
    bill=200+(call-100)*0.6
elif(call>150 and call<=200):
    bill=200+(50*0.6)+(call-150)*0.5
elif(call>200):
    bill=200+(50*0.60)+(50*0.50)+(call-200)*0.4
print("TOtal bill of",call,"calls is = ",int(bill))