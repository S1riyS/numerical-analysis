from decimal import Decimal


def convert2decimal(value: str) -> Decimal:
    """
    Converts a string representation of a float to a Decimal, replacing commas with periods.

    Args:
        value (str): The string to convert to a Decimal.

    Returns:
        float: The Decimal representation of the input string.

    Raises:
        ValueError: If the string cannot be converted to a Decimal.
    """
    value = value.replace(",", ".")
    return Decimal(value)
