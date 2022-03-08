
l = int(input("\n Enter the farm length value: "))
b = int(input("\n Enter the farm breadth value: "))

numberOfRows = (l // 2) + 1
numberOfColumns = (b // 2) + 1

numberOfPlants = numberOfRows * numberOfColumns
print(numberOfRows)
print(numberOfColumns)
print(numberOfPlants)
