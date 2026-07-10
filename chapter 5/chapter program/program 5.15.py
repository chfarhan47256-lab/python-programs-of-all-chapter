salary = int(input("Enter salary:"))
if(salary>20000):
    salary=salary-(salary*7/100)
    print("SAlary = ",salary)
elif(salary>=10000 and salary <=20000):
    salary=salary-1000
    print("Salary = ",salary)
elif(salary <10000):
    print("Salary = ",salary)