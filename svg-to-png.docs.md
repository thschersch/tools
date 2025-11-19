# SVG to PNG Converter

**SVG to PNG Converter** is a versatile, browser-based tool designed to convert SVG vector images into high-quality PNG raster images. It offers precise control over output dimensions and scaling, making it ideal for generating assets for various platforms.

## Features

- **Flexible Input Methods**:
    - **Drag & Drop**: Upload SVG files directly from your computer.
    - **Paste Code**: Paste raw SVG code directly into the text area for quick conversions.
- **Custom Output Settings**:
    - **Dimensions**: Specify exact width and height in pixels for the output PNG.
    - **Scaling**: Apply a scale factor (0.1x to 10x) to easily resize the image while maintaining quality.
- **Instant Preview**: See the generated PNG immediately before downloading.
- **Client-Side Processing**:
    - **Privacy Focused**: All conversions occur locally within your browser.
    - **Fast**: No server round-trips required.
- **Premium UI**: A clean, modern interface with responsive design and clear feedback.
- **Single File Portability**: The entire tool is contained within `svg-to-png.html`, requiring no installation or external dependencies.

## Usage

1. Open `svg-to-png.html` in any modern web browser.
2. Provide an SVG:
    - Drag and drop an `.svg` file onto the upload area.
    - Click the upload area to select a file.
    - Or, paste SVG code into the text area.
3. Configure output settings:
    - Set the desired **Width** and **Height** in pixels.
    - Adjust the **Scale Factor** if needed (default is 1).
4. Click **Convert to PNG** to generate the image.
5. Preview the result and click **Download PNG** to save it.

## Technical Details

- **Stack**: Vanilla HTML, CSS, and JavaScript.
- **Conversion Logic**:
    - Renders the SVG onto an HTML5 Canvas element.
    - Uses `canvas.toDataURL('image/png')` to generate the PNG data.
    - Supports custom dimensions by resizing the canvas before drawing.
- **Compatibility**: Works in all modern browsers supporting Canvas and File APIs.
