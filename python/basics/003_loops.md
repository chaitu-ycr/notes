# 🔁 003: Repeating Actions with Loops

Imagine you had to write `print("Hello")` one hundred times. That would be tedious! In programming, we often need to repeat actions, and doing it manually is out of the question. This is where loops come to the rescue. They are a fundamental concept for automation and iteration.

---

## 🎯 Loops: Practical, Tricky, and Fun Usages

```python
# ===== 1. For Loop Over List =====
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# ===== 2. For Loop with Range =====
for i in range(5):
    print(i)

# ===== 3. While Loop =====
count = 3
while count > 0:
    print(count)
    count -= 1
print("Done!")

# ===== 4. Break in Loop =====
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    if n == 3:
        print("Found 3, breaking!")
        break
    print(n)

# ===== 5. Continue in Loop =====
for n in range(6):
    if n % 2 == 0:
        continue
    print(n)

# ===== 6. Nested Loops =====
for i in range(2):
    for j in range(2):
        print(f"i={i}, j={j}")

# ===== 7. Looping Over Dictionary =====
d = {"a": 1, "b": 2}
for key, value in d.items():
    print(f"{key}: {value}")

# ===== 8. Fun: Multiplication Table =====
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:2}", end=" ")
    print()

# ===== 9. Else with Loop =====
for n in range(3):
    print(n)
else:
    print("Loop finished!")

# ===== 10. Infinite Loop (Careful!) =====
# while True:
#     print("This will run forever!")
#     break  # Remove break to see infinite loop

# ===== 11. Enumerate for Index and Value =====
colors = ["red", "green", "blue"]
for idx, color in enumerate(colors):
    print(f"{idx}: {color}")

# ===== 12. List Comprehension (Loop Trick) =====
squares = [x*x for x in range(5)]
print(squares)
```
