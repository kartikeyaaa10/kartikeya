n=int(input("Enter a number: "))
squared_evens = {x: x**2 for x in range(n+1) if x % 2 == 0}
print(squared_evens)