firstDay = float(input("\n Enter the hours worked in first day: "))
secondDay = float(input("\n Enter the hours worked in second day: "))
thirdDay = float(input("\n Enter the hours worked in third day: "))
fourthDay = float(input("\n Enter the hours worked in fourth day: "))
fifthDay = float(input("\n Enter the hours worked in fifth day: "))

sumOfHoursWorked = firstDay + secondDay + thirdDay + fourthDay + fifthDay

avgHoursWorked = sumOfHoursWorked / 5

print("The average hours worked by the employee is: ", avgHoursWorked,"\n")