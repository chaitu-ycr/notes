# Python Graphical User Interfaces with Tk

Below are detailed descriptions and usage examples for key Python standard libraries related to GUI development with Tk.

---

## tkinter — Python Interface to Tcl/Tk

**Description:**  
Provides a standard GUI toolkit for Python, allowing creation of windows, dialogs, and widgets.

**Usage Example:**
```python
import tkinter as tk

root = tk.Tk()
root.title("Hello Tkinter")
label = tk.Label(root, text="Hello, World!")
label.pack()
root.mainloop()
```

---

## tkinter.colorchooser — Color Choosing Dialog

**Description:**  
Provides a dialog for selecting colors.

**Usage Example:**
```python
import tkinter as tk
from tkinter import colorchooser

root = tk.Tk()
color = colorchooser.askcolor(title="Choose color")
print(color)
root.destroy()
```

---

## tkinter.font — Tkinter Font Wrapper

**Description:**  
Provides font management for Tkinter widgets.

**Usage Example:**
```python
import tkinter as tk
import tkinter.font as tkfont

root = tk.Tk()
font = tkfont.Font(family="Helvetica", size=16, weight="bold")
label = tk.Label(root, text="Custom Font", font=font)
label.pack()
root.mainloop()
```

---

## tkinter.messagebox — Tkinter Message Prompts

**Description:**  
Provides standard message dialogs (info, warning, error, etc.).

**Usage Example:**
```python
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
messagebox.showinfo("Info", "This is an info message")
root.destroy()
```

---

## tkinter.scrolledtext — Scrolled Text Widget

**Description:**  
Provides a text widget with a vertical scroll bar.

**Usage Example:**
```python
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

root = tk.Tk()
st = ScrolledText(root)
st.pack()
st.insert(tk.END, "Hello, ScrolledText!")
root.mainloop()
```

---

## tkinter.dnd — Drag and Drop Support

**Description:**  
Provides drag and drop support for Tkinter widgets.

**Usage Example:**
```python
# tkinter.dnd is not available in all Python distributions.
# See official documentation for usage and compatibility.
```

---

## tkinter.ttk — Tk Themed Widgets

**Description:**  
Provides access to Tk themed widgets for modern GUI appearance.

**Usage Example:**
```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
button = ttk.Button(root, text="Themed Button")
button.pack()
root.mainloop()
```

---

## IDLE — Python Editor and Shell

**Description:**  
IDLE is Python’s integrated development environment, built with Tkinter.

**Usage Example:**
```python
# IDLE is launched as a standalone application.
# No direct code usage; run 'python -m idlelib' from the command line.
```

---

## turtle — Turtle Graphics

**Description:**  
Provides a drawing environment for teaching programming concepts with graphics.

**Usage Example:**
```python
import turtle

t = turtle.Turtle()
t.forward(100)
t.left(90)
t.forward(100)
turtle.done()
```

---
