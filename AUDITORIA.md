# Auditoría técnica del sitio (18/11/2026)

Puntaje: **14/20 (Bueno)**. Solo se documenta; no se corrigió nada.
Método: detector de Impeccable sobre index.html, styles.css y main.js; contrastes calculados; pruebas en 390, 1024 y 1440 px.

| Dimensión | Puntaje | Hallazgo principal |
|---|---|---|
| Accesibilidad | 2 | El aviso de edad no atrapa el foco ni inertiza la página; el menú del hero tiene bajo contraste |
| Rendimiento | 3 | 3,3 MB de imágenes; la botella PNG pesa 984 KB |
| Responsive | 3 | Sin desbordes en 390/1024/1440; objetivos táctiles de 21 a 37 px |
| Temas | 3 | Tokens bien usados; quedan unos 10 colores sueltos; sin modo oscuro (no aplica a la marca) |
| Integridad | 3 | Sistema coherente; 4 de 6 hallazgos del detector son falsos positivos |

## P1 (antes de publicar)
1. **Aviso de edad sin gestión de foco** (index.html `#edad`, main.js). Se puede tabular hacia el sitio de fondo y no cierra con Escape. Falta `inert` en `<main>`, `<header>` y `<footer>` mientras está abierto. WCAG 2.4.3. `/impeccable harden`
2. **Menú del hero con bajo contraste** (styles.css `.nav`). Crema sobre cielo claro con la capa del 26%: unos 2:1 a 3:1, hace falta 4,5:1. WCAG 1.4.3. `/impeccable colorize`
3. **Enlaces legales muertos** (index.html pie: términos, privacidad, arrepentimiento van a `#`). Hay que redactar las páginas. `/impeccable clarify`

## P2
4. **Objetivos táctiles chicos**: menú 37 px, enlaces del pie 21 a 27 px. Mínimo 44 px (WCAG 2.5.8 pide 24 px, buena práctica 44). `/impeccable adapt`
5. **`dl` con `dd` antes de `dt`** en `.precios` y `.ficha`: los lectores de pantalla leen el valor antes de la etiqueta. Invertir el orden y usar CSS. `/impeccable harden`
6. **Botella sin descripción para lectores de pantalla** (`aria-hidden`): el producto no tiene texto alternativo en ninguna parte. Sumar un texto visualmente oculto o un `alt` en la primera aparición. `/impeccable clarify`
7. **Peso de imágenes**: `botella.png` 984 KB, `fondo.jpg` 1,08 MB; ninguna con `loading=lazy`; la imagen del cierre se carga al abrir. Convertir la botella a WebP/AVIF con transparencia y cargar el cierre perezosamente. `/impeccable optimize`
8. **Leyenda legal del hero** (`.hero__legal`) sobre el tronco da unos 5:1 y en celular queda pegada al borde. Revisar. `/impeccable polish`

## P3
9. Colores sueltos fuera de los tokens (#E6D0D8, #D8B7C4, #8B5FC0, #DADDEB, #E7E2EE). `/impeccable extract`
10. `text-shadow` azul oscuro en el hero: el detector lo marca como halo; es una sombra de lectura, pero se puede reemplazar por un degradado superior. `/impeccable polish`
11. `will-change` fijo en el fondo y filtro `drop-shadow` en la botella fija: son un solo elemento cada uno y no hay caídas de cuadros, pero conviene medir en celulares lentos.

## Falsos positivos del detector (verificados)
- "Texto #1d214f sobre #6b3896 en hover": el botón usa blanco, que da unos 8,7:1.
- "Jerarquía plana, h1 de 16 px": es el h2 de 15 px del pie; el h1 real mide 58 px.
- "Relleno justo en `.edad__caja`": tiene `clamp(28px, 5vw, 48px)` de relleno; el detector lo midió oculto.
- "body recorta un hijo posicionado": `overflow-x:hidden` en body; no recorta nada visible.

## Lo que funciona
- Un solo `h1`, jerarquía de encabezados correcta, `lang="es-AR"`, enlace para saltar al contenido, `:focus-visible` visible en todo.
- `prefers-reduced-motion` con alternativa real: sin desplazamiento del fondo y sin animaciones de aparición.
- Contrastes de las tarjetas: entre 7:1 y 15:1.
- Sin desbordes horizontales en 390, 1024 y 1440 px. El botón y el campo principal superan los 44 px.
- Todo con transform y opacidad, fuentes propias, un solo listener de scroll pasivo con `requestAnimationFrame`.
- Los datos del pie y de la oferta salen de los documentos del cliente.

## Orden recomendado
1. `/impeccable harden` (puntos 1 y 5)
2. `/impeccable colorize` (punto 2)
3. `/impeccable adapt` (punto 4)
4. `/impeccable optimize` (punto 7)
5. `/impeccable clarify` (puntos 3 y 6)
6. `/impeccable polish` (cierre)


## Correcciones aplicadas (18/11/2026)
- P1 1 (aviso de edad): `header`, `main` y `footer` quedan inertes mientras está abierto, el foco circula solo entre sus dos botones y se libera al aceptar. No se cierra con Escape a propósito (hay que responder). Verificado en el navegador.
- P1 2 (menú del hero): degradado oscuro arriba del hero y áreas táctiles de 44 px en el menú. En celular el hero es claro y no lleva el degradado.
- P1 3 (enlaces legales): se crearon `terminos.html`, `privacidad.html` y `arrepentimiento.html` en BORRADOR, con datos entre corchetes (CUIT, domicilio, IVA, medios de pago, regla de envío, plazos). Hay que revisarlos con un abogado antes de publicar. Llevan `noindex`.
- También: enlaces del pie con 44 px de alto (parte del P2 4).
Pendiente de la auditoría: P2 5 a 8 y P3.

## P2 corregidos (18/11/2026)
- P2 5: en `.precios` y `.ficha` la etiqueta (`dt`) va antes que el valor (`dd`) en el código; el orden visual se mantiene con CSS. Verificado.
- P2 6: texto oculto con la descripción de la botella en el hero (`.vh`), leído por lectores de pantalla.
- P2 7: botella reducida de 415x1500 a 332x1200 px (984 KB a 632 KB) y fondo de 1,08 MB a 817 KB. Las botellas de las tarjetas del celular cargan de forma perezosa (no cargan en escritorio) y la foto del cierre carga cuando el visitante se acerca. No se pudo convertir a WebP/AVIF: no hay codificador en esta máquina.
- P2 8: degradado inferior en el hero para que la leyenda legal se lea.
- P2 4: menú, enlaces del pie y mensajes ya miden 44 px.
Pendiente: P3 (colores sueltos, text-shadow, medir will-change/filtro en celulares lentos).

## P3 corregidos (18/11/2026)
- P3 9: los colores sueltos pasaron a tokens (`--rosado-claro`, `--rosado-medio`, `--violeta-claro`, `--gris-mapa`, `--lavanda`, `--lila-aviso`).
- P3 10: se quitó el `text-shadow` del hero y del cierre; la legibilidad queda con una capa oscura pareja (28% en el hero, 34% en el cierre) más los degradados superior e inferior.
- P3 11: `will-change` ya no queda fijo (se activa solo mientras hay scroll y se apaga a los 180 ms) y la botella fija perdió el filtro `drop-shadow`: ahora lleva una sombra de suelo con degradado radial.
- Medición: con el panel visible, la versión nueva y la vieja corren a 60 cuadros por segundo sin caídas (201 cuadros, 0 sobre 25 ms). En esta máquina NO hay diferencia medible; el cambio es preventivo para celulares lentos y no se probó en uno real.
