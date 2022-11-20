"""This file shows an example google docstring"""


def i_want_this_to_be_documented(input1: str, input2: str) -> str:
    """
    I want this function to be documented

    Args:
        input1: My first String
        input2: My Second String

    Returns:
        A concatenation of two strings

    Examples:
        >>> str1 = "Hello"
        >>> str2 = "World"
        >>> assert i_want_this_to_be_documented(str1,str2) == "HelloWorld"
    """

    return input1 + input2
