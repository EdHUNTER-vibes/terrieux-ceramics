import os
import shutil

# Sources
ame_bleue_src = r"C:\Users\caste\Downloads\TransferNow-Collection L ame bleue\Collection _L Ame Bleue_"
harmonie_src = r"C:\Users\caste\Downloads\TransferNow-Collection Harmonie\Collection _Harmonie_"
selva_blanca_src = r"C:\Users\caste\Downloads\TransferNow-collection Selva Blanca\Collection _Selva Blanca_"

# Destinations
assets_dir = r"C:\Users\caste\.gemini\antigravity-ide\scratch\terrieux-ceramics\assets"
ame_bleue_dest = os.path.join(assets_dir, "ame_bleue")
harmonie_dest = os.path.join(assets_dir, "harmonie")
selva_blanca_dest = os.path.join(assets_dir, "selva_blanca")

for d in [ame_bleue_dest, harmonie_dest, selva_blanca_dest]:
    os.makedirs(d, exist_ok=True)

def copy_images(src, dest):
    count = 1
    for root, dirs, files in os.walk(src):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')) and not file.startswith('.'):
                src_path = os.path.join(root, file)
                ext = file.split('.')[-1].lower()
                if ext == 'jpeg': ext = 'jpg'
                dest_path = os.path.join(dest, f"{count}.{ext}")
                shutil.copy2(src_path, dest_path)
                count += 1
    return count - 1

print(f"Copied {copy_images(ame_bleue_src, ame_bleue_dest)} images to Ame Bleue")
print(f"Copied {copy_images(harmonie_src, harmonie_dest)} images to Harmonie")
print(f"Copied {copy_images(selva_blanca_src, selva_blanca_dest)} images to Selva Blanca")

# Keep images used by index.html and atelier.html
keep = {5, 12, 13, 15, 24, 28, 29, 33}
deleted = 0
for i in range(1, 35):
    if i not in keep:
        file = os.path.join(assets_dir, f"{i}.jpeg")
        if os.path.exists(file):
            os.remove(file)
            deleted += 1
print(f"Deleted {deleted} old images.")
