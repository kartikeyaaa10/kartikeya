import re

password = input("Enter password: ")

def check_strength(password):
    if len(password) < 8:
        return "Weak - Too short (min 8 characters)"
    if not re.search(r'[A-Z]', password):
        return "Weak - Add at least one uppercase letter"
    if not re.search(r'[a-z]', password):
        return "Weak - Add at least one lowercase letter"
    if not re.search(r'\d', password):
        return "Weak - Add at least one digit"
    if not re.search(r'[!@#$%^&*]', password):
        return "Medium - Add a special character (!@#$%^&*)"
    return "Strong Password!"

print(check_strength(password))