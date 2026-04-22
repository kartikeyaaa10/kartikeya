n=int(input("Enter number for set "))
numbers = []
numbers.append(n)

print("Original list =", numbers)


numbers = list(set(numbers))

print("After removing duplicates =", numbers)