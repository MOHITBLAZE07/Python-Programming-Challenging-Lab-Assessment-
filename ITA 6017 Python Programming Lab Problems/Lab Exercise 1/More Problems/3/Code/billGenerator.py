
firstItemQuantity = int(input("\n Enter the quantity of first item: "))
pricePerFirstItem = int(input("\n Enter the price per first item: "))
secondItemQuantity = int(input("\n Enter the quantity of second item: "))
pricePerSecondItem = int(input("\n Enter the price per second item: "))
thirdItemQuantity = int(input("\n Enter the quantity of third item: "))
pricePerThirdItem = int(input("\n Enter the price per third item: "))

firstItemTotal  = firstItemQuantity * pricePerFirstItem 
secondItemTotal = secondItemQuantity * pricePerSecondItem
thirdItemTotal  = thirdItemQuantity * pricePerThirdItem

totalPrice = firstItemTotal + secondItemTotal + thirdItemTotal

print("\n Total amount to be paid is: Rs",totalPrice)
