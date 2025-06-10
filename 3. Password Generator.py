# Password Generator Application
import random
import string

def generate_password(length):
    # Define possible characters: letters, digits, and symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly select characters from the pool
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Prompt the user for the desired password length
try:
    length = int(input("Enter the desired password length: "))
    if length < 4:
        print("Password length should be at least 4 characters.")
    else:
        password = generate_password(length)
        print(f"Generated Password: {password}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
