# utils.py

from PIL import Image, ImageOps, ImageEnhance

def load_image(path: str) -> Image.Image:
    img = Image.open(path).convert('L')
    img = ImageOps.autocontrast(img)
    img = ImageEnhance.Contrast(img).enhance(1.3)
    return img

def resize_image(img: Image.Image, target_width: int, aspect: float = 0.5) -> Image.Image:
    w, h = img.size
    target_height = int(h * (target_width / w) * aspect)
    small = img.resize((target_width, target_height))
    return small.convert('1', dither=Image.FLOYDSTEINBERG).convert('L')

def read_chars(chars_file: str) -> str:
    """
    Load the char ramp from a text file (one line, darkest→lightest).
    """
    with open(chars_file, 'r', encoding='utf-8') as f:
        return f.read().strip()

def map_pixels_to_chars(img: Image.Image, chars: str, invert: bool=False) -> list[list[str]]:
    if invert:
        chars = chars[::-1]
    pixels = list(img.getdata())
    scale = (len(chars) - 1) / 255
    matrix = []
    width = img.width
    for i in range(0, len(pixels), width):
        row = pixels[i:i+width]
        matrix.append([chars[int(p * scale)] for p in row])
    return matrix
