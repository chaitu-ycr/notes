# Python Runtime Services

This section covers Python standard libraries that provide runtime services, system information, and introspection capabilities.

---

## sys — System-specific Parameters and Functions

**Description:**  
Provides access to system-specific parameters and functions.

**Usage Example:**
```python
import sys
print(sys.version)
print(sys.platform)
```

---

## sys.monitoring — Execution Event Monitoring

**Description:**  
Monitors execution events for debugging and profiling.

**Usage Example:**
```python
# sys.monitoring is an advanced feature for event hooks (Python 3.12+)
# See official docs for usage details
```

---

## sysconfig — Access to Python’s Configuration Information

**Description:**  
Provides access to Python’s configuration and installation information.

**Usage Example:**
```python
import sysconfig
print(sysconfig.get_platform())
print(sysconfig.get_python_version())
```

---

## builtins — Built-in Objects

**Description:**  
Contains built-in objects and functions available in Python.

**Usage Example:**
```python
print(dir(__builtins__))
print(len([1, 2, 3]))
```

---

## __main__ — Top-level Code Environment

**Description:**  
Represents the environment where top-level code is run.

**Usage Example:**
```python
if __name__ == "__main__":
	print("Running as main script")
```

---

## warnings — Warning Control

**Description:**  
Controls the issuance of warning messages.

**Usage Example:**
```python
import warnings
warnings.warn("This is a warning!")
```

---

## dataclasses — Data Classes

**Description:**  
Provides a decorator and functions for creating data classes.

**Usage Example:**
```python
from dataclasses import dataclass

@dataclass
class Point:
	x: int
	y: int

p = Point(1, 2)
print(p)
```

---

## contextlib — Utilities for with-statement Contexts

**Description:**  
Utilities for creating and working with context managers.

**Usage Example:**
```python
from contextlib import contextmanager

@contextmanager
def my_context():
	print("Enter context")
	yield
	print("Exit context")

with my_context():
	print("Inside context")
```

---

## abc — Abstract Base Classes

**Description:**  
Provides infrastructure for defining abstract base classes.

**Usage Example:**
```python
from abc import ABC, abstractmethod

class MyBase(ABC):
	@abstractmethod
	def do_something(self):
		pass
```

---

## atexit — Exit Handlers

**Description:**  
Registers functions to be called upon program termination.

**Usage Example:**
```python
import atexit

def goodbye():
	print("Goodbye!")

atexit.register(goodbye)
```

---

## traceback — Print or Retrieve a Stack Traceback

**Description:**  
Prints or retrieves stack tracebacks for error handling.

**Usage Example:**
```python
import traceback

try:
	1 / 0
except Exception:
	traceback.print_exc()
```

---

## __future__ — Future Statement Definitions

**Description:**  
Allows use of features from future Python versions.

**Usage Example:**
```python
from __future__ import annotations
# Enables postponed evaluation of type annotations
```

---

## gc — Garbage Collector Interface

**Description:**  
Provides an interface to the garbage collector.

**Usage Example:**
```python
import gc
gc.collect()
```

---

## inspect — Inspect Live Objects

**Description:**  
Provides functions for introspecting live objects.

**Usage Example:**
```python
import inspect

def my_func(): pass
print(inspect.getmembers(my_func))
```

---

## annotationlib — Functionality for Introspecting Annotations

**Description:**  
Provides tools for introspecting function and variable annotations.

**Usage Example:**
```python
# Example usage depends on the specific annotationlib implementation
# See official docs for details
```

---

## site — Site-specific Configuration Hook

**Description:**  
Configures site-specific settings and paths on Python startup.

**Usage Example:**
```python
import site
print(site.getsitepackages())
```

---
