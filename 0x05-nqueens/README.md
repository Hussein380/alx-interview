

```markdown
# 0x05. N Queens

## Project Overview

The N Queens puzzle is a classic problem in computer science and mathematics. The challenge is to place N non-attacking queens on an N×N chessboard. This project involves using the backtracking algorithm to solve the N Queens problem, a well-known application of recursion and backtracking techniques.

## Requirements

- **Editors:** Allowed editors include `vi`, `vim`, `emacs`.
- **Interpreter:** The code will be executed on Ubuntu 20.04 LTS using Python 3 (version 3.4.3).
- **Files:** All files should end with a new line. The first line of all files should be `#!/usr/bin/python3`.
- **Style:** The code should adhere to PEP 8 style guidelines (version 1.7.*).
- **Executable:** All files must be executable.

## Task

### 0. N Queens

Write a program that solves the N Queens problem using backtracking.

**Usage:**
```bash
./0-nqueens.py N
```

**Arguments:**
- `N`: An integer representing the size of the chessboard and the number of queens to place.

**Requirements:**
- If the program is called with the wrong number of arguments, print `Usage: nqueens N` followed by a new line, and exit with status 1.
- If `N` is not an integer, print `N must be a number` followed by a new line, and exit with status 1.
- If `N` is smaller than 4, print `N must be at least 4` followed by a new line, and exit with status 1.
- The program should print every possible solution to the problem, one solution per line. The solutions do not need to be printed in any specific order.

**Constraints:**
- You are only allowed to import the `sys` module.

## Example

```bash
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]

$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

## Additional Resources

- **Backtracking Algorithms:** Understanding backtracking algorithms to explore potential solutions and backtrack when needed.
- **Recursion:** Using recursive functions to implement backtracking algorithms.
- **List Manipulations:** Creating and manipulating lists to store queen positions.
- **Python Command Line Arguments:** Handling command-line arguments with the `sys` module.

## Repository

GitHub repository: [alx-interview](https://github.com/your-repository-link)
Directory: `0x05-nqueens`
File: `0-nqueens.py`

## License

This project is licensed under the [MIT License](LICENSE).
```

### Explanation:

- **Project Overview:** Provides a brief description of the N Queens problem and its relevance.
- **Requirements:** Lists the necessary tools, style guidelines, and execution environment.
- **Task:** Detailed instructions on how to run the program, including argument handling and output format.
- **Example:** Demonstrates how the program's output should look with example inputs.
- **Additional Resources:** Lists useful resources for understanding the concepts required for the project.
- **Repository:** Provides a link to the GitHub repository where the code can be found.
- **License:** Includes licensing information for the project.
