# PNG/JPG to ICO Converter

**PNG/JPG to ICO Converter** is a browser-based tool that converts PNG and JPG images into multi-size ICO files. Perfect for creating favicons and Windows icons from your existing images.

## Features

- **Drag & Drop Interface**: Simple and intuitive file upload by dragging and dropping image files.
- **Multi-Format Support**: Accepts both PNG and JPG/JPEG image formats.
- **Multi-Size ICO Generation**: Create ICO files containing multiple resolutions:
    - 16x16 (favicon standard)
    - 32x32 (common icon size)
    - 48x48 (Windows icon size)
    - 64x64 (high-resolution favicon)
    - 128x128 (retina displays)
    - 256x256 (Windows Vista and later)
- **Smart Scaling**: Images are automatically scaled to fit each size while maintaining aspect ratio.
- **Instant Preview**: View your image before conversion to ensure it looks correct.
- **Client-Side Processing**:
    - **Privacy Focused**: All conversions happen locally in your browser using the Canvas API.
    - **Fast**: No server uploads or downloads required.
    - **Secure**: Your images never leave your device.
- **Modern UI**: Features a clean, responsive interface with gradient backgrounds.

## Usage

1. Open `png-to-ico.html` in any modern web browser.
2. Drag and drop a `.png`, `.jpg`, or `.jpeg` file onto the upload area, or click to select a file.
3. Select the desired icon sizes from the checkboxes (16x16, 32x32, and 48x48 are selected by default).
4. Click **Convert to ICO** to generate and download your `.ico` file.

## Technical Details

- **Stack**: Vanilla HTML, CSS, and JavaScript. No external libraries or frameworks required.
- **Conversion Process**:
    - Uses the HTML5 Canvas API to render the image at different resolutions.
    - Maintains aspect ratio when scaling images to fit each size.
    - Centers smaller images on transparent backgrounds for each size.
    - Generates PNG data for each selected size.
    - Constructs the binary ICO file structure (header, directory entries, and image data) directly in JavaScript.
- **File Format**: Produces standard Windows ICO files compatible with all platforms.
- **Browser Compatibility**: Works in all modern browsers that support the Canvas API and File API.

## Use Cases

- Create multi-resolution favicons for websites
- Generate Windows application icons
- Convert existing PNG/JPG logos to ICO format
- Prepare icons for different display contexts (desktop, taskbar, etc.)
