"""Genera index.html con el mapa de Argentina inline (datos: web/assets/mapa-argentina.json, IGN via Georef)."""
import json, html

MAP = json.load(open("datos/mapa-argentina.json"))
W, H = MAP["w"], MAP["h"]


def mapa_svg():
    otros = "".join(f'<path d="{d}"/>' for n, d in MAP["paths"].items() if n != "Mendoza")
    sx, sy = MAP["sanrafael"]
    return (
        f'<svg class="mapa-fondo" viewBox="0 0 {W:.0f} {H:.0f}" role="img" '
        f'aria-label="Mapa de Argentina con la provincia de Mendoza resaltada y San Rafael marcado" '
        f'style="--fx:{sx/W:.4f};--fy:{sy/H:.4f};--ar:{W/H:.4f}">'
        f'<defs><pattern id="mapa-foto" patternUnits="userSpaceOnUse" width="{W:.0f}" height="{H:.0f}">'
        f'<image href="assets/vinedo-letras.webp" width="{W:.0f}" height="{H:.0f}" preserveAspectRatio="xMidYMid slice"/></pattern></defs>'
        f'<g class="mapa__prov">{otros}</g>'
        f'<path class="mapa__mza" d="{MAP["paths"]["Mendoza"]}"/>'
        f'<circle class="mapa__pt-o" cx="{sx:.0f}" cy="{sy:.0f}" r="6"/>'
        f'<circle class="mapa__pt-i" cx="{sx:.0f}" cy="{sy:.0f}" r="3"/>'
        f'<text class="mapa__rotulo" x="{sx+9:.0f}" y="{sy+2.5:.0f}">San Rafael</text>'
        f'</svg>'
    )


WA = "https://wa.me/message/XOJZ5AEVAY3NC1"
LEGAL = "Beber con moderación. Prohibida su venta a menores de 18 años."


def btn(txt="Pedir por WhatsApp", extra=""):
    return f'<a class="btn btn--wa {extra}" href="{WA}" target="_blank" rel="noopener"><span>{txt}</span><span class="vh"> (se abre en una pestaña nueva)</span></a>'


