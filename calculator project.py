import ast
import operator
import unittest
from dataclasses import dataclass
from datetime import datetime


# Arithmetic Calculator
class ArithmeticCalculator:
    BINARY_OPERATORS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.FloorDiv: operator.floordiv,
        ast.Mod: operator.mod,
        ast.Pow: operator.pow,
    }

    UNARY_OPERATORS = {
        ast.UAdd: operator.pos,
        ast.USub: operator.neg,
    }

    def calculate(self, expression):
        expression = expression.strip()

        if not expression:
            raise ValueError("Expression cannot be empty.")

        try:
            tree = ast.parse(expression, mode="eval")
        except SyntaxError as exc:
            raise ValueError("Invalid arithmetic expression.") from exc

        return self._evaluate(tree.body)

    def _evaluate(self, node):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)) and not isinstance(node.value, bool):
                return node.value

        if isinstance(node, ast.BinOp):
            operator_type = type(node.op)

            if operator_type not in self.BINARY_OPERATORS:
                raise ValueError("Unsupported arithmetic operator.")

            left = self._evaluate(node.left)
            right = self._evaluate(node.right)

            if operator_type in (ast.Div, ast.FloorDiv, ast.Mod) and right == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")

            try:
                return self.BINARY_OPERATORS[operator_type](left, right)
            except OverflowError as exc:
                raise ValueError("The result is too large.") from exc

        if isinstance(node, ast.UnaryOp):
            operator_type = type(node.op)

            if operator_type not in self.UNARY_OPERATORS:
                raise ValueError("Unsupported unary operator.")

            operand = self._evaluate(node.operand)
            return self.UNARY_OPERATORS[operator_type](operand)

        raise ValueError(
            "Unsupported expression. Use numbers, parentheses, +, -, *, /, //, %, and **."
        )


# Number System Converter
class BaseConverter:
    BASES = {
        "BIN": 2,
        "OCT": 8,
        "DEC": 10,
        "HEX": 16,
    }

    def parse(self, value, base_name):
        base_name = base_name.strip().upper()

        if base_name not in self.BASES:
            raise ValueError("Base must be BIN, OCT, DEC, or HEX.")

        value = value.strip()

        if not value:
            raise ValueError("Number cannot be empty.")

        try:
            return int(value, self.BASES[base_name])
        except ValueError as exc:
            raise ValueError(
                f"'{value}' is not valid {base_name} input."
            ) from exc

    def convert(self, value, source_base):
        number = self.parse(value, source_base)
        return self.format_all(number)

    def format_all(self, number):
        if not isinstance(number, int):
            raise TypeError("Number-system conversion requires an integer.")

        return {
            "BIN": format(number, "b"),
            "OCT": format(number, "o"),
            "DEC": str(number),
            "HEX": format(number, "X"),
        }


# Bitwise Calculator
class BitwiseCalculator:
    def _validate(self, a, b=None):
        if not isinstance(a, int) or isinstance(a, bool):
            raise TypeError("Bitwise operations require integer operands.")

        if b is not None:
            if not isinstance(b, int) or isinstance(b, bool):
                raise TypeError("Bitwise operations require integer operands.")

    def and_operation(self, a, b):
        self._validate(a, b)
        return a & b

    def or_operation(self, a, b):
        self._validate(a, b)
        return a | b

    def xor_operation(self, a, b):
        self._validate(a, b)
        return a ^ b

    def not_operation(self, a):
        self._validate(a)
        return ~a

    def left_shift(self, a, positions):
        self._validate(a, positions)

        if positions < 0:
            raise ValueError("Shift count cannot be negative.")

        return a << positions

    def right_shift(self, a, positions):
        self._validate(a, positions)

        if positions < 0:
            raise ValueError("Shift count cannot be negative.")

        return a >> positions


# History Manager
@dataclass
class HistoryEntry:
    timestamp: str
    category: str
    operation: str
    result: str


