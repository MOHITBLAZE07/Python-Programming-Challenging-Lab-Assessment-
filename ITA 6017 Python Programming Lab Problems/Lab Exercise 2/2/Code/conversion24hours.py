
hours = int( input( "\n Enter the hours in 24 hours format( 1 - 24 ) : " ) )

minutes = int( input( "\n Enter the minutes ( 1 - 59 ): " ) )

seconds = int( input( "\n Enter the seconds ( 1 - 59 ): " ) )

if( hours >= 24 or minutes > 59 or seconds > 59 ):
    print("\n Invalid Input\n")
else:

    if hours <= 12:
        convertedHoursValue = hours
    else: 
        convertedHoursValue = hours - 12

    print("\n 24 hours format time ->",hours,":",minutes,":",seconds)
    print("\n 12 hours format time ->",convertedHoursValue,":",minutes,":",seconds,"\n")
