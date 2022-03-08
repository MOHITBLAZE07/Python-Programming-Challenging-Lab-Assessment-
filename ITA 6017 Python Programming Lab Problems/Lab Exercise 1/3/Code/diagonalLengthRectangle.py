#importing the math package module to use square root method.
import math

#reading the perimeter value from user.
perimeter = int( input("\n Enter the perimeter of rectangle: ") )
#reading the length value from user.
length = int( input("\n Enter the length of rectangle: ") )

#finding the breadth of rectangle.
breadth = (perimeter // 2) - length

#computing the ans using pythogoras theorem
ans = length**2 + breadth**2

#computing the diagonal length.
diagonalOfRectangle = math.sqrt(ans)

#displaying the diagonal length of rectangle
print("The diagonal length of rectangle is: ",int(diagonalOfRectangle),"\n")