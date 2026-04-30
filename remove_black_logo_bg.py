"""
Remueve el fondo NEGRO del logo de La Mati para usarlo como pattern transparente.

Usa flood-fill desde los bordes igual que remove_white_bg.py pero al reves
(busca pixels casi-negros en vez de casi-blancos). Asi el flame ambar y el texto
se preservan, y solo el square negro de fondo se vuelve transparente.

Lee de   : Logo del restaurante La Mati.png
Guarda en: logo-transparent.png
"""
from collections import deque
from pathlib import Path
import numpy as np
from PIL import Image, ImageFilter

ROOT = Path(__file__).parent
SRC  = ROOT / "Logo del restaurante La Mati.png"
DST  = ROOT / "logo-transparent.png"

BLACK_THRESHOLD = 28  # max(R,G,B) <= esto = candidato a fondo negro


def flood_fill_borders(is_black: np.ndarray) -> np.ndarray:
    """BFS desde el borde, devuelve mask de fondo conectado."""
    h, w = is_black.shape
    visited = np.zeros((h, w), dtype=bool)
    q = deque()
    for x in range(w):
        if is_black[0, x] and not visited[0, x]: visited[0, x] = True; q.append((0, x))
        if is_black[h-1, x] and not visited[h-1, x]: visited[h-1, x] = True; q.append((h-1, x))
    for y in range(h):
        if is_black[y, 0] and not visited[y, 0]: visited[y, 0] = True; q.append((y, 0))
        if is_black[y, w-1] and not visited[y, w-1]: visited[y, w-1] = True; q.append((y, w-1))
    while q:
        y, x = q.popleft()
        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and is_black[ny, nx] and not visited[ny, nx]:
                visited[ny, nx] = True
                q.append((ny, nx))
    return visited


img = Image.open(SRC).convert("RGBA")
arr = np.array(img)
rgb = arr[..., :3].astype(np.int16)
max_ch = rgb.max(axis=2)

# Pixels donde TODOS los canales son <= threshold = casi negro
is_black = max_ch <= BLACK_THRESHOLD

# Solo los negros conectados al borde son fondo (preserva sombras internas del flame)
bg_mask = flood_fill_borders(is_black)

# Cierre morfologico para tapar agujeros pequeños
fg_mask = ~bg_mask
fg_img = Image.fromarray((fg_mask.astype(np.uint8) * 255), "L")
fg_closed = fg_img.filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.MinFilter(3))
fg_mask_closed = np.array(fg_closed) > 127

alpha = np.full((arr.shape[0], arr.shape[1]), 255, dtype=np.uint8)
alpha[~fg_mask_closed] = 0

img_out = Image.fromarray(np.dstack([arr[..., :3], alpha]), "RGBA")
a_band = img_out.split()[-1].filter(ImageFilter.GaussianBlur(0.5))
img_out.putalpha(a_band)

img_out.save(DST, "PNG", optimize=True)
bg_pct = 100 * bg_mask.sum() / bg_mask.size
print(f"[ok] {SRC.name}  ->  {DST.name}  (fondo negro: {bg_pct:.1f}%)")
