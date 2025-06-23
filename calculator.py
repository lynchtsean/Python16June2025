def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return "Error: Division by zero" if b == 0 else a / b

def calculator():
    print("Welcome to the interactive calculator!")
    print("Type 'exit' anytime to quit.")
    
    while True:
        op = input("Choose operation (+, -, *, /): ")
        if op.lower() == "exit":
            print("Goodbye!")
            break
        if op not in ["+", "-", "*", "/"]:
            print("Invalid operation. Please choose from +, -, *, / or type 'exit' to quit.")
            continue

        # Get first number
        first_input = input("Enter first number: ")
        if first_input.lower() == "exit":
            print("Goodbye!")
            break
        
        # Get second number
        second_input = input("Enter second number: ")
        if second_input.lower() == "exit":
            print("Goodbye!")
            break

        try:
            a = float(first_input)
            b = float(second_input)
        except ValueError:
            print("Invalid number input. Please enter numeric values.")
            continue

        if op == "+":
            result = add(a, b)
        elif op == "-":
            result = subtract(a, b)
        elif op == "*":
            result = multiply(a, b)
        elif op == "/":
            result = divide(a, b)

        print("Result:", result)
        print()  # blank line for readability

calculator()