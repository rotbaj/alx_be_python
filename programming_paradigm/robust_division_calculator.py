# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Perform division with robust error handling.

    Args:
        numerator (str): The numerator as a string.
        denominator (str): The denominator as a string.

    Returns:
        str: The result of the division or an error message.
    """
    try:
        # Convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)

        # Perform division
        result = numerator / denominator
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."