import os

# Get all images
assets_dir = r"C:\Users\caste\.gemini\antigravity-ide\scratch\terrieux-ceramics\assets"
files = [f for f in os.listdir(assets_dir) if f.startswith("WhatsApp Image") and f.endswith(".jpeg")]

# We want to insert these into collections.html
html_path = r"C:\Users\caste\.gemini\antigravity-ide\scratch\terrieux-ceramics\collections.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Clean up line 221
# We'll use a regex or string replacement to fix the broken header
import re
content = re.sub(r'<script>\s*// Setup mobile menu toggle.*?</script><div class="flex justify-center w-full md:w-1/3">.*?</header>', 
r"""<script>
  // Setup mobile menu toggle
  document.addEventListener('DOMContentLoaded', () => {
    const btn = document.getElementById('mobile-menu-btn');
    const menu = document.getElementById('mobile-menu');
    if(btn && menu) {
        btn.addEventListener('click', () => {
            menu.classList.toggle('hidden');
        });
    }
  });
</script>""", content, flags=re.DOTALL)

# 2. Build the new grid
grid_html = '<div class="columns-2 md:columns-3 gap-unit md:gap-gutter" id="gallery-grid">\n'
for i, file in enumerate(files):
    grid_html += f'''<div class="break-inside-avoid mb-unit md:mb-gutter image-reveal visible">
<div class="block w-full group overflow-hidden bg-surface-container relative cursor-pointer" onclick="openLightbox({i})">
<img alt="Ceramic Work" class="w-full h-auto object-cover transform group-hover:scale-105 transition-transform duration-[2s] ease-out gallery-img" src="assets/{file}"/>
</div>
</div>\n'''
grid_html += '</div>\n'

# 3. Add the Lightbox HTML/CSS/JS before </body>
lightbox_html = """
<!-- Lightbox -->
<div id="lightbox" class="fixed inset-0 z-[100] bg-background/95 hidden opacity-0 transition-opacity duration-300 flex items-center justify-center backdrop-blur-sm">
    <button onclick="closeLightbox()" class="absolute top-8 right-8 text-primary hover:text-secondary transition-colors z-[110]">
        <span class="material-symbols-outlined text-[32px]">close</span>
    </button>
    
    <button onclick="prevImage(event)" class="absolute left-4 md:left-8 top-1/2 -translate-y-1/2 text-primary hover:text-secondary transition-colors z-[110] p-4">
        <span class="material-symbols-outlined text-[40px]">chevron_left</span>
    </button>
    
    <img id="lightbox-img" src="" alt="Fullscreen view" class="max-h-[85vh] max-w-[85vw] object-contain shadow-2xl" />
    
    <button onclick="nextImage(event)" class="absolute right-4 md:right-8 top-1/2 -translate-y-1/2 text-primary hover:text-secondary transition-colors z-[110] p-4">
        <span class="material-symbols-outlined text-[40px]">chevron_right</span>
    </button>
</div>

<script>
    const images = Array.from(document.querySelectorAll('.gallery-img')).map(img => img.src);
    let currentIndex = 0;
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');

    function openLightbox(index) {
        currentIndex = index;
        lightboxImg.src = images[currentIndex];
        lightbox.classList.remove('hidden');
        // trigger reflow
        void lightbox.offsetWidth;
        lightbox.classList.remove('opacity-0');
        document.body.style.overflow = 'hidden';
    }

    function closeLightbox() {
        lightbox.classList.add('opacity-0');
        setTimeout(() => {
            lightbox.classList.add('hidden');
            document.body.style.overflow = '';
        }, 300);
    }

    function prevImage(e) {
        e.stopPropagation();
        currentIndex = (currentIndex - 1 + images.length) % images.length;
        updateLightboxImage();
    }

    function nextImage(e) {
        e.stopPropagation();
        currentIndex = (currentIndex + 1) % images.length;
        updateLightboxImage();
    }
    
    function updateLightboxImage() {
        lightboxImg.style.opacity = 0;
        setTimeout(() => {
            lightboxImg.src = images[currentIndex];
            lightboxImg.style.opacity = 1;
        }, 150);
    }

    // Close on background click
    lightbox.addEventListener('click', (e) => {
        if (e.target === lightbox) {
            closeLightbox();
        }
    });

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
        if (lightbox.classList.contains('hidden')) return;
        if (e.key === 'Escape') closeLightbox();
        if (e.key === 'ArrowLeft') prevImage(e);
        if (e.key === 'ArrowRight') nextImage(e);
    });
</script>
"""

# Replace the old grid
content = re.sub(r'<div class="columns-2 md:columns-3 gap-unit md:gap-gutter">.*?</section>', grid_html + '</section>', content, flags=re.DOTALL)

# Insert lightbox before </body>
content = content.replace('</body>', lightbox_html + '</body>')

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("collections.html updated successfully!")
