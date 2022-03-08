
initialLevel = int( input( "\nEnter the initial level of water in jug (in ml): " ) )

targetLevel = int( input( "\nEnter the level of water in jug required for drinking ( in ml ): " ) )

sIncreaseHeight = int( input( "\nEnter the height which small pebble will increase ( in ml ): " ) )

bIncreaseHeight = int( input( "\n Enter the height which big pebble will increase ( in ml ): " ) )

numberOfSmallPebbles = int( input("\n Enter the number of pebbles: ") )

waterLevelToBeIncreased = targetLevel - initialLevel

waterLevelLeftForBigPebble = waterLevelToBeIncreased - ( numberOfSmallPebbles * sIncreaseHeight )

numberOfBigPebble = (waterLevelLeftForBigPebble // bIncreaseHeight) + 1

print("\n Number of Big Pebbles Required: ", numberOfBigPebble, "\n" )