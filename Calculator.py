def calculate(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b
    else:
        return "Error: Invalid operation"

while True:
    try:
        num1 = float(input("Enter first number: "))
    except ValueError:
        print("Please enter a valid number")
        continue

    try:
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter a valid number")
        continue

    operation = input("Enter operation (+, -, *, /) or 'q' to quit: ")
    
    if operation == 'q':
        print("Goodbye!")
        break

    result = calculate(num1, num2, operation)
    print(f"Result: {result}")

    again = input("Calculate again? (y/n): ")
    if again.lower() != 'y':
        print("Goodbye!")
        break