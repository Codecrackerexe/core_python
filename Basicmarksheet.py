roll=int(input("Enter roll no:"))
sname=input("Enter student name:")
marks=int(input("Enter marks of student..."))
s1=int(input("Enter marks of SCI:"))
s2=int(input("Enter marks of PHY:"))
s3=int(input("Enter marks of CHEM:"))

print("The roll no of student:",roll)
print("The name of student:",sname)
print("The marks of student....",marks)

total= s1+s2+s3
print("The total of the student is:",total)

perc= total/3
print("The percentage he/she holds is:",perc)

if perc>=70:
    print("Distinction")
elif perc>=60:
    print("First rank")
elif perc>=50:
    print("Second rank")
elif perc>=40:
    print("Passed")
else:
    print("Failed!!!")

