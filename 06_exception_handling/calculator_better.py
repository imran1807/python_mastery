def add(a, b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    try:
        result = a / b  
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    else:
        return result
if __name__ == "__main__":
    while True:
        
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "5":
            print("Exiting the calculator.")
            break
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue
        if choice == "1":
            print(f"The result of addition is: {add(num1, num2)}")
        elif choice == "2":
            print(f"The result of subtraction is: {subtract(num1, num2)}")
        elif choice == "3":
            print(f"The result of multiplication is: {multiply(num1, num2)}")
        elif choice == "4":
            result = divide(num1, num2)
            if result is not None:
                print(f"The result of division is: {result}")
        else:
            print("Invalid choice. Please select a valid option.")
          