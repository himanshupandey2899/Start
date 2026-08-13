# Emoji Converter: Take text based emojis as input and convert it into graphical emojis

# Take input from the user
msg = input("Enter a message: ")

# Using string replace method to convert text based emojis to graphical emojis

msg = msg.replace(":)", "😊")
msg = msg.replace(":(", "😞")
msg = msg.replace(":D", "😃")
msg = msg.replace(";)", "😉")
msg = msg.replace(":P", "😛")
msg = msg.replace(":O", "😮")
msg = msg.replace("<3", "❤️")
msg = msg.replace(":/", "😕")
msg = msg.replace(":|", "😐")
msg = msg.replace(":*", "😘")
msg = msg.replace(":')", "😂")
msg = msg.replace(":3", "😺")
msg = msg.replace("XD", "😆")
msg = msg.replace("B)", "😎")
msg = msg.replace(":S", "😖")
msg = msg.replace(":$", "😳")
msg = msg.replace(":@", "😡")

print("Converted message:", msg)

# 2nd Method: Using a dictionary to map text based emojis to graphical emojis

msg1 = "Python is fun :D. I love coding <3. Sometimes it can be frustrating :/ but it's worth it :)"

# Define a dictionary to map text based emojis to graphical emojis

emoji_dict = {
    ":)": "😊",
    ":(": "😞",
    ":D": "😃",
    ";)": "😉",
    ":P": "😛",
    ":O": "😮",
    "<3": "❤️",
    ":/": "😕",
    ":|": "😐",
    ":*": "😘",
    ":')": "😂",
    ":3": "😺",
    "XD": "😆",
    "B)": "😎",
    ":S": "😖",
    ":$": "😳",
    ":@": "😡",
}

# Split the message into words
words = msg1.split()

# Convert each word to its corresponding emoji if it exists in the dictionary
converted_msg = []
for word in words:
    if word in emoji_dict:
        converted_msg.append(emoji_dict[word])
    else:
        converted_msg.append(word)

# Join the converted words back into a single string
final_msg = ' '.join(converted_msg)

# Print the final message with emojis
print("Converted message:", final_msg)
