# MATI — Memoria del Proyecto La Mati

> Archivo de contexto persistente. Cada cambio importante se registra aquí para mantener continuidad entre sesiones.

---

## Identidad del proyecto

- **Nombre comercial:** La Mati — Salchipapería
- **Ciudad:** **Arequipa, Perú** (cambiado de Lima a Arequipa el 2026-04-28)
- **RUC:** **20610692096**
- **Distritos de delivery referenciados:** Cayma, Yanahuara, Cerro Colorado, Cercado
- **Producto estrella:** Salchipapas con papa nativa (350g) y salsas artesanales
- **Canales de delivery:** Rappi, PedidosYa, WhatsApp
- **WhatsApp / Instagram (oficial):** `+51 922 953 468` · `@lamati_rest` (visto en posters de salsas — pendiente actualizar en `wa.me/...` del HTML)
- **Bebidas: Chicha Morada Casera** — 480 ml a S/. 2.00 · 1 litro a S/. 4.00. Ingredientes: maíz morado, clavo de olor, canela, piña, manzana y membrillo. 100% natural sin químicos.
- **Archivo principal:** `index.html` (página única)
- **Logo:** `Logo del restaurante La Mati.png`
- **Imágenes de platos (vigentes):** carpeta `Platos transparentes/` (PNG con transparencia real, archivos `1.png` … `7.png`). Generadas por script `remove_white_bg.py`.
- **Imágenes intermedias:** carpeta `Platos de la mati sin fondo/` (PNG con fondo blanco, son la fuente para el script). No se referencian directamente en HTML.
- **Imágenes deprecadas:** carpeta `Platos de La Mati/` (con fondo, ya no se usan).
- **Script de procesamiento:** `remove_white_bg.py` — convierte el blanco del fondo a alpha=0 con borde anti-alias suave, usa numpy + PIL.

---

## Paleta de colores (INMUTABLE — La Mati DNA)

| Variable    | HEX        | Uso                                |
|-------------|------------|------------------------------------|
| `--black`   | `#080808`  | Fondo principal                    |
| `--dark`    | `#111111`  | Secciones secundarias              |
| `--card`    | `#161616`  | Tarjetas / containers              |
| `--gold`    | `#FFB800`  | Acento principal, CTAs, precios    |
| `--amber`   | `#C97D20`  | Acento secundario, gradientes      |
| `--white`   | `#FFFFFF`  | Texto principal                    |
| `--muted`   | `rgba(255,255,255,0.52)` | Texto secundario     |
| `--border`  | `rgba(255,255,255,0.07)` | Separadores          |

