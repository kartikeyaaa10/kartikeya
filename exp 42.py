import re

s = input("Enter a string: ")
result = bool(re.fullmatch(r'\d+', s))
if result==True:
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")
    