---
title: "Python Q/A"
aliases:
  - "Python Q/A"
---
# Python Q/A

## 🔗 Related topics

- [Python basics](../basics/readme.md) — foundational language concepts that support the Q&A exercises
- [Python use cases](../usecases/readme.md) — practical applications such as CAN tooling and automation
- [Testing](../../testing/testing.md) — Python is a common language for unit tests and QA automation
- [GitHub Actions](../../github_actions/github_actions.md) — CI jobs often run Python validators and test suites
- [CAN](../../can/can.md) — Python is heavily used for CAN parsing, diagnostics, and analysis tooling

This note complements the rest of the Python learning track. Use it after the basics to reinforce concepts and before diving into automotive-oriented Python libraries.

## 1. Python Data Structures

### Tuple

**Q: What is a `tuple`? How is it different from a `list`?**  
A tuple is an immutable, ordered collection of items in Python. Unlike lists, tuples cannot be changed after creation (no add, remove, or update operations).  
Example:  
```python
my_tuple = (1, 2, 3)
my_list = [1, 2, 3]
# my_tuple[0] = 10  # Raises TypeError
my_list[0] = 10     # This works
```

**Q: Create a tuple with mixed data types.**  
```python
mixed_tuple = (1, "hello", 3.14, True)
print(mixed_tuple)  # Output: (1, 'hello', 3.14, True)
```

**Q: How do you check if an item exists in a tuple?**  
Use the `in` keyword.  
```python
t = (1, 2, 3)
print(2 in t)    # Output: True
print(5 in t)    # Output: False
```

**Q: Can you modify a tuple after creation? Why or why not?**  
No, tuples are immutable.  
```python
t = (1, 2, 3)
# t[0] = 10  # Raises TypeError
```

**Q: How do you concatenate two tuples?**  
Use the `+` operator.  
```python
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print(t3)  # Output: (1, 2, 3, 4)
```

**Q: Give an example of tuple unpacking.**  
```python
point = (10, 20)
x, y = point
print(x)  # Output: 10
print(y)  # Output: 20

# Extended unpacking
a, *b = (1, 2, 3, 4)
print(a)  # Output: 1
print(b)  # Output: [2, 3, 4]
```

### Set

**Q: What is a `set`? How is it different from a `list` and a `tuple`?**  
A set is an unordered collection of unique, immutable elements. Sets do not allow duplicates and do not maintain order.  
```python
my_set = {1, 2, 3}
my_list = [1, 2, 2, 3]
my_tuple = (1, 2, 3)
print(my_set)   # Output: {1, 2, 3}
print(my_list)  # Output: [1, 2, 2, 3]
print(my_tuple) # Output: (1, 2, 3)
```

**Q: Create a set with unique elements.**  
```python
unique_set = {1, 2, 3, 4, 4, 5}
print(unique_set)  # Output: {1, 2, 3, 4, 5}
```

**Q: Demonstrate adding, removing, updating, and merging sets.**  
```python
s = {1, 2, 3}
s.add(4)            # Add
s.remove(2)         # Remove
s.update([5, 6])    # Update with multiple elements
s2 = {6, 7}
merged = s.union(s2)  # Merge (union)
print(s)             # Output: {1, 3, 4, 5, 6}
print(merged)        # Output: {1, 3, 4, 5, 6, 7}
```

**Q: How do you check if an item exists in a set?**  
Use `in`.  
```python
s = {1, 2, 3}
print(2 in s)    # Output: True
print(5 in s)    # Output: False
```

**Q: Write a set comprehension to generate all even numbers from 1 to 20.**  
```python
evens = {x for x in range(1, 21) if x % 2 == 0}
print(evens)  # Output: {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
```

**Q: How do you find the intersection and union of two sets?**  
Use `&` or `intersection()` for intersection, `|` or `union()` for union.  
```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a & b)                # Output: {3, 4}
print(a.intersection(b))    # Output: {3, 4}
print(a | b)                # Output: {1, 2, 3, 4, 5, 6}
print(a.union(b))           # Output: {1, 2, 3, 4, 5, 6}
```

