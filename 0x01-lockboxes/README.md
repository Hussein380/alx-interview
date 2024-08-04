# Lock Boxes Puzzle

This project solves the "Lock Boxes" puzzle. The objective is to determine if all boxes can be unlocked starting from the first box. Each box may contain keys to other boxes, and we need to find a way to unlock all the boxes if possible.

## Description

You are given `n` boxes, each numbered from `0` to `n-1`. Each box `i` contains a list of keys that can open other boxes. The goal is to determine if you can open all the boxes starting from box `0`.

## Files

- `lock_boxes.py`: The main script that contains the logic for solving the lock boxes puzzle.

## Functions

### `find_next_box_to_check(opened_boxes)`

Finds the next box that is opened but not yet checked for keys.

- **Args:**
  - `opened_boxes (dict)`: Dictionary containing information about boxes that have been opened.
- **Returns:**
  - `list`: List of keys found in the next box to be checked, or `None` if no such box exists.

### `can_unlock_all_boxes(boxes)`

Determines if all the boxes can be unlocked.

- **Args:**
  - `boxes (list)`: List of lists, where each sublist contains the keys for the corresponding box.
- **Returns:**
  - `bool`: `True` if all boxes can be unlocked, otherwise `False`.

## Usage

To use the script, simply run the `lock_boxes.py` file. You can modify the `main` function to test different configurations of boxes.

### Example

```python
def main():
    """Entry point"""
    print(can_unlock_all_boxes([[1], [2], [3], []]))  # Example usage

if __name__ == '__main__':
    main()

