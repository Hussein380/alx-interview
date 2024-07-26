def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.
    
    Args:
    n (int): The number of rows of Pascal's Triangle to generate.
    
    Returns:
    list: A list of lists of integers representing Pascal's Triangle.
    """
    triangle = []  # Initialize the list to hold the rows of Pascal's Triangle
    
    if n > 0:  # Only proceed if n is greater than 0
        for row in range(1, n + 1):
            current_row = []  # Initialize the list to hold the current row's values
            coefficient = 1  # Binomial coefficient (C)
            
            for element in range(1, row + 1):
                current_row.append(coefficient)  # Append the current binomial coefficient to the row
                coefficient = coefficient * (row - element) // element  # Update the binomial coefficient
                
            triangle.append(current_row)  # Add the current row to the triangle
            
    return triangle  # Return the completed Pascal's Triangle
