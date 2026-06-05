import glob
import re

html_files = glob.glob(r"C:\Users\caste\.gemini\antigravity-ide\scratch\terrieux-ceramics\*.html")

old_str = r'<a class="text-on-surface-variant font-label-caps text-label-caps hover:text-secondary transition-colors duration-200" href="#">Instagram</a>'
# Let's use a regex to be safe, just in case spaces differ
pattern = re.compile(r'<a[^>]*href="[^"]*"[^>]*>\s*Instagram\s*</a>', re.IGNORECASE)

# SVG for Instagram icon (in a black circle to make the white icon visible on beige background)
# Or just the icon itself with currentColor, but user explicitly asked for "blanche" (white).
# If we just do text-white, it'll vanish on beige. Let's do a black circle with white icon.
new_str = '''<a class="text-white bg-primary hover:bg-secondary transition-colors duration-200 p-2 rounded-full flex items-center justify-center" href="https://www.instagram.com/terrieux_ceramics/" target="_blank" rel="noopener noreferrer" aria-label="Instagram">
  <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <rect width="20" height="20" x="2" y="2" rx="5" ry="5"></rect>
    <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
    <line x1="17.5" x2="17.51" y1="6.5" y2="6.5"></line>
  </svg>
</a>'''

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We might have different class strings in different files, so regex is better
    updated_content = pattern.sub(new_str, content)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(updated_content)

print(f"Updated Instagram link in {len(html_files)} files.")