class HistoryManager:
    def __init__(self, max_entries=100):
        self.max_entries = max_entries
        self.entries = []

    def add(self, category, operation, result):
        entry = HistoryEntry(
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            category=category,
            operation=operation,
            result=str(result),
        )

        self.entries.append(entry)
        self.entries = self.entries[-self.max_entries:]

    def clear(self):
        self.entries.clear()

    def get_entries(self):
        return list(self.entries)

    def display(self):
        if not self.entries:
            print("\nNo calculation history yet.")
            return

        print("\n" + "=" * 75)
        print("CALCULATION HISTORY")
        print("=" * 75)

        for index, entry in enumerate(self.entries, start=1):
            print(
                f"{index:>3}. "
                f"[{entry.timestamp}] "
                f"{entry.category:<12} "
                f"{entry.operation} = {entry.result}"
            )


# Validators
def read_integer(prompt, base_name="DEC"):
    converter = BaseConverter()
    value = input(prompt)
    return converter.parse(value, base_name)


def read_choice(prompt, valid_choices):
    value = input(prompt).strip().upper()

    if value not in valid_choices:
        choices = ", ".join(sorted(valid_choices))
        raise ValueError(f"Choose one of: {choices}.")

    return value


# Main Programming Calculator
class ProgrammingCalculator:
    def __init__(self):
        self.arithmetic = ArithmeticCalculator()
        self.converter = BaseConverter()
        self.bitwise = BitwiseCalculator()
        self.history = HistoryManager()

    def arithmetic_menu(self):
        print("\n" + "-" * 60)
        print("ARITHMETIC CALCULATOR")
        print("-" * 60)
        print("Supported operators: +  -  *  /  //  %  **")
        print("Parentheses are also supported.")

        expression = input("\nEnter expression: ")

        result = self.arithmetic.calculate(expression)

        print(f"\nResult = {result}")

        self.history.add(
            "Arithmetic",
            expression,
            result
        )

    def conversion_menu(self):
        print("\n" + "-" * 60)
        print("NUMBER SYSTEM CONVERTER")
        print("-" * 60)
        print("BIN = Binary")
        print("OCT = Octal")
        print("DEC = Decimal")
        print("HEX = Hexadecimal")

        source = input("\nEnter source base: ").strip().upper()

        if source not in {"BIN", "OCT", "DEC", "HEX"}:
            raise ValueError("Invalid base. Use BIN, OCT, DEC or HEX.")

        value = input(f"Enter {source} number: ").strip()

        result = self.converter.convert(value, source)

        print("\nConverted Values")
        print("-" * 30)

        for base, converted in result.items():
            print(f"{base:<5}: {converted}")

        self.history.add(
            "Conversion",
            f"{source} {value}",
            result
        )

    def bitwise_menu(self):
        print("\n" + "-" * 60)
        print("BITWISE OPERATIONS")
        print("-" * 60)

        print("1. AND")
        print("2. OR")
        print("3. XOR")
        print("4. NOT")
        print("5. LEFT SHIFT")
        print("6. RIGHT SHIFT")

        choice = input("\nChoose operation: ").strip()

        if choice not in {"1", "2", "3", "4", "5", "6"}:
            raise ValueError("Invalid bitwise operation.")

        if choice == "1":
            a = int(input("Enter first integer: "))
            b = int(input("Enter second integer: "))
            result = self.bitwise.and_operation(a, b)
            operation = f"{a} & {b}"

        elif choice == "2":
            a = int(input("Enter first integer: "))
            b = int(input("Enter second integer: "))
            result = self.bitwise.or_operation(a, b)
            operation = f"{a} | {b}"

        elif choice == "3":
            a = int(input("Enter first integer: "))
            b = int(input("Enter second integer: "))
            result = self.bitwise.xor_operation(a, b)
            operation = f"{a} ^ {b}"

        elif choice == "4":
            a = int(input("Enter integer: "))
            result = self.bitwise.not_operation(a)
            operation = f"~{a}"

        elif choice == "5":
            a = int(input("Enter integer: "))
            positions = int(input("Enter number of positions: "))
            result = self.bitwise.left_shift(a, positions)
            operation = f"{a} << {positions}"

        else:
            a = int(input("Enter integer: "))
            positions = int(input("Enter number of positions: "))
            result = self.bitwise.right_shift(a, positions)
            operation = f"{a} >> {positions}"

        print(f"\nResult = {result}")

        if result >= 0:
            binary = format(result, "b")
            hexadecimal = format(result, "X")
        else:
            binary = "-" + format(abs(result), "b")
            hexadecimal = "-" + format(abs(result), "X")

        print(f"Binary = {binary}")
        print(f"Hex    = {hexadecimal}")

        self.history.add(
            "Bitwise",
            operation,
            result
        )

    def run(self):
        while True:
            print("\n")
            print("=" * 60)
            print("        PROGRAMMER'S CALCULATOR")
            print("=" * 60)
            print("1. Arithmetic Calculator")
            print("2. Number System Converter")
            print("3. Bitwise Operations")
            print("4. View Calculation History")
            print("5. Clear Calculation History")
            print("0. Exit")

            choice = input("\nEnter your choice: ").strip()

            try:
                if choice == "1":
                    self.arithmetic_menu()

                elif choice == "2":
                    self.conversion_menu()

                elif choice == "3":
                    self.bitwise_menu()

                elif choice == "4":
                    self.history.display()

                elif choice == "5":
                    self.history.clear()
                    print("\nCalculation history cleared successfully.")

                elif choice == "0":
                    print("\nThank you for using Programmer's Calculator!")
                    break

                else:
                    print("\nError: Please enter a valid menu option.")

            except ZeroDivisionError as error:
                print(f"\nError: {error}")

            except (ValueError, TypeError) as error:
                print(f"\nError: {error}")

            except KeyboardInterrupt:
                print("\n\nProgram interrupted by user.")
                break


