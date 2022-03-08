
initialAmount = int(input("\n Enter the initial amount: "))
numberOfYears = int(input("\n Enter the number of years for investing: "))
expectedAmount = int(input("\n Enter the expected amount: "))

rateOfInterest = ((expectedAmount - initialAmount)/(initialAmount*numberOfYears))*100

print(rateOfInterest,"%")
