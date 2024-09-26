#!/usr/bin/python3
""" Module for calculating the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    def island_perimeter(grid):calculates the prerimeter of an island
    args:
        grid: grid to calcuate the perimeter
    returns:
        perimeter of island
    """
    if not grid:
        return 0

    perimeter = 0
    rows = len(grid)
    col = len(grid[0])

    # loop through the grid to find the rows
    for i in range(rows):
        for j in range(col):
            if grid[i][j] == 1:
                # look at the top
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # check bottom
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # check lef  col
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # check right col
                if j == col - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
