#!/usr/bin/env python3
"""
Image Optimizer for Misha's Bikes
Optimizes all bike images for web use
"""

import os
import sys
from PIL import Image

def optimize_images(input_dir='original_images', output_dir='images'):
    """
    Optimize all images in input directory and save to output directory
    """
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"✅ Created directory: {output_dir}")
    
    # Image settings
    MAX_WIDTH = 800
    MAX_HEIGHT = 600
    QUALITY = 85
    
    # Counter for stats
    total_size_before = 0
    total_size_after = 0
    processed_count = 0
    
    print(f"\n🚀 Starting image optimization...")
    print(f"📁 Input: {input_dir}")
    print(f"📁 Output: {output_dir}")
    print(f"📐 Max size: {MAX_WIDTH}x{MAX_HEIGHT}")
    print(f"🎨 Quality: {QUALITY}%\n")
    
    # Process all images
    for filename in sorted(os.listdir(input_dir)):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            input_path = os.path.join(input_dir, filename)
            
            # Ensure output is .jpg
            output_filename = os.path.splitext(filename)[0] + '.jpg'
            output_path = os.path.join(output_dir, output_filename)
            
            try:
                # Get original size
                original_size = os.path.getsize(input_path)
                total_size_before += original_size
                
                # Open and process image
                img = Image.open(input_path)
                
                # Convert RGBA to RGB if necessary
                if img.mode in ('RGBA', 'LA', 'P'):
                    rgb_img = Image.new('RGB', img.size, (255, 255, 255))
                    rgb_img.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                    img = rgb_img
                
                # Calculate new size maintaining aspect ratio
                img.thumbnail((MAX_WIDTH, MAX_HEIGHT), Image.Resampling.LANCZOS)
                
                # Save optimized image
                img.save(output_path, 'JPEG', quality=QUALITY, optimize=True)
                
                # Get new size
                new_size = os.path.getsize(output_path)
                total_size_after += new_size
                
                # Calculate savings
                savings = (1 - new_size/original_size) * 100
                
                print(f"✅ {output_filename}: {original_size//1024}KB → {new_size//1024}KB (-{savings:.0f}%)")
                processed_count += 1
                
            except Exception as e:
                print(f"❌ Error processing {filename}: {str(e)}")
    
    # Print summary
    if processed_count > 0:
        total_savings = (1 - total_size_after/total_size_before) * 100
        print(f"\n✨ Optimization Complete!")
        print(f"📊 Processed: {processed_count} images")
        print(f"💾 Total size: {total_size_before//1024//1024}MB → {total_size_after//1024//1024}MB")
        print(f"🎯 Space saved: {total_savings:.0f}%")
    else:
        print(f"\n⚠️ No images found in {input_dir}")
        print(f"Make sure to place your original images in the '{input_dir}' folder")

def check_dependencies():
    """Check if required packages are installed"""
    try:
        from PIL import Image
        return True
    except ImportError:
        print("❌ Pillow library not installed!")
        print("Install it with: pip install Pillow")
        return False

def main():
    """Main function"""
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Check for custom directories
    if len(sys.argv) > 1:
        input_dir = sys.argv[1]
        output_dir = sys.argv[2] if len(sys.argv) > 2 else 'images'
    else:
        input_dir = 'original_images'
        output_dir = 'images'
    
    # Check if input directory exists
    if not os.path.exists(input_dir):
        print(f"❌ Input directory '{input_dir}' not found!")
        print(f"\nUsage:")
        print(f"  1. Create folder: '{input_dir}'")
        print(f"  2. Put your original bike photos there")
        print(f"  3. Name them: 1.jpg, 2.jpg, ... 23.jpg")
        print(f"  4. Run: python {sys.argv[0]}")
        print(f"\nOr specify custom directories:")
        print(f"  python {sys.argv[0]} [input_dir] [output_dir]")
        sys.exit(1)
    
    # Run optimization
    optimize_images(input_dir, output_dir)

if __name__ == "__main__":
    main()