### String

**Q: What is a `string` in Python?**  
A string is an immutable sequence of Unicode characters, used to store and manipulate text data. Strings are defined using single, double, or triple quotes.

**Q: Create a string variable and demonstrate string concatenation.**  
```python
s1 = "Hello"
s2 = "World"
result = s1 + " " + s2
print(result)  # Output: Hello World
```

**Q: How do you join a list of strings into a single string?**  
Use `join()`.  
```python
words = ['Python', 'is', 'fun']
sentence = ' '.join(words)
print(sentence)  # Output: Python is fun
```

**Q: How do you search for a substring in a string?**  
Use `in`, `find()`, or `index()`.  
```python
text = "Hello, Python!"
print("Python" in text)        # Output: True
print(text.find("Python"))     # Output: 7
print(text.index("Python"))    # Output: 7
```

**Q: How do you split a string by a delimiter?**  
Use `split()`.  
```python
data = "apple,banana,cherry"
fruits = data.split(',')
print(fruits)  # Output: ['apple', 'banana', 'cherry']
```

**Q: How do you replace characters or words in a string?**  
Use `replace()`.  
```python
text = "I like apples"
new_text = text.replace("apples", "bananas")
print(new_text)  # Output: I like bananas
```

**Q: Explain string formatting with examples (`f-string`, `format()`, `%` operator).**  
- **f-string (Python 3.6+):**  
    ```python
    name = "Alice"
    age = 30
    print(f"My name is {name} and I am {age} years old.")
    # Output: My name is Alice and I am 30 years old.
    ```
- **`format()` method:**  
    ```python
    print("My name is {} and I am {} years old.".format(name, age))
    # Output: My name is Alice and I am 30 years old.
    ```
- **`%` operator:**  
    ```python
    print("My name is %s and I am %d years old." % (name, age))
    # Output: My name is Alice and I am 30 years old.
    ```

**Q: How do you reverse a string?**  
Use slicing with a step of `-1`.  
```python
s = "Python"
reversed_s = s[::-1]
print(reversed_s)  # Output: nohtyP
```

**Q: How do you check if a string is a palindrome?**  
Compare the string to its reverse.  
```python
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))  # Output: True
print(is_palindrome("hello"))  # Output: False
```
## 2. Functions and Modules

### Functions

**Q: How do you define a function in Python?**  
Use the `def` keyword, followed by the function name and parentheses.  
Example:  
```python
def greet():
    print("Hello!")
```

**Q: Write a function that returns the square of a number.**  
```python
def square(x):
    return x * x

print(square(5))  # Output: 25
```

**Q: What is the difference between `*args` and `**kwargs`?**  
- `*args` collects extra positional arguments as a tuple.  
- `**kwargs` collects extra keyword arguments as a dictionary.  
Example:  
```python
def demo(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

demo(1, 2, three=3, four=4)
# Output:
# args: (1, 2)
# kwargs: {'three': 3, 'four': 4}
```

**Q: What is a lambda function? Give an example.**  
A lambda function is an anonymous, single-expression function defined with the `lambda` keyword.  
```python
square = lambda x: x * x
print(square(4))  # Output: 16
```

**Q: How do you create and import a module?**  
To create a module, save Python code in a `.py` file (e.g., `mymodule.py`).  
To import it, use the `import` statement.

Example (`mymodule.py`):
```python
def greet(name):
    print(f"Hello, {name}!")
```
Usage in another file:
```python
import mymodule
mymodule.greet("Alice")  # Output: Hello, Alice!
```

**Q: How do you import specific functions from a module?**  
Use the `from ... import ...` syntax.  
```python
from math import sqrt, pi
print(sqrt(16))  # Output: 4.0
print(pi)        # Output: 3.141592653589793
```

