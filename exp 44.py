text = input("Enter text to write: ")

with open("output.txt", "w") as file:
    file.write(text)

print("Text written to output.txt!")
