#Simple password generator using the string and random libraries.
import string
import random

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# User input
try:
    n = int(input("Enter the length of the password: "))
    if n <= 0:
        print("Password length must be greater than 0.")
    else:
        print("Generated password:", generate_password(n))
except ValueError:
    print("Invalid input. Please enter a number.")
