# 📁 Usecase: Reading and Writing Files

Programs need a way to save data permanently so it can be used later. Whether you're saving user preferences, logging application errors, or processing a large dataset, you need to interact with files. **File handling** (also known as File I/O) is the way your Python program reads from and writes to files on your computer.

---

## 🎯 File Handling: Practical, Tricky, and Fun Usages

```python
# ===== 1. Write to a File =====
with open("hello.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("Second line.")

# ===== 2. Append to a File =====
with open("hello.txt", "a") as f:
    f.write("\nAppended line.")

# ===== 3. Read Entire File =====
with open("hello.txt", "r") as f:
    content = f.read()
    print(content)

# ===== 4. Read File Line by Line =====
with open("hello.txt", "r") as f:
    for line in f:
        print(line.strip())

# ===== 5. Check File Exists =====
import os
if os.path.exists("hello.txt"):
    print("File exists!")
else:
    print("File does not exist.")

# ===== 6. Delete a File =====
# os.remove("hello.txt")
# print("File deleted.")

# ===== 7. Fun: Write List to File =====
fruits = ["apple", "banana", "cherry"]
with open("fruits.txt", "w") as f:
    for fruit in fruits:
        f.write(fruit + "\n")

# ===== 8. Fun: Read CSV File =====
import csv
with open("fruits.txt", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# ===== 9. Context Manager Best Practice =====
# Always use 'with open(...) as ...:' for safety

# ===== 10. Exception Handling =====
try:
    with open("missing.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")

# ===== 11. Fun: Write JSON to File =====
import json
data = {"name": "Alice", "age": 30}
with open("data.json", "w") as f:
    json.dump(data, f)

# ===== 12. Fun: Read JSON from File =====
with open("data.json", "r") as f:
    loaded = json.load(f)
    print(loaded)
```
