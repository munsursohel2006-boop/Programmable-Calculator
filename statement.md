# Programmer's Calculator — Project Statement

## Overview

This project implements a command-line **Programmer's Calculator** in Python. It combines arithmetic calculations, number-system conversion, bitwise operations, and calculation-history management in one interactive application.

## Features

### 1. Arithmetic Calculator
- Supports `+`, `-`, `*`, `/`, `//`, `%`, and `**`.
- Supports parentheses.
- Uses Python's `ast` module to safely parse arithmetic expressions.
- Rejects unsupported expressions and invalid input.
- Handles division by zero and arithmetic overflow errors.

### 2. Number System Converter
Converts integer values among:
- Binary (`BIN`)
- Octal (`OCT`)
- Decimal (`DEC`)
- Hexadecimal (`HEX`)

The converter validates the selected base and the entered number before conversion.

### 3. Bitwise Operations
The calculator supports:
- AND (`&`)
- OR (`|`)
- XOR (`^`)
- NOT (`~`)
- Left shift (`<<`)
- Right shift (`>>`)

Integer operands are validated, and negative shift counts are rejected.

### 4. Calculation History
The application records:
- Timestamp
- Category
- Operation
- Result

The history is limited to the most recent 100 entries by default. Users can view or clear the stored history.

### 5. Interactive Menu
The main menu provides access to:
1. Arithmetic Calculator
2. Number System Converter
3. Bitwise Operations
4. View Calculation History
5. Clear Calculation History
0. Exit

## Validation and Error Handling

The program validates user input and reports errors for cases such as:
- Empty expressions
- Invalid arithmetic expressions
- Unsupported operators or expressions
- Invalid number-system bases
- Invalid numbers for a selected base
- Division by zero
- Invalid bitwise operands
- Negative shift counts
- Invalid menu choices

## Testing

The project includes unit tests using Python's `unittest` framework. Tests cover arithmetic calculations, parentheses, powers, division-by-zero handling, invalid expressions, number-system conversion, invalid binary input, bitwise operations, and history management.

## Main Classes

- `ArithmeticCalculator` — evaluates supported arithmetic expressions.
- `BaseConverter` — parses and converts numbers between supported bases.
- `BitwiseCalculator` — performs integer bitwise operations.
- `HistoryEntry` — stores one history record.
- `HistoryManager` — manages calculation history.
- `ProgrammingCalculator` — integrates all components and provides the interactive interface.

## Technology

- **Language:** Python
- **Standard libraries:** `ast`, `operator`, `unittest`, `dataclasses`, `datetime`

## Purpose

The purpose of this project is to provide a simple, modular programming calculator while demonstrating expression parsing, number-system conversion, bitwise computation, input validation, exception handling, object-oriented design, history management, and unit testing.