# Unit Tests
class TestArithmeticCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = ArithmeticCalculator()

    def test_addition_and_multiplication(self):
        result = self.calculator.calculate("2 + 3 * 4")
        self.assertEqual(result, 14)

    def test_parentheses(self):
        result = self.calculator.calculate("(2 + 3) * 4")
        self.assertEqual(result, 20)

    def test_power(self):
        result = self.calculator.calculate("2 ** 5")
        self.assertEqual(result, 32)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.calculate("10 / 0")

    def test_invalid_expression(self):
        with self.assertRaises(ValueError):
            self.calculator.calculate("2 + abc")


class TestBaseConverter(unittest.TestCase):
    def setUp(self):
        self.converter = BaseConverter()

    def test_hexadecimal_to_decimal(self):
        result = self.converter.parse("FF", "HEX")
        self.assertEqual(result, 255)

    def test_binary_to_decimal(self):
        result = self.converter.parse("1010", "BIN")
        self.assertEqual(result, 10)

    def test_decimal_to_all(self):
        result = self.converter.convert("255", "DEC")

        expected = {
            "BIN": "11111111",
            "OCT": "377",
            "DEC": "255",
            "HEX": "FF"
        }

        self.assertEqual(result, expected)

    def test_invalid_binary(self):
        with self.assertRaises(ValueError):
            self.converter.parse("102", "BIN")


class TestBitwiseCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = BitwiseCalculator()

    def test_and(self):
        result = self.calculator.and_operation(12, 10)
        self.assertEqual(result, 8)

    def test_or(self):
        result = self.calculator.or_operation(12, 10)
        self.assertEqual(result, 14)

    def test_xor(self):
        result = self.calculator.xor_operation(12, 10)
        self.assertEqual(result, 6)

    def test_not(self):
        result = self.calculator.not_operation(5)
        self.assertEqual(result, ~5)

    def test_left_shift(self):
        result = self.calculator.left_shift(4, 2)
        self.assertEqual(result, 16)

    def test_right_shift(self):
        result = self.calculator.right_shift(16, 2)
        self.assertEqual(result, 4)


class TestHistoryManager(unittest.TestCase):
    def test_add_and_clear(self):
        history = HistoryManager()

        history.add(
            "Arithmetic",
            "2 + 2",
            4
        )

        self.assertEqual(
            len(history.get_entries()),
            1
        )

        history.clear()

        self.assertEqual(
            len(history.get_entries()),
            0
        )


if __name__ == "__main__":
    calculator = ProgrammingCalculator()
    calculator.run()