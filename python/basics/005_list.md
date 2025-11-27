# 📋 005: Organizing Data with Lists

Lists are Python's most versatile, ordered, and mutable collections. Use them for dynamic sequences, flexible data storage, and fast access by index. Lists can hold any type, be nested, and are essential for everything from data processing to games and web apps. Their mutability and rich methods make them the workhorse of Python programming.

## 🎯 Python List: Practical, Tricky, and Fun Usages

```python
def list_usages():
    # ===== 1. Basic Creation & Indexing =====
    lst = [1, 2, 3]
    lst2 = list((4, 5, 6))
    mixed = [42, "Python", 3.14, [1, 0, 1], {'key': 'value'}, (1, 2)]
    print(lst[0], lst2[-1], mixed)

    # ===== 2. Slicing & Negative Indexing =====
    print(lst[-1], lst[1:3], lst[::2])

    # ===== 3. Adding, Removing, Modifying =====
    lst.append(4)
    lst.insert(0, 0)
    lst.extend([5, 6])
    lst.remove(2)
    popped = lst.pop()
    print(lst, popped)

    # ===== 4. Sorting & Reversing =====
    nums = [4, 1, 8, 5, 2]
    nums.sort()
    nums.sort(reverse=True)
    print(nums)

    words = ["banana", "pie", "Washington", "book"]
    words.sort(key=lambda x: (-len(x), x))
    print(words)

    # ===== 5. List Comprehensions =====
    squares = [x**2 for x in range(5)]
    evens = [x for x in range(10) if x % 2 == 0]
    matrix = [[i*j for j in range(3)] for i in range(3)]
    print(squares, evens, matrix)

    # Nested comprehension
    tricky = [x + y for x in [1, 2, 3] if x > 1 for y in [4, 5, 6] if y % 2 == 0]
    print(tricky)

    # ===== 6. Advanced Slicing & Assignment =====
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    lst[::2] = ['a'] * 5
    print(lst)

    # ===== 7. List Methods Playground =====
    stack = []
    stack.append('A')
    print(stack.pop())
    queue = []
    queue.insert(0, 'First')
    print(queue.pop())

    numbers = [5, 2, 8, 2]
    numbers.extend([1, 3])
    numbers.remove(2)
    print(numbers)

    # ===== 8. Memory Management =====
    original = [[1, 2], [3, 4]]
    shallow = original.copy()
    original[0][0] = 99
    import copy
    deep = copy.deepcopy(original)
    print(shallow, deep)

    # ===== 9. Functional Programming =====
    from functools import reduce
    product = reduce(lambda x, y: x * y, [1, 2, 3, 4])
    filtered = list(filter(lambda x: x > 5, [3, 7, 2, 8]))
    print(product, filtered)

    # ===== 10. Unpacking Tricks =====
    first, *middle, last = [1, 2, 3, 4, 5]
    combined = [*lst, *mixed]
    print(first, middle, last, combined)

    # ===== 11. Common Pitfalls =====
    def risky(value, lst=[]):
        lst.append(value)
        return lst
    print(risky(99))
    a = [1, 2, 3]
    b = a
    b[0] = 77
    print(a, b)

    # ===== 12. Advanced Usages =====
    checks = [0, 1, [], [0], '', 'a']
    print(any(checks), all(checks))
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    zipped = list(zip(keys, values))
    print(zipped)

    # ===== 13. Performance Considerations =====
    from collections import deque
    big_list = list(range(10**6))
    fast_queue = deque(big_list)
    fast_queue.popleft()

    # ===== 14. Fun Tricks =====
    matrix = [[1, 2], [3, 4], [5, 6]]
    flat = [num for row in matrix for num in row]
    print(flat)
    a, b = [10], [20]
    a, b = b, a
    print(a, b)
    palindrome = [1, 2, 3] + [3, 2, 1][::-1]
    print(palindrome)

    # ===== 15. List as Boolean =====
    print(bool([]), bool([1]))

    # ===== 16. Type Conversion =====
    chars = list("hello")
    unique = list(set([1,2,2,3]))
    print(chars, unique)

    # ===== 17. Mathematical Operations =====
    sum_total = sum([1, 2, 3])
    max_val = max([5, 3, 8])
    print(sum_total, max_val)

    # ===== 18. Surprising Behaviors =====
    surprises = [[]] * 3
    surprises[0].append(1)
    print(surprises)
    print([] is [])

    # ===== 19. Conversion Tricks =====
    pairs = [('a', 1), ('b', 2)]
    to_dict = dict(pairs)
    print(to_dict)
    joined = '|'.join(map(str, [1, 2, 3]))
    print(joined)

list_usages()
```
