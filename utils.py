def is_palindrome(s):
    """Check whether a string is a palindrome.

    Ignores case, spaces and punctuation.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if s reads the same both ways.

    Example:
        >>> is_palindrome("Madam")
        True
    """
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


def count_words(text):
    """Count the words in a piece of text.

    Args:
        text (str): The text to analyse.

    Returns:
        int: Number of words.

    Example:
        >>> count_words("AI tools are useful")
        4
    """
    return len(text.split())


def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit.

    Args:
        c (float): Temperature in Celsius.

    Returns:
        float: Temperature in Fahrenheit.

    Example:
        >>> celsius_to_fahrenheit(100)
        212.0
    """
    return c * 9 / 5 + 32