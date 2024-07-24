#!/usr/bin/python3
def pascal_triangle(n):
    # If n is less than or equal to 0, return an empty list
    if n <= 0:
        return []
    
    # Initialize an empty list to hold all rows of Pascal's Triangle
    triangle = []

    # Loop through each row index from 0 to n-1
    for row_num in range(n):
        # Initialize the current row with 1 as the first element
        row = [1]

        # If the current row is not the first row, calculate the interior values
        if row_num > 0:
            # Get the previous row from the triangle
            prev_row = triangle[row_num - 1]

            # Loop through the previous row to calculate the current row's values
            for j in range(1, row_num):
                # Each element is the sum of the two elements above it in the previous row
                row.append(prev_row[j - 1] + prev_row[j])

            # Append 1 as the last element of the current row
            row.append(1)
        
        # Add the current row to the triangle
        triangle.append(row)
    
    # Return the complete Pascal's Triangle
    return triangle
