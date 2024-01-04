#!/usr/bin/python3
"""
0-validate_utf8 module
"""


def validUTF8(data):
    """
    Helper function to check if a byte starts with the
    correct number of leading ones
    """

    def is_start_of_utf8(byte):
        """check the start of byte"""
        return bin(byte).startswith('0b' + '1' * count + '0')
    count = 0
    for byte in data:
        if count == 0:
            if (byte & 0b10000000) == 0:
                continue  # Single-byte character, move to the next byte
            elif (byte & 0b11100000) == 0b11000000:
                count = 1  # Two-byte character, expect one more byte
            elif (byte & 0b11110000) == 0b11100000:
                count = 2  # Three-byte character, expect two more bytes
            elif (byte & 0b11111000) == 0b11110000:
                count = 3  # Four-byte character, expect three more bytes
            else:
                return False  # Invalid leading byte
        else:
            if not is_start_of_utf8(byte):
                return False  # Invalid continuation byte
            count -= 1

    return count == 0  # All expected continuation bytes found
