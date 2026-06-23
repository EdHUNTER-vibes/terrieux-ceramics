import os
import re

files = ['index.html', 'collections.html', 'atelier.html', 'contact.html']
base_dir = r"C:\Users\caste\.gemini\antigravity-ide\scratch\terrieux-ceramics"

nav_html = '''<!-- TopNavBar -->
<nav class="sticky top-0 z-50 bg-surface dark:bg-background w-full transition-all duration-300" id="main-nav">
  <div class="flex justify-between items-center w-full px-margin-mobile md:px-margin-desktop py-8 max-w-[1920px] mx-auto relative">
    
    <!-- Mobile Menu Button -->
    <button id="mobile-menu-btn" aria-label="Open Menu" class="md:hidden p-2 text-primary dark:text-on-background hover:text-secondary transition-colors">
      <span class="material-symbols-outlined">menu</span>
    </button>
    
    <!-- Navigation Links (Left) -->
    <div class="hidden md:flex items-center space-x-gutter flex-1">
      <a data-i18n="nav_boutique" class="font-label-caps text-label-caps text-on-surface-variant tracking-widest uppercase hover:text-secondary transition-colors duration-300" href="boutique.html">Boutique</a>
      <a data-i18n="nav_collections" class="font-label-caps text-label-caps text-on-surface-variant tracking-widest uppercase hover:text-secondary transition-colors duration-300" href="collections.html">Collections</a>
      <a data-i18n="nav_atelier" class="font-label-caps text-label-caps text-on-surface-variant tracking-widest uppercase hover:text-secondary transition-colors duration-300" href="atelier.html">ATELIER</a>
      <a data-i18n="nav_contact" class="font-label-caps text-label-caps text-on-surface-variant tracking-widest uppercase hover:text-secondary transition-colors duration-300" href="contact.html">Contact</a>
    </div>
    
    <!-- Brand Logo (Center) -->
    <div class="flex-shrink-0 cursor-pointer transition-opacity hover:opacity-80 absolute left-1/2 -translate-x-1/2">
      <a class="flex flex-col items-center" href="index.html">
        <img alt="TERRIEUX CERAMICS Logo" class="h-12 w-auto object-contain mb-1" src="assets/Terrieux-ceramics-logo.png"/>
      </a>
    </div>
    
    <!-- Trailing Actions (Right) -->
    <div class="flex items-center space-x-4 flex-1 justify-end">
      <!-- Language Selector -->
      <div class="relative group cursor-pointer">
        <div class="flex items-center space-x-1 text-on-surface-variant hover:text-secondary transition-colors font-label-caps text-label-caps tracking-widest uppercase">
          <span id="current-lang-display">FR</span>
          <span class="material-symbols-outlined text-[16px]">expand_more</span>
        </div>
        <!-- Dropdown -->
        <div class="absolute right-0 top-full mt-2 w-24 bg-surface-container-high border border-outline-variant shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 z-[60]">
          <div class="py-2 flex flex-col">
            <button onclick="setLanguage('fr')" class="font-label-caps text-label-caps tracking-widest uppercase text-left px-4 py-2 hover:bg-surface-variant hover:text-secondary text-primary transition-colors">FR</button>
            <button onclick="setLanguage('en')" class="font-label-caps text-label-caps tracking-widest uppercase text-left px-4 py-2 hover:bg-surface-variant hover:text-secondary text-primary transition-colors">EN</button>
            <button onclick="setLanguage('es')" class="font-label-caps text-label-caps tracking-widest uppercase text-left px-4 py-2 hover:bg-surface-variant hover:text-secondary text-primary transition-colors">ES</button>
          </div>
        </div>
      </div>
    </div>
  </div>
  
  <!-- Mobile Menu Dropdown -->
  <div id="mobile-menu" class="hidden md:hidden bg-surface dark:bg-background border-t border-outline-variant px-margin-mobile py-4 flex flex-col space-y-4">
      <a data-i18n="nav_boutique" class="font-label-caps text-label-caps text-on-surface-variant tracking-widest uppercase hover:text-secondary transition-colors duration-300" href="boutique.html">Boutique</a>
      <a data-i18n="nav_collections" class="font-label-caps text-label-caps text-on-surface-variant tracking-widest uppercase hover:text-secondary transition-colors duration-300" href="collections.html">Collections</a>
      <a data-i18n="nav_atelier" class="font-label-caps text-label-caps text-on-surface-variant tracking-widest uppercase hover:text-secondary transition-colors duration-300" href="atelier.html">ATELIER</a>
      <a data-i18n="nav_contact" class="font-label-caps text-label-caps text-on-surface-variant tracking-widest uppercase hover:text-secondary transition-colors duration-300" href="contact.html">Contact</a>
  </div>
</nav>'''

