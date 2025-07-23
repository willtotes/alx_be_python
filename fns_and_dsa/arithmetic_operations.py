def perform_operation(num1: float, num2: float, operation: str):
    if operation == "add".lower():
        return num1 + num2
    elif operation == "subtract".lower():
        return num1 - num2
    elif operation == "multiply".lower():
        return num1 * num2
    elif operation == "divide".lower():
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return f"Error: Invalid operation!!!"

