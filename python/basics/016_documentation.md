# 📝 016: Documenting Your Code

Writing code that works is only half the battle. Writing code that others (and your future self!) can understand, use, and maintain is just as important. Good documentation is the key to turning a simple script into a professional, long-lasting piece of software.

In Python, there are two main ways to document your code: **comments** and **docstrings**.

---

## 🎯 Python Documentation: Practical, Tricky, and Fun Usages

```python
# ===== 1. Good vs. Bad Comments =====
# Bad: Restates the obvious
x = x + 1  # Add 1 to x

# Good: Explains the reasoning
# We need to offset the index by 1 to account for the header row.
x = x + 1

# ===== 2. Function Docstring (Google Style) =====
def calculate_average(numbers: list[float]) -> float:
    """Calculates the average of a list of numbers.

    Args:
        numbers: A list of floats or integers.

    Returns:
        The float average of the numbers, or 0.0 if the list is empty.

    Raises:
        TypeError: If the list contains non-numeric types.

    Example:
        >>> calculate_average([1, 2, 3])
        2.0
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

# Accessing docstring
print(calculate_average.__doc__)
help(calculate_average)

# ===== 3. Module Docstring =====
"""This module provides utility functions for data analysis.

Functions:
    - calculate_average(numbers)
    - find_median(numbers)
"""

# ===== 4. Class Docstring =====
class Person:
    """Represents a person.

    Attributes:
        name (str): The person's name.
        age (int): The person's age.
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

# ===== 5. Method Docstring =====
class Calculator:
    def add(self, a, b):
        """Adds two numbers and returns the result.

        Args:
            a (int or float): First number.
            b (int or float): Second number.

        Returns:
            int or float: The sum of a and b.
        """
        return a + b

# ===== 6. Docstring for Exception =====
class CustomError(Exception):
    """Exception raised for custom errors.

    Attributes:
        message (str): Explanation of the error.
    """
    def __init__(self, message):
        self.message = message
        super().__init__(message)

# ===== 7. TODO and FIXME Comments =====
# TODO: Refactor this function for efficiency
# FIXME: Handle edge case when input is None

def buggy_func(x):
    # FIXME: This will fail if x is None
    return x + 1

# ===== 8. Fun: Self-Documenting Code =====
def factorial(n: int) -> int:
    """Returns the factorial of n using recursion."""
    return 1 if n == 0 else n * factorial(n-1)

# ===== 9. NumPy Style Docstring =====
def multiply(a, b):
    """
    Multiply two numbers.

    Parameters
    ----------
    a : int or float
        First number.
    b : int or float
        Second number.

    Returns
    -------
    int or float
        The product of a and b.
    """
    return a * b
```
