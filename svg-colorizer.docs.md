# SVG Colorizer

**SVG Colorizer** is a premium, browser-based tool designed to easily customize the colors of SVG icons. It allows users to upload an SVG, modify its background and foreground colors in real-time, and export the result as either an SVG or a high-quality PNG.

## Features

- **Drag & Drop Interface**: Intuitive file upload by dragging and dropping SVG files directly into the browser.
- **Real-time Color Customization**:
    - **Background Color**: Change the background color of the icon container.
    - **Foreground Color**: Smartly overrides `fill` and `stroke` attributes to recolor the icon.
- **Dual Export Options**:
    - **Download SVG**: Get the modified vector file with the new colors and background.
    - **Download PNG**: Export a high-resolution raster image of the colored icon.
- **Premium UI**: Built with a modern, glassmorphism-inspired design using the "Outfit" font and smooth animations.
- **Single File Portability**: The entire tool is contained within a single HTML file (`svg-colorizer.html`), making it easy to share and deploy.

## Usage

1. Open `svg-colorizer.html` in any modern web browser.
2. Drag and drop an `.svg` file onto the designated area, or click to browse your files.
3. Use the "Background Color" and "Foreground Color" pickers to customize the look.
4. Click **Download SVG** or **Download PNG** to save your work.

## Technical Details

- **Stack**: Vanilla HTML, CSS, and JavaScript. No external dependencies or build steps required.
- **Color Logic**: The tool uses `window.getComputedStyle` to correctly identify and override existing fill and stroke colors, ensuring compatibility with SVGs that use CSS classes or default styles.
- **Privacy**: All processing happens locally in your browser. No files are uploaded to any server.
