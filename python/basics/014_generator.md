# ⚡ 014: Simple Iterators with Generators

Generators are Python's elegant way to create memory-efficient, lazy iterators with minimal code. Use generator functions (with yield) or generator expressions for large or infinite sequences, automatic state management, and readable, Pythonic code.

## 🎯 Python Generator: Practical, Tricky, and Fun Usages

```python
# ===== 1. Basic Generator Function =====
def countdown(start):
    print("Generator starting...")
    current = start
    while current > 0:
        yield current
        current -= 1
    print("Generator finished!")
gen = countdown(3)
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))  # ❌ StopIteration

# ===== 2. Generator Expression =====
squares = (x*x for x in range(5))
for sq in squares:
    print(sq)

# ===== 3. Infinite Generator =====
def infinite_counter():
    n = 0
    while True:
        yield n
        n += 1
counter = infinite_counter()
for i in range(3):
    print(next(counter))

# ===== 4. Using Generators in Loops =====
def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
for e in even_numbers(6):
    print(e)

# ===== 5. Send, Throw, Close Methods =====
def echo():
    while True:
        val = yield
        print(f"Received: {val}")
e = echo()
next(e)
e.send("Hello")
e.close()

# ===== 6. Generator Pipeline =====
def gen1():
    for i in range(3):
        yield i

def gen2(source):
    for val in source:
        yield val * 10
for v in gen2(gen1()):
    print(v)

# ===== 7. Fun Tricks =====
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
print(list(fibonacci(7)))

# ===== 8. Generator Pitfalls =====
g = (x for x in range(2))
print(next(g))
print(next(g))
# print(next(g))  # ❌ StopIteration

# ===== 9. Generator vs List Comprehension =====
nums = [x*x for x in range(1000000)]  # Uses lots of memory
nums_gen = (x*x for x in range(1000000))  # Memory efficient
print(next(nums_gen))

# ===== 10. Yield from =====
def subgen():
    yield 1
    yield 2
def main_gen():
    yield from subgen()
    yield 3
for x in main_gen():
    print(x)
```
