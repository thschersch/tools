# SVG to ICO Converter

**SVG to ICO Converter** is a powerful, browser-based tool designed to convert SVG vector images into multi-size ICO files. It allows users to generate standard Windows icon files containing multiple resolutions from a single SVG source, all within the browser.

## Features

- **Drag & Drop Interface**: Simple and intuitive file upload by dragging and dropping SVG files.
- **Multi-Size Support**: Generate ICO files containing any combination of standard sizes:
    - 16x16
    - 32x32
    - 48x48
    - 64x64
    - 128x128
    - 256x256
- **Instant Preview**: View your SVG file before conversion to ensure it looks correct.
- **Client-Side Processing**:
    - **Privacy Focused**: All conversions happen locally in your browser using the Canvas API.
    - **Fast**: No server uploads or downloads required.
- **Premium UI**: Features a modern, clean interface with a gradient background and responsive design.
- **Single File Portability**: The entire tool is self-contained in `svg-to-ico.html`, making it easy to deploy or use offline.

## Usage

1. Open `svg-to-ico.html` in any modern web browser.
2. Drag and drop an `.svg` file onto the upload area, or click to select a file.
3. Select the desired icon sizes from the checkboxes (16x16 and 32x32 are selected by default).
4. Click **Convert to ICO** to generate and download your `.ico` file.

## Technical Details

- **Stack**: Vanilla HTML, CSS, and JavaScript. No external libraries or frameworks.
- **Conversion Logic**:
    - Uses the HTML5 Canvas API to render the SVG at different resolutions.
    - Generates PNG data for each selected size.
    - Constructs the binary ICO file structure (header, directory entries, and image data) directly in JavaScript using `ArrayBuffer` and `DataView`.
- **Compatibility**: Works in all modern browsers that support the Canvas API and File API.
