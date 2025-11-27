# Python File and Directory Access Modules

Below are detailed descriptions and usage examples for key Python standard libraries related to file and directory access.

---

## pathlib — Object-Oriented Filesystem Paths

**Description:**  
Provides classes for manipulating filesystem paths in an object-oriented way.

**Usage Example:**
```python
from pathlib import Path

p = Path('example.txt')
print(p.exists())  # True if file exists
print(p.parent)    # Parent directory
```

---

## os.path — Common Pathname Manipulations

**Description:**  
Offers functions for manipulating and querying file paths.

**Usage Example:**
```python
import os.path

print(os.path.basename('/path/to/file.txt'))  # 'file.txt'
print(os.path.join('folder', 'file.txt'))     # 'folder/file.txt'
```

---

## stat — Interpreting stat() Results

**Description:**  
Provides constants and functions for interpreting the results of os.stat(), such as file permissions and types.

**Usage Example:**
```python
import os
import stat

info = os.stat('example.txt')
print(stat.S_ISREG(info.st_mode))  # True if regular file
```

---

## filecmp — File and Directory Comparisons

**Description:**  
Compares files and directories to check for equality.

**Usage Example:**
```python
import filecmp

print(filecmp.cmp('file1.txt', 'file2.txt'))  # True if files are identical
```

---

## tempfile — Generate Temporary Files and Directories

**Description:**  
Creates temporary files and directories that are automatically cleaned up.

**Usage Example:**
```python
import tempfile

with tempfile.TemporaryFile(mode='w+t') as f:
	f.write('Hello!')
	f.seek(0)
	print(f.read())  # 'Hello!'
```

---

## glob — Unix Style Pathname Pattern Expansion

**Description:**  
Finds all the pathnames matching a specified pattern according to Unix shell rules.

**Usage Example:**
```python
import glob

files = glob.glob('*.txt')
print(files)  # List of .txt files in current directory
```

---

## fnmatch — Unix Filename Pattern Matching

**Description:**  
Checks if filenames match Unix shell-style wildcards.

**Usage Example:**
```python
import fnmatch

print(fnmatch.fnmatch('data.csv', '*.csv'))  # True
```

---

## linecache — Random Access to Text Lines

**Description:**  
Allows random access to any line in a text file.

**Usage Example:**
```python
import linecache

line = linecache.getline('example.txt', 2)
print(line)  # Content of line 2
```

---

## shutil — High-Level File Operations

**Description:**  
Provides functions for copying, moving, and removing files and directories.

**Usage Example:**
```python
import shutil

shutil.copy('file1.txt', 'file2.txt')  # Copy file1.txt to file2.txt
```

---
