a = int(input("Enter dividend: "))
b = int(input("Enter divisor: "))

try:
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
    
    
    