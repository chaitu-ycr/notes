# 🛡️ 012: Error and Exception Handling

No matter how good a programmer you are, things can go wrong. Exception handling is your safety net for building robust, user-friendly, and reliable Python programs. Use try/except/else/finally to catch errors, clean up resources, and provide helpful feedback. Raising your own exceptions lets you signal problems in your logic.

## 🎯 Python Error & Exception Handling: Practical, Tricky, and Fun Usages

```python
# ===== 1. Basic try/except =====
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ValueError:
    print("Not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# ===== 2. Catching Multiple Exceptions =====
try:
    y = int("abc")
except (ValueError, TypeError) as e:
    print(f"Error: {e}")

# ===== 3. else and finally =====
f = None
try:
    f = open("my_file.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("File not found!")
else:
    print("File read successfully!")
finally:
    if f:
        f.close()
    print("Cleanup done.")

# ===== 4. Raising Exceptions =====
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age > 120:
        raise ValueError("Age seems unlikely.")
    print(f"Age set to {age}")
try:
    set_age(-5)
except ValueError as e:
    print(f"Custom error: {e}")

# ===== 5. Custom Exception Classes =====
class MyError(Exception):
    pass
try:
    raise MyError("Something went wrong!")
except MyError as e:
    print(e)

# ===== 6. Exception Chaining =====
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise RuntimeError("Division failed") from e
try:
    divide(1, 0)
except RuntimeError as e:
    print(e)

# ===== 7. Common Pitfalls =====
try:
    print(1/0)
except:
    print("Caught everything (not recommended)")

# ===== 8. Fun Tricks =====
try:
    import math
    print(math.sqrt(-1))
except Exception as e:
    print(type(e), e)

# ===== 9. Assertions =====
def check_positive(x):
    assert x > 0, "x must be positive!"
try:
    check_positive(-1)
except AssertionError as e:
    print(e)

# ===== 10. Context Managers & Resource Handling =====
try:
    with open("my_file.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File missing!")
```