**Regla:** Aunque cambie el estilo visual (KFC, McDonald's, etc.), la paleta SIEMPRE se mantiene. El "rojo KFC" se reemplaza por `--gold` / `--amber`.

---

## Tipografías

- **Sans / display bold:** `Inter` (300–800)
- **Serif itálico decorativo:** `Playfair Display`
- En estilo KFC: títulos en MAYÚSCULAS con `font-weight: 800/900` y `letter-spacing` apretado.

---

## Inventario de imágenes (sin fondo) — `Platos de la mati sin fondo/`

| Archivo | Plato | Ingredientes visibles |
|---------|-------|------------------------|
| `1.png` | Salchipapa Clásica | Papa nativa + salchicha Frankfürt en rodajas |
| `2.png` | Salchipollo | Papa + salchicha + pollo desmenuzado abundante |
| `3.png` | Salchipapa Arequipeña | Papa + salchicha arequipeña en rodajas grandes color claro |
| `4.png` | SalchiRoyal Especial | Papa + salchicha + pollo desmenuzado + huevo frito |
| `5.png` | Salchipapa Francesa | Papa + salchicha + pollo + queso amarillo derretido |
| `6.png` | Salchipapa Americana | Papa + salchicha + tocino + huevo frito |
| `7.png` | Salchipapa Andina | Papa + salchicha + chorizo finas hierbas + pollo |

**Importante:** son PNG con fondo transparente. En el HTML se renderizan con `object-fit: contain`, padding y `drop-shadow` sobre fondos con radial gradients dorados/ámbar para que el plato "flote" sobre el negro.

## Mapa de secciones → imagen (estado actual)

1. **Top bar** — sin imágenes
2. **Header sticky** — Logo La Mati
3. **Hero carrusel** — Slide 1 Andina (`7.png`), Slide 2 Francesa (`5.png`), Slide 3 Americana (`6.png`)
4. **Categorías** (5 cards): Clásicas `1` · Especiales `4` · Para Compartir `7` · Con Queso `5` · Con Pollo `2`
5. **Banner promo "2x1 martes"** — Clásica `1.png`
6. **Productos destacados** (8 cards): Clásica `1` · Royal `4` · Americana `6` · Salchipollo `2` · Arequipeña `3` · Francesa `5` · Andina `7` · Combo Familia `7`
7. **Bucket Familiar** — Andina `7.png`
8. **Locator** — sin imágenes
9. **App móvil** — Logo La Mati (mockup)
10. **Trabaja con nosotros** — sin imágenes
11. **Footer** — Logo La Mati

## Bitácora de cambios

### 2026-05-24 — v24: Nuevos precios + Francesa TOP + reorden secciones + chicha solo 1L
- **Trigger:** Cuatro ajustes pedidos por el usuario:
  1. Actualización de precios de platos.
  2. Francesa ahora es el plato más caro → badge "★ TOP" + diseño premium (borde dorado, glow intensificado).
  3. Sección Productos Estrella sube (va después del Hero); Categorías Destacadas baja (va después de Productos, junto a la venta de platos).
  4. Solo hay chicha morada de 1 litro — se elimina la variante 480 ml en toda la página.
- **Nuevos precios:**
  | Plato | Antes | Ahora |
  |-------|-------|-------|
  | Clásica | S/. 12.50 | S/. 13.00 |
  | SalchiRoyal Especial | S/. 15.00 | S/. 15.50 |
  | Americana | S/. 15.00 | S/. 15.00 (sin cambio) |
  | Salchipollo | S/. 13.00 | S/. 14.50 |
  | Arequipeña | S/. 13.00 | S/. 14.00 |
  | Francesa Especial | S/. 16.00 | S/. 18.00 |
  | Andina | S/. 16.50 | S/. 16.50 (sin cambio) |
- **Francesa TOP:**
  - Clase `.prod-card--top` nueva en CSS: borde gold 2px, box-shadow glow ámbar en hover, `prod-price` más grande con text-shadow dorado.
  - Badge cambiado de "Con queso" → **"★ TOP"** con gradiente gold-2→gold→amber.
  - Descripción actualizada: "Nuestro plato premium." añadido al final.
  - Hero slide 2 (Francesa): precio `S/16.00` → `S/18.00`, label "Con queso" → "Premium".
- **Reorden de secciones (nuevo orden):**
  1. Hero carrusel
  2. **Productos Estrella** (subió desde posición 4 → posición 2)
  3. **Categorías Destacadas** (bajó desde posición 2 → posición 3, junto a productos)
  4. Banner Club La Mati
  5. Bucket Familiar
  6. Toppings, Delivery, Salsas, etc.
- **Chicha morada — solo 1 litro:**
  - Eliminado botón "+ 480 ml · S/. 2" y variante `chicha-480` del JS PRODUCTS.
  - Precio de la card: "Desde S/. 2.00" → **S/. 4.00**.
  - Descripción actualizada: "Solo disponible en botella de 1 litro."
  - Alt text actualizado (quitada mención a 480 ml).
  - Bucket Familiar: "4 botellas de chicha morada 480 ml" → **"4 botellas de chicha morada 1 litro"**.
  - Combo Familia Mati card: mismo cambio.
- **Categorías actualizadas (precios):** Clásicas S/13 · Especiales S/15.50 · Con Queso S/18 · Con Pollo S/14.50.
- **Archivos modificados:** `index.html`, `memory.md`.

### 2026-04-28 — v23: Chicha visible + Toppings + Honey Mustard
- **Trigger:** Tres ajustes:
  1. La imagen de la chicha morada ocultaba las etiquetas laterales (maíz morado, piña, canela…) por usar `object-fit: cover`. Pidió "que esté un poco más atrás" para que se vean.
  2. Nueva sección de **Toppings (Porciones Adicionales)** con 6 items extras (estilo del flyer adjunto: precio dorado izq + nombre + línea punteada + descripción).
  3. Agregar **Honey Mustard** como 7ma salsa al carrusel.
- **Cambios:**
  - **Card chicha (`.prod-card.featured-wide .prod-img-wrap`):**
    - aspect-ratio 16/8 → **16/9** (más alto, más espacio vertical)
    - background con doble layer: viñeta radial oscura + var(--card-2)
    - imagen `object-fit: cover` → **`contain` con padding 14px** → se ve toda la foto incluyendo las etiquetas laterales con flechas
    - `::after` (gradient top oscuro) reducido a 50px y opacity 0.6 para no oscurecer las anotaciones top
  - **Nueva sección `.toppings`** entre Bucket Familiar y Delivery:
    - Header con "PORCIONES ADICIONALES" en chip dorado con `border-radius` orgánico irregular (efecto brush-stroke) rotado -1.5° y glow ámbar
    - Grid 2 cols en desktop, 1 col en mobile
    - 6 items con: precio gold itálico (1.5rem) | info (h4 uppercase + p descriptivo) | botón redondo `+` para agregar al carrito
    - Border-bottom dashed gold entre items, hover translate +2px
    - Botón `+` con sombra inferior tipo "botón físico" (4px amber)
  - **Catálogo del carrito:** se agregaron 6 productos `top-frank/papa/chorizo/cremas/huevo/arequip` (S/. 0.50–5.00). Thumbnail = logo-transparent.png (placeholder branded).
  - **Carrusel de salsas:** ahora 7 slides (era 6). Nuevo slide "Honey Mustard" con tag "Nuevo ingreso", chips de ingredientes (mostaza, miel, vinagre suave). Apunta a `Salsas de La Mati/Honey Mustard.jpg` que el usuario debe guardar manualmente. Dots actualizados a 7.
- **Pendiente del usuario:** guardar la imagen de Honey Mustard como `Salsas de La Mati/Honey Mustard.jpg`.
- **Estructura actual (12 secciones):** Top bar → Header → Hero → Categorías → Banner Club → Productos estrella → Bucket Familiar → **🆕 Toppings** → Delivery → Salsas (7 slides ahora) → Trabaja → Footer.
- **Archivo modificado:** `index.html`, `memory.md`.

### 2026-04-28 — v22: Categorías con fondo negro y borde dorado
- **Trigger:** Usuario pidió 3 cosas para los cards de Categorías Destacadas:
  1. Agrandar los platos (imágenes circulares)
  2. Fondo del card en negro sólido
  3. Borde de cada card en amarillo (gold) de la paleta
- **Cambios CSS `.cat-card`:**
  - Background: `var(--card)` (#161616) → **`var(--black)`** (#080808 sólido)
  - Border: `1px solid var(--border)` (sutil) → **`2px solid var(--gold)`** (dorado prominente)
  - Border-radius: 14px → 16px (más generoso)
  - Padding: 22/18/24 → 28/22/30 (más respiración)
  - Box-shadow nuevo: `0 4px 16px rgba(0,0,0,0.45)` para flotar sobre el fondo
  - Hover: borde a `gold-2` + glow dorado triple-stack: `0 14px 36px rgba(255,184,0,0.28), 0 0 0 4px rgba(255,184,0,0.14)`. Translate -8px (era -6).
- **Cambios CSS `.cat-circle` (los platos):**
  - **Tamaño: 130px → 190px** (+46% más grandes)
  - Background base: `var(--bg)` → **`#000` sólido** (matchea el card)
  - Border: `var(--border)` → `rgba(255,255,255,0.08)` (sutil interno)
  - Padding: 6 → 8 px
  - Margin-bottom: 16 → 22 px
  - Drop-shadow del plato: 6/10 → 8/14 (más profundidad)
- **Texto debajo del plato:**
  - h3: 0.92rem → 1.02rem
  - p: 0.76rem → 0.82rem, font-weight 600 (más legible)
- **Responsive:**
  - **Tablet `<= 1100px`:** circle 130 → **170px** (3 cols, sigue grande)
  - **Mobile `<= 760px`:** circle 100 → **140px** (2 cols), padding card reducido a 22/16/24, gap 12 → 14
- **Resultado:** los platos ahora se ven mucho más grandes y prominentes, cada card es un "frame" claramente delimitado por su borde dorado (parece marco de cuadro/menú de restaurante premium), y el contraste fondo-negro vs borde-gold es muy alto.
- **Archivo modificado:** `index.html`, `memory.md`.

### 2026-04-28 — v21: Hero text gigante (rellena el espacio vacío)
- **Trigger:** Usuario marcó con rojo el espacio vacío arriba/al lado/abajo del bloque de texto del hero (Salchipapa Andina) y pidió agrandar las letras para ocupar todo ese espacio.
- **Cambios CSS `.slide-text`:**
  - `.slide-eyebrow`: 0.84rem → **1rem** (+19%), letter-spacing 0.2em → 0.24em, margin-bottom 24px → 32px. Línea decorativa antes 44px → 60px.
  - `.slide-text h1`: `clamp(3.4rem, 7.2vw, 6.4rem)` → **`clamp(4.4rem, 9.5vw, 8.4rem)`** (+30% en max). En desktop ancho ahora llega a 134 px (antes 102 px). El título ocupa más superficie horizontal y vertical.
  - `.slide-text p`: 1.12rem → **1.3rem**, max-width 500px → **600px**, margin-bottom 36px → 44px. Más texto visible, ocupa más al lado derecho del texto.
  - `.slide-actions .btn-lg`: padding 18/36 → **22/44**, font-size 1rem → 1.1rem.
  - `.slide-text` padding: 70/64 → **56/56/60** (menos top, mismo lateral). Compensa el contenido más alto.
- **Responsive `<= 760px`:**
  - hero height 640 → 680 px
  - h1 2.8rem → 3.2rem
  - eyebrow, p, buttons también ligeramente más grandes para mantener proporciones
- **Resultado:** el bloque de texto izquierdo del hero ahora ocupa visualmente el espacio que estaba vacío. El título se siente cinematográfico, la descripción se extiende más a la derecha (más cerca del plato), y los botones tienen más presencia.
- **Archivo modificado:** `index.html`, `memory.md`.

### 2026-04-28 — v20: Fondo de patrón LA MATI tileado (reemplaza liquid metal)
- **Trigger:** Usuario quiere fondo con patrón de logos LA MATI tileados (mostrado como referencia: logos repetidos en grilla rotada). Pidió quitar el "marco negro" del logo y conservar la paleta original (flame ámbar + texto blanco). Pidió animación y "genialidad".
- **Logo procesado:**
  - **Nuevo script `remove_black_logo_bg.py`** (vanilla, sin scipy): flood-fill 4-conexo desde los bordes para detectar el cuadrado negro que rodea al logo. `BLACK_THRESHOLD = 28` (max(R,G,B) ≤ 28 = casi negro). Cierre morfológico para tapar agujeros pequeños. Gaussian blur 0.5 al alpha para anti-alias.
  - **Output: `logo-transparent.png`** (74.9% del área era fondo negro). Flame ámbar y texto LA MATI cremoso preservados intactos.
- **Cambio del fondo (CSS):**
  - **Eliminados:** `.bg-shader-layer.layer-1` y `.layer-2` con sus radial-gradients liquid-metal y `@keyframes shaderFlowA`/`B`.
  - **Nuevos elementos:**
    - **`.bg-pattern`**: `background-image: url("logo-transparent.png")`, `background-repeat: repeat`, `background-size: 200px 200px`, `transform: rotate(-12deg)`, `opacity: 0.10`, `inset: -30%` (overflow para que la rotación no muestre esquinas).
    - **`.bg-glow`**: radial gradient ámbar central, `mix-blend-mode: screen`, `filter: blur(60px)`. Le da el "color movement" que tenía el liquid metal.
    - **`.bg-vignette`**: radial gradient `transparent → rgba(0,0,0,0.55)` para enfocar atención al centro y dar profundidad.
  - **`.bg-shader` (contenedor):** ahora con base `var(--black)` + 2 radial-gradients dorados sutiles en esquinas opuestas (warmth).
- **Animaciones:**
  - **`bgPatternDrift`** (90s linear infinite): mueve `background-position` de 0→400px en ambos ejes. Genera efecto de "scrolling endless" diagonal de los logos.
  - **`bgGlowPulse`** (10s ease-in-out alternate): el glow dorado central crece de 1× → 1.08× con opacity 0.45→0.85 + translate sutil. Le da "respiración" cálida al fondo.
- **Mantenido de v16:** las secciones siguen semi-transparentes (categories/featured/sauces a `rgba(13,13,13,0.55)`, bucket/app-section a `rgba(17,17,17,0.7)`) para que el patrón se vea por debajo.
- **a11y:** `.bg-pattern, .bg-glow { animation: none }` en `prefers-reduced-motion`.
- **Performance:** `will-change: background-position` y `will-change: opacity, transform`. No hay filter blur sobre el patrón (más liviano que el liquid metal anterior).
- **Archivos:**
  - Nuevo: `remove_black_logo_bg.py`, `logo-transparent.png`
  - Modificado: `index.html`, `memory.md`

### 2026-04-28 — v19: Carrito + checkout vía WhatsApp
- **Trigger:** Usuario quiere que los clientes puedan agregar productos a un carrito y al pagar se redirijan a WhatsApp con un mensaje del pedido formateado.
- **Implementación 100% vanilla JS, sin dependencias.**
- **Componentes nuevos:**
  - **Botón flotante (`.cart-fab`)**: bottom-right, dorado con sombra ámbar, ícono SVG de carrito, badge rojo con contador de items. Animación `cartBump` (escala 1.22) cada vez que se agrega algo.
  - **Drawer lateral (`.cart-drawer`)**: slide desde la derecha, 420px en desktop / 100% en mobile. Header con título + close X, body scrollable con items, footer con total + CTA "Pagar por WhatsApp" + link "Vaciar carrito".
  - **Item de carrito**: thumbnail 64×64 + nombre + precio + controles `−/qty/+` + botón remove. Border-bottom suave entre items.
  - **Overlay**: backdrop oscuro con blur 4px que cierra el drawer al click.
  - **Toast (`.cart-toast`)**: notificación bottom-right "✓ X agregado", auto-dismiss 2.2s.
  - **Empty state**: mensaje cuando el carrito está vacío + el botón "Pagar" se deshabilita (opacity 0.4).
- **Catálogo en JS (`PRODUCTS`):** 10 productos con id/name/price/img:
  - clasica, royal, americana, pollo, arequip, francesa, andina (salchipapas)
  - combo (Combo Familia Mati S/. 64.90)
  - chicha-480 (S/. 2) y chicha-1l (S/. 4) como variantes separadas
- **Integración con UI existente:**
  - Las **8 cards** de productos estrella tienen ahora `data-product="<id>"` en el botón "Añadir".
  - La **chicha card** ya no tiene un solo botón "Añadir" — tiene **dos botones de variante** ("+ 480 ml · S/. 2" y "+ 1 L · S/. 4") que agregan productos distintos al carrito.
  - Los **3 botones del hero** ("Pedir Andina/Francesa/Americana") también tienen `data-product` y agregan al cart al click. Mantienen `href="#combos"` para que también haga scroll.
  - El botón **"Pedir por S/. 64.90"** del bucket familiar agrega `combo`.
  - Total: **14 botones** conectados al carrito.
- **Persistencia:** localStorage clave `lamati_cart_v1`. Al cargar la página, se restaura el carrito si existía. Si un id cambia o se elimina, se filtran los items inválidos automáticamente.
- **Checkout WhatsApp:**
  - Número: **+51 922 953 468** (extraído de los posters de salsas)
  - Formato del mensaje:
    ```
    Hola La Mati! Quiero hacer este pedido:

    • 2 × Salchipapa Clásica — S/. 25.00
    • 1 × SalchiRoyal Especial — S/. 15.00
    • 1 × Chicha Morada 480 ml — S/. 2.00

    Total: S/. 42.00

    ¡Gracias!
    ```
  - Se abre en pestaña nueva con `target="_blank"` + `noopener`.
- **A11y:** ESC cierra el drawer, aria-hidden, aria-label en todos los botones, `prefers-reduced-motion` ya cubierto por la regla global.
- **Archivo modificado:** `index.html`, `memory.md`.

### 2026-04-28 — v18: Banner Club: revert a yellow + gradiente menos intenso
- **Trigger:** El usuario prefirió el banner amarillo original (v6/v15) y rechazó el rediseño oscuro de v17. Solo pidió suavizar la intensidad del amarillo.
- **Cambios:**
  - **Revertidos TODOS los cambios estéticos de v17** (línea premium superior, fondo oscuro, texto blanco, eyebrow pill, text-shadow del título, doble glow del precio, btn-primary dorado, link con subrayado oro, filter brightness/contrast en imagen, sticker con doble ring). Vuelta al diseño v15.
  - **Único cambio mantenido en v18:** el gradiente del fondo. Antes era `linear-gradient(120deg, var(--gold) 0%, var(--amber) 100%)` (gold #FFB800 muy brillante → amber). Ahora es **`linear-gradient(120deg, var(--amber) 0%, #8a4d11 100%)`** — amber #C97D20 → marrón oscuro #8a4d11. Gradiente amarillento/cobre **menos saturado y sin el gold puro brillante**.
  - El gradiente lateral del borde izquierdo de la imagen también cambió de `var(--amber)` a `#8a4d11` para mantener consistencia (el funde con el lado derecho del nuevo gradiente, no con el viejo).
- **Resultado:** mismo diseño general (texto negro sobre amarillo, sticker negro con dorado, etc.) pero el amarillo ya no quema tanto los ojos. Tiene un tono cobre/ámbar más sofisticado.
- **Archivo modificado:** `index.html`, `memory.md`.

### 2026-04-28 — v17: Banner Club rediseñado (fuera el amarillo)
- **Trigger:** Usuario notó que el banner "Tu 5ta Salchipapa GRATIS" tenía fondo amarillo brillante que competía con el resto de la página (toda en oscuro/oro) y el texto se confundía. Pidió quitar el amarillo y hacer notar las letras y el logo.
- **Cambios CSS `.promo-banner`:**
  - **Fondo:** `linear-gradient(120deg, gold, amber)` (amarillo brillante) → **gradiente oscuro** `linear-gradient(135deg, var(--card), var(--black))` con dos radial-gradients sutiles dorados en esquinas opuestas para warmth.
  - **Borde:** añadido `1px solid rgba(255,184,0,0.22)` para definición.
  - **Línea premium superior:** nuevo `::after` con gradiente horizontal gold→gold-2→gold (3px) que se extiende como acento de "marca premium" al top del banner.
  - **Color general:** `#000` (sobre amarillo) → `var(--white)` (sobre oscuro).
  - **Eyebrow "Club La Mati":** chip negro→ ahora es un pill `rgba(255,184,0,0.14)` con borde dorado, texto `var(--gold)`. Más legible y consistente con el hero-tag.
  - **Título h3:** ahora blanco con `text-shadow: 0 2px 24px rgba(0,0,0,0.55)` para profundidad. Se lee MUY claro sobre el oscuro.
  - **Chip del precio "GRATIS":** sigue dorado pero con doble shadow — `box-shadow: 0 6px 0 amber, 0 14px 30px rgba(gold, 0.35)` que le da glow dorado.
  - **Body text:** `rgba(0,0,0,0.82)` → `rgba(255,255,255,0.78)` (legible). Las palabras `<strong>` resaltan en oro.
  - **Botón "Únete al Club":** ahora `gold` solid (no negro). Más punchy y consistente con CTAs principales del resto de la página.
  - **Link "¿Cómo funciona?":** subrayado dorado, hover lleva todo a oro.
  - **Borde izquierdo de imagen:** gradiente cambió de `amber → transparent` a `var(--black) → transparent` para fundir la foto con el banner oscuro (no clashear con amarillo).
  - **Sticker "5TA COMPRA / GRATIS":** se mantiene gold con ring negro doble (más visible sobre la foto y el contexto oscuro).
  - **Foto interior:** filter `brightness(1.05) contrast(1.05)` para hacer notar el LOGO LA MATI y los detalles de la salchipapa.
- **Resultado:** el banner ahora se siente parte del ecosistema oscuro de la página, con dorado SOLO en los acentos clave (eyebrow, precio, CTA, sticker). La imagen y el logo se ven más nítidos. Texto blanco sobre fondo oscuro = máxima legibilidad.
- **Archivo modificado:** `index.html`, `memory.md`.

### 2026-04-28 — v16: Fondo animado "liquid metal" CSS-only
- **Trigger:** Usuario pegó instrucciones de un componente React (`@paper-design/shaders-react` con `LiquidMetal`) para usar como fondo de página. El proyecto es vanilla HTML/CSS/JS — no React, no build, no Tailwind. Migrar a Next.js para un solo efecto = horas de trabajo + romper la simplicidad.
- **Decisión:** Implementar el **mismo efecto visual con CSS puro**, manteniendo la arquitectura actual y la paleta de La Mati.
- **Implementación:**
  - **Nuevo elemento `.bg-shader`** como primer hijo del `<body>`, con 2 capas (`.layer-1` y `.layer-2`) `position: fixed; inset: 0; z-index: -1`.
  - **Layer 1** — 3 radial-gradients en gold/amber (`#DC8129`, `#FFB800`, `#C97D20`), `filter: blur(80px) saturate(1.25)`, animación `shaderFlowA` 18s ease-in-out alternate (rotate ±2°, scale 1→1.06, translate hasta 2%, opacity 0.55→0.78).
  - **Layer 2** — 2 radial-gradients de highlights (`#FFD24A`, `#DC8129`), `mix-blend-mode: screen`, animación `shaderFlowB` 25s alternate-reverse para crear parallax/morph entre ambas.
  - **`html { background: var(--black); }`** y **`body { background: transparent; }`** para que el shader fixed se vea por debajo de todo.
  - **Secciones semi-transparentes** para que el efecto se vea a través:
    - `.categories`, `.featured`, `.sauces`: `rgba(13, 13, 13, 0.55)` (eran `var(--bg)` opaco)
    - `.bucket`, `.app-section`: `rgba(17, 17, 17, 0.7)` (eran `var(--dark)` opaco)
    - `.hero`, `footer` se mantienen sólidos (anclas visuales, máximo contraste con texto/imágenes)
    - `.prod-card`, `.combo-card`, `.test-card` siguen sólidas (legibilidad de contenido)
  - **`@media (prefers-reduced-motion)`**: animación deshabilitada, `opacity: 0.55` fija. Cumple a11y.
- **Comparativa con el componente React original:**
  - ✅ Mismo color base (HSL 29 77% 49% = #DC8129)
  - ✅ Mismo blur fuerte (~80px)
  - ✅ Misma sensación de "breathing" (rotation ±, scale 1.0→1.06)
  - ✅ Misma duración (~18-25s para movimiento orgánico)
  - ⚠️ Sin distortion shader real (CSS no puede deformar gradients orgánicamente). Se compensa con doble capa + mix-blend-mode + animaciones desfasadas.
- **Performance:** filter blur grande es costoso en GPU. Mitigado con `will-change: transform, opacity` y `inset: -20%` para evitar re-render de bordes durante animación.
- **Archivo modificado:** `index.html`, `memory.md`.

### 2026-04-28 — v15: Andina Mixta + chicha 480ml + nueva card Chicha Morada
- **Trigger:** Tres ajustes pedidos:
  1. La card Andina decía "Picante" — el plato realmente es **Mixta** (chorizo + pollo, no un plato necesariamente picante).
  2. La medida de la chicha era 430 ml — **es 480 ml** (corrección).
  3. Agregar un nuevo producto: **Chicha Morada Casera** con foto, ingredientes (todo natural) y dos formatos de venta (480 ml a S/. 2 / 1 litro a S/. 4).
- **Cambios HTML:**
  - **Card Andina (productos estrella, posición 7)**: tag `<span class="prod-tag hot">Picante</span>` → **`<span class="prod-tag">Mixta</span>`** (cambio de variante hot/roja a default/dorada también, porque "Mixta" no es "hot").
  - **Chicha en bucket section + Combo Familia card**: "430 ml" → **"480 ml"** (2 ocurrencias).
  - **Nueva card de bebida** al final del grid de productos:
    - Tag: **"100% Natural"**
    - Imagen: `Platos de La Mati/CHICHA MORADA.jpeg` (foto comercial con 3 botellas etiquetadas e ingredientes anotados)
    - Título: **Chicha Morada Casera**
    - Body: "Maíz morado, clavo de olor, canela, piña, manzana y membrillo. Sin químicos, sin colorantes — preparada cada mañana. Disponible en 480 ml a S/. 2 y 1 litro a S/. 4."
    - Precio destacado: **Desde S/. 2.00**
- **Nueva clase CSS `.prod-card.featured-wide`:** la card de chicha es la 9ª en un grid de 4 cols (8 perfectamente divisibles + 1 orphan). Para tratarlo como "spotlight" del nuevo producto, span 2 cols + aspect ratio horizontal 16:8 (en lugar de 4:3) para aprovechar la foto landscape de las 3 botellas. En tablet (3 cols) y mobile (2 cols), el span 2 sigue funcionando bien.
- **Datos persistidos en `Identidad del proyecto`:** WhatsApp oficial `+51 922 953 468`, Instagram `@lamati_rest`, info de chicha (precios + ingredientes).
- **Archivos:** `index.html`, `memory.md`.

### 2026-04-28 — v14: Hero más grande (texto, plato, precio)
- **Trigger:** Usuario pidió agrandar las letras, el plato y el precio del hero (primera sección).
- **Cambios CSS hero:**
  - `.hero` height: `clamp(440px, 68vh, 680px)` → **`clamp(540px, 80vh, 820px)`** (hero más alto)
  - `.slide-text` padding: `60px 56px` → `70px 64px`
  - **`.slide-text h1`** font-size: `clamp(2.6rem, 5.4vw, 4.6rem)` → **`clamp(3.4rem, 7.2vw, 6.4rem)`** (~40% más grande)
  - `.slide-eyebrow`: 0.74rem → 0.84rem, line-bar 36px → 44px
  - `.slide-text p`: 1rem → 1.12rem
  - `.slide-actions .btn-lg`: padding 16/32 → 18/36, font 0.92 → 1rem
  - **`.slide-img img`**: padding `18px` → `0` + animación con `scale(1.08)` añadido al floatPlate. El plato ahora ocupa más superficie del contenedor y se ve un 8% más grande.
  - Drop-shadows reforzados (36px de blur, glow dorado de 24px)
  - **`.slide-price`** badge: width/height **160px → 210px** (~30% más grande), strong font-size **1.9rem → 2.5rem**, small 0.62rem → 0.78rem, inset shadow más gruesa.
- **Responsive ajustado:** en `<= 760px` el hero pasa a 640px de alto, h1 a 2.8rem, badge a 130×130 con strong de 1.6rem (antes 110×110/1.4rem).
- **Archivo modificado:** `index.html`, `memory.md`.

### 2026-04-28 — v13: Nueva sección "Salsas Artesanales" con carrusel
- **Trigger:** Usuario subió 6 posters de salsas (PSD-style, vertical, dark con info y branding ya integrados) en `Salsas de La Mati/`. Quiere una nueva sección estilo carrusel del hero, ubicada cerca del final de la página.
- **Inventario `Salsas de La Mati/`:**
  - `Aji mati.jpg` — Ají amarillo + mayonesa + aceite + queso
  - `salsa de la casa.jpg` — Queso fundido + leche + ajo + cebolla caramelizada + pimentón
  - `Mayonesa.jpg` — Huevo + aceite + limón (preparada al momento)
  - `Ketchup.jpg`
  - `Mostaza.jpg`
  - `Salsa Tartara.jpg`
  - **Datos extra leídos del poster:** WhatsApp `+51 922 953 468`, Instagram `@lamati_rest`, Facebook `LA MATI`. Pendiente: actualizar el `wa.me/51999999999` de la sección delivery con este número real.
- **Nueva sección HTML:**
  - **Posición:** entre "Pide y disfruta" (delivery) y "Trabaja con nosotros".
  - **id:** `salsas`
  - **Título:** "Las 6 salsas que cambian tu salchipapa"
  - **Subtítulo:** "Recetas propias preparadas cada mañana. Sin conservantes, sin químicos — todo sabor."
  - **Mecánica:** 6 slides, 1 visible a la vez, auto-play 7s (un segundo más lento que el hero para que se distinga), arrows + dots, pausa en hover.
  - **Layout cada slide:** 2 columnas grid (text left, poster right). Texto incluye: tag dorado pulsante, título grande mayúsculas, descripción, **chips de ingredientes**, CTA "Pídela con tu salchipapa →".
- **Nuevas clases CSS:** `.sauces`, `.sauces-head`, `.sauces-carousel`, `.sauces-track`, `.sauce-slide`, `.sauce-text`, `.sauce-tag`, `.sauce-img`, `.sauce-ingredients`. Reutilizan `.hero-arrow` y `.hero-dots` existentes.
- **Refactor JS:** la función inline del hero se convirtió en **`initCarousel({trackId, prevId, nextId, dotsSel, intervalMs})`** genérica. Se llama 2 veces — hero (6s) y salsas (7s). Conserva auto-play, arrows, dots, pause-on-hover.
- **Responsive:** en `<= 1100px` los slides apilan verticalmente (texto arriba, poster abajo aspect 4/3 con padding). En `<= 760px` padding reducido, sección a 60px.
- **Estructura actual de la página (11 secciones):** Top bar → Header → Hero carrusel → Categorías → Banner Club → Productos estrella → Bucket Familiar → Pide y disfruta (delivery) → **🆕 Salsas Artesanales** → Trabaja con nosotros → Footer.
- **Archivo modificado:** `index.html`, `memory.md`.

### 2026-04-28 — v12: Bordes finos definitivos + chicha en card + Rappi/PedidosYa/WhatsApp
- **Trigger:** Tres ajustes finales:
  1. Aún quedaba un plato del hero con halo translúcido en el rim del bowl.
  2. La card "Combo Familia Mati" en productos estrella todavía decía "4 gaseosas" (solo se había corregido en bucket).
  3. La sección "App La Mati" tenía botones de App Store / Google Play, pero no existe app — debían ser botones de Rappi, PedidosYa y WhatsApp (que es la realidad operativa).
- **Cambios script `remove_white_bg.py`:**
  - `WHITE_THRESHOLD`: **246 → 250** (aún más estricto)
  - **Nuevo: `SATURATION_MAX = 8`** — un pixel se considera fondo solo si es luminoso Y neutro (max-min ≤ 8). Esto evita que el rim del bowl con sombra (que es claro pero ligeramente tintado) se clasifique como fondo.
  - **Nuevo: morphological closing** (MaxFilter 3 → MinFilter 3) sobre el foreground mask para tapar agujeros pequeños (1-2 px) que quedaban en la comida o el bowl.
  - **Resultado:** los rims ahora están sólidos en los 7 platos, sin halos.
- **Cambios HTML:**
  - **Card Combo Familia Mati**: "4 salchipapas, 4 gaseosas y pack de 6 salsas artesanales" → **"4 salchipapas, 4 botellas de chicha morada 430 ml y pack de 6 salsas"**
  - **Sección "App"** → reframed a **"Pide y disfruta · Tu salchipapa caliente en 30 minutos"**:
    - Eyebrow: "App La Mati" → **"Pide y disfruta"**
    - h2: "Pide más rápido desde tu celular" → **"Tu salchipapa caliente en 30 minutos"**
    - Body: "Descarga la app..." → **"Pide por tu app de delivery favorita o escríbenos por WhatsApp..."**
    - Perks: ahora sobre delivery (30 min, promos por app, atención WhatsApp)
    - **3 botones nuevos** (`.delivery-btn`):
      - **Rappi** (icon rojo `#FF2C55`, link a rappi.com.pe)
      - **PedidosYa** (icon rojo `#D80031`, "Y!" en blanco, link a pedidosya.com.pe)
      - **WhatsApp** (icon verde `#25D366` con SVG real, link `wa.me/51999999999` placeholder)
    - **Pendiente del usuario:** reemplazar el WhatsApp `51999999999` por su número real cuando lo tengan.
  - **CSS**: clase `.store-btn` reemplazada por `.delivery-btn` con variantes `.rappi`, `.pedidos`, `.whatsapp`. Cada variante usa color de marca para el ícono cuadrado, manteniendo el botón en oscuro/oro.
- **Archivos:** `remove_white_bg.py`, `Platos transparentes/*.png` (regenerados), `index.html`, `memory.md`.

### 2026-04-28 — v11: Club GRATIS + Combo familiar unificado + bordes finos
- **Trigger:** Tres ajustes pedidos:
  1. La 5ta salchipapa ahora es **gratis** (antes S/. 3.99).
  2. La foto del Combo Familia Mati (en productos estrella + bucket) cambió a una imagen **unificada sin divisiones de grilla**.
  3. Los bordes de los platos del hero tenían halo/transparencia parcial — había que afinarlos.
- **Cambios HTML:**
  - **Banner Club:**
    - Título: "Tu 5ta Salchipapa por S/. 3.99" → **"Tu 5ta Salchipapa GRATIS"**
    - Body: "...te la llevas a solo S/. 3.99..." → **"...totalmente gratis..."**
    - Sticker: "5TA COMPRA / S/. 3.99 / todo el año" → **"5TA COMPRA / GRATIS / todo el año"**
  - **Combo Familia Mati card** (productos estrella, posición 8): `Salchipapa Andina.png` → **`Combo familiar.png`** (4 platos juntos en mesa de madera, sin grid)
  - **Bucket section**: `pack-familiar.jpg` (versión 2×2 con líneas blancas separadoras) → **`Combo familiar.png`** (versión unificada en mesa de madera)
- **Cambios script `remove_white_bg.py`:**
  - `WHITE_THRESHOLD`: **235 → 246** (más estricto: solo blanco casi-puro cuenta como fondo)
  - Gaussian blur alpha: **0.8 → 0.4 px** (anti-alias más sutil, bordes más nítidos)
  - **Resultado:** Los rims de los bowls dejaron de tener halos translúcidos. Edges definidos sin perder anti-alias natural.
- **Archivos:** `index.html`, `remove_white_bg.py`, `Platos transparentes/*.png` (regenerados los 7), `memory.md`.
- **Archivo "huérfano":** `Platos de La Mati/pack-familiar.jpg` (versión grid 2×2) ya no se referencia. Se mantiene en disco por backup; se puede borrar manualmente si quieres limpiar.

### 2026-04-28 — v10: Fix huecos en transparencias + concepto "5ta compra"
- **Trigger 1:** Usuario notó huecos visibles dentro de los platos del hero (en la Francesa especialmente — el queso y el bowl tenían transparencias internas indebidas).
- **Causa raíz:** El script v5 (`remove_white_bg.py`) usaba un threshold de luminancia que eliminaba TODOS los pixels casi-blancos, incluidos: bowl interior, yema/clara del huevo, queso amarillo claro, salsas claras, etc.
- **Fix:** Reescrito el script con algoritmo de **flood-fill desde bordes** (BFS 4-conexo). Ahora solo se vuelven transparentes los pixels casi-blancos **conectados al borde de la imagen** (= fondo verdadero). Los blancos internos (bowl, yema, queso) se preservan porque están aislados por pixels de comida que rompen la conectividad.
- **Algoritmo nuevo:**
  1. `is_white = min(R,G,B) >= 235`
  2. BFS desde los 4 bordes de la imagen
  3. `bg_mask` = solo blancos alcanzables desde el borde
  4. `alpha[bg_mask] = 0`
  5. Gaussian blur 0.8 px al canal alpha (anti-alias)
- **Resultado:** Reportes de % de fondo detectado: Francesa 52.4% (antes ~95% por agresivo), Americana 65.8%, etc. Ratios coherentes con un plato centrado.
- **Trigger 2:** Usuario quiere reformular el banner: en lugar de "2da clásica a S/. 3.99 los martes", el concepto es "tu 5ta compra a S/. 3.99" (programa de fidelización tipo cartilla de stickers, pero **digital**).
- **Cambios banner:**
  - Eyebrow: "Martes del Club" → **"Club La Mati"**
  - Título: "Tu 2da Clásica por S/. 3.99" → **"Tu 5ta Salchipapa por S/. 3.99"**
  - Body: explica acumulación digital vía WhatsApp, sin tarjetas físicas
  - CTAs: "Pedir promo" → **"Únete al Club"** (apunta a `#club`, sección que aún no existe — ver TODO)
  - Sticker: "5TA COMPRA / S/. 3.99 / todo el año"
- **TODO próximo:** crear sección `#club` con formulario de registro (WhatsApp), y elegir backend para tracking digital de compras (ver opciones discutidas en chat).
- **Archivos modificados:** `remove_white_bg.py`, `Platos transparentes/*.png` (regenerados los 7), `index.html`, `memory.md`.

### 2026-04-28 — v9: Eliminada sección Locator
- **Trigger:** Usuario pidió quitar la sección "Tu La Mati más cerca" (locator con buscador de tiendas + stats).
- **Cambios:**
  - Eliminada `<section class="locator" id="tiendas">` completa del HTML.
  - Eliminado todo el CSS asociado (`.locator`, `.locator-card`, `.locator-form`, `.locator-form input`, `.locator-stats` y sus reglas anidadas).
  - Limpiadas las referencias residuales en media queries (la línea de padding compartido y `.locator-stats { gap: 22px }`).
  - Eliminados los **3 enlaces** que apuntaban a `#tiendas`:
    - Top bar: "Encuentra tu tienda" (eliminado del top-links)
    - Nav primario sticky: "Tiendas" (eliminado del nav)
    - Footer columna "La Mati": "Nuestras tiendas" (eliminado del listado)
- **Estructura actual de la página (10 secciones):** Top bar → Header → Hero carrusel → Categorías → Banner Martes del Club → Productos estrella → Bucket Familiar → App móvil → Trabaja con nosotros → Footer.
- **Archivo modificado:** `index.html`, `memory.md`

### 2026-04-28 — v8: Bucket familiar con collage 4 platos + chicha 430ml
- **Trigger:** Usuario subió un collage 2×2 con los 4 platos premium (Francesa con queso, Royal con huevo, Americana con tocino, Andina con pollo) — quiere usarlo en el bucket familiar con calidad y diseño. Y reemplazar las gaseosas por chicha morada de 430 ml.
- **Cambios HTML:**
  - Texto bucket-features: "4 gaseosas 355ml de cortesía" → **"4 botellas de chicha morada 430 ml"**
  - Imagen bucket: `Platos transparentes/7.png` → **`Platos de La Mati/pack-familiar.jpg`** (placeholder — el archivo lo guardará el usuario manualmente desde el chat).
- **CSS `.bucket-img` rediseñado para foto profesional:**
  - `aspect-ratio: 5/4` → **`4/3`** (matchea mejor el collage 2×2)
  - `object-fit: contain` con padding → **`cover`** (la foto llena toda la card)
  - Eliminados radial gradients dorados (sobraban: foto trae su propio fondo)
  - **Borde dorado sutil** vía `box-shadow inset` que se intensifica en hover
  - **Hover con elevación** (translateY -4px) + zoom 1.04 sobre la foto (transición 0.7s con cubic-bezier suave)
  - **Doble overlay**: viñeta radial oscura + glow dorado en esquina inferior derecha
  - **Badge "PACK FAMILIAR"** vía `::before` en esquina superior izquierda con sombra inferior dorada-ámbar
- **Pendiente del usuario:** guardar la imagen del collage como `Platos de La Mati/pack-familiar.jpg` (sin tildes, sin espacios al final).
- **Archivo modificado:** `index.html`, `memory.md`

### 2026-04-28 — v7: Productos estrella con fotos de carpeta original
- **Trigger:** Usuario pidió cambiar las 8 fotos de la sección "Productos Estrella" para usar las imágenes de la carpeta original `Platos de La Mati/` (fotos profesionales con fondo de mesa de madera/restaurante) en lugar de las PNG transparentes.
- **Cambios:**
  - **8 referencias en `.prod-img-wrap`** actualizadas:
    1. Salchipapa Clásica → `clasica.jpg` (la nueva foto premium con el logo LA MATI y anotaciones)
    2. SalchiRoyal Especial → `Salchipapa Royal Especial.png`
    3. Americana → `Salchipapa Americana.png`
    4. Salchipollo → `Salchipollo.png`
    5. Arequipeña → `Salchipapa Arequipeña.png`
    6. Francesa Especial → `Salchipapa Francesa.png`
    7. Andina → `Salchipapa Andina.png`
    8. Combo Familia Mati → `Salchipapa Andina.png` (representativa)
  - **CSS `.prod-img-wrap`** ajustado para fotos con fondo:
    - Eliminados los radial gradients dorados (sobraban: la foto trae su propio fondo)
    - `object-fit: contain` → **`cover`** (las fotos llenan completas)
    - Eliminados padding y drop-shadow (no hace falta con foto sólida)
    - Añadido pseudo-element `::after` con gradient negro top→transparente para que los badges "Top/Nuevo/Favorita" sigan legibles sobre fotos claras
    - Hover: scale `1.06` con transición de 0.5s (en lugar de 0.4s)
- **Convivencia de carpetas:** ahora la página usa AMBAS carpetas:
  - `Platos transparentes/` → hero carrusel, categorías circulares, bucket familiar (necesitan transparencia para flotar)
  - `Platos de La Mati/` → productos estrella, banner promo (foto profesional con fondo natural)
- **Archivo modificado:** `index.html`, `memory.md`

### 2026-04-28 — v6: Banner "Martes del Club" + imagen full-bleed
- **Trigger:** Usuario pidió mejorar el banner 2x1: nuevo título, segunda unidad a S/. 3.99, exclusivo para miembros del **Club La Mati**, y reemplazar la imagen por la nueva foto profesional `Platos de La Mati/clasica.jpg` con el plato grande y notorio.
- **Cambios:**
  - **Texto banner**:
    - Eyebrow: "Promo de la semana" → **"★ Martes del Club"**
    - Título: "2x1 los martes en clásicas" → **"Tu 2da Clásica por [S/. 3.99]"** (precio en chip negro rotado -2°)
    - Body: menciona "primera al precio de carta", "segunda solo S/. 3.99" y **"beneficio exclusivo Club La Mati"**.
    - CTAs: "Pedir promo →" (primary negro) + link secundario "Únete al Club".
  - **Imagen**: nueva foto profesional `Platos de La Mati/clasica.jpg` (con texto LA MATI, "350 gr de papa nativa crujiente" y "salchicha franckfurt"). Reemplaza el PNG transparente para esta sección.
  - **Layout banner**: cambió de `1.4fr 1fr` con padding interno a **`1fr 1.15fr` full-bleed** (imagen toma toda la mitad derecha sin padding). `min-height: 460px`. Gradient lateral suave (`amber → transparent`) en el borde izquierdo de la imagen para fundirla con el dorado del texto.
  - **Sticker rotado**: badge "SOLO S/. 3.99 la 2da unidad" en negro/oro sobre la imagen, esquina superior derecha, rotado 6°.
  - **Responsive**: en `<= 1100px` la imagen pasa a aspect 16/10 y el sticker se mantiene; en `<= 760px` el sticker reduce padding/tamaño.
- **Concepto de marca nuevo:** **Club La Mati** (programa de fidelización) — futuro: agregar landing/sección dedicada al Club si el usuario lo pide.
- **Archivo modificado:** `index.html`, `memory.md`

### 2026-04-28 — v5: Transparencia real + plato flotante en hero
- **Trigger:** El usuario notó que las "PNG sin fondo" en realidad tenían fondo blanco real (no transparente) y se veía un cuadrado blanco horrible en el hero. Pidió que el plato "flote como profesional".
- **Cambios:**
  - **Script nuevo `remove_white_bg.py`** (Python + numpy + PIL): convierte cualquier pixel con `min(R,G,B) >= 248` a alpha 0; entre 225 y 248 hace anti-alias lineal; aplica blur 0.6px al canal alpha para evitar bordes dentados. Procesa los 7 archivos.
  - **Carpeta nueva `Platos transparentes/`** con las 7 imágenes ahora con transparencia real.
  - **18 referencias** en `index.html` actualizadas de `Platos de la mati sin fondo/` a `Platos transparentes/`.
  - **CSS `.slide-img`** rediseñado:
    - Triple background con doble radial gradient gold/amber + linear gradient base
    - Pseudo-elemento `::after` con halo dorado blureado (60% del contenedor, blur 20px) detrás del plato
    - `filter` con triple drop-shadow apilado: sombra grande negra + sombra cercana negra + glow dorado sutil
    - Animación `floatPlate` 5s infinita que mueve el plato 10px en Y (efecto flotación)
    - `@media (prefers-reduced-motion)` ya cubierto por el bloque global existente
- **Archivos modificados:** `index.html`, `memory.md`
- **Archivos nuevos:** `remove_white_bg.py`, carpeta `Platos transparentes/` con 7 PNGs.

### 2026-04-28 — v4: Marca a Arequipa + RUC + ajuste categoría
- **Trigger:** El usuario corrigió la ciudad de la marca (Lima → Arequipa), agregó el RUC oficial y pidió renombrar la 3ª categoría.
- **Cambios:**
  - **Categorías**: 3ª card cambió de "Para Compartir" (S/. 32.90) → **"Andina"** (S/. 16.50). Mantiene la imagen `7.png`.
  - **Lima → Arequipa** en 7 lugares: title, meta description, top bar ("Pedir en Arequipa · Centro"), hero brand del footer, locator stats ("Tiendas en Arequipa"), texto de "Trabaja con nosotros" y línea legal.
  - **Distritos del buscador locator**: "San Borja, Surco, Miraflores" → "Cayma, Yanahuara, Cerro Colorado, Cercado".
  - **RUC**: placeholder `20XXXXXXXXX` → **`20610692096`** en la línea legal del footer.
- **Archivo modificado:** `index.html`, `memory.md`

### 2026-04-28 — v3: Imágenes sin fondo + reorden hero
- **Trigger:** El usuario cargó 7 fotos nuevas en `Platos de la mati sin fondo/` (PNG con transparencia, bowls centrados, mucha mejor calidad). Pidió reemplazar las antiguas y reordenar el hero.
- **Cambios de imágenes:**
  - Todas las referencias a `Platos de La Mati/*.png` (con fondo) reemplazadas por `Platos de la mati sin fondo/N.png` con su número correspondiente.
  - 18 referencias actualizadas en total (3 hero + 5 categorías + 1 promo + 8 productos + 1 bucket).
- **Reorden hero (3 slides):**
  - Slide 1: ahora **Andina** (`7.png`) — eyebrow "SABOR DEL SUR", S/. 16.50
  - Slide 2: ahora **Francesa** (`5.png`) — eyebrow "CON QUESO DERRETIDO", S/. 16.00
  - Slide 3: **Americana** (`6.png`) sin cambios — eyebrow "CLÁSICA DE LA CASA", S/. 15.00
- **Ajustes CSS** (porque las imágenes nuevas son PNG transparentes, no fotos con fondo):
  - `.slide-img`: cambió de `object-fit: cover` a `contain` con padding y `drop-shadow`. Background con doble radial gradient gold/amber.
  - `.cat-circle img`: `width/height: 110% + cover` → `100% + contain`. Background reforzado con dos radial gradients.
  - `.prod-img-wrap img`: `cover` → `contain` con padding y drop-shadow. Background con radial gradient gold.
  - `.bucket-img img`: `cover` → `contain` con padding 18px y drop-shadow grande.
  - `.promo-banner .pb-img img`: `cover` → `contain` con drop-shadow.
  - **Patrón unificado**: cada vez que un plato sin fondo se muestra, va sobre un radial gradient gold/amber sobre negro, con drop-shadow para dar volumen.
- **Archivo modificado:** `index.html`
- **Archivo deprecado (no se borra, pero ya no se referencia):** todas las imágenes en `Platos de La Mati/` (con fondo). Se mantienen en disco por si se quieren reutilizar.

### 2026-04-27 — v2: Estructura espejo de kfc.com.pe
- **Trigger:** Usuario pidió usar **kfc.com.pe** como modelo y replicar su ESTRUCTURA exacta, manteniendo solo la paleta de La Mati. (WebFetch a kfc.com.pe devolvió 403, así que se usó la estructura conocida del patrón LATAM KFC: ec/co/es).
- **Estructura nueva (orden vertical):**
  1. **Top bar** negro con selector de ubicación ("Pedir en Lima · Centro") y links rápidos (Encuentra tu tienda · Trabaja · Atención).
  2. **Header sticky** con logo + nav primario (Carta · Combos · Promos · Tiendas · Trabaja) + botones "Ingresar" (outline) y "Pedir Ahora" (primary gold).
  3. **Hero carrusel** full-width con 3 slides auto-play (6s), flechas prev/next, dots, badge circular de precio rotado -7°.
  4. **Categorías** — grid de 5 cards con imagen circular del producto (Clásicas, Especiales, Para Compartir, Con Queso, Con Pollo).
  5. **Banner promo mid** — full-width dorado con rayas diagonales (patrón KFC), CTA "2x1 los martes en clásicas".
  6. **Productos destacados** — grid 4 cols con badges (Top, Nuevo, Favorita, Picante…), botón "Añadir" estilo carrito.
  7. **Bucket Familiar** — sección 2 cols (imagen + texto con checklist) tipo bucket meal de KFC.
  8. **Locator "Encuentra tu La Mati"** — card centrada con input de búsqueda + stats (8 tiendas, 30 min, horario).
  9. **App móvil** — 2 cols (mockup + texto con perks y botones App Store / Google Play).
  10. **Join us / Trabaja con nosotros** — banner full-width con franjas diagonales doradas arriba y abajo.
  11. **Footer** multi-columna (5 cols: Brand + 4 categorías de links: Carta, La Mati, Atención, Legal) con redes y línea legal RUC.
- **Cambios técnicos:**
  - Nuevo carrusel con JS vanilla (auto-play, pause on hover, prev/next, dots, soporte teclado).
  - Nav activa con scroll spy.
  - Nueva paleta variable: `--bg #0d0d0d` (más claro que `--black` puro para distinguir secciones).
  - Mantenida paleta La Mati: rojo KFC reemplazado por `--gold #FFB800` y degradado `--gold → --amber → marrón #8a4d11` en banners promos.
  - Tipografía: solo Inter (eliminado Playfair Display — KFC no usa serif decorativo).
  - Botones rectangulares (border-radius 6px) con sombra inferior tipo "botón físico" (--gold sombra --amber).
- **Archivo modificado:** `index.html`

### 2026-04-27 — v1: Rediseño estilo KFC (interpretación libre)
- Versión intermedia con titular outline gigante, ticker rayado, combos tipo bucket, "Arma tu combo" en 4 pasos. Reemplazada por v2 que sigue la estructura real de kfc.com.pe.

---

## Reglas de trabajo aprendidas

1. **Mantener siempre la paleta de La Mati** sin importar el estilo visual de referencia.
2. **Actualizar este archivo `memory.md`** después de cada cambio significativo en la página.
3. **No tocar las imágenes existentes** en `Platos de La Mati/` — se referencian con su nombre exacto (incluyendo tildes).
4. **Mobile-first y accesibilidad** son requisitos no negociables (ver `CLAUDE.md`).
5. El proyecto se despliega vía Netlify (carpeta `.netlify` y `deploy/` presentes).
