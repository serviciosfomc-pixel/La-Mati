"""
Convierte fondo blanco a transparente, preservando blancos internos.

Algoritmo:
  1. Detecta pixels "casi blancos" (min(R,G,B) >= WHITE_THRESHOLD).
  2. BFS desde TODOS los pixels del borde de la imagen.
  3. Solo los pixels blancos conectados al borde via otros blancos se vuelven transparentes.
  4. Blancos internos (bowl, yema, queso, salsas claras) se preservan.
  5. Gaussian blur 0.8 px al canal alpha para evitar bordes dentados.

Lee de   : Platos de la mati sin fondo/   (originales con fondo blanco)
Guarda en: Platos transparentes/           (sobrescribe la version anterior)
"""
from collections import deque
from pathlib import Path
import numpy as np
from PIL import Image, ImageFilter

ROOT  = Path(__file__).parent
SRC   = ROOT / "Platos de la mati sin fondo"
DST   = ROOT / "Platos transparentes"
DST.mkdir(exist_ok=True)

WHITE_THRESHOLD = 250  # min(R,G,B) >= esto = candidato a fondo (muy estricto: blanco casi puro)
SATURATION_MAX  = 8    # max(R,G,B) - min(R,G,B) <= esto = pixel realmente neutro/blanco


def flood_fill_borders(is_white: np.ndarray) -> np.ndarray:
    """BFS desde el borde, devuelve mask de fondo conectado."""
    h, w = is_white.shape
    visited = np.zeros((h, w), dtype=bool)
    q = deque()

    # Sembrar desde los 4 bordes
    for x in range(w):
        if is_white[0, x] and not visited[0, x]:
            visited[0, x] = True; q.append((0, x))
        if is_white[h-1, x] and not visited[h-1, x]:
            visited[h-1, x] = True; q.append((h-1, x))
    for y in range(h):
        if is_white[y, 0] and not visited[y, 0]:
            visited[y, 0] = True; q.append((y, 0))
        if is_white[y, w-1] and not visited[y, w-1]:
            visited[y, w-1] = True; q.append((y, w-1))

    # BFS 4-conexo
    while q:
        y, x = q.popleft()
        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and is_white[ny, nx] and not visited[ny, nx]:
                visited[ny, nx] = True
                q.append((ny, nx))
    return visited


def process(path_src: Path, path_dst: Path) -> None:
    img = Image.open(path_src).convert("RGBA")
    arr = np.array(img)
    rgb = arr[..., :3].astype(np.int16)
    min_ch = rgb.min(axis=2)
    max_ch = rgb.max(axis=2)
    saturation = max_ch - min_ch  # 0 = gris/blanco puro

    # Mask: blancos PUROS (luminoso Y neutro). Asi el rim del bowl que tiene tinte (sombra)
    # NO se clasifica como fondo aunque sea claro.
    is_white = (min_ch >= WHITE_THRESHOLD) & (saturation <= SATURATION_MAX)

    # Solo blancos conectados al borde son fondo real
    bg_mask = flood_fill_borders(is_white)

    # Cierre morfologico: rellena agujeros chicos en el foreground (1-2 px)
    fg_mask = ~bg_mask
    fg_img = Image.fromarray((fg_mask.astype(np.uint8) * 255), "L")
    # Dilation 1px luego erosion 1px = closing
    fg_closed = fg_img.filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.MinFilter(3))
    fg_mask_closed = np.array(fg_closed) > 127

    # Aplicar transparencia
    alpha = np.full((arr.shape[0], arr.shape[1]), 255, dtype=np.uint8)
    alpha[~fg_mask_closed] = 0

    # Suavizar el borde del alpha (anti-alias muy ligero)
    img_out = Image.fromarray(np.dstack([arr[..., :3], alpha]), "RGBA")
    a_band = img_out.split()[-1].filter(ImageFilter.GaussianBlur(0.4))
    img_out.putalpha(a_band)

    img_out.save(path_dst, "PNG", optimize=True)
    bg_pct = 100 * (~fg_mask_closed).sum() / fg_mask_closed.size
    print(f"  [ok] {path_src.name}  ->  {path_dst.relative_to(ROOT)}  (fondo: {bg_pct:.1f}%)")


def main() -> None:
    files = sorted(SRC.glob("*.png"))
    if not files:
        print(f"No se encontraron PNGs en {SRC}")
        return
    print(f"Procesando {len(files)} imagenes con flood-fill desde bordes...")
    for f in files:
        process(f, DST / f.name)
    print(f"Listo. Salida: {DST}")


if __name__ == "__main__":
    main()
