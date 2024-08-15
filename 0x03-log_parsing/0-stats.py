#!/usr/bin/env python3
import sys

# Initialize variables to track total file size and status code counts
total_file_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0


def print_statistics(total_file_size, status_codes):
    """
    Print the total file size and the count of each status code that appeared.
    """
    # Print the total file size
    print(f"File size: {total_file_size}")

    # Print status code counts in ascending order
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


try:
    # Read input line by line from stdin
    for line in sys.stdin:
        # Remove any surrounding whitespace from the line
        line = line.strip()

        # Split the line into its components (IP, date, etc.)
        parts = line.split()

        # Check if the line has the correct number of parts (minimum of 7)
        if len(parts) < 7:
            continue  # If the format is incorrect, skip this line

        # Extract the status code and file size from the line
        status_code = parts[-2]  # Second last item is the status code
        file_size = parts[-1]  # Last item is the file size

        # If the status code is valid, update its count
        if status_code in status_codes:
            status_codes[status_code] += 1

        # Try to convert the file size to an integer and add it to the total
        try:
            total_file_size += int(file_size)
        except ValueError:
            continue  # If file size is not a valid number, skip this line

        # Increment the number of lines processed
        line_count += 1

        # Every 10 lines, print the current statistics
        if line_count % 10 == 0:
            print_statistics(total_file_size, status_codes)

except KeyboardInterrupt:
    # If the user interrupts the program with CTRL + C, print the final
    print_statistics(total_file_size, status_codes)
    raise  # Re-raise the interrupt to exit the program
