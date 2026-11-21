# Rugido de León · sitio web

Sitio estático (HTML, CSS y JavaScript, sin dependencias) de Rugido de León, Malbec de San Rafael, Mendoza.

- `index.html` se genera con `python3 generar.py` (textos y estructura). Para cambiar contenido, editá `generar.py` y volvé a correrlo.
- `styles.css`, `main.js`, `assets/`, `fonts/`: diseño, comportamiento, imágenes y tipografías.
- `terminos.html`, `privacidad.html`, `arrepentimiento.html`: **borradores** para revisar con un abogado antes de publicar.
- `datos/mapa-argentina.json`: provincias (IGN, Georef) para el mapa con Mendoza resaltada.

Ver en local: `python3 -m http.server 8780` y abrir http://localhost:8780

Publicado en Vercel: https://rugido-de-leon.vercel.app (con `noindex`, mientras sea borrador).

El proyecto de Vercel está conectado a este repositorio: cada commit a `main` se publica solo.
