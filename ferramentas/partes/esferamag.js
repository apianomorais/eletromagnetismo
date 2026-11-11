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

      var cor = (qual === 'B') ? cor('--vinho') : cor('--verde');
      ct.strokeStyle = cor;
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
                     X(pts[j][0]), Z(pts[j][1]), cor, 1.8);
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
