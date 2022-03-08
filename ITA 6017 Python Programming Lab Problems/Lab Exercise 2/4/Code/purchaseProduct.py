
finalBillAmount = 0
numberOfItemsPurchased = int( input( "\n Enter the number of items purchased: " ) )
if numberOfItemsPurchased <= 0:
    print("\n Invalid Input!\n")

else:

    for i in range( 1, numberOfItemsPurchased + 1 ):
        print("\n Enter details for Item",i,": \n" )
        costOfItem = int( input( "\n\t Enter the cost: " ) )
        if costOfItem <= 0:
            print("\n Invalid Input, Cost of item can't be zero or less. Program exit!\n")
            break
        quantityOfItem = int( input( "\n\t Enter the quantity: " ) )
        if quantityOfItem <= 0:
            print("\n Invalid Input, quantity of item can't be zero or less. Program exit!\n")
            break
        print()
        totalPriceForItem = costOfItem * quantityOfItem
        finalBillAmount += totalPriceForItem

    if i >= numberOfItemsPurchased:
        print("\n The Final Amount to be paid at Bill desk is: Rs", finalBillAmount,"\n")