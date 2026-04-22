n = input("Enter a string: ")

count = 0

for ch in n:
    if ch in "aeiouAEIOU":
        count = count + 1

print("Vowels count =", count)