# 🧩 002: Pattern Matching with `match` and `case`

Introduced in Python 3.10, the `match-case` statement is a powerful feature that acts like a supercharged `if-elif-else` chain. It's designed to handle complex conditional logic in a way that is both readable and efficient, especially when you're working with structured data.

---

## 🎯 Match-Case: Practical, Tricky, and Fun Usages

```python
# ===== 1. Basic Match-Case =====
status = "IN_PROGRESS"
match status:
    case "PENDING" | "QUEUED":
        print("Waiting to be processed.")
    case "IN_PROGRESS":
        print("Task running.")
    case "COMPLETED":
        print("Task finished!")
    case "FAILED":
        print("Task failed.")
    case _:
        print(f"Unknown status: {status}")

# ===== 2. Destructuring Tuples =====
point = (0, 5)
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y-axis at y={y}")
    case (x, 0):
        print(f"X-axis at x={x}")
    case (x, y):
        print(f"Coordinates: ({x}, {y})")
    case _:
        print("Not a valid point")

# ===== 3. Destructuring Lists =====
data = [1, 2, 3]
match data:
    case [1, 2, 3]:
        print("Exact match!")
    case [1, *rest]:
        print(f"Starts with 1, rest: {rest}")
    case _:
        print("No match")

# ===== 4. Matching Dictionaries =====
user = {"name": "Alice", "role": "admin"}
match user:
    case {"role": "admin"}:
        print("User is admin")
    case {"role": role}:
        print(f"User role: {role}")
    case _:
        print("Unknown user")

# ===== 5. Using Guards =====
point = (5, 5)
match point:
    case (x, y) if x == y:
        print(f"On y=x line: ({x}, {y})")
    case (x, y):
        print(f"Coordinates: ({x}, {y})")

# ===== 6. Fun: Command Parser =====
command = ("move", 10, 20)
match command:
    case ("move", x, y):
        print(f"Move to ({x}, {y})")
    case ("draw", shape):
        print(f"Draw {shape}")
    case _:
        print("Unknown command")

# ===== 7. Pattern Matching with Classes =====
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(0, 0)
match p:
    case Point(0, 0):
        print("Class: Origin")
    case Point(x, y):
        print(f"Class: ({x}, {y})")

# ===== 8. Pro-Tips =====
# Use _ as a wildcard/default case
# Use | for OR patterns
# Use guards (if ...) for extra conditions
# Destructure lists, tuples, dicts, and even classes!
```
