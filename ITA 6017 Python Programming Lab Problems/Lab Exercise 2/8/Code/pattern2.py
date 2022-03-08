rows = int( input("\n Enter number of rows: "))
if rows <= 0:
    print("\n Invalid Input!\n")
else:
    count = 1
    for i in range( 1, rows + 1 ):
        for j in range( 1, count+1):
            print("*",end="")
        count += 2
        print()
print()