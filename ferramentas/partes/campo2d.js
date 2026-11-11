  /* =================================================================
     4. Divergente e rotacional de um campo plano
     O capítulo 1 afirma duas coisas que a intuição recusa: que um campo
     de linhas circulares pode ter rotacional nulo, e que um campo de
     linhas retas e paralelas pode ter rotacional grande. Aqui os dois
     números são calculados por diferenças finitas no ponto que o aluno
     escolhe, com o campo desenhado em volta.
     ================================================================= */
  REGISTRO.campo2d = function (raiz) {
    var corpo = moldura(raiz, 'Divergente e rotacional, no ponto que você escolher');
    var cv = el('canvas');
    corpo.appendChild(cv);

    var qual = 'fonte';
    var px = 0.6, py = 0.4;

    var CAMPOS = {
      fonte:        function (x, y) { return [x, y]; },
      rotacao:      function (x, y) { return [-y, x]; },
      cisalhamento: function (x, y) { return [y, 0]; },
      fio:          function (x, y) {
        var s2 = x * x + y * y;
        if (s2 < 1e-6) s2 = 1e-6;
        return [-y / s2, x / s2];
      },
    };
    var NOMES = {
      fonte: 'v = (x, y)',
      rotacao: 'v = (−y, x)',
      cisalhamento: 'v = (y, 0)',
      fio: 'v = \\(\\vers{\\phi}/s\\), o campo do fio',
    };

    var controles = el('div', { class: 'controles' });
    corpo.appendChild(controles);
    opcoes(controles, [{ rot: 'fonte', v: 'fonte' },
                       { rot: 'rotação', v: 'rotacao' },
                       { rot: 'cisalhamento', v: 'cisalhamento' },
                       { rot: 'campo do fio', v: 'fio' }], 0,
      function (v) { qual = v; desenhar(); });
    deslizante(controles, 'posição \\(x\\)', -1.6, 1.6, 0.05, px,
      function (v) { px = v; desenhar(); }, fmt);
    deslizante(controles, 'posição \\(y\\)', -1.6, 1.6, 0.05, py,
      function (v) { py = v; desenhar(); }, fmt);
    tipografar(controles);

    var mostrar = cartoes(corpo, [
      { rot: 'campo', k: 'c' },
      { rot: 'divergente', k: 'd' },
      { rot: 'rotacional (componente z)', k: 'r' },
      { rot: 'o que a conta diz', k: 'q' },
    ]);
    tipografar(corpo);

    function fmt(v) { return v.toFixed(2).replace('.', ','); }

    /* Diferenças centrais, exatamente como no operadores_vetoriais.py */
    function derivadas(x, y, h) {
      var f = CAMPOS[qual];
      var dx = f(x + h, y), ex = f(x - h, y);
      var dy = f(x, y + h), ey = f(x, y - h);
      return {
        div: (dx[0] - ex[0]) / (2 * h) + (dy[1] - ey[1]) / (2 * h),
        rot: (dx[1] - ex[1]) / (2 * h) - (dy[0] - ey[0]) / (2 * h),
      };
    }

    function desenhar() {
      var pr = G.preparar(cv, 340);
      var ct = pr.ct, L = pr.L, A = pr.A;
      var lado = Math.min(L, A) - 24;
      var cx = L / 2, cy = A / 2, esc = lado / 4.0;
      function X(x) { return cx + x * esc; }
      function Y(y) { return cy - y * esc; }

      var f = CAMPOS[qual];
      var n = 13, passo = 3.2 / (n - 1);
      var maior = 1e-9;
      var i, j, x, y, v;
      for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
          v = f(-1.6 + i * passo, -1.6 + j * passo);
          maior = Math.max(maior, Math.hypot(v[0], v[1]));
        }
      }
      for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
          x = -1.6 + i * passo; y = -1.6 + j * passo;
          v = f(x, y);
          var m = Math.hypot(v[0], v[1]);
          if (m < 1e-9) continue;
          var k = Math.min(1, m / maior) * 0.42 * esc * passo / 0.27;
          k = Math.min(k, 0.46 * esc * passo / 0.27);
          var ux = v[0] / m, uy = v[1] / m;
          seta(ct, X(x) - ux * k / 2, Y(y) + uy * k / 2,
               X(x) + ux * k / 2, Y(y) - uy * k / 2, cor('--azul-claro'), 1.8);
        }
      }

      // o ponto de prova, com o quadradinho em que as derivadas são tomadas
      var h = 0.18;
      ct.strokeStyle = cor('--vinho'); ct.lineWidth = 1.6;
      ct.setLineDash([5, 4]);
      ct.strokeRect(X(px - h), Y(py + h), 2 * h * esc, 2 * h * esc);
      ct.setLineDash([]);
      [[px + h, py], [px - h, py], [px, py + h], [px, py - h]].forEach(function (p) {
        var w = f(p[0], p[1]);
        var mm = Math.hypot(w[0], w[1]) || 1;
        var kk = 0.26 * esc;
        seta(ct, X(p[0]), Y(p[1]), X(p[0]) + w[0] / mm * kk,
             Y(p[1]) - w[1] / mm * kk, cor('--vinho'), 2.4);
      });
      ct.fillStyle = cor('--ambar');
      ct.beginPath(); ct.arc(X(px), Y(py), 4.5, 0, 2 * Math.PI); ct.fill();

      // eixos discretos
      ct.strokeStyle = cor('--borda'); ct.lineWidth = 1;
      ct.beginPath();
      ct.moveTo(X(-1.8), Y(0)); ct.lineTo(X(1.8), Y(0));
      ct.moveTo(X(0), Y(-1.8)); ct.lineTo(X(0), Y(1.8));
      ct.stroke();

      var r = derivadas(px, py, 1e-4);
      var diagnostico;
      if (Math.abs(r.div) < 1e-6 && Math.abs(r.rot) < 1e-6) {
        diagnostico = 'não diverge nem gira';
      } else if (Math.abs(r.rot) < 1e-6) {
        diagnostico = 'só diverge';
      } else if (Math.abs(r.div) < 1e-6) {
        diagnostico = 'só gira';
      } else {
        diagnostico = 'diverge e gira';
      }

      mostrar({
        c: NOMES[qual],
        d: fmt(r.div),
        r: fmt(r.rot),
        q: diagnostico,
      });
      tipografar(corpo);
    }

    registrarRedesenho(desenhar);
  };
