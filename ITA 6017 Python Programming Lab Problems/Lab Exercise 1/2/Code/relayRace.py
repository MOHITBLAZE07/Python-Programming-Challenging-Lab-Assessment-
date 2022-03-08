                    #Relay Race Problem
print("Total distance to be covered: \n")
#get the km value to be covered from user.
kmValue = int(input("Enter the value for Km's: "))
#get the m value to be covered from user.
mValue = int(input("Enter the value for Mts's: "))

#converting the km into m
kmInM = kmValue*1000
#computing the total distance to be covered in metres.
totalDistanceInM = kmInM + mValue
#computing the total distance each runner will be covering.
distToBeCoveredByEachRunner = totalDistanceInM//4
#checking the distance is less than 1km or not if yes then just print the m value and print km as 0.
if( distToBeCoveredByEachRunner < 1000 ):
    print("0 Km and ", distToBeCoveredByEachRunner, " m.")
#if distance is greater than 1000... then compute the respective km value and m value.
else:
    ansKmVal = distToBeCoveredByEachRunner // 1000
    ansMVal = distToBeCoveredByEachRunner - ansKmVal * 1000
#print the km ans value and m ans value
    print(ansKmVal, "km and ", ansMVal, " m.")


