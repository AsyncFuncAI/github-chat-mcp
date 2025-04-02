#!/bin/bash
set -e

# Clean up any previous builds
rm -rf dist/

# Build the package
python -m pip install --upgrade build
python -m build

# Upload to PyPI
python -m pip install --upgrade twine
python -m twine upload dist/*

echo "Package published to PyPI successfully!" 