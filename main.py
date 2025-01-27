
# added this comment
def addition(a, b):
    """Function to add two numbers."""
    return a + b


def subtraction(a, b):
    """Function to subtract the second number from the first."""
    return a - b


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