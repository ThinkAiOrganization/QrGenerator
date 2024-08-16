# QR Code Generator Tool

This is a simple tool designed to generate QR codes with or without logos. It is intended for the internal use of ThinkAi and provides an easy way to create branded QR codes for various applications.

## Features

- **Generate QR Codes**: Create QR codes by simply entering a URL.
- **Logo Integration**: Optionally add a logo at the center of the QR code to enhance branding.
- **User-Friendly Interface**: A straightforward GUI built using Tkinter, allowing users to generate QR codes with just a few clicks.

## Requirements

- Python 3.x
- `qrcode` library
- `PIL` (Pillow) library
- `Tkinter` (usually included with Python)

## Installation

To install the necessary dependencies, run:

```bash
pip install qrcode[pil] pillow
```

## Usage

1. **Run the Tool**: Execute the script to open the QR Code Generator tool.

   ```bash
   python qr_code_generator.py
   ```

2. **Enter URL**: In the provided text box, enter the URL you wish to encode into a QR code.

3. **Optional - Select Logo**: Click on the "Browse" button to select a logo image (PNG, JPG, or JPEG). The logo will be placed at the center of the generated QR code.

4. **Generate QR Code**:
   - Click on "Generate QR Code with Logo" to create a QR code that includes the selected logo.
   - Alternatively, click on "Generate QR Code without Logo" to create a QR code without any logo.

5. **Save QR Code**: The generated QR code will be saved in the current directory with the filename `qrcode_with_logo.png` or `qrcode.png`, depending on your selection.

## Error Handling

- If the URL is not provided, an error message will prompt the user to enter a valid URL.
- If a logo is not selected when trying to generate a QR code with a logo, an error message will prompt the user to select a logo image.

## Example

![QR Code Example](example.png)

## License

This tool is intended for the internal use of ThinkAi. Redistribution or external use is prohibited without proper authorization.
