
print("\n Enter the marks out of 100 in 5 different subjects!\n")

subject1 = int( input("\n Enter the marks of 1st subject: "))
subject2 = int( input("\n Enter the marks of 2nd subject: "))
subject3 = int( input("\n Enter the marks of 3rd subject: "))
subject4 = int( input("\n Enter the marks of 4th subject: "))
subject5 = int( input("\n Enter the marks of 5th subject: "))

totalMarks = 500

sumOfFiveSubjects = subject1 + subject2 + subject3 + subject4 + subject5

percentage = int((sumOfFiveSubjects/totalMarks) * 100)

print( "\nTotal Secured marks: ", sumOfFiveSubjects, "/", totalMarks )
print( "\nYour Percentage: ", percentage,"%" )

if percentage <= 0 or percentage > 100:
    print("\ninvalid input!")
elif percentage >= 90:
    grade = "S"
    print("\nYou have secured ", grade, "grade.\n")
elif percentage < 90 and percentage >= 80:
    grade = "A"
    print("\nYou have secured ", grade, "grade.\n")
elif percentage < 80 and percentage >= 70:
    grade = "B"
    print("\nYou have secured ", grade, "grade.\n") 
elif percentage < 70 and percentage >= 60:
    grade = "C"
    print("\nYou have secured ", grade, "grade.\n")
elif percentage < 60 and percentage >= 50:
    grade = "D"
    print("\nYou have secured ", grade, "grade.\n")
elif percentage < 50 and percentage >= 40:
    grade = "E"
    print("\nYou have secured ", grade, "grade.\n")
elif percentage < 40:
    grade = "N or F"
    print("\nYou have secured ", grade, "grade.\n")
