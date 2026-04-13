# Assignment 1: Basic Arithmetic and Comparison

# Write a program that takes two numbers and prints:
    # Their sum, difference, and product
    # Whether the first number is greater than the second

# Get input from the user
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

# Calculate sum, difference, and product
sum = x + y
diff = x - y
product = x * y

# Print the results
print(f"The sum of {x} and {y} is: {sum}")
print(f"The difference between {x} and {y} is: {diff}")
print(f"The product of {x} and {y} is: {product}")

# Check if the first number is greater than the second
if x > y:
    print(f"{x} is greater than {y}.")
else:    print(f"{x} is less than {y}.")

#                       -**************************************************************************-

# Assignment 2: Section A: Theory Questions

# Question 1: What are data types in Python? List any 4 with examples?

# Answer 1: Data types in Python are classifications of data that determine the type of value a variable can hold. They define the operations that can be performed on the data and the way it is stored in memory. Here are four common data types in Python with examples:

# 1. Integer (int): Represents whole numbers.
# Example:  x = 10

# 2. Float (float): Represents decimal numbers.
# Example:  y = 3.14

# 3. String (str): Represents a sequence of characters.
# Example:  name = "Alice"

# 4. Boolean (bool): Represents True or False values.
# Example:  is_valid = True


# Question 2: What is the difference between implicit and explicit type conversion? Give one example of each?

# Answer 2: Implicit type conversion, also known as type coercion, is when Python automatically converts one data type to another during an operation. Explicit type conversion, on the other hand, is when the programmer manually converts a data type using built-in functions.

# Example of implicit type conversion:
a = 5  # Integer
b = 2.5  # Float
c = a + b  # Implicitly converts 'a' to float
print(c, type(c))  # Output: 7.5

# Example of explicit type conversion:
x = "10"  # String
y = int(x)  # Explicitly converts 'x' to integer
print(y, type(y))  # Output: 10


# Question 3: What are operators in Python? Explain any three types with examples?
# Answer 3: Operators in Python are special symbols that perform specific operations on operands. They are used to manipulate data and variables. Here are three types of operators with examples:

# 1. Arithmetic Operators: Used for mathematical operations.
# Example:  a = 5 + 3  # Addition

# 2. Comparison Operators: Used to compare values.
# Example:  b = 5 > 3  # Greater than

# 3. Logical Operators: Used to combine conditional statements.
# Example:  c = (5 > 3) and (2 < 4)  # Logical AND

#                       -**************************************************************************-

# Assignment 2: Section B: Coding Questions

# 1️⃣ Smart Temperature Converter
    # Take input in Celsius and print its equivalent in Fahrenheit and Kelvin.
    # (Use explicit type conversion and arithmetic operators.)
        # Formula:
            # Fahrenheit = (C × 9/5) + 32
            # Kelvin = C + 273.15

# Get input from the user
celsius = float(input("Enter temperature in Celsius: "))
c = celsius

# Convert to Fahrenheit and Kelvin
fahrenheit = (c * 9/5) + 32
f = fahrenheit

kelvin = c + 273.15
k = kelvin

# Print the results
print(f"{c}°C is equivalent to {f}°F and {k}K.")

# 2️⃣ Bill Split Calculator
    # Write a program that takes total bill amount and number of friends as input.
    # Calculate how much each person will pay.
    # Also print the data type of each variable used.
    # (Hint: use float() and division operator)

# Get input from the user
total_bill = float(input("Enter the total bill amount: "))
num_friends = int(input("Enter the number of friends: "))

# Calculate the amount each person will pay
amount_per_person = total_bill / num_friends 

# Print the results with data types of each variable
print(f"The total bill is {total_bill} and its data type is {type(total_bill)}")
print(f"Number of Friends is {num_friends} and its data type is {type(num_friends)}")
print(f"Each person will pay is {amount_per_person} and its data type is {type(amount_per_person)}")

