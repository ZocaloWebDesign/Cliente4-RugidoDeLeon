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
    edad.hidden = true;
    bloquear(false);
    document.body.style.overflow = "";
    listo();
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

  /* 3. Fondo continuo: una sola imagen que se desplaza más lento que el contenido */
  var img = document.getElementById("bg-img");
  var ticking = false, idle;
  function pan() {
    ticking = false;
    if (reduce) return;
    var vh = window.innerHeight;
    var max = Math.max(0, img.offsetHeight - vh);
    var doc = document.documentElement.scrollHeight - vh;
    var p = doc > 0 ? Math.min(1, Math.max(0, window.scrollY / doc)) : 0;
    img.style.transform = "translate3d(0," + (-p * max).toFixed(1) + "px,0)";
    document.documentElement.style.setProperty("--bgy", (-p * max).toFixed(1) + "px");
  }
  function onScroll() {
    if (!ticking) { ticking = true; requestAnimationFrame(pan); }
    img.style.willChange = "transform";                       /* solo mientras se desplaza */
    clearTimeout(idle);
    idle = setTimeout(function () { img.style.willChange = "auto"; }, 180);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", onScroll);
  pan();

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
