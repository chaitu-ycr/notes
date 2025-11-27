# 🌀 013: The Iterator Protocol

The iterator protocol powers Python's for loops, memory efficiency, and lazy evaluation. Iterables can be looped over; iterators produce items one at a time. Mastering iterators lets you process huge data, build custom sequences, and write elegant, Pythonic code.

## 🎯 Python Iterator: Practical, Tricky, and Fun Usages

```python
# ===== 1. Basic Iteration =====
lst = [1, 2, 3]
for x in lst:
    print(x)

# ===== 2. Manual Iteration =====
it = iter(lst)
print(next(it))
print(next(it))
print(next(it))
# print(next(it))  # ❌ StopIteration

# ===== 3. Custom Iterator Class =====
class Countdown:
    def __init__(self, start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1
for n in Countdown(3):
    print(n)

# ===== 4. Iterating Strings, Dicts, Files =====
for c in "abc":
    print(c)
d = {'a': 1, 'b': 2}
for k in d:
    print(k, d[k])
# with open('file.txt') as f:
#     for line in f:
#         print(line)

# ===== 5. Infinite Iterators =====
import itertools
counter = itertools.count(1)
for i in range(3):
    print(next(counter))

# ===== 6. Multiple Iterators from One Iterable =====
lst = [10, 20, 30]
it1 = iter(lst)
it2 = iter(lst)
print(next(it1), next(it2))

# ===== 7. Iterator Pitfalls =====
it = iter([1])
next(it)
# next(it)  # ❌ StopIteration

# ===== 8. Fun Tricks =====
# Reverse iteration
for x in reversed([1,2,3]):
    print(x)
# Enumerate
for idx, val in enumerate(['a', 'b', 'c']):
    print(idx, val)
# Zip
for a, b in zip([1,2], ['x','y']):
    print(a, b)

# ===== 9. Custom Iterable (not iterator) =====
class EvenNumbers:
    def __init__(self, stop):
        self.stop = stop
    def __iter__(self):
        return (x for x in range(0, self.stop, 2))
for e in EvenNumbers(6):
    print(e)

# ===== 10. Generator Expressions =====
gen = (x*x for x in range(3))
for val in gen:
    print(val)
```
