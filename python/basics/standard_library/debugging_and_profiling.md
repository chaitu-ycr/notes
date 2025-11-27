# Debugging and Profiling in Python

This section covers Python standard libraries for debugging, profiling, and auditing code execution.

---

## Audit Events Table

Python provides audit hooks for security and debugging. Audit events are triggered for various actions (e.g., imports, file access).

| Event Name         | Description                          |
|--------------------|--------------------------------------|
| sys.addaudithook   | Adding an audit hook                 |
| import             | Importing a module                   |
| open               | Opening a file                       |
| os.remove          | Removing a file                      |
| subprocess.Popen   | Creating a new process               |
| socket.connect     | Connecting a socket                  |
| ...                | Many more events available           |

---

## bdb — Debugger Framework

**Description:**  
Base class for Python debuggers; used to build custom debuggers.

**Usage Example:**
```python
import bdb

class MyDebugger(bdb.Bdb):
	def user_line(self, frame):
		print(f"Stopped at {frame.f_code.co_name}")

debugger = MyDebugger()
# Use debugger.run('your_code_here') to debug code
```

---

## faulthandler — Dump the Python Traceback

**Description:**  
Enables dumping Python tracebacks explicitly or on a fault.

**Usage Example:**
```python
import faulthandler
faulthandler.enable()
# Now faults will print tracebacks to stderr
```

---

## pdb — The Python Debugger

**Description:**  
Interactive source code debugger for Python programs.

**Usage Example:**
```python
import pdb

def buggy_function():
	x = 1
	pdb.set_trace()
	y = 2
	return x + y

buggy_function()
```

---

## The Python Profilers

Python provides several profilers for performance analysis:

- **cProfile** — Recommended built-in profiler.
- **profile** — Pure Python profiler.

**Usage Example (cProfile):**
```python
import cProfile

def slow_function():
	sum = 0
	for i in range(10000):
		sum += i
	return sum

cProfile.run('slow_function()')
```

---

## timeit — Measure Execution Time of Small Code Snippets

**Description:**  
Measures execution time of small code snippets.

**Usage Example:**
```python
import timeit

print(timeit.timeit('sum(range(100))', number=1000))
```

---

## trace — Trace or Track Python Statement Execution

**Description:**  
Tracks program execution, generates coverage reports.

**Usage Example:**
```python
import trace

tracer = trace.Trace(count=True, trace=True)
tracer.run('for i in range(3): print(i)')
```

---

## tracemalloc — Trace Memory Allocations

**Description:**  
Monitors memory allocations to help find memory leaks.

**Usage Example:**
```python
import tracemalloc

tracemalloc.start()
# ... run code ...
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')
for stat in top_stats[:10]:
	print(stat)
```

---