**Q: What is the difference between a module and a package?**  
- A **module** is a single Python file (`.py`) containing code.
- A **package** is a directory containing multiple modules and an `__init__.py` file (can be empty), allowing hierarchical organization of modules.

Example structure:
```
mypackage/
    __init__.py
    module1.py
    module2.py
```
Usage:
```python
from mypackage import module1
```

## 3. Object-Oriented Programming

### Classes and Objects

**Q: What is a class? What is an object?**  
A class is a blueprint for creating objects (instances) in Python. It defines attributes (data) and methods (functions) that describe the behavior of the objects.  
An object is an instance of a class, containing real values for the attributes defined by the class.

**Q: Write a class with attributes and methods. How do you create and use an object?**  
Example:
```python
class Person:
    def __init__(self, name, age):
        self.name = name      # attribute
        self.age = age        # attribute

    def greet(self):          # method
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

p = Person("Alice", 30)  # create object
p.greet()                # Output: Hello, my name is Alice and I am 30 years old.
print(p.name)            # Output: Alice
print(p.age)             # Output: 30
```

**Q: What is inheritance? How do you inherit from a class? Give an example.**  
Inheritance allows a class (child/derived) to inherit attributes and methods from another class (parent/base).  
Example:
```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        print("Woof!")

a = Animal()
a.speak()  # Output: Animal speaks

d = Dog()
d.speak()  # Output: Woof!
```

**Q: What is a class variable vs. an instance variable?**  
- A **class variable** is shared by all instances of the class.
- An **instance variable** is unique to each object.

Example:
```python
class Counter:
    count = 0  # class variable

    def __init__(self):
        Counter.count += 1
        self.id = Counter.count  # instance variable

a = Counter()
b = Counter()
print(a.id)        # Output: 1
print(b.id)        # Output: 2
print(Counter.count)  # Output: 2
```

**Q: How do you read, write, and append data to a text file?**  
Use the built-in `open()` function with appropriate modes:  
```python
# Write to a file
with open('example.txt', 'w') as f:
    f.write('Hello, World!\n')

# Read from a file
with open('example.txt', 'r') as f:
    content = f.read()
    print(content)  # Output: Hello, World!

# Append to a file
with open('example.txt', 'a') as f:
    f.write('Appended line.\n')
```

**Q: How do you handle exceptions when working with files?**  
Use `try-except` blocks to catch exceptions like `FileNotFoundError` or `IOError`:  
```python
try:
    with open('nonexistent.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("File not found.")
except IOError as e:
    print(f"IO error occurred: {e}")
```

**Q: What is threading? When should you use it?**  
- Threading allows concurrent execution of multiple parts of a program (threads).
- Use threading for I/O-bound tasks like file I/O, network operations, or waiting for user input in parallel.

**Q: What is the output of the following code?**
```python
for i in range(len(animals)):
    animals[i] = animals[i].upper()
print(animals)
```
**A:**  
This code updates each element in the list to its uppercase version.  
**Output:**  
```
['CAT', 'DOG']
```

**Q: What is the output of the following code?**
```python
i = 6
while True:
    if i % 4 == 0:
        break
    print(i)
    i -= 2
```
**A:**  
- First iteration: `i = 6`, `6 % 4 = 2` (not 0), so print 6, then `i = 4`
- Second iteration: `i = 4`, `4 % 4 = 0`, so break

**Output:**  
```
6
```

**Q: Write code to print each character in a word entered by the user.**
```python
word = input("Enter a word: ")
for char in word:
    print(char)
```

**Q: What is the output of the following code?**
```python
for item in ('a', 'b', 'c', 'd'):
    print(item)
    if item == 'c':
        break
    continue
```
**A:**  
The loop prints each item. When `item` is `'c'`, it breaks out of the loop.  
**Output:**  
```
a
b
c
```

