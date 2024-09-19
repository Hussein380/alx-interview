Here’s a basic README template for your project:

---

# 0x08 - Making Change

## Project Overview

This project tackles the **coin change problem**, where the goal is to determine the fewest number of coins needed to meet a given amount, using a list of available coin denominations. The project challenges the application of **greedy algorithms** and **dynamic programming** to find an efficient solution.

### Problem Description

You are given a pile of coins of different denominations. You need to determine the minimum number of coins required to achieve a target amount (`total`). If it’s impossible to reach the target with the available denominations, the function should return `-1`.

### Requirements

- **Python Version**: The code will be executed on Ubuntu 20.04 LTS using Python 3.4.3.
- The project must adhere to **PEP 8** style guidelines.
- All files must be executable.
- The first line of your Python files should be `#!/usr/bin/python3`.
- Include a `README.md` file at the root of the folder.

### Prototype

```python
def makeChange(coins, total):
    """
    Function to determine the minimum number of coins needed to meet a given total amount.

    :param coins: List of available coin denominations.
    :param total: The target amount to be achieved.
    :return: Minimum number of coins needed or -1 if not possible.
    """
```

### Example

```bash
$ ./0-main.py
7
-1
```

In the example above:
- For `coins = [1, 2, 25]` and `total = 37`, the minimum number of coins is `7`.
- For `coins = [1256, 54, 48, 16, 102]` and `total = 1453`, it's not possible to reach the total, so the function returns `-1`.

### Key Concepts

- **Greedy Algorithms**: Attempting to solve the problem by picking the largest possible coin first and working downwards.
- **Dynamic Programming**: An approach that builds solutions to smaller sub-problems and uses these solutions to find the overall result.

### Files

- **`0-making_change.py`**: Contains the `makeChange` function which implements the solution.
- **`0-main.py`**: Main file for testing the `makeChange` function.

### Usage

Run the Python file using the following command:

```bash
./0-main.py
```

### Resources

- [GeeksforGeeks - Coin Change Problem (DP-7)](https://www.geeksforgeeks.org/coin-change-dp-7/)
- [Dynamic Programming - Coin Change Problem (YouTube)](https://www.youtube.com/watch?v=jgiZlGzXMBw)

### Author

- GitHub: [Hussein380](https://github.com/Hussein380)

---
