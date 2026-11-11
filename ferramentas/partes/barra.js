  /* =================================================================
     3. A barra deslizante: fem de movimento e freio magnético
     O capítulo afirma três coisas que ficam abstratas no papel: que o
     campo freia como um atrito viscoso, com constante de tempo mR/(Bh)²;
     que a velocidade terminal é FR/(Bh)²; e que a potência mecânica
     gasta por quem puxa é exatamente a dissipada no resistor. Aqui os
     três números aparecem juntos, e o deslizante do tempo percorre a
     exponencial.
     ================================================================= */
  REGISTRO.barra = function (raiz) {
    var corpo = moldura(raiz, 'Barra deslizante nos trilhos');
    var cv = el('canvas');
    corpo.appendChild(cv);

    var B = 0.35;     // campo, em tesla
    var R = 0.50;     // resistência total, em ohm
    var F = 0.02;     // força externa constante, em newton
    var M = 0.020;    // massa da barra, em quilogramas
    var H = 0.12;     // comprimento da barra, em metros
    var t = 1.0;      // instante mostrado, em unidades de tau

    var controles = el('div', { class: 'controles' });
    corpo.appendChild(controles);
    deslizante(controles, 'campo \\(B\\) (T)', 0.05, 1.2, 0.01, B,
      function (v) { B = v; desenhar(); }, fmt2);
    deslizante(controles, 'resistência \\(R\\) (\\(\\Omega\\))', 0.1, 3, 0.05, R,
      function (v) { R = v; desenhar(); }, fmt2);
    deslizante(controles, 'força externa \\(F\\) (N)', 0.002, 0.08, 0.002, F,
      function (v) { F = v; desenhar(); }, fmt3);
    deslizante(controles, 'tempo \\(t/\\tau\\)', 0, 4, 0.05, t,
      function (v) { t = v; desenhar(); }, fmt2);
    tipografar(controles);

    var mostrar = cartoes(corpo, [
      { rot: 'velocidade', k: 'v' },
      { rot: 'fem \\(vBh\\)', k: 'e' },
      { rot: 'corrente', k: 'i' },
      { rot: 'potência dissipada', k: 'p' },
    ]);
    tipografar(corpo);

    function fmt2(v) { return v.toFixed(2).replace('.', ','); }
    function fmt3(v) { return v.toFixed(3).replace('.', ','); }

    function desenhar() {
      var k = (B * H) * (B * H) / R;      // atrito magnético
      var tau = M / k;
      var vt = F / k;                     // velocidade terminal
      var v = vt * (1 - Math.exp(-t));    // t já vem em unidades de tau
      var fem = v * B * H;
      var i = fem / R;
      var pot = i * i * R;

      var pr = G.preparar(cv, 320);
      var ct = pr.ct, L = pr.L, A = pr.A;
      var meio = Math.min(L * 0.56, L - 230);

      // ---------- esquerda: o circuito, com a barra onde ela estaria
      var xr = 40, xf = meio - 20, cy = A / 2 - 10, h2 = 58;
      ct.fillStyle = cor('--azul-pastel');
      ct.fillRect(xr - 14, cy - h2 - 26, xf - xr + 34, 2 * h2 + 52);
      ct.strokeStyle = cor('--borda'); ct.lineWidth = 1.4;
      ct.strokeRect(xr - 14, cy - h2 - 26, xf - xr + 34, 2 * h2 + 52);

      // símbolos de campo entrando na tela
      ct.strokeStyle = cor('--tinta-suave'); ct.lineWidth = 1.4;
      for (var a = 0; a < 6; a++) {
        for (var b = 0; b < 2; b++) {
          var xx = xr + 16 + a * (xf - xr - 20) / 5;
          var yy = cy - h2 / 1.6 + b * h2 * 1.25;
          ct.beginPath(); ct.arc(xx, yy, 5.5, 0, 2 * Math.PI); ct.stroke();
          ct.beginPath();
          ct.moveTo(xx - 3.8, yy - 3.8); ct.lineTo(xx + 3.8, yy + 3.8);
          ct.moveTo(xx + 3.8, yy - 3.8); ct.lineTo(xx - 3.8, yy + 3.8);
          ct.stroke();
        }
      }

      // trilhos e resistor
      ct.strokeStyle = cor('--azul'); ct.lineWidth = 2.6;
      ct.beginPath();
      ct.moveTo(xr, cy - h2); ct.lineTo(xf, cy - h2);
      ct.moveTo(xr, cy + h2); ct.lineTo(xf, cy + h2);
      ct.stroke();
      ct.beginPath();
      ct.moveTo(xr, cy - h2); ct.lineTo(xr, cy - 26);
      ct.lineTo(xr - 10, cy - 16); ct.lineTo(xr + 10, cy - 2);
      ct.lineTo(xr - 10, cy + 12); ct.lineTo(xr + 10, cy + 26);
      ct.lineTo(xr, cy + h2);
      ct.stroke();
      rotulo(ct, 'R', xr - 18, cy, cor('--azul'));

      // a barra, posicionada pela distância já percorrida
      var x0 = xr + 70;
      var caminho = vt * (t - 1 + Math.exp(-t));       // em unidades de tau*vt
      var frac = vt > 0 ? Math.min(1, caminho / (vt * 3.5)) : 0;
      var xb = x0 + frac * (xf - x0 - 24);
      ct.strokeStyle = cor('--vinho'); ct.lineWidth = 5;
      ct.lineCap = 'round';
      ct.beginPath(); ct.moveTo(xb, cy - h2); ct.lineTo(xb, cy + h2); ct.stroke();
      ct.lineCap = 'butt';

      // velocidade e força, com comprimento proporcional
      var esc = 46 / Math.max(vt, 1e-9);
      seta(ct, xb + 10, cy - h2 - 16, xb + 10 + Math.min(70, v * esc),
           cy - h2 - 16, cor('--azul'), 2.6);
      rotulo(ct, 'v', xb + 16 + Math.min(70, v * esc), cy - h2 - 28, cor('--azul'));
      var fesc = 46 / Math.max(F, 1e-9);
      seta(ct, xb - 10, cy + h2 + 18, xb - 10 - Math.min(70, k * v * fesc),
           cy + h2 + 18, cor('--verde'), 2.6);
      rotulo(ct, 'freio', xb - 24 - Math.min(70, k * v * fesc), cy + h2 + 30,
             cor('--verde'));

      // ---------- direita: a curva v(t), com o instante marcado
      var gx0 = meio + 54, gx1 = L - 18, gy0 = 26, gy1 = A - 44;
      ct.strokeStyle = cor('--borda'); ct.lineWidth = 1;
      ct.beginPath();
      ct.moveTo(gx0, gy0); ct.lineTo(gx0, gy1); ct.lineTo(gx1, gy1);
      ct.stroke();
      ct.setLineDash([5, 5]);
      ct.beginPath(); ct.moveTo(gx0, gy0 + 6); ct.lineTo(gx1, gy0 + 6); ct.stroke();
      ct.setLineDash([]);
      rotulo(ct, 'v terminal', gx0 + 54, gy0 - 2, cor('--tinta-suave'));
      rotulo(ct, 't / tau', (gx0 + gx1) / 2, gy1 + 20, cor('--tinta-suave'));

      ct.strokeStyle = cor('--vinho'); ct.lineWidth = 2.4;
      ct.beginPath();
      for (var n = 0; n <= 160; n++) {
        var tt = 4 * n / 160;
        var yy2 = gy1 - (1 - Math.exp(-tt)) * (gy1 - gy0 - 6);
        var xx2 = gx0 + tt / 4 * (gx1 - gx0);
        if (n === 0) ct.moveTo(xx2, yy2); else ct.lineTo(xx2, yy2);
      }
      ct.stroke();
      var xm = gx0 + t / 4 * (gx1 - gx0);
      var ym = gy1 - (1 - Math.exp(-t)) * (gy1 - gy0 - 6);
      ct.fillStyle = cor('--ambar');
      ct.beginPath(); ct.arc(xm, ym, 4.5, 0, 2 * Math.PI); ct.fill();

      mostrar({
        v: fmt2(v) + ' m/s  <small>de ' + fmt2(vt) + '</small>',
        e: fmt3(fem) + ' V',
        i: fmt3(i) + ' A',
        p: fmt3(pot * 1e3) + ' mW',
      });
    }

    registrarRedesenho(desenhar);
  };
