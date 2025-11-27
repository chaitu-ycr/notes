
# Python Data Types Services

Below are detailed descriptions and usage examples for key Python standard libraries related to data types and structures.

---

## datetime — Basic Date and Time Types

**Description:**  
Provides classes for manipulating dates and times.

**Usage Example:**
```python
import datetime

now = datetime.datetime.now()
print(now)  # Current date and time
```

---

## zoneinfo — IANA Time Zone Support

**Description:**  
Offers support for IANA time zones, allowing accurate time zone conversions.

**Usage Example:**
```python
from zoneinfo import ZoneInfo
from datetime import datetime

dt = datetime(2025, 11, 27, 12, 0, tzinfo=ZoneInfo("Asia/Kolkata"))
print(dt)  # 2025-11-27 12:00:00+05:30
```

---

## calendar — General Calendar-Related Functions

**Description:**  
Provides functions for working with calendars, including formatting and calculations.

**Usage Example:**
```python
import calendar

print(calendar.month(2025, 11))
```

---

## collections — Container Datatypes

**Description:**  
Offers specialized container datatypes like namedtuple, deque, Counter, OrderedDict, defaultdict, and ChainMap.

**Usage Example:**
```python
from collections import Counter

c = Counter('banana')
print(c)  # Counter({'a': 3, 'b': 1, 'n': 2})
```

---

## collections.abc — Abstract Base Classes for Containers

**Description:**  
Defines abstract base classes for container types, useful for type checking and custom container implementations.

**Usage Example:**
```python
from collections.abc import Iterable

print(isinstance([1, 2, 3], Iterable))  # True
```

---

## heapq — Heap Queue Algorithm

**Description:**  
Implements a min-heap queue algorithm, useful for priority queues.

**Usage Example:**
```python
import heapq

heap = [3, 1, 4]
heapq.heapify(heap)
heapq.heappush(heap, 2)
print(heapq.heappop(heap))  # 1
```

---

## bisect — Array Bisection Algorithm

**Description:**  
Provides functions for maintaining sorted lists using bisection algorithms.

**Usage Example:**
```python
import bisect

lst = [1, 3, 4, 7]
bisect.insort(lst, 5)
print(lst)  # [1, 3, 4, 5, 7]
```

---

## array — Efficient Arrays of Numeric Values

**Description:**  
Implements space-efficient arrays of basic numeric types.

**Usage Example:**
```python
import array

arr = array.array('i', [1, 2, 3])
print(arr)  # array('i', [1, 2, 3])
```

---

## weakref — Weak References

**Description:**  
Allows referencing objects without preventing their garbage collection.

**Usage Example:**
```python
import weakref

class MyClass: pass
obj = MyClass()
ref = weakref.ref(obj)
print(ref())  # <__main__.MyClass object at ...>
```

---

## types — Dynamic Type Creation and Names for Built-in Types

**Description:**  
Provides names for built-in types and functions for dynamic type creation.

**Usage Example:**
```python
import types

def func(): pass
print(type(func) == types.FunctionType)  # True
```

---

## copy — Shallow and Deep Copy Operations

**Description:**  
Supports copying objects, both shallow and deep.

**Usage Example:**
```python
import copy

lst = [[1, 2], [3, 4]]
deep_lst = copy.deepcopy(lst)
print(deep_lst)  # [[1, 2], [3, 4]]
```

---

## pprint — Data Pretty Printer

**Description:**  
Provides a capability to pretty-print data structures.

**Usage Example:**
```python
import pprint

data = {'fruits': ['apple', 'banana', 'cherry']}
pprint.pprint(data)
```

---

## reprlib — Alternate repr() Implementation

**Description:**  
Offers a means to create abbreviated representations of objects.

**Usage Example:**
```python
import reprlib

lst = list(range(100))
print(reprlib.repr(lst))  # '[0, 1, 2, ..., 99]'
```

---

## enum — Support for Enumerations

**Description:**  
Provides support for enumerations, allowing creation of symbolic names bound to unique, constant values.

**Usage Example:**
```python
from enum import Enum

class Color(Enum):
	RED = 1
	GREEN = 2
	BLUE = 3

print(Color.RED)  # Color.RED
```

---

## graphlib — Functionality to Operate with Graph-Like Structures

**Description:**  
Provides graph-related algorithms, such as topological sorting.

**Usage Example:**
```python
from graphlib import TopologicalSorter

ts = TopologicalSorter()
ts.add(1, 2)
ts.add(2, 3)
order = list(ts.static_order())
print(order)  # [3, 2, 1]
```

---
