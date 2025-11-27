# 🍇 006: Storing Unchanging Data with Tuples

Tuples are Python's immutable, ordered collections—perfect for storing data you don't want to accidentally change. Once created, their contents cannot be modified, making them ideal for constants, configuration, and safe data passing. Tuples can hold any type, support fast access, and are often used for returning multiple values, dictionary keys, and more. Their immutability is a feature, not a limitation!

## 🎯 Python Tuple: Practical, Tricky, and Fun Usages

```python
def tuple_usages():
    # ===== 1. Basic Creation & Indexing =====
    t1 = (1, 2, 3)
    t2 = 4, 5, 6  # Parentheses optional
    t3 = (42,)    # Single-element tuple
    t4 = tuple([7, 8, 9])
    print(t1[0], t2[-1], t3, t4)

    # ===== 2. Tuple Packing & Unpacking =====
    a, b, c = t1
    x, y, *rest = (10, 20, 30, 40)
    print(a, b, c, x, y, rest)

    # Swap variables
    a, b = b, a
    print(a, b)

    # Multiple return values
    def stats(values):
        return min(values), max(values), sum(values)
    lo, hi, total = stats([1, 2, 3])
    print(lo, hi, total)

    # ===== 3. Immutability & Operations =====
    t = (1, 2, 3)
    # t[0] = 99  # ❌ TypeError
    t2 = t + (4, 5)
    t3 = t * 2
    print(t2, t3)

    # ===== 4. Tuple Methods =====
    nums = (1, 2, 2, 3)
    print(nums.count(2), nums.index(3))

    # ===== 5. Tuples as Dictionary Keys =====
    d = {}
    coord = (52.5, 13.4)
    d[coord] = "Berlin"
    print(d)

    # ===== 6. Nested & Mixed Tuples =====
    matrix = ((1, 2), (3, 4), (5, 6))
    print(matrix[1][0])
    mixed = (42, "Python", 3.14, [1, 0, 1], {'key': 'value'}, (1, 2))
    print(mixed)

    # ===== 7. Conversion Tricks =====
    chars = tuple("hello")
    unique = tuple(set([1,2,2,3]))
    print(chars, unique)

    # ===== 8. Zipping, Enumerating, Slicing =====
    keys = ('a', 'b', 'c')
    values = (1, 2, 3)
    zipped = tuple(zip(keys, values))
    print(zipped)
    print(t1[1:])

    # ===== 9. Boolean & Truthiness =====
    print(bool(()), bool((1,)))

    # ===== 10. Performance & Memory =====
    import sys
    big_tuple = tuple(range(10**6))
    print(sys.getsizeof(big_tuple))

    # ===== 11. Fun & Advanced Tricks =====
    palindrome = (1, 2, 3) + (3, 2, 1)
    print(palindrome)
    repeated = (None,) * 5
    print(repeated)
    # Tuple identity
    print(() is ())
    # Tuple to string
    joined = '|'.join(map(str, (1, 2, 3)))
    print(joined)

    # ===== 12. Common Pitfalls =====
    # Mutable elements inside tuple
    t = ([1,2], 3)
    t[0][0] = 99  # Allowed, but can be confusing
    print(t)
    # Single-element tuple confusion
    not_a_tuple = (42)
    is_a_tuple = (42,)
    print(type(not_a_tuple), type(is_a_tuple))

    # Tuple as default argument
    def risky(val, tup=()):
        return tup + (val,)
    print(risky(5))

    # Tuple unpacking with *
    first, *middle, last = (1, 2, 3, 4, 5)
    print(first, middle, last)

    # Tuple in comprehensions
    pairs = [(x, x**2) for x in range(5)]
    print(pairs)

    # Tuple in sorting
    data = [(2, 'b'), (1, 'a'), (3, 'c')]
    print(sorted(data))

    # Tuple in enumerate
    for idx, val in enumerate(('a', 'b', 'c')):
        print(idx, val)

tuple_usages()
```
