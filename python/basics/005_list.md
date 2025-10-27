# 📋 005: Organizing Data with Lists

Lists are one of the most versatile and commonly used data structures in Python. They are your go-to tool for storing a collection of items in a specific order. Think of them as a dynamic, super-powered to-do list or a shopping cart that you can add to, remove from, and rearrange at any time.

---

## 🤔 What Is a List?

A list is an **ordered and changeable (mutable)** collection of items. You create a list by placing items inside square brackets `[]`, separated by commas.

```python
# A list of favorite fruits
fruits = ["apple 🍎", "banana 🍌", "cherry 🍒"]

# A list can hold different data types
mixed_data = ["hello", 42, True, 3.14]

# You can even have a list of lists (a nested list)
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
```

The "ordered" part means that the items have a defined position, and the "mutable" part means you can change the list after it has been created—by adding, removing, or changing items.

## ✨ Why Are Lists So Important?

Lists are the workhorse of Python data structures. You'll use them constantly for:

*   **Storing Collections:** Grouping related items together, like a list of users, sensor readings, or to-do items.
*   **Maintaining Order:** The order of items is preserved, which is crucial for things like step-by-step instructions or a playlist.
*   **Flexibility:** Because they are mutable, you can easily build and modify collections of data on the fly as your program runs.

Whether you're processing data, building a game, or creating a web application, you'll find lists indispensable.

---

## 🚀 How Do I Work with Lists?

Let's get hands-on with the most common list operations.

### 1. Accessing and Slicing

Just like strings, you access list items using their index (starting from 0).

```python
#      0         1         2
fruits = ["apple", "banana", "cherry"]

# Get the first item
first_fruit = fruits[0] # 'apple'

# Get the last item
last_fruit = fruits[-1] # 'cherry'

# Get a "slice" of the list (a sub-list)
some_fruits = fruits[1:3] # ['banana', 'cherry']

print(f"First fruit: {first_fruit}")
print(f"Slice of fruits: {some_fruits}")
```

### 2. Adding and Removing Items

Because lists are mutable, you can easily modify them.

*   **Adding Items:**
    ```python
    # Let's start with a to-do list
    todos = ["learn Python"]
    print(f"Initial todos: {todos}")

    # Add an item to the end
    todos.append("build a project")
    print(f"After append: {todos}")

    # Insert an item at a specific position
    todos.insert(0, "wake up")
    print(f"After insert: {todos}")
    ```

*   **Removing Items:**
    ```python
    # Let's say we've completed a task
    todos.remove("wake up") # Removes the first matching value
    print(f"After remove: {todos}")

    # Or remove an item by its position and get it back
    done_task = todos.pop(0) # Removes the item at index 0
    print(f"I just finished: {done_task}")
    print(f"Remaining todos: {todos}")
    ```

### 3. Sorting and Organizing

You can easily sort and reverse lists.

```python
numbers = [4, 1, 8, 5, 2]
print(f"Original numbers: {numbers}")

# Sort the list in place (modifies the original list)
numbers.sort()
print(f"Sorted numbers: {numbers}")

# Sort in descending order
numbers.sort(reverse=True)
print(f"Reverse sorted numbers: {numbers}")
```

### 4. The Pythonic Way: List Comprehensions

List comprehensions are a concise and elegant way to create lists. They let you combine a `for` loop, an optional `if` condition, and an expression into a single line.

**Standard way:**
```python
squares = []
for i in range(5):
    squares.append(i * i)
# squares is now [0, 1, 4, 9, 16]
```

**With a list comprehension:**
```python
squares = [i * i for i in range(5)]
# squares is also [0, 1, 4, 9, 16] - much cleaner!

# You can even add an if condition
even_squares = [i * i for i in range(10) if i % 2 == 0]
print(f"Squares of even numbers: {even_squares}")
```

Lists are a powerful and flexible tool in your Python arsenal. Get comfortable with them, and you'll be able to handle a wide range of programming tasks!