replacements = [
    (r'<nav class="sticky top-0 z-50 bg-surface dark:bg-background w-full transition-all duration-300" id="main-nav">.*?</nav>', nav_html),
    
    # Common Footer
    (r'© 2026 TERRIEUX CERAMICS\. TOUS DROITS RÉSERVÉS\.', r'<span data-i18n="footer_copyright">© 2026 TERRIEUX CERAMICS. TOUS DROITS RÉSERVÉS.</span>'),
    
    # index.html
    (r'>\s*Un artisanat silencieux\.\s*</h1>', r' data-i18n="index_title">Un artisanat silencieux.</h1>'),
    (r'>\s*Découvrez des objets singuliers, nés de la terre et façonnés par le temps\.\s*</p>', r' data-i18n="index_subtitle">Découvrez des objets singuliers, nés de la terre et façonnés par le temps.</p>'),
    (r'>\s*DÉCOUVRIR LES COLLECTIONS\s*</a>', r' data-i18n="index_cta">DÉCOUVRIR LES COLLECTIONS</a>'),
    (r'>\s*L\'ARTISANAT\s*</h3>', r' data-i18n="index_artisanat_label">L\'ARTISANAT</h3>'),
    (r'>\s*Chaque pièce est unique, porteuse des empreintes de sa création\. Un design minimaliste, ancré dans l\'authenticité de la matière\.\s*</p>', r' data-i18n="index_artisanat_desc">Chaque pièce est unique, porteuse des empreintes de sa création. Un design minimaliste, ancré dans l\'authenticité de la matière.</p>'),
    (r'>\s*L\'ÉMOTION MATÉRIELLE\s*</h3>', r' data-i18n="index_emotion_label">L\'ÉMOTION MATÉRIELLE</h3>'),
    (r'>\s*Des textures brutes et des formes organiques qui invitent au toucher\. Une célébration de l\'imperfection naturelle\.\s*</p>', r' data-i18n="index_emotion_desc">Des textures brutes et des formes organiques qui invitent au toucher. Une célébration de l\'imperfection naturelle.</p>'),
    (r'>\s*L\'ATELIER\s*</h3>', r' data-i18n="index_atelier_label">L\'ATELIER</h3>'),
    (r'>\s*Découvrez le sanctuaire où la terre prend vie\. Un espace de création dédié au slow design et à la pleine conscience\.\s*</p>', r' data-i18n="index_atelier_desc">Découvrez le sanctuaire où la terre prend vie. Un espace de création dédié au slow design et à la pleine conscience.</p>'),

    # collections.html
    (r'>\s*Collections\s*</h1>', r' data-i18n="collections_title">Collections</h1>'),
    (r'>\s*Vaisselle sculpturale, objets décoratifs et pièces artistiques composent des collections pensées pour habiter les espaces avec caractère, calme et authenticité\.\s*</p>', r' data-i18n="collections_subtitle">Vaisselle sculpturale, objets décoratifs et pièces artistiques composent des collections pensées pour habiter les espaces avec caractère, calme et authenticité.</p>'),

    # atelier.html
    (r'>\s*L\'Atelier &amp; L\'Artisan\s*</h1>', r' data-i18n="atelier_title">L\'Atelier &amp; L\'Artisan</h1>'),
    (r'>\s*Un sanctuaire du slow design, où l\'émotion se révèle dans la matière brute\s*</p>', r' data-i18n="atelier_subtitle">Un sanctuaire du slow design, où l\'émotion se révèle dans la matière brute</p>'),
    (r'>\s*Antony, Le Céramiste\s*</h2>', r' data-i18n="atelier_antony_title">Antony, Le Céramiste</h2>'),
    (r'>\s*Antony Terrieux crée des pièces céramiques uniques où la terre devient texture, mouvement et présence\. Son univers artistique puise dans les formes organiques, les matières brutes et une esthétique minimaliste profondément contemporaine\. Chaque création est façonnée à la main avec une attention particulière portée à l’équilibre, aux sensations et aux détails\.\s*</p>', r' data-i18n="atelier_antony_desc">Antony Terrieux crée des pièces céramiques uniques où la terre devient texture, mouvement et présence. Son univers artistique puise dans les formes organiques, les matières brutes et une esthétique minimaliste profondément contemporaine. Chaque création est façonnée à la main avec une attention particulière portée à l’équilibre, aux sensations et aux détails.</p>'),
    (r'>\s*Savoir-Faire\s*</h2>', r' data-i18n="atelier_savoir_title">Savoir-Faire</h2>'),
    (r'>\s*La Matière\s*</h3>', r' data-i18n="atelier_matiere_title">La Matière</h3>'),
    (r'>\s*Une sélection rigoureuse des grès et porcelaines, choisis pour leurs qualités tactiles et leur capacité à capter la lumière\.\s*</p>', r' data-i18n="atelier_matiere_desc">Une sélection rigoureuse des grès et porcelaines, choisis pour leurs qualités tactiles et leur capacité à capter la lumière.</p>'),
    (r'>\s*Le Geste\s*</h3>', r' data-i18n="atelier_geste_title">Le Geste</h3>'),
    (r'>\s*Le tournage est abordé comme une méditation\. Chaque courbe est intentionnelle, cherchant l\'équilibre parfait entre force et fragilité\.\s*</p>', r' data-i18n="atelier_geste_desc">Le tournage est abordé comme une méditation. Chaque courbe est intentionnelle, cherchant l\'équilibre parfait entre force et fragilité.</p>'),
    (r'>\s*La Patience\s*</h3>', r' data-i18n="atelier_patience_title">La Patience</h3>'),
    (r'>\s*Le temps est le principal ingrédient\. Du séchage lent aux multiples cuissons à haute température, la céramique enseigne l\'humilité\.\s*</p>', r' data-i18n="atelier_patience_desc">Le temps est le principal ingrédient. Du séchage lent aux multiples cuissons à haute température, la céramique enseigne l\'humilité.</p>'),

    # contact.html
    (r'>\s*Contact\s*</h1>', r' data-i18n="contact_title">Contact</h1>'),
    (r'>\s*Créations artisanales, collaborations artistiques et commandes sur mesure disponibles sur demande\.\s*</p>', r' data-i18n="contact_subtitle">Créations artisanales, collaborations artistiques et commandes sur mesure disponibles sur demande.</p>'),
    (r'>\s*Réseaux Sociaux\s*</h3>', r' data-i18n="contact_social_title">Réseaux Sociaux</h3>'),
    (r'>\s*Retrouvez les dernières créations sur instagram :\s*</p>', r' data-i18n="contact_social_desc">Retrouvez les dernières créations sur instagram :</p>'),
    (r'>\s*Studio\s*</h3>', r' data-i18n="contact_studio_title">Studio</h3>'),
    (r'>\s*Seulement sur rendez-vous\s*</p>', r' data-i18n="contact_studio_desc">Seulement sur rendez-vous</p>'),
    (r'>\s*Direct\s*</h3>', r' data-i18n="contact_direct_title">Direct</h3>'),
    (r'>Nom</label>', r' data-i18n="contact_form_name">Nom</label>'),
    (r'placeholder="Votre nom"', r'placeholder="Votre nom" data-i18n="contact_form_name_ph"'),
    (r'>Email</label>', r' data-i18n="contact_form_email">Email</label>'),
    (r'placeholder="adresse@email\.com"', r'placeholder="adresse@email.com" data-i18n="contact_form_email_ph"'),
    (r'>Type de projet</label>', r' data-i18n="contact_form_project">Type de projet</label>'),
    (r'>Sélectionner une option\.\.\.</option>', r' data-i18n="contact_form_select">Sélectionner une option...</option>'),
    (r'>Commande personnalisée</option>', r' data-i18n="contact_form_opt1">Commande personnalisée</option>'),
    (r'>Collaboration</option>', r' data-i18n="contact_form_opt2">Collaboration</option>'),
    (r'>Autre</option>', r' data-i18n="contact_form_opt3">Autre</option>'),
    (r'>Message</label>', r' data-i18n="contact_form_message">Message</label>'),
    (r'placeholder="Comment pouvons-nous vous aider \?"', r'placeholder="Comment pouvons-nous vous aider ?" data-i18n="contact_form_placeholder"'),
    (r'>ENVOYER LE MESSAGE</button>', r' data-i18n="contact_form_submit">ENVOYER LE MESSAGE</button>'),
]

for filename in files:
    path = os.path.join(base_dir, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply replacements
    for pattern, repl in replacements:
        content = re.sub(pattern, repl, content, flags=re.DOTALL)
    
    # Ensure i18n.js script is included before </body>
    if '<script src="js/i18n.js"></script>' not in content:
        content = content.replace('</body>', '<script src="js/i18n.js"></script>\n</body>')
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("i18n integration applied successfully.")
