#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a square 2D matrix (n x n) 90 degrees clockwise in place.

    Args:
        matrix (list of list of int): The n x n matrix to rotate.
    """
    n = len(matrix)  # Get the size of the matrix (n x n)

    # Loop through each layer (from outer to inner)
    for layer in range(n // 2):
        # Define the first and last index for the current layer
        first = layer
        last = n - layer - 1

        # Loop through each element in the current layer
        for i in range(first, last):
            offset = i - first  # Calculate how far we are from the edge

            # Save the top element temporarily (will be overwritten)
            top = matrix[first][i]

            # Move the left element to the top
            matrix[first][i] = matrix[last - offset][first]

            # Move the bottom element to the left
            matrix[last - offset][first] = matrix[last][last - offset]

            # Move the right element to the bottom
            matrix[last][last - offset] = matrix[i][last]

            # Move the top element (from the temp variable) to the right
            matrix[i][last] = top
