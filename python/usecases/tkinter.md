# 🖼️ Usecase: Building GUIs with `tkinter`

**Tkinter** (short for "Tk interface") is Python's standard, built-in library for creating graphical user interfaces (GUIs). Because it comes with Python, you don't need to install anything extra, making it the quickest and most straightforward way to build simple desktop applications, tools, and utilities.

While it may not look as modern as some other frameworks out of the box (see `customtkinter` for that!), it's reliable, cross-platform, and perfect for learning the fundamentals of event-driven programming.

---

## 🎯 tkinter: Practical, Tricky, and Fun Usages

```python
# ===== 1. Basic Window =====
import tkinter as tk
root = tk.Tk()
root.title("Hello Tkinter")
root.geometry("300x200")
root.mainloop()

# ===== 2. Add Widgets =====
label = tk.Label(root, text="Enter your name:")
label.pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

# ===== 3. Button and Event =====
def greet():
    name = entry.get()
    result.config(text=f"Hello, {name}!")
button = tk.Button(root, text="Greet", command=greet)
button.pack(pady=10)
result = tk.Label(root, text="")
result.pack(pady=20)

# ===== 4. Fun: Counter App =====
counter = 0
def inc():
    global counter
    counter += 1
    count_label.config(text=f"Count: {counter}")
count_label = tk.Label(root, text="Count: 0")
count_label.pack(pady=5)
inc_btn = tk.Button(root, text="Increment", command=inc)
inc_btn.pack(pady=5)

# ===== 5. Layout with grid =====
label2 = tk.Label(root, text="Grid Example")
label2.grid(row=0, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=0, column=1)

# ===== 6. Fun: Color Picker =====
def pick_color():
    color = tk.colorchooser.askcolor()[1]
    if color:
        root.config(bg=color)
color_btn = tk.Button(root, text="Pick Color", command=pick_color)
color_btn.pack(pady=5)

# ===== 7. Pro-Tips =====
# Use .pack(), .grid(), .place() for layout
# Use StringVar, IntVar for variable binding
# Use root.mainloop() at the end
# Use customtkinter for modern look
```