page = f"""<!doctype html>
<html lang="es-AR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Rugido de León | Malbec de San Rafael, Mendoza</title>
<meta name="description" content="Malbec 2025 de San Rafael, Mendoza. Seco, de frutas rojas y taninos suaves. Pedilo por WhatsApp.">
<meta property="og:title" content="Rugido de León | La libertad no se negocia, se conquista">
<meta property="og:description" content="Malbec 2025 de San Rafael, Mendoza. Pedilo por WhatsApp.">
<meta property="og:image" content="assets/og.jpg">
<meta name="theme-color" content="#0F1633">
<link rel="preload" href="assets/hero-leon.webp" as="image" media="(min-width: 861px)" fetchpriority="high">
<link rel="preload" href="assets/hero-leon-celular.webp" as="image" media="(max-width: 860px)" fetchpriority="high">
<link rel="preload" href="assets/botella.webp" as="image">
<link rel="preload" href="fonts/LibreBaskerville-Variable.ttf" as="font" type="font/ttf" crossorigin>
<link rel="stylesheet" href="styles.css?v=173">
<noscript><style>.pie{{background-image:url("assets/pie-andes.webp")}}.reveal>*{{opacity:1!important;transform:none!important}}.ln>span{{transform:none!important}}.hero__cta>*{{opacity:1!important;transform:none!important}}</style></noscript>
</head>
<body>
<a class="skip" href="#marca">Saltar al contenido</a>

<div class="tramo">
<!-- La botella acompaña el scroll y queda clavada al final de la sección de mayoristas -->
<div class="riel" aria-hidden="true">
  <div class="botella" id="botella">
    <img src="assets/botella.webp" alt="" width="332" height="1200" fetchpriority="high" decoding="async">
  </div>
</div>

<header class="hero" id="inicio">
  <div class="hero__fondo" aria-hidden="true"><i class="capa"></i></div>
  <nav class="nav" aria-label="Principal">
    <a href="#marca">El vino</a>
    <a href="#origen">Origen</a>
    <a href="#vino-en-accion">Para negocios</a>
    <a href="#envios">Comprar</a>
  </nav>
  <div class="hero__grid">
    <h1 class="hero__titulo"><span class="ln" style="--l:0"><span>La libertad no se negocia,</span></span> <span class="ln" style="--l:1"><span>se conquista.</span></span></h1>
    <div class="hero__cta">
      <p class="hero__texto">Malbec 2025<br>San Rafael · Mendoza</p>
      {btn()}
    </div>
  </div>
  <p class="vh">Botella de Rugido de León Malbec 2025, con cápsula violeta y etiqueta azul y crema con un león rugiendo, apoyada sobre un muro de piedra, con un viñedo detrás y los Andes nevados y rosados por el atardecer al fondo.</p>
  <p class="hero__legal">{LEGAL}</p>
</header>

<main class="pila">

<section class="card acc-violeta" id="marca" aria-labelledby="t-marca">
  <h2 class="vh" id="t-marca">Rugido de León</h2>
  <div class="titulo-marca reveal" aria-hidden="true">
    <span class="h-foto h-foto--izq">RUGIDO</span>
    <span class="h-foto h-foto--der">DE LEÓN</span>
  </div>
  <div class="card__grid">
    <div class="col col--izq reveal">
      <p class="lead">Este vino captura esa fuerza salvaje en una botella: un vino noble, franco y con la personalidad de quien no teme alzar la voz.</p>
      <ul class="notas">
        <li><span class="detalle">Notas</span>Notas de frutas rojas bien marcadas</li>
        <li><span class="detalle">Toques</span>Sutiles toques de madera</li>
        <li><span class="detalle">Taninos</span>Taninos suaves y gran persistencia</li>
      </ul>
    </div>
    <div class="col__centro"></div>
    <div class="col col--der reveal">
      <dl class="ficha ficha--dos">
        <div class="ancho"><dt class="detalle">Cepa</dt><dd>Malbec</dd></div>
        <div><dt class="detalle">Alcohol</dt><dd><span class="num" data-valor="13.1" data-dec="1" data-suf="%">13,1%</span></dd></div>
        <div><dt class="detalle">Estilo</dt><dd>Seco</dd></div>
        <div><dt class="detalle">Cosecha</dt><dd><span class="num" data-valor="2025" data-dec="0" data-sep="0">2025</span></dd></div>
        <div><dt class="detalle">Medida</dt><dd><span class="num" data-valor="750" data-dec="0" data-suf=" ml">750 ml</span></dd></div>
      </dl>
    </div>
  </div>
  <img class="mbotella" src="assets/botella.webp" alt="" aria-hidden="true" width="332" height="1200" loading="lazy" decoding="async">
</section>

<section class="card acc-azul" id="origen" aria-labelledby="t-origen">
  {mapa_svg()}
  <div class="card__grid">
    <div class="col col--izq reveal">
      <h2 class="h1 h1--chico" id="t-origen">Hecho en San Rafael,<br>Mendoza.</h2>
      <div class="origen">
        <p class="cuerpo">Se elabora y fracciona en la bodega Almabras, en Las Paredes, al sur de Mendoza, con Malbec de la zona.</p>
      </div>
    </div>
    <div class="col__centro"></div>
    <div class="col col--der reveal">
      <p class="frase">Malbec del sur de Mendoza, hecho en San Rafael.</p>
      <ul class="notas-chicas">
        <li><span class="detalle">Elabora y fracciona</span>Almabras S.A.</li>
        <li><span class="detalle">Bodega</span>Los Sauces 2227, Las Paredes, San Rafael</li>
        <li><span class="detalle">Registro INV</span>K72643. Vino de libre circulación, con certificado de análisis del INV.</li>
      </ul>
    </div>
  </div>
  <img class="mbotella" src="assets/botella.webp" alt="" aria-hidden="true" width="332" height="1200" loading="lazy" decoding="async">
</section>

<section class="card acc-violeta" id="vino-en-accion" aria-labelledby="t-accion">
  <div class="card__grid">
    <div class="col col--izq reveal">
      <h2 class="h1" id="t-accion">El vino<br>en acción</h2>
      <p class="lead">Para restaurantes, vinotecas y distribuidoras.</p>
      <ul class="lista-may">
        <li>Precios por cantidad y por palet. Escribinos y te pasamos la lista.</li>
        <li>Caja de seis botellas.</li>
        <li>Palet: 150 cajas, 900 botellas, con envío sin cargo a Buenos Aires y a otras provincias, a consultar.</li>
      </ul>
      {btn("Pedir la lista por WhatsApp")}
    </div>
    <div class="col__centro"></div>
    <div class="col col--der reveal">
      <figure class="foto-accion">
        <img src="assets/vino-en-accion.webp" width="671" height="802" loading="lazy" decoding="async" alt="Botella de Rugido de León en la mano, junto a un fuego de leña encendido">
      </figure>
    </div>
  </div>
  <img class="mbotella" src="assets/botella.webp" alt="" aria-hidden="true" width="332" height="1200" loading="lazy" decoding="async">
</section>

<section class="card acc-envios" id="envios" aria-labelledby="t-envios">
  <div class="card__grid">
    <div class="col col--izq reveal">
      <h2 class="h2" id="t-envios">Envíos</h2>
      <ul class="envios">
        <li><strong>A las sucursales</strong><span>Sin cargo. Retirá tu pedido en San Francisco, Buenos Aires, Córdoba, Rafaela o Rosario (direcciones al pie).</span></li>
        <li><strong>A domicilio</strong><span>Sin cargo desde 3 cajas en Rafaela, Córdoba, CABA, AMBA, Rosario y San Francisco. Con menos de 3 cajas, la entrega cuesta $29.000. En San Francisco siempre es sin cargo.</span></li>
        <li><strong>Palet de 900 botellas</strong><span>Envío sin cargo a Buenos Aires y a otras provincias. Las consultás y te confirmamos.</span></li>
      </ul>
    </div>
    <div class="col__centro"></div>
    <div class="col col--der reveal">
      <h2 class="h2" id="t-comprar">Cómo comprar</h2>
      <ol class="pasos">
        <li><span class="paso__n">1</span><div><strong>Escribinos por WhatsApp</strong><span>Contanos qué necesitás y consultá por la oferta de fin de año.</span></div></li>
        <li><span class="paso__n">2</span><div><strong>Elegí botellas o caja</strong><span>Caja de seis botellas.</span></div></li>
        <li><span class="paso__n">3</span><div><strong>Coordiná el pago y el envío</strong><span>Sucursal o domicilio, por WhatsApp.</span></div></li>
      </ol>
      <!-- A CONFIRMAR con el cliente: vigencia de la oferta de fin de año. Envío: regla confirmada el 19/11/2026 (gratis desde 3 cajas) -->
      <p class="oferta"><strong>Oferta de fin de año:</strong> caja de seis botellas y envío a domicilio sin cargo desde 3 cajas.</p>
      {btn("Consultá por la oferta de fin de año")}
    </div>
  </div>
  <img class="mbotella" src="assets/botella.webp" alt="" aria-hidden="true" width="332" height="1200" loading="lazy" decoding="async">
</section>

</main>
</div><!-- /tramo -->

<footer class="pie" id="pie">
  <div class="pie__top">
    <div class="pie__marca reveal">
      <p class="pie__lema">La libertad no se negocia, se conquista.</p>
      {btn("Consultá por la oferta de fin de año")}
      <p class="pie__legal">{LEGAL}<br>Elaborado por Almabras S.A., San Rafael, Mendoza (INV K72643).<br>Comercializa Quilam S.A.S., San Francisco, Córdoba.</p>
    </div>
    <div class="pie__col reveal">
      <h2 class="detalle">Contacto</h2>
      <ul class="pie__lista">
        <li><a href="{WA}" target="_blank" rel="noopener">WhatsApp 3564 507507<span class="vh"> (se abre en una pestaña nueva)</span></a></li>
        <li><a href="https://www.instagram.com/rugidodeleon.oficial/" target="_blank" rel="noopener">@rugidodeleon.oficial<span class="vh"> (se abre en una pestaña nueva)</span></a></li>
      </ul>
      <h2 class="detalle">Información</h2>
      <!-- Páginas legales en BORRADOR: revisar con un abogado y completar los datos entre corchetes antes de publicar -->
      <ul class="pie__lista">
        <li><a href="terminos.html">Términos de venta</a></li>
        <li><a href="privacidad.html">Política de privacidad</a></li>
        <li><a href="arrepentimiento.html">Botón de arrepentimiento</a></li>
      </ul>
    </div>
    <div class="pie__col pie__col--suc reveal">
      <h2 class="detalle">Sucursales</h2>
      <ul class="pie__lista pie__lista--suc">
        <li><strong>San Francisco</strong>Santiago Pampiglione 4611, Parque Industrial</li>
        <li><strong>Buenos Aires</strong>Int. Rabanal 1456 (ex Roca), Nueva Pompeya, CABA</li>
        <li><strong>Córdoba</strong>Parque Industrial Polo 52, Nave 84</li>
        <li><strong>Rafaela</strong>Gálvez 281</li>
        <li><strong>Rosario</strong>Av. Alberdi 25 / 25 bis</li>
      </ul>
    </div>
  </div>
  <div class="pie__andes" aria-hidden="true">
    <p class="pie__nombre"><span>RUGIDO</span><span>DE LEÓN</span></p>
  </div>
</footer>

<!-- Aviso de mayoría de edad -->
<div class="edad" id="edad" role="dialog" aria-modal="true" aria-labelledby="t-edad" hidden>
  <div class="edad__caja">
    <div class="edad__lado" aria-hidden="true"><img src="assets/botella.webp" alt="" width="332" height="1200" decoding="async"></div>
    <div class="edad__cuerpo">
      <span class="edad__sello" aria-hidden="true">+18</span>
      <h2 id="t-edad">¿Sos mayor de 18 años?</h2>
      <p class="edad__txt">Este sitio promociona bebidas alcohólicas. La venta está prohibida a menores de 18 años.</p>
      <div class="edad__botones">
        <button class="btn" id="edad-si" type="button">Sí, soy mayor de 18</button>
        <button class="btn btn--sec" id="edad-no" type="button">No</button>
      </div>
      <p class="edad__nota" id="edad-nota" hidden>Gracias por tu honestidad. Volvé cuando tengas 18 años.</p>
      <p class="edad__legal">{LEGAL}</p>
    </div>
  </div>
</div>

<script src="main.js?v=142"></script>
</body>
</html>
"""
open("index.html", "w").write(page)
print("index.html", len(page))


