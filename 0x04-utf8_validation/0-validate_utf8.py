#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    UTF-8 encoding can be 1 to 4 bytes long. The first byte indicates how many
    bytes are in the character:
    - 1-byte character: Starts with 0xxxxxxx
    - 2-byte character: Starts with 110xxxxx and followed by 10xxxxxx
    - 3-byte character: Starts with 1110xxxx and followed by two 10xxxxxx
    - 4-byte character: Starts with 11110xxx and followed by three 10xxxxxx
    """

    # Number of bytes remaining to be validated in a character
    bytes_to_process = 0

    # Masks for checking the leading bits of the current byte
    most_significant_bit_mask = 1 << 7  # 10000000
    second_significant_bit_mask = 1 << 6  # 01000000

    for byte in data:
        # Mask to check the leading bits of the byte
        check_leading_bits = 1 << 7  # Start with the most significant bit

        if bytes_to_process == 0:
            # Determine how many bytes the current UTF-8 character should have
            while check_leading_bits & byte:
                bytes_to_process += 1
                check_leading_bits = check_leading_bits >> 1

            # If the byte doesn't start with 1 (indicating a 1-byte character
            if bytes_to_process == 0:
                continue

            # UTF-8 characters can be 1 to 4 bytes long
            if bytes_to_process == 1 or bytes_to_process > 4:
                return False

        else:
            # Continuation bytes must follow the pattern 10xxxxxx
            if not (byte & most_significant_bit_mask and not (
                    byte & second_significant_bit_mask)):
                return False

        # Decrement the remaining bytes to process for the current character
        bytes_to_process -= 1

    # If all bytes have been processed correctly, return True
    return bytes_to_process == 0
