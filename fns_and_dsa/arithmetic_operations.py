def perform_operation(num1: float, num2: float, operation: str):
    if operation == "add".lower():
        print(num1 + num2)
    elif operation == "subtract".lower():
        print(num1 - num2)
    elif operation == "multiply".lower():
        print(num1 * num2)
    elif operation == "divide".lower():
        print(num1 / num2)
    else:
        print("Unknown Input")

# still needs to be edited