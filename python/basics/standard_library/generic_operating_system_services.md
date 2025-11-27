# Python Generic Operating System Services Modules

Below are detailed descriptions and usage examples for key Python standard libraries related to operating system services.

---

## os — Miscellaneous Operating System Interfaces

**Description:**  
Provides a way of using operating system dependent functionality like file and directory management, environment variables, and process management.

**Usage Example:**
```python
import os

print(os.name)  # 'nt' (Windows), 'posix' (Linux/Mac)
print(os.listdir('.'))  # List files in current directory
```

---

## io — Core Tools for Working with Streams

**Description:**  
Provides Python’s main facilities for dealing with streams (text, binary, buffered I/O).

**Usage Example:**
```python
import io

stream = io.StringIO("Hello\nWorld")
print(stream.read())  # 'Hello\nWorld'
```

---

## time — Time Access and Conversions

**Description:**  
Provides functions for working with time, including getting the current time, sleeping, and converting between time representations.

**Usage Example:**
```python
import time

print(time.time())      # Current time in seconds since the epoch
time.sleep(1)           # Sleep for 1 second
```

---

## logging — Logging Facility for Python

**Description:**  
Provides a flexible framework for emitting log messages from Python programs.

**Usage Example:**
```python
import logging

logging.basicConfig(level=logging.INFO)
logging.info('This is an info message')
```

---

## logging.config — Logging Configuration

**Description:**  
Provides configuration utilities for the logging module, including file-based and dictionary-based configuration.

**Usage Example:**
```python
import logging
import logging.config

config = {
	'version': 1,
	'formatters': {'default': {'format': '%(levelname)s:%(message)s'}},
	'handlers': {'console': {'class': 'logging.StreamHandler', 'formatter': 'default'}},
	'root': {'handlers': ['console'], 'level': 'INFO'},
}
logging.config.dictConfig(config)
logging.info('Configured logging')
```

---

## logging.handlers — Logging Handlers

**Description:**  
Provides a variety of useful logging handlers, such as rotating file handlers and email handlers.

**Usage Example:**
```python
import logging
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler('app.log', maxBytes=1000, backupCount=3)
logger = logging.getLogger()
logger.addHandler(handler)
logger.setLevel(logging.INFO)
logger.info('Log message to rotating file')
```

---

## platform — Access to Underlying Platform’s Identifying Data

**Description:**  
Provides functions to access platform-specific information, such as OS, architecture, and Python version.

**Usage Example:**
```python
import platform

print(platform.system())      # 'Windows', 'Linux', 'Darwin'
print(platform.python_version())  # '3.10.0'
```

---

## errno — Standard errno System Symbols

**Description:**  
Defines standard error numbers used in operating system error reporting.

**Usage Example:**
```python
import errno

print(errno.ENOENT)  # Error number for 'No such file or directory'
```

---

## ctypes — A Foreign Function Library for Python

**Description:**  
Allows calling functions in DLLs/shared libraries and manipulating C data types in Python.

**Usage Example:**
```python
import ctypes

print(ctypes.sizeof(ctypes.c_int))  # Size of C int type
```

---
