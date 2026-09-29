# Programmer's Calculator

## Overview

Programmer's Calculator is a Python-based calculator designed for arithmetic and programming-related number operations. It provides a simple command-line interface that allows users to perform arithmetic calculations, convert numbers between different number systems, perform bitwise operations, and maintain a history of previous calculations.

The project is implemented as a modular Python application with input validation, error handling, and unit testing.

## Features

- Arithmetic calculations using:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`)
  - Division (`/`)
  - Floor division (`//`)
  - Modulus (`%`)
  - Power (`**`)
  - Parentheses
- Number system conversion between Binary (BIN), Octal (OCT), Decimal (DEC), and Hexadecimal (HEX)
- Bitwise operations: AND (`&`), OR (`|`), XOR (`^`), NOT (`~`), Left Shift (`<<`), and Right Shift (`>>`)
- Calculation history with timestamps
- Input validation and error handling
- Unit tests for the main calculator components

## Technologies Used

- Python 3
- Python Standard Library
- `ast` for safe arithmetic expression parsing
- `operator` for arithmetic operations
- `dataclasses` for history records
- `datetime` for timestamps
- `unittest` for testing

No external Python packages are required.

## Requirements

- Python 3.9 or newer is recommended.
- VS Code, PyCharm, IDLE, or any other Python-compatible editor can be used.
- A terminal or command prompt.

## Installation

1. Download or clone the project.
2. Open the project folder in a terminal.
3. Check that Python is installed:

```bash
python --version
```

4. Run the calculator:

```bash
python main.py
```

## How to Use

When the program starts, the following main menu is displayed:

```text
============================================================
        PROGRAMMER'S CALCULATOR
============================================================
1. Arithmetic Calculator
2. Number System Converter
3. Bitwise Operations
4. View Calculation History
5. Clear Calculation History
0. Exit
```

Enter the number corresponding to the operation you want to perform.

### 1. Arithmetic Calculator

Select option `1`.

Example:

```text
Enter expression: (10 + 5) * 2
```

Output:

```text
Result = 30
```

Another example:

```text
Enter expression: 2 ** 8
```

Output:

```text
Result = 256
```

### 2. Number System Converter

Select option `2` and choose the source number system:

```text
BIN = Binary
OCT = Octal
DEC = Decimal
HEX = Hexadecimal
```

Example:

```text
Enter source base: HEX
Enter HEX number: FF
```

Output:

```text
Converted Values
------------------------------
BIN  : 11111111
OCT  : 377
DEC  : 255
HEX  : FF
```

### 3. Bitwise Operations

Select option `3`.

Available operations:

```text
1. AND
2. OR
3. XOR
4. NOT
5. LEFT SHIFT
6. RIGHT SHIFT
```

Example:

```text
Choose operation: 1
Enter first integer: 12
Enter second integer: 10
```

Output:

```text
Result = 8
Binary = 1000
Hex    = 8
```

### 4. View Calculation History

Select option `4` to display previous calculations.

Example:

```text
  1. [2026-09-29 20:10:15] Arithmetic   10 + 5 = 15
  2. [2026-09-29 20:11:02] Bitwise      12 & 10 = 8
```

### 5. Clear Calculation History

Select option `5` to remove all stored calculation history.

### 0. Exit

Select option `0` to close the program.

## Error Handling

The program provides user-friendly error messages for common problems, including invalid expressions, division by zero, invalid number-system values, invalid menu choices, invalid bitwise operands, and negative shift counts.

Example:

```text
Error: Division by zero is not allowed.
```

## Testing

The project contains unit tests for arithmetic calculations, number conversion, bitwise operations, and calculation history.

Run the tests from the project root directory with:

```bash
python -m unittest discover -s tests -v
```

## Project Structure

```text
programming_calculator/
│
├── main.py
│
├── calculator/
│   ├── __init__.py
│   ├── arithmetic.py
│   ├── base_converter.py
│   ├── bitwise.py
│   ├── core.py
│   ├── history.py
│   └── validators.py
│
└── tests/
    └── test_calculator.py
```

## Main Modules

- `main.py` - Starts the application.
- `arithmetic.py` - Performs safe arithmetic expression evaluation.
- `base_converter.py` - Converts numbers between BIN, OCT, DEC, and HEX.
- `bitwise.py` - Performs bitwise and shift operations.
- `history.py` - Stores and displays calculation history.
- `validators.py` - Provides input validation helpers.
- `core.py` - Connects the modules and manages the command-line menu.
- `test_calculator.py` - Contains automated unit tests.

## Security and Reliability

The arithmetic calculator parses supported expressions using Python's Abstract Syntax Tree (`ast`) instead of unrestricted `eval()`. This limits arithmetic input to the operations supported by the application.

The application also validates user input and catches common runtime errors so that incorrect input does not unnecessarily terminate the program.

## Future Enhancements

Possible future improvements include:

- Graphical user interface (GUI)
- Scientific calculator functions
- Memory functions such as `M+`, `M-`, `MR`, and `MC`
- Support for binary/hexadecimal arithmetic expressions
- Exporting calculation history to a file
- Keyboard shortcuts
- More comprehensive automated tests

## License

This project is intended for academic and educational use.
