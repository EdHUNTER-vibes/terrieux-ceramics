import re

html_path = r"C:\Users\caste\.gemini\antigravity-ide\scratch\terrieux-ceramics\collections.html"
requested_order = [18, 6, 14, 19, 33, 3, 20, 34, 2, 28, 22, 23, 8, 27, 13, 10, 4, 17, 5, 25, 12, 7, 26, 16, 9, 31, 11, 21, 15]

grid_html = '<div class="columns-2 md:columns-3 gap-unit md:gap-gutter" id="gallery-grid">\n'
for i, num in enumerate(requested_order):
    file = f"{num}.jpeg"
    grid_html += f'''<div class="break-inside-avoid mb-unit md:mb-gutter image-reveal visible">
<div class="block w-full group overflow-hidden bg-surface-container relative cursor-pointer" onclick="openLightbox({i})">
<img alt="Ceramic Work" class="w-full h-auto object-cover transform group-hover:scale-105 transition-transform duration-[2s] ease-out gallery-img" src="assets/{file}"/>
</div>
</div>\n'''
grid_html += '</div>\n'

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Regex to match the gallery-grid div and all its children up to the closing div before </section>
pattern = r'<div class="columns-2 md:columns-3 gap-unit md:gap-gutter" id="gallery-grid">.*?</div>\s*</section>'
replacement = grid_html + '</section>'

new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Grid updated successfully!")
