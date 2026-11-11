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
      ct.strokeStyle = '#d9ddea'; ct.lineWidth = 1;
      ct.beginPath(); ct.moveTo(46, Y(0)); ct.lineTo(L - 16, Y(0)); ct.stroke();
      rotulo(ct, 'y', L - 22, Y(0) + 14, '#4a5560');
      rotulo(ct, 'z', 34, 24, '#4a5560');

      // os dois campos, no canto
      seta(ct, 70, A - 60, 70, A - 96, '#a8181d', 2.4);
      rotulo(ct, 'E', 82, A - 92, '#a8181d');
      ct.strokeStyle = '#1c2c60'; ct.lineWidth = 2;
      ct.beginPath(); ct.arc(118, A - 78, 9, 0, 2 * Math.PI); ct.stroke();
      ct.beginPath();
      ct.moveTo(112, A - 84); ct.lineTo(124, A - 72);
      ct.moveTo(124, A - 84); ct.lineTo(112, A - 72); ct.stroke();
      rotulo(ct, 'B', 132, A - 88, '#1c2c60');

      // a trajetória
      ct.strokeStyle = '#1c2c60'; ct.lineWidth = 2.2;
      ct.lineJoin = 'round'; ct.beginPath();
      pts.forEach(function (p, i) {
        var x = X(p[0]), y = Y(p[1]);
        if (i === 0) ct.moveTo(x, y); else ct.lineTo(x, y);
      });
      ct.stroke();

      // a reta de deriva, para comparar
      var vd = E0 / B0;
      ct.strokeStyle = '#a8181d'; ct.lineWidth = 1.4;
      ct.setLineDash([6, 5]);
      ct.beginPath();
      ct.moveTo(X(0), Y(vd ? (zmin + zmax) / 2 : 0));
      ct.lineTo(X(ymax), Y((zmin + zmax) / 2));
      ct.stroke();
      ct.setLineDash([]);

      ct.fillStyle = '#b5831f';
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
