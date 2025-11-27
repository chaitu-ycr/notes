# 🧩 010: Creating Reusable Code with Functions

Functions are Python's reusable, named blocks of code. They let you organize logic, avoid repetition, and build modular, maintainable programs. Functions can take parameters, return values, and support flexible argument patterns. Mastering functions is key to writing clean, professional Python code.

## 🎯 Python Function: Practical, Tricky, and Fun Usages

```python
# ===== 1. Basic Definition & Calling =====
def greet(name):
  print(f"Hello, {name}!")
greet("Alice")

# ===== 2. Return Values =====
def add(a, b):
  return a + b
print(add(2, 3))

# ===== 3. Parameters & Arguments =====
def welcome(name="World"):
  print(f"Welcome, {name}!")
welcome()
welcome("Bob")

# ===== 4. Positional, Keyword, Default =====
def show(a, b=10, c=20):
  print(a, b, c)
show(1)
show(1, c=99)

# ===== 5. *args and **kwargs =====
def demo(*args, **kwargs):
  print(args, kwargs)
demo(1, 2, 3, x=4, y=5)

# ===== 6. Multiple Returns & Unpacking =====
def stats(lst):
  return min(lst), max(lst), sum(lst)
lo, hi, total = stats([1, 2, 3])
print(lo, hi, total)

# ===== 7. Nested Functions & Closures =====
def outer(x):
  def inner(y):
    return x + y
  return inner
f = outer(10)
print(f(5))

# ===== 8. Lambda & Anonymous Functions =====
add_one = lambda x: x + 1
print(add_one(7))
print(list(map(lambda x: x**2, [1,2,3])))

# ===== 9. Docstrings & Annotations =====
def foo(x: int) -> int:
  """Returns x squared."""
  return x * x
print(foo.__doc__, foo(4))

# ===== 10. Scope & Globals =====
val = 10
def change():
  global val
  val = 99
change()
print(val)

# ===== 11. Common Pitfalls =====
def risky(val, lst=[]):
  lst.append(val)
  return lst
print(risky(1), risky(2))

# ===== 12. Decorators (Preview) =====
def simple_decorator(fn):
  def wrapper(*args, **kwargs):
    print("Before call")
    result = fn(*args, **kwargs)
    print("After call")
    return result
  return wrapper
@simple_decorator
def hello():
  print("Hello!")
hello()

# ===== 13. Fun Tricks =====
def palindrome(s):
  return s == s[::-1]
print(palindrome("level"))

# Recursive function
def factorial(n):
  return 1 if n==0 else n*factorial(n-1)
print(factorial(5))

# ===== 14. Function as First-Class Citizens =====
def apply_func(f, value):
  return f(value)
print(apply_func(lambda x: x**2, 6))

```
