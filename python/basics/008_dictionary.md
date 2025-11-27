# 🗝️ 008: Storing Labeled Data with Dictionaries

Dictionaries are Python's flexible, mutable key-value stores. They let you label data, retrieve values instantly by key, and represent complex structures like JSON. Keys must be immutable; values can be anything. Use dictionaries for fast lookups, meaningful data, and real-world modeling. They're essential for web, data, and automation work.

## 🎯 Python Dictionary: Practical, Tricky, and Fun Usages

```python
def dict_usages():
    # ===== 1. Basic Creation & Access =====
    d = {'a': 1, 'b': 2, 'c': 3}
    print(d['a'])         # 1
    print(d.get('z', 'Not found'))

    # ===== 2. Dictionary Comprehension Magic =====
    squares = {x: x**2 for x in range(5)}
    evens = {x: 'even' for x in range(10) if x % 2 == 0}
    print(squares, evens)

    # ===== 3. Dictionary Methods Playground =====
    d = {'x': 1, 'y': 2}
    d['z'] = 3
    d.update({'w': 4})
    d.pop('x')
    del d['y']
    print(d)

    # ===== 4. Looping Tricks =====
    for k, v in d.items():
        print(f"{k}: {v}")
    for k in d:
        print(f"Key: {k}")
    for v in d.values():
        print(f"Value: {v}")

    # ===== 5. Nested Dictionaries =====
    user = {
        'name': 'Alice',
        'address': {'city': 'Wonderland', 'zip': 12345},
        'skills': ['Python', 'AI']
    }
    print(user['address']['city'])

    # ===== 6. Conversion Tricks =====
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    zipped = dict(zip(keys, values))
    print(zipped)

    # ===== 7. Default Values =====
    from collections import defaultdict
    dd = defaultdict(int)
    dd['missing'] += 1
    print(dd['missing'])

    # ===== 8. Counter =====
    from collections import Counter
    cnt = Counter('banana')
    print(cnt)

    # ===== 9. Common Pitfalls =====
    # Mutable keys not allowed
    # d = {[1,2]: 'bad'}  # ❌ TypeError
    d = {'a': 1}
    print(d.get('z'))

    # KeyError vs get()
    # print(d['z'])  # ❌ KeyError

    # Mutable default argument
    def risky(val, dct={}):
        dct[val] = True
        return dct
    print(risky('x'))

    # ===== 10. Fun Tricks & Advanced Usages =====
    # Swap keys and values
    d = {'x': 1, 'y': 2}
    swapped = {v: k for k, v in d.items()}
    print(swapped)

    # Merge dictionaries
    d1 = {'a': 1}
    d2 = {'b': 2}
    merged = {**d1, **d2}
    print(merged)

    # Dictionary as Boolean
    print(bool({}), bool({'a': 1}))

    # Dictionary to string
    print(str({'a': 1, 'b': 2}))

    # Sorting by key or value
    d = {'b': 2, 'a': 1, 'c': 3}
    print(sorted(d))
    print(sorted(d.items(), key=lambda x: x[1]))

    # Enumerate over dictionary
    for idx, (k, v) in enumerate(d.items()):
        print(idx, k, v)

    # Dictionary comprehension with condition
    filtered = {k: v for k, v in d.items() if v > 1}
    print(filtered)

dict_usages()
```
