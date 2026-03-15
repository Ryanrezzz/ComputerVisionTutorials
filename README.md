<div align="center">

# 👁️ Computer Vision with OpenCV

**A hands-on collection of OpenCV fundamentals — from reading images to contour detection.**  
Built with Python · OpenCV 4.10.0 · NumPy

![Python](https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.10.0-green?style=for-the-badge&logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-latest-013243?style=for-the-badge&logo=numpy&logoColor=white)

</div>

---

## 📁 Project Structure

```
ComputerVision/
│
├── 📷  input_image.py          # Read, write & display an image
├── 📐  resizing_image.py       # Resize images to custom dimensions
├── ✂️   crop_img.py             # Crop a region from an image
├── 🎨  colorspace.py           # Convert between color spaces (BGR, RGB, Gray, HSV)
├── 🌫️   blur.py                 # Average, Gaussian & Median blur
├── 🧹  remove_noise.py         # Remove salt & pepper noise with Median blur
├── ⬛  threshold.py            # Simple binary thresholding
├── 🔲  adaptive_threshold.py   # Adaptive (Gaussian) thresholding
├── 🔍  edge_detect.py          # Canny edge detection + Dilation & Erosion
├── ✏️   drawing.py              # Draw lines, rectangles, circles & text
├── 🦎  contours.py             # Find & draw contours with bounding boxes
├── 🎬  video.py                # Play a video file frame by frame
└── 📹  web_cam.py              # Live webcam feed (press Q to quit)
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have a Python virtual environment set up with the required libraries:

```bash
pip install opencv-python numpy
```

### Running any script

```bash
python <script_name>.py
```

> **Note:** Update the `image_path` / `img_path` / `video_path` variable inside each script to point to your own image or video file before running.

---

## 📜 File Descriptions

### 📷 `input_image.py` — Read, Write & Display
The entry point to any CV project. Loads an image from disk, saves a copy as a new file, and displays it in a window.

```python
image = cv2.imread(img_path)
cv2.imwrite("new_image.jpg", image)
cv2.imshow("Image", image)
```

---

### 📐 `resizing_image.py` — Image Resizing
Loads an image, prints its original shape, resizes it to a custom dimension, and displays both the original and resized versions side by side.

```python
resized_img = cv2.resize(image, (200, 306))
```
> ⚠️ Both width and height must be **integers**.

---

### ✂️ `crop_img.py` — Image Cropping
Crops a rectangular region from an image using NumPy array slicing. Displays both the original and cropped versions.

```python
cropped_image = image[100:900, 200:1200]  # [y1:y2, x1:x2]
```

---

### 🎨 `colorspace.py` — Color Space Conversion
Converts a BGR image (OpenCV default) into three different color spaces and displays all four versions simultaneously.

| Output | Conversion Code |
|--------|----------------|
| RGB | `cv2.COLOR_BGR2RGB` |
| Grayscale | `cv2.COLOR_BGR2GRAY` |
| HSV | `cv2.COLOR_BGR2HSV` |

---

### 🌫️ `blur.py` — Image Blurring
Demonstrates three types of blur with a kernel size of 11:

| Type | Function | Best For |
|------|----------|----------|
| Average | `cv2.blur()` | Simple smoothing |
| Gaussian | `cv2.GaussianBlur()` | Natural blur, general use |
| Median | `cv2.medianBlur()` | Salt & pepper noise |

> ⚠️ `GaussianBlur` and `medianBlur` require an **odd** kernel size (e.g. 3, 5, 7, 11...).

---

### 🧹 `remove_noise.py` — Noise Removal
Uses Median blur specifically to clean up noisy images. Ideal for images with random black/white pixel artifacts (salt & pepper noise).

```python
median_correcct_img = cv2.medianBlur(image, 7)
```

---

### ⬛ `threshold.py` — Binary Thresholding
Converts image to grayscale, then applies a global binary threshold at pixel value 127. Every pixel above 127 becomes white, below becomes black.

```python
ret, thresh_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
```

---

### 🔲 `adaptive_threshold.py` — Adaptive Thresholding
Applies both global and adaptive (Gaussian) thresholding. Adaptive thresholding works much better on images with uneven lighting (e.g. handwriting, documents).

```python
adaptive_thresh = cv2.adaptiveThreshold(
    gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 17, 2
)
```

---

### 🔍 `edge_detect.py` — Edge Detection + Morphology
Uses the **Canny edge detector** to find edges, then applies **dilation** and **erosion** to manipulate the edge thickness.

```python
edge_img  = cv2.Canny(image, 100, 200)
dil_img   = cv2.dilate(edge_img, np.ones((3,3), dtype=np.int8))   # thickens edges
erod_img  = cv2.erode(edge_img,  np.ones((1,1), dtype=np.int8))   # thins edges
```

| Operation | Effect |
|-----------|--------|
| `Canny` | Detects edges |
| `dilate` | Thickens / grows edges |
| `erode` | Shrinks / thins edges |

---

### ✏️ `drawing.py` — Drawing Shapes & Text
Draws geometric shapes and text directly onto an image canvas using OpenCV's drawing functions.

```python
cv2.line(img, (300,300), (300,1000), (0,255,0), 3)           # Green line
cv2.rectangle(img, (320,320), (800,800), (0,0,255), 5)       # Red rectangle
cv2.circle(img, (1000,1000), 100, (255,0,0), 5)              # Blue circle
cv2.putText(img, "How are you?", (900,800), ...)             # Text overlay
```

---

### 🦎 `contours.py` — Contour Detection
Finds all contours in a thresholded image and draws bounding boxes around those with area > 1000 pixels — useful for object detection and segmentation.

```python
contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cont in contours:
    if cv2.contourArea(cont) > 1000:
        x, y, w, h = cv2.boundingRect(cont)
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
```

---

### 🎬 `video.py` — Video Playback
Reads and plays a video file frame by frame using `VideoCapture`. Each frame is displayed with a 30ms delay to match real-time playback.

```python
video = cv2.VideoCapture(video_path)
while ret:
    ret, frame = video.read()
    cv2.imshow('frame', frame)
    cv2.waitKey(30)
```

---

### 📹 `web_cam.py` — Live Webcam Feed
Opens the default webcam (device `0`) and streams live video. Press **`Q`** to quit.

```python
web_cam = cv2.VideoCapture(0)
while True:
    ret, frame = web_cam.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
```

---

## 🧠 Key Concepts Reference

| Concept | Quick Note |
|---------|------------|
| BGR vs RGB | OpenCV loads images in **BGR** order, not RGB |
| Kernel size | Must always be **odd** for `GaussianBlur` & `medianBlur` |
| `waitKey(0)` | Waits forever for a key press |
| `waitKey(30)` | Waits 30ms — used for video playback loops |
| `cv2.resize()` | Dimensions must be **integers** |
| Contour filtering | Use `contourArea > N` to ignore tiny noise contours |

---

<div align="center">

Made with ❤️ while learning Computer Vision

</div>
