"""
try:
    num = int(input("Enter a number: "))
    print("The number is:", num)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
else:
    print("Input was successful.")
"""
try:
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    result=a/b
except ValueError:
    print("Invalid input. Please enter a valid integer.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("The result of division is:", result)
finally:
    print("Execution completed.")