**Q: What is the output of the following code?**
```python
i = j = 10
if i > j:
    print('i is greater than j')
elif i <= j:
    print('i is smaller than j')
else:
    print('both i and j are equal')
```
**A:**  
Since `i` and `j` are both 10, `i <= j` is `True`, so it prints:  
```
i is smaller than j
```
*Note: The logic is misleading; the message should be "i is smaller than or equal to j".*

**Q: What is the output of the following code?**
```python
i = 2
j = 16
minimum_val = i < j and i or j
print(minimum_val)
```
**A:**  
`i < j` is `True`, so `minimum_val` is set to `i` (which is 2).  
**Output:**  
```
2
```
*Note: This is a common Python 2 idiom for a ternary operation, but for clarity, use `i if i < j else j` in modern code.*

**Q: What is the output of the following code?**
```python
a = 0
b = 9
i = [True, False][a > b]
print(i)
```
**A:**  
`a > b` is `False` (which is 0), so `i = [True, False][0]` → `True`.  
**Output:**  
```
True
```

**Q: What are the two major loop statements in Python?**  
- `for` loop: Iterates over a sequence (like list, tuple, string).
- `while` loop: Repeats as long as a condition is `True`.

**Q: How do you use a ternary operator in Python?**  
The ternary operator is written as:  
```python
result = a if condition else b
```
Example:  
```python
x = 5
parity = "Even" if x % 2 == 0 else "Odd"
print(parity)  # Output: Odd
```

**Q: How many `except` statements can a `try-except` block have?**  
A `try` block can have multiple `except` clauses to handle different exception types:
```python
try:
    # some code
except ValueError:
    print("Value error")
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print("Other exception:", e)
```
Only one matching `except` block will execute per exception.

**Q: What is the output of the following code?**
```python
def foo():
    try:
        print(1)
    finally:
        print(2)
foo()
```
**A:**  
The `try` block prints `1`, then `finally` prints `2`.  
**Output:**  
```
1
2
```

**Q: What is the difference between `Exception` and `BaseException`?**  
- `BaseException` is the base class for all built-in exceptions.
- `Exception` is the base class for most user-defined and built-in exceptions, but not for system-exiting exceptions like `SystemExit`, `KeyboardInterrupt`, etc., which inherit directly from `BaseException`.
```python
issubclass(Exception, BaseException)  # True
issubclass(SystemExit, BaseException) # True
issubclass(SystemExit, Exception)     # False
```

**Q: How do you use `else` and `finally` with `try-except` blocks?**  
- The `else` block runs if no exception occurs in the `try` block.
- The `finally` block always runs, whether or not an exception occurred.
```python
try:
    print("Try block")
except Exception:
    print("Exception occurred")
else:
    print("No exception")
finally:
    print("Always runs")
```
**Output:**
```
Try block
No exception
Always runs
```

### Decorators

**Q: What is a decorator? Give an example.**  
A decorator is a function that takes another function and extends or modifies its behavior without changing its code. Decorators are commonly used for logging, access control, and timing.

Example:
```python
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function call
# Hello!
# After function call
```

### enumerate() and zip()

**Q: How do you use `enumerate()` and `zip()`?**  
- `enumerate()` adds a counter to an iterable and returns pairs of (index, value).
- `zip()` combines multiple iterables into tuples of corresponding elements.

Examples:
```python
# enumerate
fruits = ['apple', 'banana', 'cherry']
for idx, fruit in enumerate(fruits):
    print(idx, fruit)
# Output:
# 0 apple
# 1 banana
# 2 cherry

# zip
names = ['Alice', 'Bob']
scores = [85, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
# Output:
# Alice: 85
# Bob: 92
```

### Global Interpreter Lock (GIL)

**Q: What is the Global Interpreter Lock (GIL)?**  
The Global Interpreter Lock (GIL) is a mutex in CPython (the standard Python implementation) that allows only one thread to execute Python bytecode at a time. This limits multi-threaded programs from fully utilizing multiple CPU cores for CPU-bound tasks, but I/O-bound tasks can still benefit from threading.



