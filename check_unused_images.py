import os
import glob

def find_unused_images():
    # Define directories
    base_dir = os.getcwd()
    images_dir = os.path.join(base_dir, 'images')
    
    # Get all image files
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp', '.ico', '.JPG', '.JPEG'}
    all_images = []
    for root, dirs, files in os.walk(images_dir):
        for file in files:
            if os.path.splitext(file)[1] in image_extensions:
                all_images.append(file)
    
    print(f"Total images found: {len(all_images)}")
    
    # Get all source files (html, css, js)
    source_files = []
    for root, dirs, files in os.walk(base_dir):
        if 'node_modules' in root or '.git' in root:
            continue
        for file in files:
            if file.endswith(('.html', '.css', '.js')):
                source_files.append(os.path.join(root, file))
                
    print(f"Total source files to scan: {len(source_files)}")
    
    # Scan content
    used_images = set()
    for source_file in source_files:
        try:
            with open(source_file, 'r', encoding='utf-8') as f:
                content = f.read()
                for image in all_images:
                    if image in content:
                        used_images.add(image)
        except Exception as e:
            print(f"Error reading {source_file}: {e}")
            
    # Determine unused images
    unused_images = [img for img in all_images if img not in used_images]
    
    print("\nUnused Images:")
    for img in unused_images:
        print(os.path.join(images_dir, img))

if __name__ == "__main__":
    find_unused_images()
