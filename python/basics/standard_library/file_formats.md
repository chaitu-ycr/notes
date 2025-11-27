# Python File Formats Modules

Below are detailed descriptions and usage examples for key Python standard libraries related to file formats.

---

## csv — CSV File Reading and Writing

**Description:**  
Provides functionality to read from and write to CSV (Comma Separated Values) files.

**Usage Example:**
```python
import csv

# Writing to a CSV file
with open('data.csv', 'w', newline='') as f:
	writer = csv.writer(f)
	writer.writerow(['name', 'age'])
	writer.writerow(['Alice', 30])

# Reading from a CSV file
with open('data.csv', 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		print(row)
```

---

## configparser — Configuration File Parser

**Description:**  
Reads and writes configuration files in INI format.

**Usage Example:**
```python
import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {'Server': 'localhost', 'Port': '8080'}
with open('config.ini', 'w') as f:
	config.write(f)

config.read('config.ini')
print(config['DEFAULT']['Server'])  # 'localhost'
```

---

## tomllib — Parse TOML Files

**Description:**  
Parses TOML (Tom's Obvious, Minimal Language) files.

**Usage Example:**
```python
import tomllib

with open('config.toml', 'rb') as f:
	data = tomllib.load(f)
print(data)
```

---

## netrc — netrc File Processing

**Description:**  
Parses .netrc files used for automatic login information.

**Usage Example:**
```python
import netrc

auth = netrc.netrc('sample.netrc')
print(auth.hosts)
```

---

## plistlib — Generate and Parse Apple .plist Files

**Description:**  
Reads and writes Apple Property List (plist) files.

**Usage Example:**
```python
import plistlib

data = {'name': 'Alice', 'age': 30}
with open('data.plist', 'wb') as f:
	plistlib.dump(data, f)

with open('data.plist', 'rb') as f:
	loaded = plistlib.load(f)
print(loaded)
```

---
