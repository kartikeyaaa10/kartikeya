word = input("Enter a word: ")

if word == word[::-1]:
    print(word, "is a Palindrome")
else:
    print(word, "is NOT a Palindrome")