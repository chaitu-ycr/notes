# 🚦 001: Making Decisions with `if`, `elif`, and `else`

Computers are great at following instructions, but they're even more powerful when they can make decisions. This is where Python's `if`, `elif`, and `else` statements come in. They are the tools you'll use to control the flow of your programs.

---

## 🎯 If-Elif-Else: Practical, Tricky, and Fun Usages

```python
# ===== 1. Basic If-Elif-Else =====
x = 10
if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but not more than 15")
else:
    print("x is 5 or less")

# ===== 2. Multiple Elif =====
score = 72
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# ===== 3. Nested If Statements =====
age = 20
has_license = False
if age >= 18:
    print("Old enough to drive.")
    if has_license:
        print("You can drive!")
    else:
        print("Get a license first.")
else:
    print("Too young to drive.")

# ===== 4. One-Liner If-Else (Ternary) =====
status = "adult" if age >= 18 else "minor"
print(status)

# ===== 5. Checking Multiple Conditions =====
a, b = 5, 10
if a < 10 and b > 5:
    print("Both conditions are True!")

# ===== 6. Fun: FizzBuzz =====
for i in range(1, 16):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# ===== 7. Using If with Input =====
user = input("Enter your name: ")
if user:
    print(f"Hello, {user}!")
else:
    print("No name entered.")

# ===== 8. Pro-Tips =====
# Don't forget the colon!
# Indentation matters!
# Use == for comparison, = for assignment.

# ===== 9. Trick: Chained Comparisons =====
y = 7
if 5 < y < 10:
    print("y is between 5 and 10")
```
