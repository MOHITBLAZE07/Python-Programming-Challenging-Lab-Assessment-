number = int( input( "\n Enter the number: " ) )
factorialResult = 1

for count in range( number, 0, -1 ):
    factorialResult *= count
print("\n The factorial of",number,"is",factorialResult,"\n")