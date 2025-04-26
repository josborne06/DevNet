# ascii_art.py

import argparse
from utils import load_image, resize_image, read_chars, map_pixels_to_chars

def main():
    parser = argparse.ArgumentParser(
        prog='ascii_art.py',
        description='Convert an image into ASCII art.',
        epilog='Example: python ascii_art.py -i photo.jpg -w 80 -o art.txt',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        '-i', '--input',
        required=True,
        help='Path to the source image file'
    )
    parser.add_argument(
        '-w', '--width',
        type=int,
        default=100,
        help='Target character width'
    )
    parser.add_argument(
        '-o', '--output',
        default=None,
        help='File to write ASCII art (prints to console if omitted)'
    )
    parser.add_argument(
        '--invert',
        action='store_true',
        help='Invert brightness mapping'
    )

    args = parser.parse_args()

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
