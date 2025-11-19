# NATO Alphabet Converter

**NATO Alphabet Converter** is a bilingual browser-based tool designed to convert text into NATO phonetic alphabets. It supports both the German standard (DIN 5009) and the international/English NATO alphabet, with real-time conversion as you type, making it easy to spell out words, names, or complex terms over the phone or radio.

## Features

- **Dual Language Support**: Toggle between German (DIN 5009) and English/International NATO alphabets with a single click.
- **Real-time Conversion**: Instantly displays the NATO phonetic alphabet equivalent as you type.
- **German Standard (DIN 5009)**: Includes the official German spelling alphabet with special characters (Ä, Ö, Ü, ß).
- **International Standard**: Full English NATO alphabet (Alfa, Bravo, Charlie, etc.).
- **Number Support**: Automatically converts digits 0-9 to their word equivalents in the selected language.
- **Localized Interface**: All UI text switches based on the selected language for a native experience.
- **Special Character Handling**: Gracefully handles spaces and unsupported characters with clear indicators.
- **Clean, Modern UI**: Built with a premium gradient design, smooth transitions, and an intuitive toggle interface.
- **Single File Portability**: The entire tool is contained within a single HTML file (`nato-converter.html`), making it easy to share and deploy.

## Usage

1. Open `nato-converter.html` in any modern web browser.
2. Select your preferred language using the 🇩🇪 Deutsch or 🇬🇧 English toggle buttons.
3. Type any word, name, or text into the input field.
4. The NATO phonetic spelling will appear instantly below in an easy-to-read format.
5. Each letter is shown alongside its corresponding NATO word (e.g., "B = Berta" in German or "B = Bravo" in English).

## Technical Details

- **Stack**: Vanilla HTML, CSS, and JavaScript. No external dependencies or build steps required.
- **Alphabet Standards**:
  - German: Complete DIN 5009 standard including all umlauts and special characters
  - English: International NATO phonetic alphabet
- **Language Switching**: Dynamic UI updates with instant re-conversion of current text when switching languages.
- **Privacy**: All processing happens locally in your browser. No data is sent to any server.
- **Responsive Design**: Works seamlessly on desktop and mobile devices.
