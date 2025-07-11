#!/usr/bin/env python3
"""
WebP to PNG Converter
Double-click this script to convert all .webp files in the same folder to .png format
"""

import os
import sys
from PIL import Image
import glob

def convert_webp_to_png():
    """Convert all .webp files in the script's directory to .png format"""
    
    # Get the directory where the script is located
    if getattr(sys, 'frozen', False):
        # Running as PyInstaller executable
        script_dir = os.path.dirname(sys.executable)
    else:
        # Running as Python script
        script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Find all .webp files in the script directory
    webp_files = glob.glob(os.path.join(script_dir, "*.webp"))
    
    if not webp_files:
        print("No .webp files found in the current directory.")
        input("Press Enter to exit...")
        return
    
    print(f"Found {len(webp_files)} .webp file(s) to convert:")
    
    # Create output folder for converted images
    output_folder = os.path.join(script_dir, "converted_png")
    os.makedirs(output_folder, exist_ok=True)
    print(f"Output folder: {output_folder}")
    
    converted_count = 0
    failed_count = 0
    
    for webp_file in webp_files:
        try:
            # Get the base filename without extension
            base_name = os.path.splitext(os.path.basename(webp_file))[0]
            
            # Create the output PNG filename with duplicate handling
            png_file = os.path.join(output_folder, f"{base_name}.png")
            
            # Handle duplicate names
            counter = 1
            while os.path.exists(png_file):
                png_file = os.path.join(output_folder, f"{base_name}_{counter}.png")
                counter += 1
            
            # Open and convert the image
            with Image.open(webp_file) as img:
                # Convert RGBA to RGB if necessary (PNG supports both)
                if img.mode in ('RGBA', 'LA'):
                    # Keep transparency for PNG
                    img.save(png_file, 'PNG', optimize=True)
                else:
                    # Convert to RGB for non-transparent images
                    img.convert('RGB').save(png_file, 'PNG', optimize=True)
            
            print(f"✓ Converted: {os.path.basename(webp_file)} → {os.path.basename(png_file)}")
            converted_count += 1
            
        except Exception as e:
            print(f"✗ Failed to convert {os.path.basename(webp_file)}: {str(e)}")
            failed_count += 1
    
    print(f"\nConversion completed!")
    print(f"Successfully converted: {converted_count} files")
    if failed_count > 0:
        print(f"Failed conversions: {failed_count} files")
    
    input("Press Enter to exit...")

if __name__ == "__main__":
    try:
        convert_webp_to_png()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        input("Press Enter to exit...")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        input("Press Enter to exit...")
