# Simple login program
# Secure coding review task (beginner level)

import hashlib

username = input("Enter username: ")
password = input("Enter password: ")

hashed_password = hashlib.sha256(password.encode()).hexdigest()

stored_username = "admin"
stored_password = hashlib.sha256("admin123".encode()).hexdigest()

if username == stored_username and hashed_password == stored_password:
    print("Login successful")
else:
    print("Invalid credentials")
