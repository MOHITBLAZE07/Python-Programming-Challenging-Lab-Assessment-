
counter = int( input( "\n Enter the N value: " ) )
sum = 0
initialVal = 2
for i in range( 1, counter + 1):
    sum += initialVal
    initialVal += 2
print("\n The sum of first",counter, "even natural numbers is:",sum,"\n")