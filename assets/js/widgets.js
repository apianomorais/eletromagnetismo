/* ===================================================================
   widgets.js: simuladores e calculadoras interativas
   Uso nas páginas: <div data-widget="nome"></div>
   Eletromagnetismo / LFCA–URCA
   =================================================================== */

(function () {
  'use strict';

  /* ---------- utilitários de DOM ---------- */
  function el(tag, attrs, filhos) {
    var n = document.createElement(tag);
    if (attrs) Object.keys(attrs).forEach(function (k) {
      if (k === 'class') n.className = attrs[k];
      else if (k === 'html') n.innerHTML = attrs[k];
      else if (k === 'texto') n.textContent = attrs[k];
      else n.setAttribute(k, attrs[k]);
    });
    (filhos || []).forEach(function (c) { n.appendChild(c); });
    return n;
  }

  function moldura(raiz, titulo) {
    raiz.classList.add('widget');
    raiz.appendChild(el('div', { class: 'widget-cabeca', texto: titulo }));
    var corpo = el('div', { class: 'widget-corpo' });
    raiz.appendChild(corpo);
    return corpo;
  }

  /* Devolve o <input type=range>, para que o chamador possa movê-lo por código. */
  function deslizante(pai, rot, min, max, passo, inicial, aoMudar, formata) {
    var campo = el('div', { class: 'campo' });
    var lab = el('label');
    var val = el('span', { class: 'valor' });
    var inp = el('input', { type: 'range', min: min, max: max, step: passo, value: inicial });
    function mostrar() {
      val.innerHTML = formata ? formata(Number(inp.value)) : String(inp.value).replace('.', ',');
    }
    lab.innerHTML = rot + ' ';
    lab.appendChild(val);
    campo.appendChild(lab);
    campo.appendChild(inp);
    pai.appendChild(campo);
    inp.addEventListener('input', function () { mostrar(); aoMudar(Number(inp.value)); });
    mostrar();
    return inp;
  }

  /* Botões mutuamente exclusivos. Devolve uma função que troca a seleção. */
  function opcoes(pai, lista, inicial, aoMudar) {
    var cx = el('div', { class: 'botoes' });
    var bs = lista.map(function (o, i) {
      var b = el('button', { type: 'button', texto: o.rot });
      if (i !== inicial) b.classList.add('sec');
      b.addEventListener('click', function () {
        bs.forEach(function (x) { x.classList.add('sec'); });
        b.classList.remove('sec');
        aoMudar(o.v, o);
      });
      cx.appendChild(b);
      return b;
    });
    pai.appendChild(cx);
    return function (i) { bs[i].click(); };
  }

  function cartoes(pai, lista) {
    var g = el('div', { class: 'grade-num' });
    lista.forEach(function (c) {
      g.appendChild(el('div', { class: 'cartao-num', html:
        '<span class="rot">' + c.rot + '</span><span class="val" data-k="' + c.k + '">·</span>' }));
    });
    pai.appendChild(g);
    return function (vals) {
      Object.keys(vals).forEach(function (k) {
        var n = g.querySelector('[data-k="' + k + '"]');
        if (n) n.innerHTML = vals[k];
      });
    };
  }

  /* O widget costuma ser montado antes de o MathJax terminar de carregar,
     e nesse caso typesetPromise ainda não existe. Em vez de desistir em
     silêncio, deixando \(\mu_0\) cru na tela, espera a promessa de
     inicialização e tipografa depois. */
  function tipografar(no) {
    var mj = window.MathJax;
    if (!mj) {
      window.addEventListener('load', function () {
        if (window.MathJax && window.MathJax.typesetPromise) tipografar(no);
      }, { once: true });
      return;
    }
    if (mj.typesetPromise) { mj.typesetPromise([no]).catch(function () {}); return; }
    if (mj.startup && mj.startup.promise) {
      mj.startup.promise.then(function () {
        if (window.MathJax.typesetPromise) {
          window.MathJax.typesetPromise([no]).catch(function () {});
        }
      });
    }
  }

  /* As cores dos desenhos vêm do CSS, e não escritas à mão aqui, para que
     trocar a paleta do site troque também o que é pintado no canvas. */
  function cor(nome, alternativa) {
    var v = getComputedStyle(document.documentElement).getPropertyValue(nome);
    return (v || '').trim() || alternativa || '#2b3240';
  }

  var REGISTRO = {};


  /* Seta com ponta, usada por quase todo widget de cinemática. */
  function seta(ct, xa, ya, xb, yb, cor, esp, tracejado) {
    var dx = xb - xa, dy = yb - ya, r = Math.sqrt(dx * dx + dy * dy);
    if (r < 1.5) return;
    var ux = dx / r, uy = dy / r, p = Math.min(8, r * 0.42);
    ct.save();
    ct.strokeStyle = cor; ct.fillStyle = cor;
    ct.lineWidth = esp || 2; ct.lineCap = 'round'; ct.lineJoin = 'round';
    if (tracejado) ct.setLineDash(tracejado);
    ct.beginPath(); ct.moveTo(xa, ya); ct.lineTo(xb - ux * p * 0.8, yb - uy * p * 0.8);
    ct.stroke();
    ct.setLineDash([]);
    ct.beginPath();
    ct.moveTo(xb, yb);
    ct.lineTo(xb - ux * p - uy * p * 0.46, yb - uy * p + ux * p * 0.46);
    ct.lineTo(xb - ux * p + uy * p * 0.46, yb - uy * p - ux * p * 0.46);
    ct.closePath(); ct.fill();
    ct.restore();
  }

  /* Rótulo com halo branco, legível por cima de qualquer desenho. */
  function rotulo(ct, texto, x, y, cor, al, bl, fonte, corHalo) {
    ct.save();
    ct.font = fonte || '600 11px system-ui, sans-serif';
    ct.textAlign = al || 'center'; ct.textBaseline = bl || 'middle';
    ct.lineJoin = 'round'; ct.lineWidth = 3.5; ct.strokeStyle = corHalo || '#fff';
    ct.strokeText(texto, x, y);
    ct.fillStyle = cor; ct.fillText(texto, x, y);
    ct.restore();
  }

  /* =================================================================
     1. A trajetória de uma carga em campos cruzados
     O texto deduz a cicloide e afirma três coisas que só convencem
     desenhadas: que sem campo elétrico a órbita fecha num círculo de
     raio mv/qB; que ligando E o círculo começa a caminhar, e sempre
     perpendicularmente aos dois campos; e que a velocidade média da
     deriva não depende nem da carga nem da massa, só da razão E/B.
     A integração é pelo método de Boris, o mesmo do script do Spyder.
     ================================================================= */
  REGISTRO.trajetoria = function (raiz) {
    var corpo = moldura(raiz, 'Carga em campos cruzados');
    var cv = el('canvas');
    corpo.appendChild(cv);

    var E0 = 1.0;      // campo elétrico, em z
    var B0 = 1.0;      // campo magnético, em x (para dentro da tela)
    var v0 = 0.0;      // velocidade inicial, em y
    var sinal = 1;     // carga positiva ou negativa

    var controles = el('div', { class: 'controles' });
    corpo.appendChild(controles);
    deslizante(controles, 'campo elétrico \\(E_0\\)', 0, 2.5, 0.05, E0,
      function (v) { E0 = v; desenhar(); }, fmt);
    deslizante(controles, 'campo magnético \\(B_0\\)', 0.3, 2.5, 0.05, B0,
      function (v) { B0 = v; desenhar(); }, fmt);
    deslizante(controles, 'velocidade inicial \\(v_{y0}\\)', -2, 3, 0.05, v0,
      function (v) { v0 = v; desenhar(); }, fmt);
    opcoes(controles, [{ rot: 'carga +', v: 1 }, { rot: 'carga −', v: -1 }], 0,
      function (v) { sinal = v; desenhar(); });
    tipografar(controles);

    var mostrar = cartoes(corpo, [
      { rot: 'deriva \\(E_0/B_0\\)', k: 'd' },
      { rot: 'período \\(2\\pi m/qB_0\\)', k: 'T' },
      { rot: 'raio \\(m v / q B_0\\)', k: 'R' },
      { rot: 'curva', k: 'tipo' },
    ]);

    function fmt(v) { return v.toFixed(2).replace('.', ','); }

    /* Um passo de Boris: meio empurrão elétrico, rotação pura em torno
       de B, outro meio empurrão. A rotação preserva |v| por construção,
       que é o que a física manda para a força magnética. */
    function passo(v, dt, q) {
      var ex = 0, ez = E0;                      // E = E0 ẑ
      var b = q * B0 * dt / 2;                  // B = B0 x̂, movimento no plano yz
      var vy = v[0] + 0 * dt / 2;
      var vz = v[1] + q * ez * dt / 2;
      var s = 2 * b / (1 + b * b);
      var vyl = vy + vz * b;
      var vzl = vz - vy * b;
      var vy2 = vy + vzl * s;
      var vz2 = vz - vyl * s;
      return [vy2 + 0 * dt / 2, vz2 + q * ez * dt / 2];
    }

    function integrar(q) {
      var dt = 0.004, n = 9000;
      var p = [0, 0], v = [v0, 0], pts = [[0, 0]];
      for (var i = 0; i < n; i++) {
        v = passo(v, dt, q);
        p = [p[0] + v[0] * dt, p[1] + v[1] * dt];
        if (i % 3 === 0) pts.push([p[0], p[1]]);
      }
      return pts;
    }

    function desenhar() {
      var q = sinal;
      var pts = integrar(q);
      var pr = G.preparar(cv, 330);
      var ct = pr.ct, L = pr.L, A = pr.A;

      // janela que acompanha a trajetória
      var ymin = Infinity, ymax = -Infinity, zmin = Infinity, zmax = -Infinity;
      pts.forEach(function (p) {
        if (p[0] < ymin) ymin = p[0];
        if (p[0] > ymax) ymax = p[0];
        if (p[1] < zmin) zmin = p[1];
        if (p[1] > zmax) zmax = p[1];
      });
      var folga = 0.12 * Math.max(ymax - ymin, 0.5);
      ymin -= folga; ymax += folga;
      var meio = (zmin + zmax) / 2;
      var alt = (ymax - ymin) * A / L;
      zmin = meio - alt / 2; zmax = meio + alt / 2;

      function X(y) { return 46 + (y - ymin) / (ymax - ymin) * (L - 62); }
      function Y(z) { return A - 36 - (z - zmin) / (zmax - zmin) * (A - 54); }

      // eixos
      ct.strokeStyle = cor('--borda'); ct.lineWidth = 1;
      ct.beginPath(); ct.moveTo(46, Y(0)); ct.lineTo(L - 16, Y(0)); ct.stroke();
      rotulo(ct, 'y', L - 22, Y(0) + 14, cor('--tinta-suave'));
      rotulo(ct, 'z', 34, 24, cor('--tinta-suave'));

      // os dois campos, no canto
      seta(ct, 70, A - 60, 70, A - 96, cor('--vinho'), 2.4);
      rotulo(ct, 'E', 82, A - 92, cor('--vinho'));
      ct.strokeStyle = cor('--azul'); ct.lineWidth = 2;
      ct.beginPath(); ct.arc(118, A - 78, 9, 0, 2 * Math.PI); ct.stroke();
      ct.beginPath();
      ct.moveTo(112, A - 84); ct.lineTo(124, A - 72);
      ct.moveTo(124, A - 84); ct.lineTo(112, A - 72); ct.stroke();
      rotulo(ct, 'B', 132, A - 88, cor('--azul'));

      // a trajetória
      ct.strokeStyle = cor('--azul'); ct.lineWidth = 2.2;
      ct.lineJoin = 'round'; ct.beginPath();
      pts.forEach(function (p, i) {
        var x = X(p[0]), y = Y(p[1]);
        if (i === 0) ct.moveTo(x, y); else ct.lineTo(x, y);
      });
      ct.stroke();

      // a reta de deriva, para comparar
      var vd = E0 / B0;
      ct.strokeStyle = cor('--vinho'); ct.lineWidth = 1.4;
      ct.setLineDash([6, 5]);
      ct.beginPath();
      ct.moveTo(X(0), Y(vd ? (zmin + zmax) / 2 : 0));
      ct.lineTo(X(ymax), Y((zmin + zmax) / 2));
      ct.stroke();
      ct.setLineDash([]);

      ct.fillStyle = cor('--ambar');
      ct.beginPath(); ct.arc(X(0), Y(0), 4.5, 0, 2 * Math.PI); ct.fill();

      var vtot = Math.abs(v0);
      var tipo = (E0 === 0) ? 'círculo'
        : (Math.abs(v0 - vd) < 0.03 ? 'cicloide comum'
          : (v0 < vd ? 'cicloide encurtada' : 'cicloide alongada'));
      mostrar({
        d: fmt(vd), T: fmt(2 * Math.PI / B0), R: fmt(vtot / B0), tipo: tipo,
      });
    }

    registrarRedesenho(desenhar);
  };

  /* =================================================================
     2. A esfera uniformemente magnetizada: B contra H
     O texto afirma que B e H não se parecem, e a afirmação é difícil
     de engolir enquanto as duas figuras não estão lado a lado. Aqui
     as linhas são integradas dos campos exatos: dentro, B é uniforme
     e vale (2/3) mu0 M, enquanto H vale -M/3; fora, os dois são o
     mesmo campo de dipolo, a menos do fator mu0.
     ================================================================= */
  REGISTRO.esferamag = function (raiz) {
    var corpo = moldura(raiz, 'Esfera uniformemente magnetizada');
    var cv = el('canvas');
    corpo.appendChild(cv);

    var R = 1.0;       // raio, em unidades do desenho
    var M = 1.0;       // magnetização, normalizada
    var qual = 'B';    // campo mostrado
    var mostraK = true;

    var controles = el('div', { class: 'controles' });
    corpo.appendChild(controles);
    opcoes(controles, [{ rot: 'linhas de B', v: 'B' },
                       { rot: 'linhas de H', v: 'H' }], 0,
      function (v) { qual = v; desenhar(); });
    opcoes(controles, [{ rot: 'com a corrente ligada', v: true },
                       { rot: 'sem', v: false }], 0,
      function (v) { mostraK = v; desenhar(); });
    deslizante(controles, 'magnetização \\(M\\)', 0.2, 2, 0.05, M,
      function (v) { M = v; desenhar(); }, fmt);
    tipografar(controles);

    var mostrar = cartoes(corpo, [
      { rot: '\\(B\\) dentro', k: 'bi' },
      { rot: '\\(H\\) dentro', k: 'hi' },
      { rot: 'momento \\(m\\)', k: 'm' },
      { rot: '\\(K_b\\) no equador', k: 'k' },
    ]);
    tipografar(corpo);

    function fmt(v) { return v.toFixed(2).replace('.', ','); }

    /* Campo no plano xz, em unidades de mu0 M (para B) ou de M (para H).
       Dentro: B = (2/3) ẑ e H = -(1/3) ẑ. Fora: dipolo de m = (4/3) pi R^3 M,
       que dá B = (R^3/3) [3(ẑ·r̂)r̂ - ẑ] / r^3, e H = B / mu0. */
    function campo(x, z) {
      var r2 = x * x + z * z;
      if (r2 < R * R) {
        return (qual === 'B') ? [0, 2 / 3 * M] : [0, -M / 3];
      }
      var r = Math.sqrt(r2), c = z / r;
      var k = M * R * R * R / (3 * r * r * r);
      return [k * 3 * c * (x / r), k * (3 * c * c - 1)];
    }

    /* Uma linha de campo, integrada nos dois sentidos com Runge-Kutta 4
       de passo fixo no comprimento de arco. Parar na borda da esfera não
       serve: as linhas de B atravessam o material, e é esse o ponto. */
    function linha(x0, z0, sentido, passos, lim, parar) {
      var pts = [[x0, z0]], x = x0, z = z0, h = sentido * 0.035;
      function u(x, z) {
        var v = campo(x, z), n = Math.hypot(v[0], v[1]);
        return n < 1e-12 ? [0, 0] : [v[0] / n, v[1] / n];
      }
      for (var i = 0; i < passos; i++) {
        var a = u(x, z);
        var b = u(x + h / 2 * a[0], z + h / 2 * a[1]);
        var c = u(x + h / 2 * b[0], z + h / 2 * b[1]);
        var d = u(x + h * c[0], z + h * c[1]);
        x += h / 6 * (a[0] + 2 * b[0] + 2 * c[0] + d[0]);
        z += h / 6 * (a[1] + 2 * b[1] + 2 * c[1] + d[1]);
        if (!isFinite(x) || !isFinite(z)) break;
        /* As linhas de H nascem e morrem na superfície, onde mora a carga
           magnética efetiva: ali o campo é descontínuo e seguir em frente
           só produziria um vaivém numérico. */
        if (parar && (Math.hypot(x, z) - R) * (Math.hypot(x0, z0) - R) < 0) {
          pts.push([x, z]);
          break;
        }
        if (Math.hypot(x, z) > lim) { pts.push([x, z]); break; }
        pts.push([x, z]);
      }
      return pts;
    }

    function desenhar() {
      var pr = G.preparar(cv, 360);
      var ct = pr.ct, L = pr.L, A = pr.A;
      var esc = Math.min(L, A) / 7.2;
      var cx = L / 2, cz = A / 2;
      function X(x) { return cx + x * esc; }
      function Z(z) { return cz - z * esc; }

      // a esfera
      ct.fillStyle = cor('--azul-pastel');
      ct.strokeStyle = cor('--azul');
      ct.lineWidth = 2;
      ct.beginPath(); ct.arc(cx, cz, R * esc, 0, 2 * Math.PI);
      ct.fill(); ct.stroke();

      // as sementes: dentro da esfera para B, fora dela para H
      var sementes = [], k;
      for (k = -3; k <= 3; k++) {
        if (k !== 0) sementes.push([k * 0.24 * R, 0]);
      }
      if (qual === 'B') {
        for (k = 1; k <= 2; k++) {
          sementes.push([R * (1 + 0.55 * k), 0]);
          sementes.push([-R * (1 + 0.55 * k), 0]);
        }
      } else {
        for (k = 1; k <= 4; k++) {
          sementes.push([R * Math.sin(k * 0.33), R * Math.cos(k * 0.33) + 0.05 * R]);
          sementes.push([-R * Math.sin(k * 0.33), R * Math.cos(k * 0.33) + 0.05 * R]);
        }
      }

      var traco = (qual === 'B') ? cor('--vinho') : cor('--verde');
      ct.strokeStyle = traco;
      ct.lineWidth = 1.6;
      ct.lineJoin = 'round';
      var lim = 0.5 * Math.min(L, A) / esc;
      sementes.forEach(function (s) {
        [1, -1].forEach(function (sentido) {
          var pts = linha(s[0], s[1], sentido, 1400, lim, qual === 'H');
          if (pts.length < 3) return;
          ct.beginPath();
          pts.forEach(function (p, i) {
            var xx = X(p[0]), zz = Z(p[1]);
            if (i === 0) ct.moveTo(xx, zz); else ct.lineTo(xx, zz);
          });
          ct.stroke();
          // pontas ao longo do caminho, para dizer o sentido
          if (sentido === 1) {
            [0.28, 0.62].forEach(function (f) {
              var j = Math.floor(pts.length * f);
              if (j > 6) {
                seta(ct, X(pts[j - 6][0]), Z(pts[j - 6][1]),
                     X(pts[j][0]), Z(pts[j][1]), traco, 1.8);
              }
            });
          }
        });
      });

      // a magnetização, sempre visível
      seta(ct, cx, cz + 0.42 * esc, cx, cz - 0.42 * esc, cor('--azul'), 2.6);
      rotulo(ct, 'M', cx + 14, cz - 0.3 * esc, cor('--azul'));

      // a corrente ligada de superfície, Kb = M sen(theta) phi^
      if (mostraK) {
        [-1, 1].forEach(function (lado) {
          for (var i = -2; i <= 2; i++) {
            var ang = i * 0.5;
            var xx = cx + lado * R * esc * Math.cos(ang);
            var zz = cz - R * esc * Math.sin(ang);
            var rr = 4.2 + 2.4 * Math.cos(ang);
            ct.strokeStyle = cor('--azul-claro'); ct.lineWidth = 1.6;
            ct.beginPath(); ct.arc(xx, zz, rr, 0, 2 * Math.PI); ct.stroke();
            if (lado > 0) {
              ct.beginPath();
              ct.moveTo(xx - rr * 0.6, zz - rr * 0.6);
              ct.lineTo(xx + rr * 0.6, zz + rr * 0.6);
              ct.moveTo(xx + rr * 0.6, zz - rr * 0.6);
              ct.lineTo(xx - rr * 0.6, zz + rr * 0.6);
              ct.stroke();
            } else {
              ct.fillStyle = cor('--azul-claro');
              ct.beginPath(); ct.arc(xx, zz, 1.9, 0, 2 * Math.PI); ct.fill();
            }
          }
        });
        rotulo(ct, 'Kb', cx + R * esc + 26, cz + 0.8 * esc, cor('--azul-claro'));
      }

      mostrar({
        bi: fmt(2 / 3 * M) + ' \\(\\mu_0 M_0\\)',
        hi: '−' + fmt(M / 3) + ' \\(M_0\\)',
        m: fmt(4 / 3 * Math.PI * M) + ' \\(R^3 M_0\\)',
        k: fmt(M) + ' \\(M_0 R\\)',
      });
      tipografar(corpo);
    }

    registrarRedesenho(desenhar);
  };

  /* ---------- inicialização ---------- */
  document.addEventListener('DOMContentLoaded', function () {
    Array.prototype.forEach.call(document.querySelectorAll('[data-widget]'), function (n) {
      var f = REGISTRO[n.getAttribute('data-widget')];
      if (f) {
        try { f(n); }
        catch (e) {
          n.innerHTML = '<div class="saida">Não foi possível carregar este componente.</div>';
          if (window.console) console.error(e);
        }
      }
    });
  });
})();
