# 🖼️ Usecase: Image Manipulation with `Pillow`

While libraries like OpenCV are built for complex computer vision analysis, sometimes you just need to perform simple image manipulations: resize a user's profile picture, add a watermark to a photo, or convert a batch of JPEGs to PNGs. For these tasks, **Pillow** is the perfect tool.

Pillow (a friendly fork of the original Python Imaging Library, or PIL) is the de-facto standard library for general-purpose image manipulation in Python. It's user-friendly, powerful, and much simpler to get started with than a heavy-duty computer vision library.

---

## 🎯 Pillow: Practical, Tricky, and Fun Usages

```python
# ===== 1. Install Pillow =====
# pip install Pillow

# ===== 2. Open and Inspect Image =====
from PIL import Image
img = Image.open("./_data/opencv/butterfly.jpg")
print(img.format, img.size, img.mode)
img.show()

# ===== 3. Resize and Crop =====
thumb = img.resize((200, 150))
thumb.show()
crop = img.crop((100, 50, 400, 300))
crop.show()

# ===== 4. Convert to Grayscale =====
gray = img.convert("L")
gray.show()

# ===== 5. Draw Text on Image =====
from PIL import ImageDraw, ImageFont
img2 = img.copy()
draw = ImageDraw.Draw(img2)
try:
    font = ImageFont.truetype("arial.ttf", 20)
except IOError:
    font = ImageFont.load_default()
draw.text((10, 10), "© My Website", font=font, fill=(255,255,255,128))
img2.show()

# ===== 6. Save Images =====
img2.save("watermarked.png")
thumb.save("thumbnail.jpg", "jpeg", quality=90)

# ===== 7. Fun: Batch Convert JPG to PNG =====
import os
for fname in os.listdir("./_data/opencv/"):
    if fname.endswith(".jpg"):
        img = Image.open(f"./_data/opencv/{fname}")
        img.save(f"./_data/opencv/{fname[:-4]}.png")

# ===== 8. Fun: Create Blank Image =====
blank = Image.new("RGB", (300, 200), color="white")
blank.show()

# ===== 9. Pro-Tips =====
# Use .copy() before editing to preserve original
# Use .show() for quick preview
# Use .save() to export in different formats
# Use ImageDraw for shapes and text
```
