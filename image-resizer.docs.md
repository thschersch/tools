# Image Resizer

**Image Resizer** is a browser-based tool designed to resize PNG images to 1024x1024 pixels and convert JPG images to PNG format with 1024x1024 dimensions. It's perfect for preparing images for platforms that require square images with specific dimensions.

## Features

- **PNG Resizing**: Resize PNG images to exactly 1024x1024 pixels
- **JPG to PNG Conversion**: Convert JPG/JPEG images to PNG format and resize to 1024x1024 pixels
- **Flexible Input Methods**:
    - **Drag & Drop**: Upload images directly from your computer
    - **File Upload**: Click to browse and select files
- **Smart Scaling**: 
    - Maintains aspect ratio while fitting within 1024x1024 bounds
    - Centers the image on a transparent background
- **Instant Preview**: See both original and resized images side-by-side before downloading
- **Client-Side Processing**:
    - **Privacy Focused**: All conversions occur locally within your browser
    - **Fast**: No server round-trips required
    - **Secure**: Your images never leave your device
- **Premium UI**: A clean, modern interface with responsive design and clear feedback
- **Single File Portability**: The entire tool is contained within `image-resizer.html`, requiring no installation or external dependencies

## Usage

1. Open `image-resizer.html` in any modern web browser
2. Upload an image:
    - Drag and drop a PNG or JPG file onto the upload area
    - Or click the upload area to select a file
3. Click **Resize Image** to process
4. Preview the result:
    - Original image is shown on the left
    - Resized 1024x1024 PNG is shown on the right
5. Click **Download PNG (1024x1024)** to save the resized image

## Technical Details

- **Stack**: Vanilla HTML, CSS, and JavaScript
- **Conversion Logic**:
    - Loads the image into an HTML5 Canvas element
    - Creates a 1024x1024 canvas with transparent background
    - Scales the image to fit within 1024x1024 while maintaining aspect ratio
    - Centers the scaled image on the canvas
    - Exports as PNG using `canvas.toDataURL('image/png')`
- **Supported Formats**:
    - **Input**: PNG, JPG, JPEG
    - **Output**: PNG (always)
- **Aspect Ratio**: Preserved - images are scaled to fit within 1024x1024 and centered
- **Background**: Transparent (for areas not covered by the image)
- **Compatibility**: Works in all modern browsers supporting Canvas and File APIs

## Use Cases

- Preparing profile pictures for social media platforms
- Creating square thumbnails for galleries
- Converting and standardizing image formats
- Batch preparing images for applications requiring 1024x1024 dimensions
- Converting JPG photos to PNG with transparency support
