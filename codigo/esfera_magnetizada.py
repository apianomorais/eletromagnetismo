# -*- coding: utf-8 -*-
"""A esfera uniformemente magnetizada, resolvida pela corrente ligada.

O QUE RESOLVE
    Toma uma esfera de raio R com magnetização uniforme M = M ẑ, substitui o
    material pela corrente ligada de superfície Kb = M x n, e integra
    Biot-Savart sobre essa corrente para achar B dentro e fora. Depois monta
    H = B/mu0 - M e mostra que os dois campos não se parecem nada.

A FÍSICA
    Corrente ligada é corrente de verdade: não há truque de contabilidade. Com
    M uniforme a corrente de volume Jb = rot M é nula, e sobra apenas a de
    superfície, Kb = M x n = M sen(theta) phi^, que é a mesma distribuição da
    casca esférica girante do capítulo 5. Por isso o campo interno sai
    uniforme, e o externo sai exatamente dipolar.

    A esfera é fatiada em anéis de latitude; cada anel é uma espira circular
    de raio R sen(theta) na altura R cos(theta), carregando a corrente
    dI = Kb R d(theta) = M R sen(theta) d(theta).

COMO CONFERIR SE ESTÁ CERTO
    1. Dentro, B tem de ser uniforme e valer (2/3) mu0 M. O programa mede o
       campo em vários pontos do interior e imprime o desvio.
    2. Fora, tem de ser o campo de um dipolo de momento m = (4/3) pi R^3 M.
       O programa compara ponto a ponto.
    3. Dentro, H = B/mu0 - M tem de dar -M/3, ou seja, apontar CONTRA a
       magnetização. É o campo desmagnetizante, e o fator 1/3 é o da esfera.

Prof. Apiano Morais - LFCA/URCA - Eletromagnetismo II
"""

import numpy as np
import matplotlib.pyplot as plt

from biot_savart import MU0, campo, espira_circular

R = 0.05          # raio da esfera, em metros
M = 1.0e5         # magnetização, em A/m (da ordem de um ímã de ferrite)
N_ANEIS = 400     # fatias de latitude
N_SEG = 240       # segmentos por anel


def aneis(n_aneis=N_ANEIS, n_seg=N_SEG):
    """Devolve a lista de (espira, corrente) que substitui o material.

    O ponto médio de cada faixa evita o viés que apareceria usando a borda.
    """
    bordas = np.linspace(0.0, np.pi, n_aneis + 1)
    tet = 0.5 * (bordas[1:] + bordas[:-1])
    dtet = bordas[1] - bordas[0]
    saida = []
    for t in tet:
        raio = R * np.sin(t)
        if raio < 1e-9:
            continue
        dI = M * R * np.sin(t) * dtet          # Kb R dtheta
        saida.append((espira_circular(R=raio, z0=R * np.cos(t), n_seg=n_seg), dI))
    return saida


def campo_total(alvos):
    """Soma a contribuição de todos os anéis nos pontos pedidos."""
    alvos = np.atleast_2d(np.asarray(alvos, dtype=float))
    total = np.zeros_like(alvos)
    for espira, dI in aneis():
        total += campo(espira, dI, alvos)
    return total


def campo_dipolo(m, alvos):
    """Campo de um dipolo pontual m = m ẑ, para comparação."""
    alvos = np.atleast_2d(np.asarray(alvos, dtype=float))
    r = np.linalg.norm(alvos, axis=1)
    z = alvos[:, 2]
    fora = MU0 * m / (4 * np.pi * r[:, None] ** 5)
    radial = 3 * z[:, None] * alvos
    axial = np.zeros_like(alvos)
    axial[:, 2] = r ** 2
    return fora * (radial - axial)


# --------------------------------------------------------------- 1. interior
dentro = np.array([
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 0.5 * R],
    [0.4 * R, 0.0, 0.0],
    [0.3 * R, 0.3 * R, -0.4 * R],
])
B_dentro = campo_total(dentro)
B_teorico = 2.0 / 3.0 * MU0 * M

print('INTERIOR: B tem de ser uniforme e valer (2/3) mu0 M')
print('  previsto      Bz = %.6e T' % B_teorico)
for p, b in zip(dentro, B_dentro):
    print('  em (%.3f, %.3f, %.3f): Bz = %.6e   Bx = %+.2e   desvio = %.2e'
          % (p[0], p[1], p[2], b[2], b[0], abs(b[2] - B_teorico) / B_teorico))

H_dentro = B_dentro / MU0 - np.array([0.0, 0.0, M])
print('  H dentro: Hz = %.4e A/m, previsto -M/3 = %.4e A/m'
      % (H_dentro[0, 2], -M / 3.0))

# ---------------------------------------------------------------- 2. exterior
m = 4.0 / 3.0 * np.pi * R ** 3 * M
fora = np.array([
    [0.0, 0.0, 3.0 * R],
    [0.0, 0.0, -4.0 * R],
    [3.0 * R, 0.0, 0.0],
    [2.0 * R, 0.0, 2.0 * R],
])
B_fora = campo_total(fora)
B_dip = campo_dipolo(m, fora)

print()
print('EXTERIOR: tem de ser o dipolo de momento m = (4/3) pi R^3 M = %.4e A m^2' % m)
for p, b, d in zip(fora, B_fora, B_dip):
    erro = np.linalg.norm(b - d) / np.linalg.norm(d)
    print('  em (%.3f, %.3f, %.3f): |B| = %.4e   dipolo = %.4e   erro = %.2e'
          % (p[0], p[1], p[2], np.linalg.norm(b), np.linalg.norm(d), erro))

# ------------------------------------------------------------------ 3. figura
z = np.linspace(-4 * R, 4 * R, 161)
alvos = np.column_stack([np.zeros_like(z), np.zeros_like(z), z])
Bz = campo_total(alvos)[:, 2]
Mz = np.where(np.abs(z) < R, M, 0.0)
Hz = Bz / MU0 - Mz

fig, eixo = plt.subplots(1, 2, figsize=(11, 4.2))

eixo[0].plot(z / R, Bz * 1e3, lw=2)
eixo[0].axhline(B_teorico * 1e3, ls='--', lw=1)
eixo[0].axvspan(-1, 1, alpha=0.12)
eixo[0].set_xlabel('z / R')
eixo[0].set_ylabel('B_z  (mT)')
eixo[0].set_title('B no eixo: contínuo e uniforme dentro')

eixo[1].plot(z / R, Hz * 1e-3, lw=2)
eixo[1].axhline(-M / 3.0 * 1e-3, ls='--', lw=1)
eixo[1].axvspan(-1, 1, alpha=0.12)
eixo[1].set_xlabel('z / R')
eixo[1].set_ylabel('H_z  (kA/m)')
eixo[1].set_title('H no eixo: negativo dentro, o campo desmagnetizante')

fig.tight_layout()
plt.show()
