#calculate the area of a triangle, given their side's sizes
import math
side1 = float(input("Enter the size of one triangle side: "))
side2 = float(input("Enter the size of a second triangle side: "))
side3 = float(input("Enter the size the third triangle side: "))

semi_p = side1 + side2 + side3 / 2
area_of_triangle = math.sqrt(semi_p * (semi_p - side1) 
* (semi_p - side2) 
* (semi_p - side3))

print(area_of_triangle)
