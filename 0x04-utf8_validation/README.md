---

# 0x04. UTF-8 Validation

## Project Overview

This project involves writing a Python function to determine if a given dataset represents a valid UTF-8 encoding. The function will analyze a sequence of integers, each representing a byte, and validate if they adhere to the rules of UTF-8 encoding.

The goal is to strengthen your understanding of bitwise operations, data representation at the byte level, and UTF-8 encoding schemes, while practicing algorithmic problem-solving using Python.

## Learning Objectives

By completing this project, you should gain an understanding of the following concepts:

- **Bitwise Operations in Python:** Learn how to manipulate bits using operators like AND (`&`), OR (`|`), XOR (`^`), NOT (`~`), and shifts (`<<`, `>>`).
- **UTF-8 Encoding Scheme:** Understand how characters are encoded into one or more bytes according to UTF-8 rules and recognize patterns that represent valid UTF-8 encoded characters.
- **Data Representation:** Understand how to work with data at the byte level, specifically focusing on handling the least significant bits (LSB) of integers to simulate byte data.
- **List Manipulation in Python:** Learn how to iterate through lists, access list elements, and use list comprehensions effectively.
- **Boolean Logic:** Apply logical operations to make decisions within your program.

## Requirements

- All code will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.
- Your code should be PEP 8 compliant.
- Your Python files must start with `#!/usr/bin/python3`.
- All files should be executable.
- A `README.md` file at the root of the project is mandatory.

## Usage

To test your implementation, run the following commands:

```bash
$ ./0-main.py
```

This will output whether the data sets in the test cases are valid UTF-8 encodings.

### Example Output

```bash
True
True
False
```

## Task Description

### 0. UTF-8 Validation (Mandatory)

Write a Python method that checks if a given data set represents a valid UTF-8 encoding:

- **Prototype:** `def validUTF8(data)`
- **Input:** A list of integers where each integer represents a byte of data (you only need to handle the 8 least significant bits).
- **Output:** `True` if the data set is valid UTF-8 encoding; otherwise, `False`.
- **UTF-8 Encoding Rules:**
  - A character can be 1 to 4 bytes long.
  - The first byte determines how many bytes the character has:
    - 1-byte character: Starts with `0xxxxxxx`.
    - 2-byte character: Starts with `110xxxxx` followed by `10xxxxxx`.
    - 3-byte character: Starts with `1110xxxx` followed by two `10xxxxxx`.
    - 4-byte character: Starts with `11110xxx` followed by three `10xxxxxx`.

### Example Test Cases

1. **Input:** `[65]`  
   **Output:** `True`  
   **Explanation:** This is a valid 1-byte character.

2. **Input:** `[80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]`  
   **Output:** `True`  
   **Explanation:** This is a valid UTF-8 string.

3. **Input:** `[229, 65, 127, 256]`  
   **Output:** `False`  
   **Explanation:** The integer `256` is invalid as it exceeds the 8-bit range.

## Files

The project includes the following files:

- `0-validate_utf8.py`: The implementation of the `validUTF8` function.
- `0-main.py`: The main file for testing the function.

## Resources

To help you understand the concepts, check out the following resources:

- [Bitwise Operations in Python](https://realpython.com/python-bitwise-operators/)
- [UTF-8 Wikipedia](https://en.wikipedia.org/wiki/UTF-8)
- [Characters, Symbols, and the Unicode Miracle](https://www.joelonsoftware.com/2003/10/08/)
- [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets](https://www.joelonsoftware.com/2003/10/08/)

## Author

- Hussein Yussuf Garane

## License

This project is licensed under the MIT License.

---
