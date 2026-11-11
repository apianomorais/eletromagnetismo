# -*- coding: utf-8 -*-
"""Por que as bobinas de Helmholtz ficam separadas por exatamente um raio.

O QUE RESOLVE
    Usa biot_savart.py para calcular o campo no eixo de duas bobinas coaxiais
    iguais, separadas por uma distância d, e mostra que a uniformidade no
    centro é máxima quando d = R.

A FÍSICA
    No centro, por simetria, a derivada primeira de B em z já é nula para
    qualquer d. A escolha d = R é o que anula também a derivada SEGUNDA: com
    isso o primeiro termo de erro é de quarta ordem, e o campo fica constante
    dentro de uma região grande.

COMO CONFERIR SE ESTÁ CERTO
    1. O campo no centro, para d = R, tem de valer B = (4/5)^(3/2) mu0 N I / R.
       O programa compara.
    2. A curvatura numérica em z = 0 tem de trocar de sinal ao passar por
       d = R: antes o campo tem máximo no centro, depois tem mínimo.

Prof. Apiano Morais - LFCA/URCA - Eletromagnetismo II
"""

import numpy as np
import matplotlib.pyplot as plt

from biot_savart import MU0, campo, espira_circular

R = 0.10          # raio das bobinas, em metros
I = 1.0           # corrente
N = 1             # espiras por bobina


def campo_no_eixo(d, z):
    """Campo no eixo de duas bobinas separadas por d, centradas em +-d/2."""
    a = espira_circular(R=R, z0=+d / 2, n_seg=600)
    b = espira_circular(R=R, z0=-d / 2, n_seg=600)
    alvos = np.column_stack([np.zeros_like(z), np.zeros_like(z), z])
    return N * (campo(a, I, alvos)[:, 2] + campo(b, I, alvos)[:, 2])


z = np.linspace(-R, R, 241)

print('campo no centro, separação d = R:')
B0 = campo_no_eixo(R, np.array([0.0]))[0]
B0_teorico = (4.0 / 5.0) ** 1.5 * MU0 * N * I / R
print('  numérico %.6e T   teórico %.6e T   erro %.2e'
      % (B0, B0_teorico, abs(B0 - B0_teorico) / B0_teorico))

print('\ncurvatura do campo no centro (d^2B/dz^2):')
for fator in (0.6, 0.8, 1.0, 1.2, 1.5):
    d = fator * R
    B = campo_no_eixo(d, z)
    meio = len(z) // 2
    h = z[1] - z[0]
    curv = (B[meio + 1] - 2 * B[meio] + B[meio - 1]) / h ** 2
    print('  d = %.2f R   B(0) = %.4e T   curvatura = %+.4e' % (fator, B[meio], curv))

fig, ax = plt.subplots(figsize=(7.2, 4.4))
for fator, cor in ((0.6, '#b5831f'), (1.0, '#1c2c60'), (1.5, '#a8181d')):
    B = campo_no_eixo(fator * R, z)
    ax.plot(z * 100, B / B[len(z) // 2], lw=2.2, color=cor,
            label='$d = %.1f\\,R$' % fator)
ax.axhline(1.0, color='#999', lw=0.8, ls=':')
ax.set_xlabel('posição no eixo [cm]')
ax.set_ylabel('$B(z)\\,/\\,B(0)$')
ax.set_title('uniformidade do campo de duas bobinas')
ax.legend(frameon=False)
fig.tight_layout()
plt.show()
