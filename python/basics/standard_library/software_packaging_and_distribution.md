# Software Packaging and Distribution in Python

This section covers Python standard libraries for packaging, distributing, and managing Python environments and archives.

---

## ensurepip — Bootstrapping the pip Installer

**Description:**  
Bootstraps the pip installer into Python environments.

**Usage Example:**
```python
import ensurepip
ensurepip.bootstrap()
# Installs pip if not already present
```

---

## venv — Creation of Virtual Environments

**Description:**  
Creates isolated Python environments for project dependencies.

**Usage Example:**
```python
# In terminal
python -m venv myenv
# Activating (Windows)
myenv\Scripts\activate
# Activating (Unix)
source myenv/bin/activate
```

---

## zipapp — Manage Executable Python Zip Archives

**Description:**  
Creates and manages executable Python zip archives.

**Usage Example:**
```python
# In terminal, create a zipapp from a directory
python -m zipapp myappdir -o myapp.pyz
# Run the archive
python myapp.pyz
```

---
