cgpa = int( input( "\n Enter the CGPA: " ) )

if cgpa < 0 or cgpa > 10:
    print("\n Invalid Input!\n")
elif cgpa <= 10 and cgpa >= 9:
    print("\n Outstanding\n")
elif cgpa < 9 and cgpa >= 8:
    print("\n Excellent\n")
elif cgpa < 8 and cgpa >= 7:
    print("\n Good\n")
elif cgpa < 7 and cgpa >= 6:
    print("\n Average\n")
elif cgpa < 6 and cgpa >= 5:
    print("\n Better\n")
elif cgpa < 5:
    print("\nPoor\n")