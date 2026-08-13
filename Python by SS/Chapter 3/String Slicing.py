# String Slicing

str0 = input("Enter Your Value: ") #"Python"

# Syntax: string[start:end] # start index is inclusive and end index is exclusive

print(str0[0:3])  # Output: 'Pyt'
print(str0[3:])   # Output: 'hon'
print(str0[:3])   # Output: 'Pyt'
print(str0[:])    # Output: 'Python'
print(str0[3:5])  # Output: 'ho'
print(str0[::1])  # Output: 'Python' (every character)
print(str0[::2])  # Output: 'Pto' (every second character)
print(str0[::3])  # Output: 'Ph' (every third character)
print(str0[1::2]) # Output: 'yhn' (every second character starting from index 1)
print(str0[0::])  # Output: 'Python' (every character starting from index 0)
print(str0[1::])  # Output: 'ython' (every character starting from index 1)
print(str0[1:3:3])# Output: 'y' (from index 1 to 3, step 3)
print(str0[1:5:2])# Output: 'yh' (from index 1 to 5, step 2)

# Practice
# Take input from the user and print the first 3 characters, middle 3 characters, last 3 characters, and every second character of the string.

# Green

str = input("Enter a Value: ")

print("First 3 characters:", str[:3])  # First 3 characters

mid = len(str)//2
output = str[mid-1:mid+2]
print("Middle 3 characters:", output)  # Middle 3 characters

print("Middle 3 characters:", str[len(str)//2 - 1:len(str)//2 + 2])  # Middle 3 characters
print("Last 3 characters:", str[-3:])  # Last 3 characters
print("Every second character:", str[::2])  # Every second character
