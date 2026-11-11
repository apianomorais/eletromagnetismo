# -*- coding: utf-8 -*-
"""Indutância mútua pela fórmula de Neumann, e a prova numérica de que M12 = M21.

O QUE RESOLVE
    Calcula

        M = (mu0/4pi) * integral dupla de (dl1 . dl2) / |r2 - r1|

    para duas espiras circulares coaxiais de raios a e b separadas por d,
    discretizando cada contorno em segmentos retos.

A FÍSICA
    A fórmula de Neumann é simétrica na troca das duas espiras, e por isso
    M12 = M21 seja qual for a geometria. O resultado é útil na prática: calcula-se
    o lado fácil e lê-se a resposta do lado difícil, como no exemplo do
    solenoide curto dentro do longo.

COMO CONFERIR SE ESTÁ CERTO
    1. Trocando as espiras de papel, e usando discretizações DIFERENTES para
       cada uma, M12 e M21 têm de coincidir até o erro de truncamento.
    2. Para espiras coaxiais existe fórmula fechada com integrais elípticas
       completas; o programa compara.
    3. Para d muito maior que os raios, M tem de tender ao resultado de dipolo,
       mu0 pi a^2 b^2 / (2 d^3).

Prof. Apiano Morais - LFCA/URCA - Eletromagnetismo II
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import ellipk, ellipe

from biot_savart import campo, espira_circular

MU0 = 4.0e-7 * np.pi


def espira(raio, z0, n, fase=0.0):
    """Pontos médios e vetores dl de uma espira circular discretizada."""
    bordas = np.linspace(0.0, 2 * np.pi, n + 1) + fase
    pontos = np.column_stack([raio * np.cos(bordas), raio * np.sin(bordas),
                              np.full(n + 1, float(z0))])
    dl = pontos[1:] - pontos[:-1]
    meio = 0.5 * (pontos[1:] + pontos[:-1])
    return meio, dl


def neumann(e1, e2):
    """M pela integral dupla. Cada espira é (pontos médios, dl)."""
    p1, dl1 = e1
    p2, dl2 = e2
    produto = dl1 @ dl2.T                      # dl1 . dl2 para todo par
    dif = p1[:, None, :] - p2[None, :, :]
    dist = np.sqrt((dif ** 2).sum(axis=2))
    return MU0 / (4 * np.pi) * np.sum(produto / dist)


def exata(a, b, d):
    """Fórmula fechada para duas espiras circulares coaxiais."""
    k2 = 4 * a * b / ((a + b) ** 2 + d ** 2)
    k = np.sqrt(k2)
    return MU0 * np.sqrt(a * b) * ((2 / k - k) * ellipk(k2) - (2 / k) * ellipe(k2))


A, B, D = 0.080, 0.025, 0.060

# ---------------------------------------------------- 1. a simetria de Neumann
# de propósito com números de segmentos diferentes e uma fase relativa, para
# que a igualdade não seja consequência da malha ser a mesma
e1 = espira(A, 0.0, 600)
e2 = espira(B, D, 437, fase=0.31)
m21 = neumann(e1, e2)
m12 = neumann(e2, e1)

print('espiras coaxiais: a = %.3f m, b = %.3f m, separação d = %.3f m' % (A, B, D))
print('  M21 (integrando 1 depois 2) = %.9e H' % m21)
print('  M12 (integrando 2 depois 1) = %.9e H' % m12)
print('  diferença relativa = %.2e' % (abs(m21 - m12) / m21))

# ------------------------------------- 1b. a reciprocidade por caminho independente
# A simetria da fórmula de Neumann é manifesta, de modo que compará-la consigo
# mesma não prova nada. O teste de verdade é calcular cada fluxo pelo seu
# próprio caminho: campo de uma espira por Biot-Savart, integrado no disco da
# outra. Aí os dois números saem de contas diferentes.
def fluxo(raio_fonte, z_fonte, corrente, raio_alvo, z_alvo, nr=120, nt=240):
    fio = espira_circular(R=raio_fonte, z0=z_fonte, n_seg=1200)
    r = (np.arange(nr) + 0.5) / nr * raio_alvo
    t = (np.arange(nt) + 0.5) / nt * 2 * np.pi
    rr, tt = np.meshgrid(r, t, indexing='ij')
    alvos = np.column_stack([(rr * np.cos(tt)).ravel(), (rr * np.sin(tt)).ravel(),
                             np.full(rr.size, float(z_alvo))])
    bz = campo(fio, corrente, alvos)[:, 2].reshape(nr, nt)
    da = (raio_alvo / nr) * (2 * np.pi / nt) * rr
    return float(np.sum(bz * da))


m21_bs = fluxo(A, 0.0, 1.0, B, D)     # fluxo da espira 1 (grande) na espira 2
m12_bs = fluxo(B, D, 1.0, A, 0.0)     # fluxo da espira 2 na espira 1
print()
print('reciprocidade por Biot-Savart, com contas independentes:')
print('  fluxo de 1 em 2, por ampère = %.9e H' % m21_bs)
print('  fluxo de 2 em 1, por ampère = %.9e H' % m12_bs)
print('  diferença relativa = %.2e' % (abs(m21_bs - m12_bs) / m21_bs))

# ----------------------------------------------------- 2. contra a fórmula exata
print()
print('contra a fórmula com integrais elípticas:')
print('  exata   = %.9e H' % exata(A, B, D))
print('  Neumann = %.9e H   erro relativo = %.2e'
      % (m21, abs(m21 - exata(A, B, D)) / exata(A, B, D)))

print()
print('convergência com o número de segmentos nas DUAS espiras:')
for n in (50, 100, 200, 400, 800):
    m = neumann(espira(A, 0.0, n), espira(B, D, n))
    print('  n = %4d : M = %.9e H   erro = %.2e'
          % (n, m, abs(m - exata(A, B, D)) / exata(A, B, D)))

# -------------------------------------------------- 3. o limite de dipolo longe
print()
print('limite de dipolo, M -> mu0 pi a^2 b^2 / 2 d^3:')
for d in (0.3, 0.6, 1.2, 2.4):
    m = neumann(espira(A, 0.0, 400), espira(B, d, 400))
    dip = MU0 * np.pi * A ** 2 * B ** 2 / (2 * d ** 3)
    print('  d = %.1f m : Neumann = %.4e   dipolo = %.4e   razão = %.5f'
          % (d, m, dip, m / dip))

# ------------------------------------------------------------------- figura
ds = np.linspace(0.01, 0.50, 60)
ms = np.array([neumann(espira(A, 0.0, 400), espira(B, d, 400)) for d in ds])
dip = MU0 * np.pi * A ** 2 * B ** 2 / (2 * ds ** 3)

fig, eixo = plt.subplots(figsize=(7, 4.4))
eixo.loglog(ds, ms * 1e6, lw=2, label='Neumann')
eixo.loglog(ds, exata(A, B, ds) * 1e6, ls='--', lw=1.4, label='fórmula exata')
eixo.loglog(ds, dip * 1e6, ls=':', lw=1.6, label='aproximação de dipolo')
eixo.set_xlabel('separação d (m)')
eixo.set_ylabel('M (microhenry)')
eixo.set_title('Indutância mútua de duas espiras coaxiais')
eixo.legend(frameon=False)
fig.tight_layout()
plt.show()
