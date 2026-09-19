---
title: "Python"
aliases:
  - "Python"
---
# 🐍 Welcome to the Wonderful World of Python!

Ready to start your programming adventure? You've picked a great starting point! Python is one of the most popular, versatile, and beginner-friendly languages on the planet. Whether you want to build websites, analyze data, or automate boring tasks, Python has your back.

This guide will be your friendly companion, walking you through the core concepts of Python with fun examples and clear explanations. Let's dive in!

## 🔗 Related topics

- [Bash](../bash/bash.md) — shell automation and scripting complementing Python workflows
- [GitHub Actions](../github_actions/github_actions.md) — CI/CD jobs often run Python-based validation and build steps
- [Testing](../testing/testing.md) — Python is widely used for unit tests, automation, and QA tooling
- [CAN](../can/can.md) — Python is often used for CAN logging, parsing, and validation tools
- [Integration](../integration/integration.md) — Python frequently powers automation and build tooling in delivery pipelines

## 🛠️ Setting Up Your Python Playground

Before you can write code, you need a place to run it. A **virtual environment** is like a clean, isolated workshop for each of your projects. It keeps your tools (packages) for one project from getting mixed up with another.

**Here's the 3-step process:**
1.  **Create the environment:**
    ```bash
    python -m venv .venv
    ```
2.  **Activate it:**
    *   **Windows:** `.venv\Scripts\activate`
    *   **macOS/Linux:** `source .venv/bin/activate`
3.  **Install packages:**
    ```bash
    pip install <package_name>
    ```
You'll know it's active because your terminal prompt will change to show `(.venv)`.

## 🧩 Organizing Your Code with Functions

Functions are reusable blocks of code that perform a specific task. They are the key to writing clean, organized, and non-repetitive ("DRY" - Don't Repeat Yourself) code.

Here's a simple function that calculates the average of a list of numbers.

```python
def calculate_average(numbers):
    """Calculates the average of a list of numbers."""
    if not numbers: # Handle the case of an empty list
        return 0
    total = sum(numbers)
    return total / len(numbers)

# Let's use our function
scores = [88, 92, 100, 75, 95]
average_score = calculate_average(scores)
print(f"The average score is: {average_score}") # Output: The average score is: 90.0
```

## 📂 Working with Files (File I/O)

Python makes it incredibly easy to read from and write to files. The `with` statement is the recommended way to do this, as it automatically handles closing the file for you.

**Writing to a file:**
```python
# Let's create a list of guests
guests = ["Alice", "Bob", "Charlie"]

with open("guests.txt", "w") as f:
    for guest in guests:
        f.write(guest + "\n")
```
This creates a file named `guests.txt` with each name on a new line.

**Reading from a file:**
```python
print("\nReading guests from file:")
with open("guests.txt", "r") as f:
    for line in f:
        # .strip() removes any leading/trailing whitespace, like the newline character
        print(f"Hello, {line.strip()}!")
```

## 🔗 Useful Resources & Next Steps

*   **Official Docs:** The [official Python documentation](https://docs.python.org/3/) is your ultimate source of truth.
*   **PyPI:** The [Python Package Index](https://pypi.org/) is where you can find and download third-party libraries.
*   **Real Python:** An amazing resource with in-depth tutorials for all skill levels.

Once you're comfortable with these basics, you can start exploring exciting areas like web development with **Django** or **Flask**, or data science with **Pandas** and **NumPy**!


