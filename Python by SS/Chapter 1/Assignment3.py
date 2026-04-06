# Question - Take diameter as input and calculate the area of a circle.

# Solution -
# Area of a circle is given by the formula A = π * r^2, where r is the radius of the circle. The radius can be calculated from the diameter using the formula r = d / 2, where d is the diameter.
import math
# Take diameter as input from the user
diameter = float(input("Enter the diameter of the circle: "))
# Calculate the radius
radius = diameter / 2
# Calculate the area of the circle
area = math.pi * radius ** 2
# Print the area
print(f"The area of the circle with diameter {diameter:.2f} is: {area:.2f}")
