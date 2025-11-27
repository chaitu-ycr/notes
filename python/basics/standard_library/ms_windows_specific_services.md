# MS Windows Specific Services

This section covers Python standard libraries that provide services specific to Microsoft Windows.

---

## msvcrt — Useful Routines from the MS VC++ Runtime

**Description:**  
Provides access to functions from the Microsoft Visual C++ runtime library.

**Usage Example:**
```python
import msvcrt
msvcrt.putch(b'A')  # Prints 'A' to the console
```

---

## winreg — Windows Registry Access

**Description:**  
Provides access to the Windows registry for reading and writing keys.

**Usage Example:**
```python
import winreg
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software")
print(winreg.QueryInfoKey(key))
winreg.CloseKey(key)
```

---

## winsound — Sound-playing Interface for Windows

**Description:**  
Provides access to the Windows sound-playing interface.

**Usage Example:**
```python
import winsound
winsound.Beep(1000, 500)  # Beep at 1000 Hz for 500 ms
```

---
