# 🧵 004: Working with Text Using Strings

Strings are one of the most fundamental data types in Python. They are how you represent and work with text, from a single character to an entire book. If your program needs to handle names, messages, file contents, or any other kind of textual data, you'll be using strings!

---

## 🎯 Strings: Practical, Tricky, and Fun Usages

```python
# ===== 1. Creating Strings =====
a = 'Hello'
b = "World"
c = '''Multi-line
string'''

# ===== 2. Indexing and Slicing =====
s = "Python"
print(s[0])      # 'P'
print(s[-1])     # 'n'
print(s[1:4])    # 'yth'

# ===== 3. String Concatenation =====
msg = "Hello, " + "World!"
print(msg)

# ===== 4. String Formatting =====
name = "Alice"
age = 30
print(f"{name} is {age} years old.")
print("{} is {} years old.".format(name, age))

# ===== 5. Changing Case =====
text = "PyThOn"
print(text.lower())   # 'python'
print(text.upper())   # 'PYTHON'
print(text.title())   # 'Python'

# ===== 6. Stripping Whitespace =====
raw = "   hello   "
print(raw.strip())    # 'hello'

# ===== 7. Find and Replace =====
phrase = "I like cats."
print(phrase.replace("cats", "dogs"))
print(phrase.find("cats"))

# ===== 8. Splitting and Joining =====
data = "a,b,c"
parts = data.split(",")
print(parts)
joined = "-".join(parts)
print(joined)

# ===== 9. String Immutability =====
word = "hello"
# word[0] = "H"  # TypeError!
word = "H" + word[1:]
print(word)

# ===== 10. Fun: Palindrome Check =====
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("madam"))

# ===== 11. Reversing a String =====
rev = "Python"[::-1]
print(rev)

# ===== 12. Count Occurrences =====
text = "banana"
print(text.count("a"))

# ===== 13. Escape Characters =====
quote = "She said, \"Hello!\""
print(quote)

# ===== 14. Multiline String =====
poem = """
Roses are red,
Violets are blue,
Python is awesome,
And so are you!
"""
print(poem)
```
