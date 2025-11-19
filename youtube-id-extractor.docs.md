# YouTube ID Extractor

**YouTube ID Extractor** is a simple, efficient utility for extracting the unique video ID from any YouTube URL. It supports a wide variety of URL formats, making it a reliable tool for developers and content creators who need to isolate video IDs.

## Features

- **Universal URL Support**: Accurately extracts IDs from multiple YouTube URL formats:
    - Standard URLs (`youtube.com/watch?v=...`)
    - Shortened URLs (`youtu.be/...`)
    - Embed URLs (`youtube.com/embed/...`)
    - Mobile URLs (`m.youtube.com/watch?v=...`)
    - URLs with extra parameters (playlists, timestamps, etc.)
- **Real-time Extraction**: Instantly displays the ID as you type or paste a URL.
- **One-Click Copy**: Easily copy the extracted ID to your clipboard with a single button press.
- **Visual Feedback**: Clear visual indicators for valid IDs (green) and invalid inputs (red).
- **Responsive Design**: Works perfectly on desktop and mobile devices.
- **Single File Portability**: The entire tool is contained within `youtube-id-extractor.html`, requiring no installation or external dependencies.

## Usage

1. Open `youtube-id-extractor.html` in any modern web browser.
2. Paste a YouTube URL into the input field.
3. The tool will automatically extract and display the video ID.
4. Click the **Copy ID** button to copy the result to your clipboard.

## Technical Details

- **Stack**: Vanilla HTML, CSS, and JavaScript.
- **Extraction Logic**:
    - Uses a robust set of Regular Expressions (Regex) to identify and capture the video ID from various URL patterns.
    - Handles edge cases like query parameters and different subdomains.
- **Privacy**: All processing happens locally in your browser. No data is sent to any server.
