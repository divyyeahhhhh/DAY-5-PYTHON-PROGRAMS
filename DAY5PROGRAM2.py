grade=input("ENTER THE GRADE OF THE EMPLOYEE: ")
sal=float(input("ENTER THE EMPLOYEE SALARY: "))

bonus=0

if sal>0 and (grade=="A" or grade=="B"):
    if grade=='A':
        if sal<10000:
            bonus=(0.1*sal)+(0.02*sal)
        else:
            bonus=0.1*sal
    if grade=='B':
        if sal<10000:
            bonus=(0.1*sal)+(0.02*sal)
        else:
            bonus=0.1*sal

else:
    if sal<0:
        print("SALARY CAN'T BE ZERO..!!")
    if grade>="C" and grade<="Z":
        print("GRADE DOESN'T EXIST..!")

print("Salary= ",sal)
print("Bonus= ",bonus)
print("Total to be paid: ",bonus+sal)
