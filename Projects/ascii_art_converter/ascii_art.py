# ascii_art.py

import argparse
from utils import load_image, resize_image, read_chars, map_pixels_to_chars

def main():
    p = argparse.ArgumentParser(
        prog='ascii_art.py',
        description='Convert an image into ASCII art.',
        epilog='Example: python ascii_art.py -i photo.jpg -w 80 -a 0.45 -o art.txt',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    p.add_argument('-i','--input', required=True, help='Source image file')
    p.add_argument('-w','--width', type=int, default=100, help='Character width')
    p.add_argument('-a','--aspect', type=float, default=0.5, help='Height/width aspect ratio factor')
    p.add_argument('-o','--output', help='Output file (stdout if omitted)')
    p.add_argument('--invert', action='store_true', help='Invert brightness mapping')
    args = p.parse_args()

    img = load_image(args.input)
    img = resize_image(img, args.width, args.aspect)
    chars = read_chars('chars.txt')
    art = map_pixels_to_chars(img, chars, args.invert)
    lines = [''.join(row) for row in art]

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
    else:
        print('\n'.join(lines))

if __name__=='__main__':
    main()
