#!/bin/bash

# Spanish Playing Cards Conversion Wrapper for Linux and macOS

# Check for Python 3
if ! command -v python3 &> /dev/null; then
    echo "Error: python3 is not installed. Please install it to continue."
    exit 1
fi

# Function to check and install dependencies
check_dependencies() {
    echo "Checking Python dependencies..."
    python3 -c "import cairosvg, PIL, scour, pillow_avif" &> /dev/null
    if [ $? -ne 0 ]; then
        echo "Missing dependencies. Attempting to install..."
        python3 -m pip install cairosvg pillow pillow-avif-plugin scour
        if [ $? -ne 0 ]; then
            echo "Error: Failed to install dependencies. Please run: pip install cairosvg pillow pillow-avif-plugin scour"
            exit 1
        fi
    fi
}

check_dependencies

# Run the Python script with all passed arguments
echo "Starting conversion..."
python3 convert_cards.py "$@"

if [ $? -eq 0 ]; then
    echo "Finished successfully!"
else
    echo "Conversion failed. Please ensure Cairo is installed on your system."
    echo "Linux: sudo apt-get install libcairo2"
    echo "macOS: brew install cairo"
fi
