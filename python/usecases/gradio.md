# 🤖 Usecase: Creating Web Demos with `gradio`

You've just trained an amazing machine learning model or written a cool Python function. Now you want to share it with the world, or at least with your non-programmer colleagues. How do you do that? Building a web application from scratch is complicated.

This is the exact problem **Gradio** was designed to solve. Gradio is a Python library that allows you to create and share a user-friendly web interface for any Python function with just a few lines of code. It's the fastest way to go from a Python script to an interactive demo.

---

## 🎯 Gradio: Practical, Tricky, and Fun Usages

```python
# ===== 1. Install Gradio =====
# pip install gradio

# ===== 2. Simple Text Demo =====
def greet(name):
    if not name:
        return "Hello, mysterious stranger!"
    return f"Hello, {name}! 👋"
import gradio as gr
demo = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(label="Your Name"),
    outputs=gr.Textbox(label="Greeting"),
    title="Friendly Greeter",
    description="Type your name and get a greeting!"
)
demo.launch()

# ===== 3. Image Analysis Demo =====
from PIL import Image
def analyze(img: Image.Image):
    if img is None:
        return "No image uploaded."
    w, h = img.size
    return f"Image size: {w}x{h}"
image_demo = gr.Interface(
    fn=analyze,
    inputs=gr.Image(type="pil", label="Upload Image"),
    outputs=gr.Textbox(label="Result")
)
# image_demo.launch()

# ===== 4. Multiple Inputs/Outputs =====
def add_and_multiply(a, b):
    return a + b, a * b
multi_demo = gr.Interface(
    fn=add_and_multiply,
    inputs=[gr.Number(label="A"), gr.Number(label="B")],
    outputs=[gr.Number(label="Sum"), gr.Number(label="Product")]
)
# multi_demo.launch()

# ===== 5. Fun: Slider and Dropdown =====
def fun_demo(x, color):
    return f"You picked {color} and value {x}"
fun_ui = gr.Interface(
    fn=fun_demo,
    inputs=[gr.Slider(0, 10), gr.Dropdown(["red", "green", "blue"])],
    outputs=gr.Textbox()
)
# fun_ui.launch()

# ===== 6. Share Public Link =====
# demo.launch(share=True)

# ===== 7. Pro-Tips =====
# Use gr.Blocks for advanced layouts
# Use .launch(share=True) for public demos
# Combine with ML models for instant web apps
```
