# 🧐 Usecase: Pattern Matching with Regular Expressions

Simple string methods like `.find()` are great if you know the exact text you're looking for. But what if you need to find a *pattern*? For example, how would you find all the email addresses in a document, or extract all the phone numbers from a web page?

For this, you need a more powerful tool: **Regular Expressions** (often shortened to "regex"). A regular expression is a special sequence of characters that defines a search pattern. Python's built-in `re` module is the key to unlocking this power.

---

## 🎯 Regular Expressions: Practical, Tricky, and Fun Usages

```python
# ===== 1. Find All Matches =====
import re
text = "My phone number is 415-555-1234, or (415) 555-9876."
phones = re.findall(r"\d{3}-\d{3}-\d{4}", text)
print(phones)

# ===== 2. Flexible Pattern with Groups =====
pattern = r"\(?([0-9]{3})\)?[-\s]?([0-9]{3})[-\s]?([0-9]{4})"
matches = re.findall(pattern, text)
print(matches)

# ===== 3. Find First Match =====
sentence = "The quick brown fox jumps."
match = re.search(r"fox", sentence)
if match:
    print(match.start(), match.end(), match.group(0))

# ===== 4. Find and Replace =====
text2 = "Hello, my name is Alice. Hello, Bob."
new_text = re.sub(r"Hello", "Hi", text2)
print(new_text)

# ===== 5. Compile Pattern =====
name_pat = re.compile(r"[A-Z][a-z]+")
names = name_pat.findall("John: 30, Jane: 25, David: 40")
print(names)

# ===== 6. Fun: Extract Emails =====
email_text = "Contact: alice@example.com, bob@work.org"
emails = re.findall(r"[\w.-]+@[\w.-]+", email_text)
print(emails)

# ===== 7. Fun: Validate Password =====
def is_strong(pw):
    return bool(re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$", pw))
print(is_strong("Abc12345"))

# ===== 8. Pro-Tips =====
# Use r"..." for raw strings
# Use () for capturing groups
# Use | for OR patterns
# Use ? for optional
# Use ^ and $ for start/end anchors
```
