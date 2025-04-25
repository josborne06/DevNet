# ASCII Art Converter
A simple Python CLI tool to convert images into ASCII art using Pillow.

## 📁 Project Structure
```
ascii_art_converter/
├── ascii_art.py         # Main script
├── utils.py             # Helper functions (loading, mapping, etc.)
├── chars.txt            # ASCII characters ordered by darkness
├── README.md            # Project overview & usage (this file)
└── requirements.txt     # Python dependencies
```

## 🚀 Getting Started

1. **Clone the Repo**
   ```bash
   git clone <repo_url>
   cd ascii_art_converter
   ```

2. **Install Dependencies**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Run the Converter**
   ```bash
   python ascii_art.py --input path/to/image.jpg --width 80 --output art.txt
   ```

4. **View Output**
   - Check `art.txt` or view directly in terminal.

## 🛠️ Usage & CLI Options
```
usage: ascii_art.py [-h] --input INPUT [--width WIDTH] [--output OUTPUT]

Options:
  -h, --help            show this help message and exit
  --input INPUT         Path to the source image file
  --width WIDTH         Target character width (default: 100)
  --output OUTPUT       File to write ASCII art (prints to console if omitted)
  --invert              Invert brightness mapping
```

## 📓 Pillow Cheat Sheet
Quick reference for common Pillow operations used in this project:

### 1. Importing & Opening Images
```python
from PIL import Image
img = Image.open('path/to/image.jpg')
```

### 2. Inspecting & Converting Modes
```python
print(img.mode, img.size)    # e.g., 'RGB', (width, height)
gray = img.convert('L')       # 'L' = 8-bit grayscale
```

### 3. Resizing While Preserving Aspect Ratio
```python
# Given target_width
w, h = gray.size
target_height = int(h * (target_width / w) * 0.5)
resized = gray.resize((target_width, target_height))
```

### 4. Accessing Pixel Data
```python
pixels = resized.getdata()    # flat sequence of pixel values (0–255)
# Or as matrix:
px_matrix = list(resized.getpixel((x, y)) for y in range(resized.height) for x in range(resized.width))
```

### 5. Saving Modified Images
```python
resized.save('small_gray.jpg')
```

### 6. Creating New Images/Text Masks
```python
from PIL import ImageDraw, ImageFont
canvas = Image.new('RGB', (width, height), color='black')
draw = ImageDraw.Draw(canvas)
font = ImageFont.load_default()
draw.text((0,0), 'ASCII ART', font=font, fill='white')
canvas.save('with_text.png')
```

## ⭐ How It Works (High Level)
1. **Load & Resize**: Open image, convert to grayscale, resize for terminal aspect.
2. **Map Brightness**: Translate each pixel to a character from `chars.txt` based on brightness.
3. **Output**: Print rows of characters or write to a file.
4. **Extras**: Support inversion, ANSI color, and custom char sets.

## 📂 Extending the Project
- Add color ANSI output for terminals.
- Experiment with different `chars.txt` palettes.
- Build a GUI front-end with `tkinter` or `PySimpleGUI`.

---
*Happy ASCII arting!*

