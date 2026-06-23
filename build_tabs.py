import os
import re

html_path = r"C:\Users\caste\.gemini\antigravity-ide\scratch\terrieux-ceramics\collections.html"
assets_dir = r"C:\Users\caste\.gemini\antigravity-ide\scratch\terrieux-ceramics\assets"

collections = {
    "ame_bleue": {"name": "L'Âme Bleue", "folder": "ame_bleue", "count": 31},
    "harmonie": {"name": "Harmonie", "folder": "harmonie", "count": 22},
    "selva_blanca": {"name": "Selva Blanca", "folder": "selva_blanca", "count": 14}
}

# 1. Build Tab UI
tabs_html = '''
<div class="flex justify-center mt-12 md:mt-16 border-b border-outline-variant">
  <div class="flex space-x-8 md:space-x-16 overflow-x-auto no-scrollbar px-4">
    <button onclick="switchTab('ame_bleue')" id="tab-ame_bleue" class="tab-btn font-label-caps text-label-caps tracking-widest uppercase pb-4 border-b-2 border-primary text-primary transition-colors whitespace-nowrap">L'Âme Bleue</button>
    <button onclick="switchTab('harmonie')" id="tab-harmonie" class="tab-btn font-label-caps text-label-caps tracking-widest uppercase pb-4 border-b-2 border-transparent text-on-surface-variant hover:text-primary transition-colors whitespace-nowrap">Harmonie</button>
    <button onclick="switchTab('selva_blanca')" id="tab-selva_blanca" class="tab-btn font-label-caps text-label-caps tracking-widest uppercase pb-4 border-b-2 border-transparent text-on-surface-variant hover:text-primary transition-colors whitespace-nowrap">Selva Blanca</button>
  </div>
</div>
'''

# 2. Build Grids
grids_html = ''
for key, data in collections.items():
    hidden_class = '' if key == 'ame_bleue' else 'hidden'
    grids_html += f'<div id="grid-{key}" class="tab-pane {hidden_class} columns-2 md:columns-3 gap-unit md:gap-gutter">\n'
    for i in range(1, data['count'] + 1):
        # We need the correct extension. Let's find it.
        folder_path = os.path.join(assets_dir, data['folder'])
        ext = 'jpg'
        if os.path.exists(os.path.join(folder_path, f"{i}.jpeg")): ext = 'jpeg'
        if os.path.exists(os.path.join(folder_path, f"{i}.png")): ext = 'png'
        
        file_path = f"assets/{data['folder']}/{i}.{ext}"
        grids_html += f'''<div class="break-inside-avoid mb-unit md:mb-gutter image-reveal visible">
<div class="block w-full group overflow-hidden bg-surface-container relative cursor-pointer" onclick="openLightbox('{key}', {i-1})">
<img alt="Ceramic Work - {data['name']}" class="w-full h-auto object-cover transform group-hover:scale-105 transition-transform duration-[2s] ease-out gallery-img-{key}" src="{file_path}"/>
</div>
</div>\n'''
    grids_html += '</div>\n'

# 3. Read HTML
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace Tab UI inside the header section
header_pattern = r'(<h1 class="font-display-lg-mobile md:font-display-lg text-display-lg-mobile md:text-display-lg text-center font-light mb-6">Collections</h1>\s*<p class="font-body-lg text-body-lg text-center text-on-surface-variant max-w-2xl mx-auto italic">Des objets façonnés par le temps, conçus pour sublimer le quotidien.</p>)'
content = re.sub(header_pattern, r'\1' + '\n' + tabs_html, content)

# Replace Grid Section
grid_pattern = r'<div class="columns-2 md:columns-3 gap-unit md:gap-gutter" id="gallery-grid">.*?</div>\s*</section>'
content = re.sub(grid_pattern, grids_html + '</section>', content, flags=re.DOTALL)

# 4. Update Lightbox JS
js_pattern = r'<script>\s*const images = Array\.from\(document\.querySelectorAll.*?</script>'
new_js = '''<script>
    let currentTab = 'ame_bleue';
    let currentIndex = 0;
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');

    function getImagesForTab(tab) {
        return Array.from(document.querySelectorAll('.gallery-img-' + tab)).map(img => img.src);
    }

    function switchTab(tabId) {
        currentTab = tabId;
        
        // Update Buttons
        document.querySelectorAll('.tab-btn').forEach(btn => {
            btn.classList.remove('border-primary', 'text-primary');
            btn.classList.add('border-transparent', 'text-on-surface-variant');
        });
        const activeBtn = document.getElementById('tab-' + tabId);
        activeBtn.classList.remove('border-transparent', 'text-on-surface-variant');
        activeBtn.classList.add('border-primary', 'text-primary');

        // Update Grids
        document.querySelectorAll('.tab-pane').forEach(pane => {
            pane.classList.add('hidden');
        });
        document.getElementById('grid-' + tabId).classList.remove('hidden');
    }

    function openLightbox(tabId, index) {
        if (currentTab !== tabId) switchTab(tabId);
        currentIndex = index;
        const images = getImagesForTab(currentTab);
        lightboxImg.src = images[currentIndex];
        lightbox.classList.remove('hidden');
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
        const images = getImagesForTab(currentTab);
        currentIndex = (currentIndex - 1 + images.length) % images.length;
        updateLightboxImage(images);
    }

    function nextImage(e) {
        e.stopPropagation();
        const images = getImagesForTab(currentTab);
        currentIndex = (currentIndex + 1) % images.length;
        updateLightboxImage(images);
    }
    
    function updateLightboxImage(images) {
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
</script>'''

content = re.sub(js_pattern, new_js, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("collections.html successfully updated with tabs!")
