# Sitio de Rugido de León (versión 1, sin publicar)

HTML, CSS y JavaScript simples, sin dependencias. Las fuentes y las imágenes están en la carpeta (autoalojadas).

## Cómo verlo
Abrí `index.html` desde un servidor local, por ejemplo:

```bash
cd web/sitio && python3 -m http.server 8765
```
y entrá a http://localhost:8765. (También está configurado en `.claude/launch.json` como `sitio-rugido`.)

## Archivos
- `index.html`: se genera con `python3 generar.py` (incluye el mapa de Argentina desde `../assets/mapa-argentina.json`). Para cambiar textos, editá `generar.py` y volvé a correrlo.
- `styles.css`: colores, tipografía y diseño (paleta en `paleta/roles-de-color.md`, escala en `tipografia/`).
- `main.js`: aviso de edad, fondo continuo, botella fija y aparición de textos.
- `assets/`: imágenes optimizadas. `fonts/`: Libre Baskerville y Barlow (licencia OFL).

## Cómo funciona (actualizado 18/11/2026, versión final del pedido)
- **Home** a pantalla completa. Los álamos del fondo se mueven con el viento: dos capas con la misma foto, recortadas a la zona de los árboles (`.viento--tronco` se balancea lento; `.viento--hojas` tiembla rápido). Se apaga con `prefers-reduced-motion`. Si cambia la proporción de la pantalla, el recorte de los árboles puede correrse un poco (`.viento` en `styles.css`).
- **Pila de tarjetas** blancas, más angostas que la pantalla (se ve el fondo a los costados), pegadas entre sí sin huecos verticales. El acento (violeta, azul de la etiqueta, bordó) rota en títulos, precios y números.
- **Fondo continuo**: una sola imagen vertical (`assets/fondo.jpg`) que se desplaza más lento que el contenido.
- **Botella**: acompaña el scroll y queda clavada al final de la sección de mayoristas (sale con esa sección; si se sube, vuelve a acompañar). Se hace con `position: sticky` dentro de `.riel`. En celular solo acompaña la entrada y cada tarjeta lleva su botella.
- **Cierre**: tarjeta con la foto de la botella sobre el tronco (`assets/cierre.jpg`, carga perezosa).
- **Pie** de ancho completo y sin imagen a los costados, provisorio.
- **Animaciones**: títulos que suben línea por línea, bloques escalonados, botones con flecha y aro. Todo respeta `prefers-reduced-motion`.

## Pendiente antes de publicar
- Términos de venta, Política de privacidad y Botón de arrepentimiento: los enlaces del pie van a `#` (hay que redactarlos con un abogado).
- Vigencia de la oferta: marcado con comentario en `generar.py`. La regla de envío ya está aplicada (19/11/2026: sucursales sin cargo; a domicilio sin cargo desde 3 cajas, $29.000 con menos, San Francisco siempre sin cargo).
- Confirmar que Quilam S.A.S. puede vender al público (ARCA hoy muestra solo actividad mayorista).
- Botella y escenas: la etiqueta dice "RUGIDO DE LEON" sin tilde; la estancia es una escena generada, no la real.
- Hosting y dominio, favicon, Open Graph con imagen propia y medición (analytics).
- Aviso de edad: es una pantalla simple de autodeclaración.
