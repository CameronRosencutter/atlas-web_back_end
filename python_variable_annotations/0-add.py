def add(a: float, b: float) -> float:
    """
    Adds two floating-point numbers and returns the result.

    Parameters:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The sum of a and b.
    """
    result = a + b
    return result


num1 = 444
num2 = 2.0
result_sum = add(num1, num2)
print(f"The sum of {num1} and {num2} is: {result_sum}")