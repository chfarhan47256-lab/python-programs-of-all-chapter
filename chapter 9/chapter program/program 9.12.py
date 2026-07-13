def grade (marks):
    if(marks>=80):
        print("Grade A")
    elif(marks>=60):
        print("Grade B")
    elif(marks>=40):
        print("Grade C")
    elif(marks<40):
        print("Grade F")
marks=int(input("Enter marks:"))
grade(marks)