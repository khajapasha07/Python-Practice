# Password Generator
# Author: Khaja Pasha

import random
import string

print("=== Random Password Generator ===")

# Ask the user for the password length
length = int(input("Enter the password length: "))

# Store all possible characters
characters = string.ascii_letters + string.digits + string.punctuation

# Create an empty password
password = ""

# Generate the password
for i in range(length):
    password += random.choice(characters)

# Display the generated password
print("\nGenerated Password:", password)

print("\nThank you for using the Password Generator!")
