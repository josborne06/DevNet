# ascii_art.py

import argparse
from utils import load_image, resize_image, read_chars, map_pixels_to_chars

def main():
    p = argparse.ArgumentParser(description='Image → ASCII')
    p.add_argument('--input',  required=True)
    p.add_argument('--width', type=int, default=100)
    p.add_argument('--output', default=None)
    p.add_argument('--invert', action='store_true')
    args = p.parse_args()

    img = load_image(args.input)
    img = resize_image(img, args.width)
    chars = read_chars('chars.txt')
    art = map_pixels_to_chars(img, chars, args.invert)

    lines = [''.join(row) for row in art]
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
    else:
        print('\n'.join(lines))

if __name__ == '__main__':
    main()
