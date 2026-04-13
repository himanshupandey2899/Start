# Program to take age as input and print value entered and its data type

# Note: The input() function returns a string, so the data type of age will be <class 'str'>. If you want to convert it to an integer, you can use int(age).

age = float(input("Enter your age: "))
print("Your age is:", age)
print("Data type of age is:", type(age))