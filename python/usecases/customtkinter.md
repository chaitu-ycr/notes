# ✨ Usecase: Building Modern GUIs with `customtkinter`

Python's built-in library for creating desktop applications, `tkinter`, is powerful and reliable, but let's be honest—it can look a bit dated right out of the box. What if you want to create a simple GUI that looks modern and professional without learning a massive new framework like Qt or wxPython?

This is where `customtkinter` shines. It's a library that builds on top of `tkinter`, giving you beautifully styled, modern, and themeable widgets with a very similar and easy-to-learn API.

---

## 🎯 customtkinter: Practical, Tricky, and Fun Usages

```python
# ===== 1. Install customtkinter =====
# pip install customtkinter

# ===== 2. Main Window Setup =====
import customtkinter as ctk
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
app.title("Modern App")
app.geometry("400x500")

# ===== 3. Add Widgets =====
label = ctk.CTkLabel(app, text="Hello, CustomTkinter!", font=ctk.CTkFont(size=20, weight="bold"))
label.pack(pady=20)
entry = ctk.CTkEntry(app, placeholder_text="Type something...")
entry.pack(pady=10)
slider = ctk.CTkSlider(app, from_=0, to=100)
slider.pack(pady=10)
slider.set(50)

# ===== 4. Button and Event Handling =====
def show_value():
    val = entry.get()
    slider_val = slider.get()
    result.configure(text=f"Entry: {val}\nSlider: {slider_val}")
button = ctk.CTkButton(app, text="Show Values", command=show_value)
button.pack(pady=20)
result = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=16))
result.pack(pady=10)

# ===== 5. Fun: Tip Calculator =====
bill_entry = ctk.CTkEntry(app, placeholder_text="Bill amount")
bill_entry.pack(pady=10)
tip_slider = ctk.CTkSlider(app, from_=0, to=30)
tip_slider.pack(pady=10)
tip_slider.set(15)
def calc_tip():
    try:
        bill = float(bill_entry.get())
        tip = tip_slider.get()
        total = bill + bill * tip / 100
        tip_result.configure(text=f"Tip: ${bill*tip/100:.2f}\nTotal: ${total:.2f}")
    except ValueError:
        tip_result.configure(text="Invalid bill amount!")
tip_btn = ctk.CTkButton(app, text="Calculate Tip", command=calc_tip)
tip_btn.pack(pady=10)
tip_result = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=16))
tip_result.pack(pady=10)

# ===== 6. Run the App =====
app.mainloop()

# ===== 7. Pro-Tips =====
# Use set_appearance_mode for dark/light/system themes
# Use CTkFont for custom fonts
# Widgets: CTkLabel, CTkEntry, CTkButton, CTkSlider, CTkSwitch, CTkFrame, etc.
# Layout: .pack(), .grid(), .place() for positioning
```
