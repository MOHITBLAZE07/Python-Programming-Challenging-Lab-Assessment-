
number = int( input( "\n Enter the number: " ) )
print()
if number < 0:
    print(" Invalid Input!\n")
elif number % 2 == 0:
    print(" The number", number, "is even.\n")
else:
    print(" The number ", number, "is odd.\n")