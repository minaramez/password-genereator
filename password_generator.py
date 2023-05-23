#!/usr/bin/env python3

import random
import string
import re
import os


os.system('clear')


print("")
print("")
print("Script written by: Mina Ramez Farag")
print("")
print("       *****************************************************")
print("       *******PASSWORD GENERATOR AND STRENGTH CHECKER*******")
print("       *****************************************************")
print("")

def generate_secure_password():
    length = 12  # Length of the secure password
    characters = string.ascii_letters + string.digits + string.punctuation

    secure_password = None
    while True:
        secure_password = ''.join(random.choice(characters) for _ in range(length))

        # Ensure the password meets the desired criteria
        has_uppercase = any(char.isupper() for char in secure_password)
        has_lowercase = any(char.islower() for char in secure_password)
        has_digit = any(char.isdigit() for char in secure_password)
        has_special = any(char in string.punctuation for char in secure_password)

        if has_uppercase and has_lowercase and has_digit and has_special:
            break

    return secure_password

def analyze_password_strength(password):
    # Define the criteria for password strength
    min_length = 8
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False
    common_patterns = ['123456', 'password', 'qwerty', 'admin']

    # Check password length
    if len(password) < min_length:
        return "Password is too short. Minimum length should be {} characters.".format(min_length)

    # Check for uppercase, lowercase, digit, and special characters
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True

    # Check if all the required criteria are met
    if not has_uppercase:
        return "Password should contain at least one uppercase letter."
    if not has_lowercase:
        return "Password should contain at least one lowercase letter."
    if not has_digit:
        return "Password should contain at least one digit."
    if not has_special:
        return "Password should contain at least one special character."

    # Check for common patterns
    for pattern in common_patterns:
        if re.search(pattern, password, re.IGNORECASE):
            return "Password should not contain common patterns or easily guessable sequences."

    # Password passed all criteria, so it is considered strong
    return "Password is strong."

# Prompt the user for choices until "quit" is entered
while True:
    print("")
    print("Choose an option:")
    print("1. Generate a secure password")
    print("2. Test the strength of a password")
    choice = input("Enter your choice (1, 2, or 'quit' to exit): ")

    # Generate a secure password if chosen
    if choice == '1':
        secure_password = generate_secure_password()
        print("")
        print("Generated secure password:", secure_password)

    # Analyze the strength of a password if chosen
    elif choice == '2':
        print("")
        password = input("Enter a password to analyze: ")
        result = analyze_password_strength(password)
        print(result)

    # Exit the loop if "quit" is entered
    elif choice.lower() == 'quit':
        break

    else:
        print("Invalid choice. Please select 1, 2, or type 'quit' to exit.")
