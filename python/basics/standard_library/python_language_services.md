# Python Language Services

This section covers Python standard libraries for parsing, compiling, and analyzing Python code.

---

## ast — Abstract Syntax Trees

**Description:**  
Parses Python source code into its abstract syntax tree (AST) representation.

**Usage Example:**
```python
import ast
tree = ast.parse('x = 1')
print(ast.dump(tree))
```

---

## symtable — Access to the Compiler’s Symbol Tables

**Description:**  
Accesses the symbol tables used by the Python compiler.

**Usage Example:**
```python
import symtable
table = symtable.symtable('x = 1', '<string>', 'exec')
print(table.get_symbols())
```

---

## token — Constants Used with Python Parse Trees

**Description:**  
Defines constants used with Python parse trees.

**Usage Example:**
```python
import token
print(token.NAME)
```

---

## keyword — Testing for Python Keywords

**Description:**  
Tests whether a string is a Python keyword.

**Usage Example:**
```python
import keyword
print(keyword.iskeyword('def'))  # True
```

---

## tokenize — Tokenizer for Python Source

**Description:**  
Tokenizes Python source code into its component tokens.

**Usage Example:**
```python
import tokenize
from io import BytesIO

code = b"x = 1\n"
for tok in tokenize.tokenize(BytesIO(code).readline):
	print(tok)
```

---

## tabnanny — Detection of Ambiguous Indentation

**Description:**  
Checks Python source files for ambiguous indentation.

**Usage Example:**
```python
import tabnanny
tabnanny.check('myscript.py')
```

---

## pyclbr — Python Module Browser Support

**Description:**  
Supports browsing Python modules and classes.

**Usage Example:**
```python
import pyclbr
info = pyclbr.readmodule('os')
print(info)
```

---

## py_compile — Compile Python Source Files

**Description:**  
Compiles Python source files to bytecode.

**Usage Example:**
```python
import py_compile
py_compile.compile('myscript.py')
```

---

## compileall — Byte-compile Python Libraries

**Description:**  
Byte-compiles all Python files in a directory tree.

**Usage Example:**
```python
import compileall
compileall.compile_dir('myproject')
```

---

## dis — Disassembler for Python Bytecode

**Description:**  
Disassembles Python bytecode into a human-readable format.

**Usage Example:**
```python
import dis
def f(x): return x + 1
dis.dis(f)
```

---

## pickletools — Tools for Pickle Developers

**Description:**  
Provides tools for analyzing and optimizing pickle bytecode.

**Usage Example:**
```python
import pickletools
data = b'\x80\x03K\x01.'
pickletools.dis(data)
```

---
