#!/usr/bin/env python3
import argparse
import os
import sys
from pathlib import Path

import cairosvg
from PIL import Image
import pillow_avif  # Register AVIF plugin
from scour import scour

def optimize_svg(input_path, output_path):
    """Optimizes SVG by removing metadata and simplifying paths using scour."""
    print(f"Optimizing SVG: {input_path.name}")
    try:
        with open(input_path, 'rb') as f_in:
            input_svg = f_in.read().decode('utf-8')

        # Scour options
        options = scour.sanitizeOptions()
        options.remove_metadata = True
        options.strip_ids = True
        options.enable_viewboxing = True
        options.indent_type = 'none'

        output_svg = scour.scourString(input_svg, options=options)

        with open(output_path, 'w', encoding='utf-8') as f_out:
            f_out.write(output_svg)
    except Exception as e:
        print(f"Error optimizing {input_path.name}: {e}")

def convert_card(input_path, output_format, width, height, quality):
    """Converts SVG to specified format with given dimensions and quality."""
    format_lower = output_format.lower()
    output_dir = Path(format_lower)
    output_dir.mkdir(exist_ok=True)

    if format_lower == 'svg_optimized':
        output_path = output_dir / f"{input_path.stem}.svg"
        optimize_svg(input_path, output_path)
        return

    output_path = output_dir / f"{input_path.stem}.{format_lower}"

    print(f"Converting {input_path.name} to {format_lower.upper()}...")

    try:
        # Step 1: SVG to PNG (Intermediate if not PNG)
        # We use cairosvg to render the SVG to a PNG in memory or temp file
        # cairosvg.svg2png returns bytes if write_to is None
        png_data = cairosvg.svg2png(
            url=str(input_path),
            output_width=width,
            output_height=height
        )

        if format_lower == 'png':
            with open(output_path, 'wb') as f:
                f.write(png_data)
        else:
            # Step 2: Use Pillow for other formats
            from io import BytesIO
            img = Image.open(BytesIO(png_data))

            if format_lower == 'jpeg':
                # JPEGs don't support transparency, use white background as requested
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'RGBA':
                    background.paste(img, mask=img.split()[3])
                else:
                    background.paste(img)
                background.save(output_path, 'JPEG', quality=quality)
            elif format_lower == 'webp':
                img.save(output_path, 'WEBP', quality=quality)
            elif format_lower == 'avif':
                img.save(output_path, 'AVIF', quality=quality)
            else:
                print(f"Unsupported format: {format_lower}")

    except Exception as e:
        print(f"Error converting {input_path.name} to {format_lower}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Convert Spanish Playing Cards SVGs to various formats.")
    parser.add_argument(
        '--formats',
        nargs='+',
        default=['png'],
        choices=['png', 'jpeg', 'webp', 'avif', 'svg_optimized'],
        help="Target formats (default: png)"
    )
    parser.add_argument('--width', type=int, default=207, help="Target width (default: 207)")
    parser.add_argument('--height', type=int, default=319, help="Target height (default: 319)")
    parser.add_argument('--quality', type=int, default=90, help="Image quality 1-100 (default: 90)")
    parser.add_argument('--input', nargs='*', help="Specific SVG files to convert (default: all SVGs in current dir)")

    args = parser.parse_args()

    # Identify input files
    if args.input:
        input_files = [Path(f) for f in args.input if Path(f).suffix.lower() == '.svg']
    else:
        input_files = sorted(list(Path('.').glob('*.[sS][vV][gG]')))

    if not input_files:
        print("No SVG files found to process.")
        return

    # Process files
    for fmt in args.formats:
        for svg_file in input_files:
            convert_card(svg_file, fmt, args.width, args.height, args.quality)

    print("\nProcessing complete!")

if __name__ == "__main__":
    main()
