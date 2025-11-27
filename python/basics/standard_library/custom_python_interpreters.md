# Custom Python Interpreters

This section covers Python standard libraries for building and working with custom interpreters.

---

## code — Interpreter Base Classes

**Description:**  
Provides base classes for implementing custom Python interpreters.

**Usage Example:**
```python
import code

interpreter = code.InteractiveConsole()
interpreter.interact()
# Starts an interactive interpreter session
```

---

## codeop — Compile Python Code

**Description:**  
Provides utilities for compiling Python code, useful for interpreters.

**Usage Example:**
```python
import codeop

compiler = codeop.Compile()
code_obj = compiler("print('Hello World')", '<string>', 'exec')
exec(code_obj)
```

---
