const fs = require('fs');
const path = require('path');

const header = `<!-- TopNavBar -->
<nav class="sticky top-0 z-50 bg-surface dark:bg-background flex justify-between items-center w-full px-margin-mobile md:px-margin-desktop py-8 max-w-[1920px] mx-auto flat no shadows transition-all duration-300" id="main-nav">
<!-- Mobile Menu Button (Hidden on Desktop) -->
<button aria-label="Open Menu" class="md:hidden p-2 text-primary dark:text-on-background hover:text-secondary transition-colors">
<span class="material-symbols-outlined">menu</span>
</button>
<!-- Navigation Links (Left) -->
<div class="hidden md:flex items-center space-x-gutter">
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
<div class="flex items-center space-x-4">
<button aria-label="Shopping Bag" class="p-2 text-primary dark:text-on-background hover:text-secondary transition-colors cursor-pointer">
</button>
</div>
</nav>`;

const footer = `<!-- Footer -->
<footer class="bg-surface-container-low w-full border-t border-outline-variant"><div class="flex flex-col md:flex-row justify-between items-center w-full px-margin-mobile md:px-margin-desktop py-16 max-w-[1920px] mx-auto gap-8">
<div class="w-full max-w-[140px] h-auto">
<img alt="TERRIEUX" class="w-full h-auto object-contain" src="assets/Terrieux-ceramics-logo.png"/>
</div>
<nav class="flex gap-8">
<a class="text-on-surface-variant font-label-caps text-label-caps hover:text-secondary transition-colors duration-200" href="#">Instagram</a>
</nav>
<div class="text-on-surface-variant font-label-caps text-label-caps text-right">
    © 2026 TERRIEUX CERAMICS. TOUS DROITS RÉSERVÉS.
  </div>
</div></footer>`;

const files = ['index.html', 'collections.html', 'atelier.html', 'contact.html'];

const assetsDir = path.join(__dirname, 'assets');
const assetFiles = fs.readdirSync(assetsDir).filter(f => f.endsWith('.jpeg') || f.endsWith('.png'));

let assetIndex = 0;

files.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');

    // Replace Header (nav block)
    content = content.replace(/<!-- TopNavBar -->[\s\S]*?<\/nav>/, header);
    
    // Replace Footer (footer block)
    content = content.replace(/<!-- Footer -->[\s\S]*?<\/footer>/, footer);

    // Some footers might not have the exact comment, fallback:
    if (!content.includes(footer)) {
        content = content.replace(/<footer[\s\S]*?<\/footer>/, footer);
    }

    // Replace Images
    content = content.replace(/src="https:\/\/lh3\.googleusercontent\.com[^"]+"/g, (match) => {
        // if it's already a logo in our new header/footer it won't match this regex
        // we cycle through local assets
        let img = assetFiles[assetIndex % assetFiles.length];
        assetIndex++;
        return `src="assets/${img}"`;
    });

    // Replace parallax images
    content = content.replace(/url\('https:\/\/lh3\.googleusercontent\.com[^']+'\)/g, (match) => {
        let img = assetFiles[assetIndex % assetFiles.length];
        assetIndex++;
        return `url('assets/${img}')`;
    });

    fs.writeFileSync(file, content, 'utf8');
    console.log(`Processed ${file}`);
});