```python
# 🎯 Python List: Practical, Tricky, and Fun Usages

def list_usages():
    # ===== 1. Basic Creation & Indexing =====
    primes = [2, 3, 5, 7, 11]
    mixed = [42, "Python", 3.14, [1, 0, 1], {'key': 'value'}, (1, 2)]
    
    # Negative indexing and custom slicing
    print(primes[-1])        # 11 (last element)
    print(primes[1:4:2])     # [3, 7] (start:stop:step)
    
    # ===== 2. List Comprehension Magic =====
    squares = [x**2 for x in range(10) if x % 2 == 0]  # [0, 4, 16, 36, 64]
    matrix = [[i*j for j in range(3)] for i in range(3)]  # 3x3 matrix
    
    # Nested comprehension with multiple conditions
    tricky = [x + y for x in [1, 2, 3] if x > 1 for y in [4, 5, 6] if y % 2 == 0]
    # Result: [2+4, 2+6, 3+4, 3+6] → [6, 8, 7, 9]
    
    # ===== 3. Advanced Slicing Techniques =====
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    lst[::2] = ['a', 'a', 'a', 'a', 'a']  # Replace every other element
    # Result: ['a', 1, 'a', 3, 'a', 5, 'a', 7, 'a', 9]
    
    # ===== 4. List Methods Playground =====
    stack = []
    stack.append('A')          # Push
    stack.pop()                # Pop → 'A'
    
    queue = []
    queue.insert(0, 'First')   # Enqueue (inefficient)
    queue.pop()                # Dequeue → 'First'
    
    numbers = [5, 2, 8, 2]
    numbers.extend([1, 3])     # [5, 2, 8, 2, 1, 3]
    numbers.remove(2)          # Remove first occurrence → [5, 8, 2, 1, 3]
    
    # ===== 5. Sorting Tricks =====
    words = ["banana", "pie", "Washington", "book"]
    words.sort(key=lambda x: (-len(x), x))  # Sort by length descending, then alphabetically
    # Result: ['Washington', 'banana', 'book', 'pie']
    
    # ===== 6. Memory Management =====
    original = [[1, 2], [3, 4]]
    shallow = original.copy()
    original[0][0] = 99  # Affects both!
    
    # Deep copy alternative
    import copy
    deep = copy.deepcopy(original)
    
    # ===== 7. Functional Programming =====
    from functools import reduce
    product = reduce(lambda x, y: x * y, [1, 2, 3, 4])  # 24
    filtered = list(filter(lambda x: x > 5, [3, 7, 2, 8]))  # [7, 8]
    
    # ===== 8. Unpacking Tricks =====
    first, *middle, last = [1, 2, 3, 4, 5]  # first=1, middle=[2,3,4], last=5
    combined = [*primes, *mixed]  # Merge lists
    
    # ===== 9. Common Pitfalls =====
    # Mutable default argument
    def risky(value, lst=[]):  # Same list reused!
        lst.append(value)
        return lst
    
    # List references
    a = [1, 2, 3]
    b = a
    b[0] = 99  # Both a and b change!
    
    # ===== 10. Advanced Usages =====
    # Truthy/Falsy values
    checks = [0, 1, [], [0], '', 'a']
    truthy = any(checks)  # True
    falsy = all(checks)   # False
    
    # Zipping and enumerating
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    zipped = list(zip(keys, values))  # [('a',1), ('b',2), ('c',3)]
    
    # ===== 11. Performance Considerations =====
    from collections import deque
    big_list = list(range(10**6))
    
    # Fast pops from both ends
    fast_queue = deque(big_list)
    fast_queue.popleft()  # O(1) vs O(n) for list
    
    # ===== 12. Fun Tricks =====
    # Flatten matrix
    matrix = [[1, 2], [3, 4], [5, 6]]
    flat = [num for row in matrix for num in row]  # [1,2,3,4,5,6]
    
    # Swap values
    a, b = [10], [20]
    a, b = b, a  # Now a=[20], b=[10]
    
    # Create palindrome
    palindrome = [1, 2, 3] + [3, 2, 1][::-1]  # [1,2,3,1,2,3]
    
    # ===== 13. List as Boolean =====
    if []:  # False
        print("Empty list is falsy")
    
    # ===== 14. Type Conversion =====
    chars = list("hello")  # ['h','e','l','l','o']
    unique = list(set([1,2,2,3]))  # [1,2,3]
    
    # ===== 15. Mathematical Operations =====
    sum_total = sum([1, 2, 3])  # 6
    max_val = max([5, 3, 8])    # 8
    
    # ===== 16. Surprising Behaviors =====
    # List multiplication
    surprises = [[]] * 3
    surprises[0].append(1)  # All sublists get 1 → [[1], [1], [1]]
    
    # List identity
    print([] is [])  # False - new list each time
    
    # ===== 17. Conversion Tricks =====
    # List to dictionary
    pairs = [('a', 1), ('b', 2)]
    to_dict = dict(pairs)  # {'a':1, 'b':2}
    
    # List to string
    joined = '|'.join(map(str, [1, 2, 3]))  # "1|2|3"

list_usages()
```
