#!/usr/bin/python3

import sys

def print_msg(dict_sc, total_file_size):
    """
    Method to print the total file size and counts of each status code.
    
    Args:
        dict_sc (dict): Dictionary of status codes with their counts.
        total_file_size (int): Total size of files processed.
    
    Returns:
        None
    """
    # Print the total file size
    print("File size: {}".format(total_file_size))
    
    # Print status code counts in ascending order if they are non-zero
    for key, val in sorted(dict_sc.items()):
        if val != 0:
            print("{}: {}".format(key, val))

# Initialize variables
total_file_size = 0  # Total file size accumulated
code = 0  # Variable to store the status code from each line
counter = 0  # Counter to track the number of lines processed
dict_sc = {  # Dictionary to store counts for each status code
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    # Read input line by line from stdin
    for line in sys.stdin:
        # Split the line into components
        parsed_line = line.split()  # Split the line into a list of strings
        
        # Reverse the list to process status code and file size more easily
        parsed_line = parsed_line[::-1]  # Reverse the list

        # Process the line if it has more than 2 parts
        if len(parsed_line) > 2:
            counter += 1  # Increment the line counter

            if counter <= 10:
                # Update total file size and status code count
                total_file_size += int(parsed_line[0])  # File size is now at index 0 after reversing
                code = parsed_line[1]  # Status code is now at index 1 after reversing

                # Update the status code count in the dictionary if it is valid
                if code in dict_sc.keys():
                    dict_sc[code] += 1

            # Every 10 lines, print the current statistics and reset the counter
            if counter == 10:
                print_msg(dict_sc, total_file_size)  # Print statistics
                counter = 0  # Reset the counter

finally:
    # Print final statistics when the program ends or is interrupted
    print_msg(dict_sc, total_file_size)

