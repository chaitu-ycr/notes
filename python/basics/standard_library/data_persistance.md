# Python Data Persistence Modules

Below are detailed descriptions and usage examples for key Python standard libraries related to data persistence.

---

## pickle — Python Object Serialization

**Description:**  
Serializes and deserializes Python objects to and from byte streams.

**Usage Example:**
```python
import pickle

data = {'a': 1, 'b': 2}
with open('data.pkl', 'wb') as f:
	pickle.dump(data, f)

with open('data.pkl', 'rb') as f:
	loaded = pickle.load(f)
print(loaded)  # {'a': 1, 'b': 2}
```

---

## copyreg — Register Pickle Support Functions

**Description:**  
Allows customization of how objects are pickled by registering custom pickling functions.

**Usage Example:**
```python
import copyreg
import pickle

class MyClass:
	def __init__(self, value):
		self.value = value

def pickle_myclass(obj):
	return MyClass, (obj.value,)

copyreg.pickle(MyClass, pickle_myclass)

obj = MyClass(10)
data = pickle.dumps(obj)
restored = pickle.loads(data)
print(restored.value)  # 10
```

---

## shelve — Python Object Persistence

**Description:**  
Implements a persistent, dictionary-like object database.

**Usage Example:**
```python
import shelve

with shelve.open('mydata') as db:
	db['key'] = [1, 2, 3]
	print(db['key'])  # [1, 2, 3]
```

---

## marshal — Internal Python Object Serialization

**Description:**  
Serializes and deserializes Python objects, mainly used for Python’s .pyc files. Not recommended for general persistence.

**Usage Example:**
```python
import marshal

data = [1, 2, 3]
bytes_data = marshal.dumps(data)
restored = marshal.loads(bytes_data)
print(restored)  # [1, 2, 3]
```

---

## dbm — Interfaces to Unix “Databases”

**Description:**  
Provides a dictionary-like interface to Unix database files.

**Usage Example:**
```python
import dbm

with dbm.open('exampledb', 'c') as db:
	db['key'] = b'value'
	print(db['key'])  # b'value'
```

---

## sqlite3 — DB-API 2.0 Interface for SQLite Databases

**Description:**  
Implements a SQL database engine that stores data in a single file.

**Usage Example:**
```python
import sqlite3

conn = sqlite3.connect('example.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)')
cur.execute('INSERT INTO users VALUES (?, ?)', (1, 'Alice'))
conn.commit()
cur.execute('SELECT * FROM users')
print(cur.fetchall())  # [(1, 'Alice')]
conn.close()
```

---
