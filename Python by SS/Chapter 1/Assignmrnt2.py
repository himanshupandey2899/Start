# Question - Take diameter as input and calculate the area of a circle.
import math
diameter = float(input("Enter the diameter of the circle: "))
radius = diameter / 2  
area = math.pi * radius ** 2
print("The area of the circle is:", area)