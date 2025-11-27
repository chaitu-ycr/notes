# Python Concurrent Execution Modules

Below are detailed descriptions and usage examples for key Python standard libraries related to concurrent execution.

---

## threading — Thread-based Parallelism

**Description:**  
Provides a way to run multiple threads (lightweight processes) within a program.

**Usage Example:**
```python
import threading

def worker():
	print("Thread is running")

t = threading.Thread(target=worker)
t.start()
t.join()
```

---

## multiprocessing — Process-based Parallelism

**Description:**  
Supports spawning processes using an API similar to the threading module.

**Usage Example:**
```python
import multiprocessing

def worker():
	print("Process is running")

p = multiprocessing.Process(target=worker)
p.start()
p.join()
```

---

## multiprocessing.shared_memory — Shared Memory for Direct Access Across Processes

**Description:**  
Allows direct access to shared memory segments between processes.

**Usage Example:**
```python
from multiprocessing import shared_memory

shm = shared_memory.SharedMemory(create=True, size=10)
shm.buf[:5] = b'hello'
print(bytes(shm.buf[:5]))  # b'hello'
shm.close()
shm.unlink()
```

---

## concurrent.futures — Launching Parallel Tasks

**Description:**  
Provides a high-level interface for asynchronously executing callables using threads or processes.

**Usage Example:**
```python
from concurrent.futures import ThreadPoolExecutor

def worker(x):
	return x * x

with ThreadPoolExecutor() as executor:
	future = executor.submit(worker, 5)
	print(future.result())  # 25
```

---

## concurrent.interpreters — Multiple Interpreters in the Same Process

**Description:**  
Allows running multiple Python interpreters in the same process (advanced use).

**Usage Example:**
```python
import concurrent.interpreters

# Example usage is advanced and may require Python 3.9+
# See official documentation for details.
```

---

## subprocess — Subprocess Management

**Description:**  
Allows spawning new processes, connecting to their input/output/error pipes, and obtaining their return codes.

**Usage Example:**
```python
import subprocess

result = subprocess.run(['echo', 'Hello'], capture_output=True, text=True)
print(result.stdout)  # Hello
```

---

## sched — Event Scheduler

**Description:**  
Implements a general purpose event scheduler.

**Usage Example:**
```python
import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)
def event():
	print("Event triggered")

scheduler.enter(2, 1, event)
scheduler.run()
```

---

## queue — A Synchronized Queue Class

**Description:**  
Provides a thread-safe FIFO implementation.

**Usage Example:**
```python
import queue

q = queue.Queue()
q.put(1)
print(q.get())  # 1
```

---

## contextvars — Context Variables

**Description:**  
Supports managing, storing, and accessing context-local state.

**Usage Example:**
```python
import contextvars

var = contextvars.ContextVar('var', default=42)
print(var.get())  # 42
```

---

## _thread — Low-level Threading API

**Description:**  
Provides low-level primitives for working with threads (use threading module for most cases).

**Usage Example:**
```python
import _thread

def worker():
	print("Low-level thread running")

_thread.start_new_thread(worker, ())
```

---
