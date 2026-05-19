# Spanish Playing Cards SVG Collection

High-quality SVG vector versions of traditional Spanish playing cards (Baraja Española).

## Contents

- 48 playing cards (4 suits × 12 ranks)
- 1 card back design
- **Total: 49 SVG files**

### Suits
- **Oros (Coins)** - `card_coins_01.svg` to `card_coins_12.svg`
- **Copas (Cups)** - `card_cups_01.svg` to `card_cups_12.svg`
- **Espadas (Swords)** - `card_swords_01.svg` to `card_swords_12.svg`
- **Bastos (Clubs)** - `card_clubs_01.svg` to `card_clubs_12.svg`

### Ranks
- 1 (Ace/As)
- 2-9 (Number cards)
- 10 (Sota/Jack)
- 11 (Caballo/Knight)
- 12 (Rey/King)

## Technical Details

- **Source**: Vectorized from PNG raster images
- **Tracing**: Inkscape with 64 color scans (maximum quality)
- **Original dimensions**: 207 × 319 pixels
- **SVG viewBox**: 66.24 × 102.08 units
- **Average file size**: ~1.8 MB per card (card back: 11 MB)

## Attribution & License

The original artwork was created by [Basquetteur](https://commons.wikimedia.org/wiki/User:Basquetteur) and is available on [Wikimedia Commons](https://commons.wikimedia.org/wiki/Category:Spanish_playing_cards).

### License: CC BY-SA 4.0

This work is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

**You are free to:**
- **Share** — copy and redistribute the material in any medium or format
- **Adapt** — remix, transform, and build upon the material for any purpose, including commercially

**Under the following terms:**
- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made.
- **ShareAlike** — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.

### Attribution Example

```
Spanish playing card artwork by Basquetteur (Wikimedia Commons)
Licensed under CC BY-SA 4.0
https://creativecommons.org/licenses/by-sa/4.0/
```

## Tools & Automation

### Image Conversion Script (`convert_cards.py`)

A powerful Python script is included to convert the SVG collection into various raster formats and optimized vectors.

#### Features
- **Multi-format support**: Convert to PNG, JPEG, WebP, and AVIF.
- **SVG Optimization**: Create smaller, cleaner SVG files by removing metadata and simplifying paths.
- **Customizable**: Adjust output dimensions and image quality via command-line arguments.
- **Batch Processing**: Process all cards at once or select specific files.
- **Transparent backgrounds**: Handles transparency during conversion (JPEGs use a white background).

#### Prerequisites

To run the script, you need Python 3 and several dependencies. You can install them using:

```bash
pip install cairosvg pillow pillow-avif-plugin scour
```

*Note: `cairosvg` requires the Cairo system library to be installed on your machine (`libcairo2` on Linux, `cairo` on macOS via Homebrew).*

#### Usage Examples

**Convert all cards to PNG (default):**
```bash
python convert_cards.py
```

**Convert all cards to multiple formats with custom size:**
```bash
python convert_cards.py --formats png webp avif --width 414 --height 638
```

**Create optimized SVGs and high-quality JPEGs:**
```bash
python convert_cards.py --formats svg_optimized jpeg --quality 95
```

**Convert specific cards:**
```bash
python convert_cards.py --input card_coins_01.svg card_swords_12.svg --formats webp
```

#### Command Line Arguments
- `--formats`: Target formats (choices: `png`, `jpeg`, `webp`, `avif`, `svg_optimized`). Default: `png`.
- `--width`: Target width in pixels. Default: `207`.
- `--height`: Target height in pixels. Default: `319`.
- `--quality`: Image quality (1-100). Default: `90`.
- `--input`: Specific SVG files to convert. If omitted, all SVGs in the directory are processed.

## Integration & Usage

These assets are ideal for:
- Card game applications (Android, iOS, web)
- Educational materials about Spanish/Italian card games
- Print-on-demand products (with proper attribution)
- Game development projects

### For Android

Place files in `res/drawable-nodpi/` to use as drawable resources. The `-nodpi` qualifier ensures the vectors aren't scaled by density.

```kotlin
// Example usage
imageView.setImageResource(R.drawable.card_coins_01)
```

## Games Using Spanish Cards

- Brisca / Briscola
- Tute
- Mus
- Escoba
- Chinchón
- Conquian

## Contributing

If you improve these SVGs or create additional assets, please consider sharing them back under the same CC BY-SA 3.0 license.
