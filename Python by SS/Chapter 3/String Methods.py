# String Methods

# str = input("Enter Your Value: ")
str = "Himanshu pandey"

print("The Original String is: ", str, type(str))
print("The String in Upper Case is: ", str.upper())
print("The String in Lower Case is: ", str.lower())
print("The String in Title Case is: ", str.title())
print("The String for finding a character is: ", str.find("ey"))
print("The String for replacing a character is: ", str.replace("man", "boy"))
print("The Index position of 'u' in the string is: ", str.index("u"))
print("The Count of 'a' in the string is: ", str.count("a"))
print("The String for Capitalize Case is: ", str.capitalize())
print("The String in Swap Case is: ", str.swapcase())
print("The String in Casefold is: ", str.casefold())
print("The String in Centered is: ", str.center(30, '*'))

# Practice: Write a program to demonstrate the use of string methods in Python. Take a sentence as a string input from the user and apply the given methods. Print the results of each method to the console.

# Take input from the user
input = input("Enter a sentence: ")

# Apply string methods
print("The Original String is: ", input, type(input))

# Convert to Lower Case
print("The String in Lower Case is: ", input.lower())

# Replace all " " with "_"
print("The String after replacing spaces with underscores is: ", input.replace(" ", "_"))