"""
Prepara carpeta deploy/ con nombres de archivo URL-safe
y actualiza las rutas en index.html automáticamente.
"""
import os
import shutil

BASE   = os.path.dirname(os.path.abspath(__file__))
DEPLOY = os.path.join(BASE, "deploy")

# Mapa: archivo original -> nombre seguro en deploy/
FILES = {
    "Logo del restaurante La Mati.png": "logo-la-mati.png",
    "Platos de La Mati/Salchipapa Clasica.png":        "img/salchipapa-clasica.png",
    "Platos de La Mati/Salchipollo.png":               "img/salchipollo.png",
    "Platos de La Mati/Salchipapa Arequipeña.png":"img/salchipapa-arequipena.png",
    "Platos de La Mati/Salchipapa Royal Especial.png": "img/salchipapa-royal-especial.png",
    "Platos de La Mati/Salchipapa Francesa.png":       "img/salchipapa-francesa.png",
    "Platos de La Mati/Salchipapa Americana.png":      "img/salchipapa-americana.png",
    "Platos de La Mati/Salchipapa Andina.png":         "img/salchipapa-andina.png",
}

# Mapa de reemplazos en el HTML (original src -> nuevo src)
HTML_REPLACEMENTS = {
    'src="Logo del restaurante La Mati.png"':              'src="logo-la-mati.png"',
    'src="Platos de La Mati/Salchipapa Clasica.png"':      'src="img/salchipapa-clasica.png"',
    'src="Platos de La Mati/Salchipollo.png"':             'src="img/salchipollo.png"',
    'src="Platos de La Mati/Salchipapa%20Arque%C3%B1a.png"':'src="img/salchipapa-arequipena.png"',
    'src="Platos de La Mati/Salchipapa Royal Especial.png"':'src="img/salchipapa-royal-especial.png"',
    'src="Platos de La Mati/Salchipapa Francesa.png"':     'src="img/salchipapa-francesa.png"',
    'src="Platos de La Mati/Salchipapa Americana.png"':    'src="img/salchipapa-americana.png"',
    'src="Platos de La Mati/Salchipapa Andina.png"':       'src="img/salchipapa-andina.png"',
}

# Crear carpeta deploy
if os.path.exists(DEPLOY):
    shutil.rmtree(DEPLOY)
os.makedirs(os.path.join(DEPLOY, "img"), exist_ok=True)

# Copiar imágenes con nombres seguros
for src_rel, dst_rel in FILES.items():
    src = os.path.join(BASE, src_rel)
    dst = os.path.join(DEPLOY, dst_rel)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"  OK  {src_rel}  ->  {dst_rel}")
    else:
        print(f"  !!  NO ENCONTRADO: {src_rel}")

# Leer index.html y reemplazar rutas
html_path = os.path.join(BASE, "index.html")
with open(html_path, encoding="utf-8") as f:
    html = f.read()

for old, new in HTML_REPLACEMENTS.items():
    html = html.replace(old, new)

# Guardar index.html en deploy/
out_path = os.path.join(DEPLOY, "index.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"\n  index.html guardado en deploy/")
print(f"\nCarpeta deploy/ lista en: {DEPLOY}")
print("Puedes arrastrarla a https://netlify.com/drop para publicarla.")
