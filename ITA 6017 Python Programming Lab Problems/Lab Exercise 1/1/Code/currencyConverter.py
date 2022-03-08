# Currency Converter Program

# rsVal to store float type value in rupees equivalent to 1 dollar.
rsVal = float(input("Enter ₹ Equivalent to $1: "))
# amount to  store the float type value in rupees to be converted in dollar.
amount = float(input("Enter amount(₹) to be converted in $: "))
#dollarVal to store the equivalent dollar value to amount given in RS. upto 2 decimal places
dollarVal = format(amount / rsVal, ".2f")

#Displaying the final OUTPUT in dollars
print( "The Dollar Value equivalent to ₹", amount, " is: $", dollarVal)
