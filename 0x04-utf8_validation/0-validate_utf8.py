#!/usr/bin/python3
"""
0-validate_utf8 module
"""


def validUTF8(data):
    """
    Initialize a variable to keep track of the number
    of remaining bytes to read for the current character.
    """
    remaining_bytes = 0

    """Iterate through the list of integers."""
    for byte in data:
        """
        Check if this byte is the start of a new
        character.
        """
        if remaining_bytes == 0:
            """
            Determine the number of leading 1s in the
            byte to identify the character length.
            """
            if byte < 128:
                remaining_bytes = 0
            elif byte >= 192 and byte < 224:
                remaining_bytes = 1
            elif byte >= 224 and byte < 240:
                remaining_bytes = 2
            elif byte >= 240 and byte < 248:
                remaining_bytes = 3
            else:
                """Invalid start byte."""
                return False
        else:
            """
            Check if the current byte is a continuation
            byte (starts with 10).
            """
            if byte < 128 or byte >= 192:
                remaining_bytes -= 1
            else:
                """Invalid continuation byte."""
                return False

    """
    After iterating through all bytes, if there
    are remaining bytes to read, it's invalid.
    """
    return remaining_bytes == 0
