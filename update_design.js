const fs = require('fs');
const path = require('path');

const files = ['index.html', 'collections.html', 'atelier.html', 'contact.html'];

const newNav = `<!-- TopNavBar -->
<nav class="sticky top-0 z-50 bg-surface dark:bg-background w-full transition-all duration-300" id="main-nav">
  <div class="flex justify-between items-center w-full px-margin-mobile md:px-margin-desktop py-8 max-w-[1920px] mx-auto relative">
    <!-- Mobile Menu Button -->
    <button id="mobile-menu-btn" aria-label="Open Menu" class="md:hidden p-2 text-primary dark:text-on-background hover:text-secondary transition-colors">
      <span class="material-symbols-outlined">menu</span>
    </button>
    <!-- Navigation Links (Left) -->
    <div class="hidden md:flex items-center space-x-gutter flex-1">
      <a class="font-label-caps text-label-caps text-on-surface-variant tracking-widest uppercase hover:text-secondary transition-colors duration-300" href="collections.html">Collections</a>
      <a class="font-label-caps text-label-caps text-on-surface-variant tracking-widest uppercase hover:text-secondary transition-colors duration-300" href="atelier.html">ATELIER</a>
      <a class="font-label-caps text-label-caps text-on-surface-variant tracking-widest uppercase hover:text-secondary transition-colors duration-300" href="contact.html">Contact</a>
    </div>
    <!-- Brand Logo (Center) -->
    <div class="flex-shrink-0 cursor-pointer transition-opacity hover:opacity-80 absolute left-1/2 -translate-x-1/2">
      <a class="flex flex-col items-center" href="index.html">
        <img alt="TERRIEUX CERAMICS Logo" class="h-12 w-auto object-contain mb-1" src="assets/Terrieux-ceramics-logo.png"/>
      </a>
    </div>
    <!-- Trailing Actions (Right) -->
    <div class="flex items-center space-x-4 flex-1 justify-end">
      <!-- empty bag button removed to clean up if not needed, or kept empty -->
    </div>
  </div>
  <!-- Mobile Menu Dropdown -->
  <div id="mobile-menu" class="hidden md:hidden bg-surface dark:bg-background border-t border-outline-variant px-margin-mobile py-4 flex flex-col space-y-4">
      <a class="font-label-caps text-label-caps text-on-surface-variant tracking-widest uppercase hover:text-secondary transition-colors duration-300" href="collections.html">Collections</a>
      <a class="font-label-caps text-label-caps text-on-surface-variant tracking-widest uppercase hover:text-secondary transition-colors duration-300" href="atelier.html">ATELIER</a>
      <a class="font-label-caps text-label-caps text-on-surface-variant tracking-widest uppercase hover:text-secondary transition-colors duration-300" href="contact.html">Contact</a>
  </div>
</nav>
<script>
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
</script>`;

files.forEach(file => {
    if (!fs.existsSync(file)) return;
    let content = fs.readFileSync(file, 'utf8');

    // Remove old mobile menu script if exists
    content = content.replace(/<script>\s*\/\/ Setup mobile menu toggle[\s\S]*?<\/script>/, '');

    // Replace the old TopNavBar logic
    content = content.replace(/<!-- TopNavBar -->[\s\S]*?<\/nav>/, newNav);

    if (file === 'index.html') {
        // 1. augment logo size in hero
        content = content.replace(
            /class="h-24 md:h-32 w-auto object-contain mb-6 invert brightness-0"/,
            'class="h-36 md:h-48 w-auto object-contain mb-6 invert brightness-0"'
        );

        // 2. augment font size of "sculpter la matiere..."
        content = content.replace(
            /<p class="font-label-caps text-label-caps text-on-primary tracking-widest uppercase">Sculpter la matière, révéler l'émotion<\/p>/,
            '<p class="font-label-caps text-[18px] text-on-primary tracking-widest uppercase">Sculpter la matière, révéler l\'émotion</p>'
        );

        // 3. delete EDITIONS LIMITEES
        content = content.replace(
            /<span class="hidden md:block font-label-caps text-label-caps text-on-surface-variant tracking-widest uppercase">Éditions Limitées<\/span>/,
            ''
        );

        // 4. link 'découvrir les collections' to collections.html
        content = content.replace(
            /href="#collections"([^>]*)>\s*Découvrir les collections/g,
            'href="collections.html"$1>\n                    Découvrir les collections'
        );

        // 5. link 'notre philosophie' to atelier.html
        // original line has href="#" right after transition-colors"
        content = content.replace(
            /href="#">\s*Notre philosophie/g,
            'href="atelier.html">\n                            Notre philosophie'
        );

        // 6. Gallery links to collections.html
        // Original: <a class="group md:col-span-7 flex flex-col relative" href="#">
        // Need to replace all <a class="group ... flex flex-col relative" href="#"> to href="collections.html"
        content = content.replace(
            /<a class="group ([^"]+) flex flex-col relative" href="#">/g,
            '<a class="group $1 flex flex-col relative" href="collections.html">'
        );
    }

    fs.writeFileSync(file, content, 'utf8');
    console.log(`Updated ${file}`);
});
