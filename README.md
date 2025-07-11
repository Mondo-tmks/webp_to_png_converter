# WebP to PNG Converter

A simple, user-friendly tool that converts all WebP images to PNG format with just a double-click. This converter automatically organizes your converted images into a separate folder while preserving the original files.

## What This Tool Does

This converter takes the hassle out of image format conversion by automating the entire process. When you run the tool, it scans the current directory for WebP files, converts each one to PNG format while preserving image quality and transparency, and then neatly organizes the converted files in a dedicated folder.

The tool is designed with simplicity in mind - no complex commands, no technical knowledge required. Just place the converter in your folder with WebP images and double-click to start the conversion process.

## Features

**Automatic File Discovery**: The converter intelligently finds all WebP files in the same directory where you place the tool, so you don't need to manually select files.

**Smart Name Handling**: If converted files would have duplicate names, the tool automatically adds numbered suffixes (like `image_1.png`, `image_2.png`) to prevent overwriting existing files.

**Organized Output**: All converted PNG files are placed in a dedicated `converted_png` folder, keeping your workspace clean and organized while preserving your original WebP files.

**Transparency Preservation**: The converter maintains image transparency when converting from WebP to PNG, ensuring your images look exactly as intended.

**Progress Feedback**: The tool provides real-time feedback during conversion, showing you which files are being processed and whether the conversion succeeded.

## Requirements

Before using this tool, you'll need to ensure Python and the required image processing library are installed on your system.

**For Python Script Version:**
- Python 3.6 or higher
- Pillow library (install with `pip install Pillow`)

**For Executable Version:**
- No additional requirements - the executable includes everything needed

## Installation and Setup

**Option 1: Using the Executable (Recommended for most users)**

If you have the pre-compiled executable version, simply download the `.exe` file and place it in any folder containing WebP images. No installation is required.

**Option 2: Using the Python Script**

First, ensure you have Python installed on your system. Then install the required image processing library by opening a command prompt or terminal and running:

```bash
pip install Pillow
```

Download the `webp_to_png_converter.py` file and place it in the folder containing your WebP images.

**Option 3: Creating Your Own Executable**

If you prefer to compile the script yourself, you can create an executable using PyInstaller:

```bash
pip install pyinstaller
pyinstaller --onefile --console webp_to_png_converter.py
```

The executable will be created in the `dist` folder.

## How to Use

Using this converter is straightforward and requires no technical expertise:

**Step 1**: Place the converter (either the `.exe` file or the `.py` script) in the folder containing your WebP images.

**Step 2**: Double-click the converter to run it. A console window will open showing the conversion progress.

**Step 3**: Watch as the tool automatically finds and converts all WebP files. You'll see real-time feedback showing which files are being processed.

**Step 4**: Once conversion is complete, press Enter to close the program. Your converted PNG files will be in the newly created `converted_png` folder.

## Understanding the Conversion Process

The converter works by using advanced image processing techniques to ensure high-quality conversions. Here's what happens during the conversion process:

**File Detection**: The tool scans the current directory and identifies all files with the `.webp` extension.

**Image Processing**: Each WebP file is opened and analyzed to determine its color mode and whether it contains transparency information.

**Format Conversion**: The image data is converted to PNG format while preserving all visual information, including transparency channels when present.

**Quality Optimization**: The PNG files are optimized for size without losing quality, ensuring efficient storage.

**Organization**: Converted files are systematically placed in the designated output folder with appropriate naming to avoid conflicts.

## Folder Structure After Conversion

After running the converter, your folder structure will look like this:

```
Your Folder/
├── webp_to_png_converter.exe (or .py)
├── photo1.webp
├── photo2.webp
├── image.webp
└── converted_png/
    ├── photo1.png
    ├── photo2.png
    └── image.png
```

This organization keeps your original WebP files intact while providing easy access to the converted PNG versions.

## Troubleshooting Common Issues

**"No .webp files found" Message**: This indicates there are no WebP files in the current directory. Ensure you've placed the converter in the correct folder and that your image files have the `.webp` extension.

**Conversion Failures**: If specific files fail to convert, they may be corrupted or use an unsupported WebP variant. The tool will report these failures and continue processing other files.

**Permission Errors**: If the tool cannot create the output folder or write files, ensure you have write permissions in the directory where you're running the converter.

**Missing Dependencies (Script Version)**: If you see import errors when running the Python script, install the Pillow library using `pip install Pillow`.

## Technical Details

This converter is built using Python and the Pillow imaging library, which provides robust support for various image formats. The tool handles different WebP variants including those with transparency (RGBA) and without (RGB), ensuring compatibility with images created by various applications and platforms.

The conversion process maintains image quality by using lossless PNG compression, which means your converted images will have the same visual quality as the original WebP files, though file sizes may differ due to the different compression algorithms used by each format.

## Why Convert WebP to PNG?

While WebP is an excellent format for web use due to its efficient compression, PNG remains more widely supported across different applications and platforms. Converting to PNG ensures maximum compatibility with image editors, document processors, and older software that may not support WebP format.

PNG also offers some advantages in specific use cases, such as better support for transparency in certain applications and broader compatibility with printing workflows.

## Support and Feedback

This tool is designed to be reliable and user-friendly. If you encounter any issues or have suggestions for improvement, the converter's error messages will help identify common problems, and the pause at the end of execution allows you to read any important messages before the program closes.