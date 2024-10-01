
```markdown
# Prime Game

## Overview

The **Prime Game** is a strategic two-player game developed in Python where Maria and Ben take turns selecting prime numbers from a set of consecutive integers starting from 1 to a given upper limit \( n \). The player who cannot make a move (i.e., has no prime numbers left to choose) loses the game. The game is played for multiple rounds, and the objective is to determine which player wins the most rounds based on optimal play.

## Game Rules

1. Players take turns picking a prime number from the available numbers.
2. After picking a prime number \( p \), the player must remove \( p \) and all of its multiples from the set.
3. The game continues until no prime numbers are left for a player to choose.
4. The player who cannot make a move loses the round.
5. The game can be played for multiple rounds, and the player with the most wins is declared the overall winner.

## Installation

To run the Prime Game, you need Python 3 installed on your system. 

1. Clone the repository:

   ```bash
   git clone https://github.com/Hussein380/alx-interview.git
   ```

2. Navigate to the project directory:

   ```bash
   cd alx-interview/0x0A-primegame
   ```

3. Ensure you have Python 3 installed. You can check this by running:

   ```bash
   python3 --version
   ```

## Usage

To use the Prime Game functionality, you can import the `is_winner` function from the `0-prime_game.py` file.

### Function Prototype

```python
def is_winner(x, nums):
```

- **Parameters**:
  - `x` (int): The number of rounds to play.
  - `nums` (list): A list of integers representing the upper limit (n) for each round.

- **Returns**: 
  - The name of the player who won the most rounds ("Maria" or "Ben"), or `None` if the winner cannot be determined.

### Example

Here’s how you can use the function in a Python script:

```python
#!/usr/bin/python3

from 0-prime_game import is_winner

# Example usage
rounds = 3
nums = [4, 5, 1]
winner = is_winner(rounds, nums)
print(f"Winner: {winner}")
```

### Sample Output

For the input `is_winner(3, [4, 5, 1])`, the output will be:

```
Winner: Ben
```

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [Khan Academy](https://www.khanacademy.org) for resources on prime numbers.
- Various online tutorials for insights into game theory and algorithm optimization.
```

### Key Sections
- **Overview**: Provides a concise description of the game and its rules.
- **Installation**: Steps for cloning the repository and ensuring Python is installed.
- **Usage**: Instructions on how to use the `is_winner` function, including function prototype and example usage.
- **Contributing**: Guidelines for contributing to the project.
- **License**: Basic information about licensing.
- **Acknowledgements**: Credits to sources that helped in understanding the concepts.

