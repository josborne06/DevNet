# utils.py

from PIL import Image

def load_image(path: str) -> Image.Image:
    return Image.open(path).convert('L')

def resize_image(img: Image.Image, target_width: int) -> Image.Image:
    w, h = img.size
    target_height = int(h * (target_width / w) * 0.5)
    return img.resize((target_width, target_height))

def read_chars(chars_file: str) -> str:
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
