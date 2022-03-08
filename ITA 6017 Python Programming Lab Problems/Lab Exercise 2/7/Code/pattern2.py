rows = int(input("\n Enter the number of rows: " ) )
if rows <= 0:
    print("\nInvalid Input!\n")
else:
    print()
    for i in range(1, rows+1):
        for j in range(1, rows+1):
            if j <= i:
                print(i, end=" ")
            else: 
                print(j, end = " ")
        print()
    print()