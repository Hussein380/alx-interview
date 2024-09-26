---

# Island Perimeter

## Project Overview

The **Island Perimeter** project focuses on applying algorithms and data structures to calculate the perimeter of a single island in a given grid. The grid is represented by a 2D array of integers, where `1` indicates land and `0` indicates water. The objective is to efficiently determine the total perimeter of the island based on its layout within the grid.

### Project Timeline
- **Start Date:** September 23, 2024, 6:00 AM
- **End Date:** September 27, 2024, 6:00 AM
- **Checker Release:** September 24, 2024, 6:00 AM
- **Auto Review Deadline:** September 27, 2024, 6:00 AM

## Table of Contents
- [Concepts Needed](#concepts-needed)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Algorithm Explanation](#algorithm-explanation)
- [Code Structure](#code-structure)
- [Contributing](#contributing)
- [License](#license)

## Concepts Needed

### 1. 2D Arrays (Matrices)
- Accessing and iterating over elements in a 2D array.
- Navigating through adjacent cells (horizontally and vertically).

### 2. Conditional Logic
- Applying conditions to determine whether a cell contributes to the perimeter of the island.

### 3. Counting Techniques
- Developing a method to count the edges that contribute to the island’s perimeter.

### 4. Problem-Solving Strategies
- Breaking down the problem into smaller tasks, such as identifying land cells and calculating their contribution to the perimeter.

### 5. Python Programming
- Using nested loops for iterating over grid cells.
- Employing conditional statements to check the status of adjacent cells.

### Resources
- **Python Official Documentation:** [Nested Lists](https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions)
- **GeeksforGeeks Articles:** [Multi-dimensional Arrays in Python](https://www.geeksforgeeks.org/multi-dimensional-arrays-in-python/)
- **TutorialsPoint:** [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm)
- **YouTube Tutorials:** Search for "Python 2D arrays and lists."

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using `python3` (version 3.4.3).
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/python3`.
- A `README.md` file, located at the root of the project folder, is mandatory.
- Code should adhere to PEP 8 style (version 1.7).
- No external modules are allowed; all modules and functions must be documented.
- All files must be executable.

## Installation

To get started with the project, clone the repository and navigate to the project directory:

```bash
git clone https://github.com/your_username/alx-interview.git
cd alx-interview/0x09-island_perimeter
```

## Usage

To run the island perimeter calculation, you can use the provided main script `0-main.py`:

```bash
./0-main.py
```

### Example Input
The following grid represents a sample input:

```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
```

### Example Output
The output will display the perimeter of the island:

```bash
12
```

## Algorithm Explanation

The algorithm follows these steps to calculate the perimeter:

1. **Iterate Over the Grid:** Use nested loops to access each cell in the grid.
2. **Check for Land Cells:** For each land cell (1), check its adjacent cells (up, down, left, right).
3. **Count Perimeter Contribution:** If an adjacent cell is water (0) or out of bounds, it contributes to the perimeter.
4. **Sum Up Contributions:** Keep a running total of all contributions to determine the total perimeter.

## Code Structure

- `0-island_perimeter.py`: Contains the main function `island_perimeter(grid)` that calculates the perimeter.
- `0-main.py`: A test script that provides sample grid input and prints the perimeter.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and create a pull request with your proposed changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
