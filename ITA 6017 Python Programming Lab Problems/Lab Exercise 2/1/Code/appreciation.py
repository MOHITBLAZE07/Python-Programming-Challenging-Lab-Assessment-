sGrades = int( input( "\n Enter the number of 'S' grades: " ) )
attendance = int( input( "\n Enter the attendance (%): " ) )
sportsParticipation = int( input( "\n Enter the sports Participation value: " ) )

if(sGrades >= 0 and sGrades <= 8 and attendance >= 0 and attendance <= 100 and sportsParticipation >= 0 and sportsParticipation <= 10):
    if( sGrades >= 3 and attendance >= 90 and sportsParticipation >= 2 ):
        print("\n Excellent\n")
    elif( sGrades >= 3 and attendance >= 90 ):
        print("\n Very Good\n")
    elif( sGrades >= 3 and sportsParticipation >= 2 ):
        print("\n Good\n")
else:
    print("\nInvalid Input\n")