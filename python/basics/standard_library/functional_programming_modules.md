# Python Functional Programming Modules

Below are detailed descriptions and usage examples for key Python standard libraries related to functional programming.

---

## itertools — Functions Creating Iterators for Efficient Looping

**Description:**  
Provides building blocks for constructing iterators for efficient looping, such as infinite iterators, combinatoric generators, and more.

**Usage Example:**
```python
import itertools

# Create an iterator that returns consecutive numbers starting from 10
counter = itertools.count(10)
print(next(counter))  # 10
print(next(counter))  # 11

# Chain multiple iterables together
for item in itertools.chain([1, 2], ['a', 'b']):
	print(item)
# Output: 1 2 a b
```

---

## functools — Higher-Order Functions and Operations on Callable Objects

**Description:**  
Provides tools for higher-order functions, such as decorators, partial function application, and caching.

**Usage Example:**
```python
import functools

# Create a function that multiplies by 2
def multiply(x, y):
	return x * y

double = functools.partial(multiply, 2)
print(double(5))  # 10

# Use lru_cache to cache function results
@functools.lru_cache(maxsize=128)
def fib(n):
	if n < 2:
		return n
	return fib(n-1) + fib(n-2)

print(fib(10))  # 55
```

---

## operator — Standard Operators as Functions

**Description:**  
Implements standard operators as functions, allowing them to be passed as arguments to higher-order functions.

**Usage Example:**
```python
import operator

print(operator.add(2, 3))      # 5
print(operator.mul(4, 5))      # 20

lst = [1, 2, 3]
print(list(map(operator.neg, lst)))  # [-1, -2, -3]
```

---
