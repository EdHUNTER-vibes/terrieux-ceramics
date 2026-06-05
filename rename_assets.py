import os
import glob

assets_dir = r"C:\Users\caste\.gemini\antigravity-ide\scratch\terrieux-ceramics\assets"
html_files = glob.glob(r"C:\Users\caste\.gemini\antigravity-ide\scratch\terrieux-ceramics\*.html")

image_files = [f for f in os.listdir(assets_dir) if f.startswith("WhatsApp Image") and f.endswith(".jpeg")]
image_files.sort() # Ensure consistent ordering

mapping = {}
for i, old_name in enumerate(image_files, start=1):
    new_name = f"{i}.jpeg"
    mapping[old_name] = new_name

# Rename the actual files
for old_name, new_name in mapping.items():
    old_path = os.path.join(assets_dir, old_name)
    new_path = os.path.join(assets_dir, new_name)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)

# Update references in all HTML files
for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old_name, new_name in mapping.items():
        # Replace literal occurrences
        content = content.replace(f"assets/{old_name}", f"assets/{new_name}")
        
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Successfully renamed {len(mapping)} images and updated {len(html_files)} HTML files.")
