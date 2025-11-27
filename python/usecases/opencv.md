# 🖼️ Usecase: Computer Vision with OpenCV

**OpenCV** (Open Source Computer Vision Library) is the world's most popular library for computer vision. It's a massive, powerful, and highly optimized tool that provides everything you need to load, process, analyze, and save images and videos. If you want to work with visual data in Python, OpenCV is the place to start.

---

## 🎯 OpenCV: Practical, Tricky, and Fun Usages

```python
# ===== 1. Install OpenCV =====
# pip install opencv-python

# ===== 2. Read and Display Image =====
import cv2
img = cv2.imread("./_data/opencv/butterfly.jpg", cv2.IMREAD_COLOR)
if img is not None:
    cv2.imshow("Butterfly", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found!")

# ===== 3. Convert to Grayscale =====
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ===== 4. Gaussian Blur =====
blur = cv2.GaussianBlur(gray, (5,5), 0)
cv2.imshow("Blurred", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ===== 5. Canny Edge Detection =====
edges = cv2.Canny(blur, 100, 200)
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("butterfly_edges.jpg", edges)

# ===== 6. Draw Rectangle =====
img2 = img.copy()
cv2.rectangle(img2, (50,50), (200,200), (0,255,0), 2)
cv2.imshow("Rectangle", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ===== 7. Fun: Face Detection =====
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
people = cv2.imread("./_data/opencv/players.jpg")
gray_people = cv2.cvtColor(people, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_people, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(people, (x, y), (x+w, y+h), (255,0,0), 2)
cv2.imshow("Faces", people)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ===== 8. Fun: Save Image =====
cv2.imwrite("output.jpg", img)

# ===== 9. Pro-Tips =====
# OpenCV uses BGR, not RGB
# Use cv2.waitKey(0) to pause for viewing
# Use cv2.destroyAllWindows() to close windows
# Images are NumPy arrays, so use slicing and math!
```
