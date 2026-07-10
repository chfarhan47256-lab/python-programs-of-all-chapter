hours=int(input("Enter number of hours:"))
weak=hours/168
hours=hours%168
day=hours/24
fhour=hours%24
print("Weak = ",int(weak))
print("Days = ",int(day))
print("Hours = ",fhour)