(function () {
  "use strict";
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* 1. Títulos: cada línea (separada por <br>) se envuelve para animarla con una máscara */
  document.querySelectorAll(".display,.h1,.h2,.hero__titulo").forEach(function (h) {
    var lineas = h.innerHTML.split(/<br\s*\/?>/i);
    h.innerHTML = lineas.map(function (t, i) {
      return '<span class="ln"><span style="--l:' + i + '">' + t.trim() + "</span></span>";
    }).join("");
  });
  /* hijos de cada bloque: orden de entrada escalonado */
  document.querySelectorAll(".reveal,.hero__cta").forEach(function (b) {
    Array.prototype.forEach.call(b.children, function (c, i) { c.style.setProperty("--i", i); });
  });

  /* 2. Aviso de mayoría de edad (se recuerda en la sesión) */
  var edad = document.getElementById("edad");
  var fondo = document.querySelectorAll("body > .tramo, body > footer, body > .skip");
  var ok = false;
  try { ok = sessionStorage.getItem("rdl-edad") === "1"; } catch (e) {}
  function bloquear(on) {
    fondo.forEach(function (n) { if (on) { n.setAttribute("inert", ""); } else { n.removeAttribute("inert"); } });
  }
  function listo() { document.body.classList.add("listo"); }
  if (!ok) {
    edad.hidden = false;
    bloquear(true);
    document.body.style.overflow = "hidden";
    document.getElementById("edad-si").focus();
  } else {
    requestAnimationFrame(listo);
  }
  document.getElementById("edad-si").addEventListener("click", function () {
    try { sessionStorage.setItem("rdl-edad", "1"); } catch (e) {}
    bloquear(false);
    document.body.style.overflow = "";
    listo();
    if (reduce) { edad.hidden = true; }
    else { edad.classList.add("saliendo"); setTimeout(function () { edad.hidden = true; edad.classList.remove("saliendo"); }, 190); }
  });
  /* el foco no sale del aviso mientras esta abierto (no se cierra con Escape: hay que responder) */
  edad.addEventListener("keydown", function (e) {
    if (e.key !== "Tab" || edad.hidden) return;
    var bt = edad.querySelectorAll("button");
    var first = bt[0], last = bt[bt.length - 1];
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
  });
  document.getElementById("edad-no").addEventListener("click", function () {
    document.getElementById("edad-nota").hidden = false;
  });

  /* 3b. Letras de "Rugido de León": la foto de adentro se desplaza hacia abajo al bajar y hacia arriba al subir */
  var letras = document.querySelectorAll(".h-foto");
  var vhActual = window.innerHeight;
  function leerLetras() {
    if (reduce) return [];
    return Array.prototype.map.call(letras, function (el) {
      var r = el.getBoundingClientRect();
      return { el: el, top: r.top, h: r.height };
    });
  }
  function escribirLetras(lec) {
    lec.forEach(function (l) {
      if (l.top > vhActual || l.top + l.h < 0) return;     /* fuera de pantalla: no se repinta nada */
      var p = Math.min(1, Math.max(0, (vhActual - l.top) / (vhActual + l.h)));
      l.el.style.setProperty("--py", ((1 - p) * 100).toFixed(1) + "%");
    });
  }
  /* 3c. Momento principal: al bajar, el título del home se retira (se aleja y se apaga) mientras la primera sección lo cubre */
  var hTitulo = document.querySelector(".hero__titulo");
  var hCta = document.querySelector(".hero__cta");
  function retirarHome(sy) {
    if (reduce || !hTitulo) return;
    var p = Math.min(1, Math.max(0, sy / (vhActual * 0.85)));
    var q = p * p;                                   /* arranca suave y se acelera cuando la sección ya lo cubre */
    if (q < 0.002) {                                  /* en reposo no se deja ninguna capa animada: el texto se dibuja nítido */
      hTitulo.style.opacity = ""; hTitulo.style.transform = "";
      if (hCta) { hCta.style.opacity = ""; }
      return;
    }
    hTitulo.style.opacity = (1 - q).toFixed(3);
    hTitulo.style.transform = "translate3d(0," + (-q * 44).toFixed(1) + "px,0) scale(" + (1 - q * 0.04).toFixed(4) + ")";
    if (hCta) { hCta.style.opacity = (1 - q).toFixed(3); }
  }

  /* 3c-bis. Las transiciones entre secciones solo corren mientras la sección entra o sale; en reposo el texto queda sin capas y se ve nítido */
  var cartas = document.querySelectorAll(".pila > .card:not(.card--foto)");
  function estadoCartas(lista) {
    var vh = vhActual;
    lista.forEach(function (t) {
      t.c.classList.toggle("a-sale", t.top < 0 && t.bottom > -vh * 0.1);
    });
  }

  /* 3e. El fondo del pie se carga cuando el pie está por aparecer */
  var pie = document.getElementById("pie");
  if (pie) {
    if ("IntersectionObserver" in window) {
      var iop = new IntersectionObserver(function (es) {
        if (es[0].isIntersecting) { pie.classList.add("lista"); iop.disconnect(); }
      }, { rootMargin: "900px 0px" });
      iop.observe(pie);
    } else { pie.classList.add("lista"); }
  }

  var tl = false;
  function tick() {
    vhActual = window.innerHeight;
    var lec = leerLetras();                              /* lecturas */
    var tarjetas = Array.prototype.map.call(cartas, function (c) { var r = c.getBoundingClientRect(); return { c: c, top: r.top, bottom: r.bottom }; });
    var sy = window.scrollY;
    escribirLetras(lec);                                 /* escrituras */
    retirarHome(sy);
    estadoCartas(tarjetas);
  }
  function pedirLetras() { if (!tl) { tl = true; requestAnimationFrame(function () { tl = false; tick(); }); } }
  window.addEventListener("scroll", pedirLetras, { passive: true });
  window.addEventListener("resize", pedirLetras);
  tick();

  /* 3d. Origen: el contorno de Mendoza se dibuja al llegar a la sección y después aparece el punto de San Rafael */
  var mza = document.querySelector(".mapa__mza");
  var origen = document.getElementById("origen");
  if (mza && origen && !reduce && "IntersectionObserver" in window && mza.getTotalLength) {
    mza.style.setProperty("--len", Math.ceil(mza.getTotalLength()));
    origen.classList.add("mapa-pre");
    var iom = new IntersectionObserver(function (es) {
      if (es[0].isIntersecting) { origen.classList.add("mapa-go"); iom.disconnect(); }
    }, { threshold: 0.3 });
    iom.observe(origen);
  }

  /* 3e. Botones de WhatsApp: el destello del borde solo corre mientras el botón está en pantalla */
  var botones = document.querySelectorAll(".btn--wa");
  if (!reduce && "IntersectionObserver" in window) {
    var iob = new IntersectionObserver(function (es) {
      es.forEach(function (e) { e.target.classList.toggle("vista", e.isIntersecting); });
    }, { threshold: 0.3 });
    botones.forEach(function (b) { iob.observe(b); });
  }

  /* 3f. Cifras de la ficha (alcohol, cosecha, medida): cuentan hasta su valor al entrar en pantalla */
  var nums = document.querySelectorAll(".num");
  function formato(v, dec, sep, suf) {
    var t = v.toLocaleString("es-AR", { minimumFractionDigits: dec, maximumFractionDigits: dec, useGrouping: sep !== "0" });
    return t + (suf || "");
  }
  if (!reduce && "IntersectionObserver" in window && nums.length) {
    nums.forEach(function (n) {
      var fin = parseFloat(n.getAttribute("data-valor")), dec = +n.getAttribute("data-dec") || 0;
      var sep = n.getAttribute("data-sep"), suf = n.getAttribute("data-suf") || "";
      n.setAttribute("aria-label", n.textContent);          /* el lector de pantalla lee el valor final */
      n.style.minWidth = n.getBoundingClientRect().width + "px";
      n.textContent = formato(0, dec, sep, suf);
      var ion = new IntersectionObserver(function (es) {
        if (!es[0].isIntersecting) return;
        ion.disconnect();
        var t0 = null, dur = 1900;
        function paso(ts) {
          if (t0 === null) t0 = ts;
          var p = Math.min(1, (ts - t0) / dur);
          var e = 1 - Math.pow(1 - p, 4);                    /* frena sin rebote */
          n.textContent = formato(fin * e, dec, sep, suf);
          if (p < 1) requestAnimationFrame(paso); else n.textContent = formato(fin, dec, sep, suf);
        }
        requestAnimationFrame(paso);
      }, { threshold: 0.6 });
      ion.observe(n);
    });
  }

  /* 4. La foto del cierre carga cuando se acerca */
  var foto = document.getElementById("foto-cierre");
  if (foto) {
    if ("IntersectionObserver" in window) {
      var iof = new IntersectionObserver(function (es) {
        if (es[0].isIntersecting) { foto.classList.add("lista"); iof.disconnect(); }
      }, { rootMargin: "900px 0px" });
      iof.observe(foto);
    } else { foto.classList.add("lista"); }
  }

  /* 5. Aparición de textos al entrar en pantalla */
  var rev = document.querySelectorAll(".reveal");
  if (reduce || !("IntersectionObserver" in window)) {
    rev.forEach(function (n) { n.classList.add("in"); });
  } else {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
    }, { threshold: 0.2 });
    rev.forEach(function (n) { io.observe(n); });
  }
})();
