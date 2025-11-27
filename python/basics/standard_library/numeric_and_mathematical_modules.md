# Python Numeric and Mathematical Modules

Below are detailed descriptions and usage examples for key Python standard libraries related to numeric and mathematical operations.

---

## numbers — Numeric Abstract Base Classes

**Description:**  
Defines abstract base classes for numeric types, useful for type checking and custom numeric implementations.

**Usage Example:**
```python
import numbers

print(isinstance(5, numbers.Integral))  # True
print(isinstance(3.14, numbers.Real))   # True
```

---

## math — Mathematical Functions

**Description:**  
Provides mathematical functions like trigonometry, logarithms, and constants.

**Usage Example:**
```python
import math

print(math.sqrt(16))      # 4.0
print(math.pi)            # 3.141592653589793
```

---

## cmath — Mathematical Functions for Complex Numbers

**Description:**  
Supplies mathematical functions for complex numbers.

**Usage Example:**
```python
import cmath

z = complex(1, 2)
print(cmath.polar(z))     # (2.23606797749979, 1.1071487177940904)
```

---

## decimal — Decimal Fixed-Point and Floating-Point Arithmetic

**Description:**  
Implements decimal floating-point arithmetic with more precision and control than the built-in float.

**Usage Example:**
```python
from decimal import Decimal, getcontext

getcontext().prec = 4
d = Decimal('1.2345') * Decimal('6.789')
print(d)  # 8.380
```

---

## fractions — Rational Numbers

**Description:**  
Supports rational number arithmetic using fractions.

**Usage Example:**
```python
from fractions import Fraction

f = Fraction(3, 4) + Fraction(1, 2)
print(f)  # 5/4
```

---

## random — Generate Pseudo-Random Numbers

**Description:**  
Generates pseudo-random numbers for various distributions and operations.

**Usage Example:**
```python
import random

print(random.randint(1, 10))      # Random integer between 1 and 10
print(random.choice(['a', 'b']))  # Randomly selects 'a' or 'b'
```

---

## statistics — Mathematical Statistics Functions

**Description:**  
Provides functions for calculating mathematical statistics of numeric data.

**Usage Example:**
```python
import statistics

data = [1, 2, 3, 4, 5]
print(statistics.mean(data))   # 3
print(statistics.median(data)) # 3
```

---
