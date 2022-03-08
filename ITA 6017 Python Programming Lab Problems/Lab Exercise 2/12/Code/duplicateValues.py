a = int( input("\n Enter the first value: ") )
b = int( input("\n Enter the second value: ") )
c = int( input("\n Enter the third value: ") )
d = int( input("\n Enter the fourth value: ") )
e = int( input("\n Enter the fifth value: ") )

if a == b or a == c or a == d or a == e or b == c or b == d or b == e or c == d or c == e or d == e:
    print("\n DUPLICATES\n")
else:
    print("\n ALL UNIQUE \n")