# ---------- paginas legales (BORRADOR: revisar con un abogado antes de publicar) ----------
def legal(archivo, titulo, cuerpo):
    h = f"""<!doctype html>
<html lang="es-AR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>{titulo} | Rugido de León</title>
<link rel="stylesheet" href="styles.css">
</head>
<body class="legal-body">
<main class="legal">
  <a class="legal__volver" href="index.html">&larr; Volver al sitio</a>
  <h1>{titulo}</h1>
  <p class="legal__aviso">Borrador para revisión legal. Completá los datos entre corchetes antes de publicar.</p>
{cuerpo}
</main>
</body>
</html>
"""
    open(archivo, "w").write(h)

VENDEDOR = "Quilam S.A.S., [CUIT a completar], [domicilio legal a completar], San Francisco, Córdoba"

legal("terminos.html", "Términos de venta", f"""
  <h2>Quién vende</h2>
  <p>El vino Rugido de León es comercializado por {VENDEDOR}. Está elaborado por Almabras S.A., San Rafael, Mendoza (INV K72643).</p>
  <h2>Quién puede comprar</h2>
  <p>La venta de bebidas alcohólicas está prohibida a menores de 18 años. Al hacer un pedido declarás ser mayor de edad.</p>
  <h2>Cómo se hace un pedido</h2>
  <p>Los pedidos se hacen por WhatsApp al 3564 507507. El pedido se confirma cuando te respondemos con el detalle, el precio y la forma de pago.</p>
  <h2>Precios</h2>
  <p>Los precios publicados son por botella de 750 ml y por caja de seis botellas, en pesos argentinos, [con IVA incluido: a confirmar]. Las ofertas rigen [hasta la fecha a completar] y mientras haya stock.</p>
  <h2>Envíos</h2>
  <p>El envío a las sucursales (San Francisco, Buenos Aires, Córdoba, Rafaela y Rosario) es sin cargo. La entrega a domicilio en Rafaela, Córdoba, CABA, AMBA, Rosario y San Francisco es sin cargo desde 3 cajas; con menos de 3 cajas cuesta $29.000, salvo en San Francisco, donde siempre es sin cargo. Para los palets, las provincias y las condiciones se consultan y se confirman por WhatsApp.</p>
  <h2>Formas de pago</h2>
  <p>[Medios de pago a completar.]</p>
  <h2>Cambios y devoluciones</h2>
  <p>Podés arrepentirte de la compra dentro de los 10 días corridos de recibido el producto. Mirá la página de Botón de arrepentimiento. Si el producto llega dañado, escribinos por WhatsApp y lo resolvemos.</p>
  <h2>Consumo responsable</h2>
  <p>Beber con moderación. Prohibida su venta a menores de 18 años.</p>
""")

