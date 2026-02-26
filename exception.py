

try:
   
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    
    result = num1 / num2

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter valid numeric values.")

else:
    print("Result:", result)

finally:
    print("Program execution completed.")