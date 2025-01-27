

def addition(a, b):
    """Function to add two numbers."""
    return a + b


def subtraction(a, b):
    """Function to subtract the second number from the first."""
    return a - b

def division(a, b):
    """Function to divide the first number by the second."""
    if b == 0:
        return "Division by zero is not allowed."
    return a / b

def factorial(n):
    """Function to calculate the factorial of a number."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

if __name__ == "__main__":
    # Example usage
    num1 = 10
    num2 = 5

    # Call the addition function
    sum_result = addition(num1, num2)
    print(f"The sum of {num1} and {num2} is: {sum_result}")

    # Call the subtraction function
    subtract_result = subtraction(num1, num2)
    print(f"The difference when {num2} is subtracted from {num1} is: {subtract_result}")