legal("privacidad.html", "Política de privacidad", f"""
  <h2>Responsable de los datos</h2>
  <p>{VENDEDOR}.</p>
  <h2>Qué datos tratamos</h2>
  <p>Cuando nos escribís por WhatsApp recibimos tu número de teléfono y el contenido de tu mensaje. Si hacés un pedido, además, los datos de entrega y de contacto que nos pasás. Este sitio no usa cookies de seguimiento ni formularios. [Confirmar si se suma medición de visitas.]</p>
  <h2>Para qué los usamos</h2>
  <p>Para responder tu consulta, gestionar el pedido, coordinar el envío y cumplir obligaciones legales y fiscales.</p>
  <h2>Con quién los compartimos</h2>
  <p>Con quien haga el envío y con los proveedores de pago, solo en lo necesario para entregarte el pedido. No vendemos tus datos.</p>
  <h2>Tus derechos</h2>
  <p>Podés pedir acceso, rectificación o supresión de tus datos escribiéndonos por WhatsApp al 3564 507507. La Agencia de Acceso a la Información Pública (AAIP) es el órgano de control de la Ley 25.326 y puede atender denuncias.</p>
  <h2>Cambios</h2>
  <p>Podemos actualizar esta política. La versión vigente es la publicada en esta página.</p>
""")

legal("arrepentimiento.html", "Botón de arrepentimiento", f"""
  <h2>Tu derecho</h2>
  <p>Si compraste a distancia, podés revocar la compra dentro de los 10 días corridos contados desde que recibiste el producto, sin costo para vos (art. 34 de la Ley 24.240 de Defensa del Consumidor).</p>
  <h2>Cómo pedirlo</h2>
  <p>Escribinos por WhatsApp al 3564 507507 indicando tu nombre, el número o la fecha del pedido y que querés revocar la compra.</p>
  <p><a class="btn" href="{WA}" target="_blank" rel="noopener">Revocar mi compra por WhatsApp</a></p>
  <h2>Qué pasa después</h2>
  <p>Te confirmamos la recepción de tu pedido de revocación, coordinamos la devolución del producto sin abrir y te devolvemos el dinero por el mismo medio de pago. [Plazos y forma de devolución a completar.]</p>
  <p>Datos del vendedor: {VENDEDOR}.</p>
""")
print("paginas legales generadas")
