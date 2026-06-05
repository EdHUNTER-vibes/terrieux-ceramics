import os
import math
from PIL import Image, ImageDraw, ImageFont

img_dir = r"C:\Users\caste\.gemini\antigravity-ide\scratch\terrieux-ceramics\assets"
files = [f for f in os.listdir(img_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Define thumbnail size
thumb_w, thumb_h = 300, 300

# Calculate grid
n = len(files)
cols = 6
rows = math.ceil(n / cols)

# Create canvas
canvas_w = cols * thumb_w
canvas_h = rows * thumb_h
canvas = Image.new('RGB', (canvas_w, canvas_h), 'white')
draw = ImageDraw.Draw(canvas)

for i, f in enumerate(files):
    row = i // cols
    col = i % cols
    x = col * thumb_w
    y = row * thumb_h
    
    img_path = os.path.join(img_dir, f)
    try:
        with Image.open(img_path) as img:
            img.thumbnail((thumb_w - 20, thumb_h - 40))
            # Paste centered in cell
            paste_x = x + (thumb_w - img.width) // 2
            paste_y = y + (thumb_h - 40 - img.height) // 2
            canvas.paste(img, (paste_x, paste_y))
            # Draw text
            # Use basic font since we might not have a specific one
            draw.text((x + 10, y + thumb_h - 30), f[:30], fill='black')
    except Exception as e:
        print(f"Error loading {f}: {e}")

canvas.save(os.path.join(img_dir, "mosaic_temp.jpg"))
print("Mosaic created.")
