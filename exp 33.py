string = input("Enter a string: ")

freq = {}

for ch in string:
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1

print("\n--- Character Frequency ---")
for key, value in freq.items():
    print(key, ":", value)