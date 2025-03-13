from decimal import Decimal


def convert2decimal(value: str) -> Decimal:
    """
    Converts a string representation of a float to a float, replacing commas with periods.

    Args:
        value (str): The string to convert to a float.

    Returns:
        float: The float representation of the input string.

    Raises:
        ValueError: If the string cannot be converted to a float.
    """
    value = value.replace(",", ".")
    return Decimal(value)
