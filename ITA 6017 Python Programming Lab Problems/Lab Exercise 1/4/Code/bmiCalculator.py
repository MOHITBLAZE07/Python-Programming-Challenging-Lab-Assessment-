weight = float(input("\n Enter the weight value in pounds: "))
height = float(input("\n Enter the height value in inches: "))

onePoundValue = 0.4536 
oneInchValue = 2.54
weightInKg = weight * onePoundValue
heightInM = height * oneInchValue

bmi = format((weightInKg) / (heightInM ** 2), ".2f")

print("The BMI value is: ",bmi,"\n")