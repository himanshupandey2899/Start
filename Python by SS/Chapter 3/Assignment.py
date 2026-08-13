# Assignment 1: Write a program that takes a word or a sentence as input and prints:
                    # 1. The number of characters in the input
                    # 2. The number of words in the input
                    # 3. Uppercase version of the input
                    # 4. Lowercase version of the input

# Taking input from the user
#input_text = input("Please enter a word or a sentence: ")
input_text = "Python is fun"

# Calculating the number of characters
num_characters = len(input_text)

# Calculating the number of words
num_words = len(input_text.split())

# Converting to uppercase
uppercase_text = input_text.upper()

# Converting to lowercase
lowercase_text = input_text.lower()

# Printing the results
print(f"Number of characters: {num_characters}")
print(f"Number of words: {num_words}")
print(f"Uppercase version: {uppercase_text}")
print(f"Lowercase version: {lowercase_text}")


# Assignment 2: Write a program that takes a word or a sentence as input and prints:
                    # 1. The number of characters in the input
                    # 2. The first character of the input
                    # 3. The last character of the input

# Taking input from the user
#input_text1 = input("Please enter a word or a sentence: ")
input_text1 = "Green"

# Calculating the number of characters
num_characters = len(input_text1)

# Getting the first character
first_character = input_text1[0] if num_characters > 0 else None
#first_character = input_text1[0]

# Getting the last character
last_character = input_text1[-1] if num_characters > 0 else None
#last_character = input_text1[-1]

# Printing the results
print(f"Number of characters: {num_characters}")
print(f"First character: {first_character}")
print(f"Last character: {last_character}")
