number = int( input( "\n Enter the number: " ) )

dummyNumber = number
reversedNumber = 0
while number > 0:
    lastDigit = int(number%10)
    reversedNumber = reversedNumber * 10 + lastDigit
    number = int(number/10)

if reversedNumber == dummyNumber:
    print("\n The number",dummyNumber ,"is a Palindromic Number.\n")
else: 
    print("\n The number",dummyNumber ,"is not a Palindromic Number.\n")