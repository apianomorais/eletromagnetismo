# -*- coding: utf-8 -*-
"""A esfera magnetizada por separação de variáveis, conferida contra a corrente ligada.

O QUE RESOLVE
    A mesma esfera uniformemente magnetizada de esfera_magnetizada.py, agora
    por outro caminho: como não há corrente livre, rot H = 0, e H deriva de um
    potencial escalar magnético, H = -grad W, que satisfaz a equação de Laplace
    dentro e fora. A solução sai da expansão em polinômios de Legendre,

        W_dentro = soma_l  A_l r^l P_l(cos theta)
        W_fora   = soma_l  B_l P_l(cos theta) / r^(l+1),

    com as condições de contorno em r = R.

A FÍSICA
    A magnetização uniforme produz uma "carga magnética" efetiva de superfície
    sigma_m = M . n = M cos(theta), que é puro P_1. Pela ortogonalidade dos
    polinômios de Legendre só o termo l = 1 sobrevive, e sai

        W_dentro = (M/3) r cos(theta)        =>  H = -(M/3) z^
        W_fora   = (M R^3/3) cos(theta)/r^2  =>  dipolo de m = (4/3) pi R^3 M.

    O programa resolve os coeficientes numericamente, sem usar o resultado
    acima, e depois compara com a integração direta da corrente ligada de
    superfície pela lei de Biot-Savart, que é um método completamente
    diferente.

COMO CONFERIR SE ESTÁ CERTO
    1. Projetando sigma_m sobre os P_l, só o coeficiente l = 1 pode ser não
       nulo, e tem de valer M.
    2. Resolvido o sistema 2x2 das condições de contorno, A_1 tem de dar M/3.
    3. O campo B obtido do potencial escalar tem de bater, ponto a ponto, com o
       obtido por Biot-Savart a partir de Kb = M x n.

Prof. Apiano Morais - LFCA/URCA - Eletromagnetismo II
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import legendre as leg

from biot_savart import MU0, campo, espira_circular

R = 0.05          # raio da esfera, em metros
M = 1.0e5         # magnetização, em A/m
LMAX = 8          # até onde levar a série


# ------------------------------------------------- 1. projeção da fonte em P_l
def coeficiente(l, n=40001):
    """(2l+1)/2 * integral de sigma_m(theta) P_l(cos theta) d(cos theta),
    com sigma_m = M cos(theta)."""
    u = np.linspace(-1.0, 1.0, n)
    c = np.zeros(l + 1)
    c[l] = 1.0
    return (2 * l + 1) / 2 * np.trapezoid(M * u * leg.legval(u, c), u)


print('projeção de sigma_m = M cos(theta) na base de Legendre, em unidades de M:')
TOL = 1e-6          # abaixo disto é resíduo da quadratura, não física
sig = []
for l in range(LMAX):
    c = coeficiente(l)
    if abs(c) < TOL * M:
        c = 0.0
    sig.append(c)
    print('   l = %d : %+.9f' % (l, c / M))
print('   só l = 1 sobrevive; o resto é resíduo de quadratura, zerado abaixo')
print('   de %.0e relativo, senão ele reaparece amplificado por R^-(l-1)' % TOL)

# ------------------------------------- 2. as condições de contorno, ordem a ordem
# Continuidade de W:            A_l R^l = B_l / R^(l+1)
# Salto da derivada normal:     -(l+1) B_l / R^(l+2) - l A_l R^(l-1) = -sigma_l
print()
print('coeficientes da solução (resolvidos numericamente, sem usar o resultado):')
A = np.zeros(LMAX)
B = np.zeros(LMAX)
for l in range(LMAX):
    if l == 0:
        continue
    mat = np.array([[R ** l, -R ** (-(l + 1))],
                    [l * R ** (l - 1), (l + 1) * R ** (-(l + 2))]])
    vet = np.array([0.0, sig[l]])
    A[l], B[l] = np.linalg.solve(mat, vet)
    if abs(A[l]) > 1e-12 * M:
        print('   l = %d : A_l = %+.6e,  B_l = %+.6e' % (l, A[l], B[l]))
print('   previsto para l = 1 : A_1 = M/3 = %.6e' % (M / 3))
print('   obtido              : A_1     = %.6e   erro = %.2e'
      % (A[1], abs(A[1] - M / 3) / (M / 3)))


# --------------------------------------- 3. os campos a partir do potencial
def campos_serie(r, tet):
    """H e B em (r, theta), a partir da série resolvida acima."""
    u = np.cos(tet)
    hr = ht = 0.0
    for l in range(LMAX):
        if abs(A[l]) < 1e-30 and abs(B[l]) < 1e-30:
            continue
        c = np.zeros(l + 1)
        c[l] = 1.0
        pl = leg.legval(u, c)
        dpl = leg.legval(u, leg.legder(c))
        if r <= R:
            hr += -l * A[l] * r ** (l - 1) * pl
            ht += A[l] * r ** (l - 1) * dpl * np.sin(tet)
        else:
            hr += (l + 1) * B[l] * r ** (-(l + 2)) * pl
            ht += B[l] * r ** (-(l + 2)) * dpl * np.sin(tet)
    # B = mu0 (H + M) dentro, mu0 H fora
    mr, mt = (M * np.cos(tet), -M * np.sin(tet)) if r <= R else (0.0, 0.0)
    return (hr, ht), (MU0 * (hr + mr), MU0 * (ht + mt))


# ----------------------------- 4. o mesmo campo pela corrente ligada, Biot-Savart
def aneis(n=400, n_seg=220):
    """A casca de corrente ligada Kb = M sen(theta) phi^, em anéis."""
    bordas = np.linspace(0.0, np.pi, n + 1)
    tet = 0.5 * (bordas[1:] + bordas[:-1])
    dt = bordas[1] - bordas[0]
    saida = []
    for t in tet:
        raio = R * np.sin(t)
        if raio < 1e-9:
            continue
        saida.append((espira_circular(R=raio, z0=R * np.cos(t), n_seg=n_seg),
                      M * R * np.sin(t) * dt))
    return saida


ANEIS = aneis()


def campo_bs(r, tet):
    """B em (r, theta) pela integração direta da corrente ligada."""
    alvo = np.array([[r * np.sin(tet), 0.0, r * np.cos(tet)]])
    tot = np.zeros(3)
    for espira, di in ANEIS:
        tot += campo(espira, di, alvo)[0]
    br = tot[0] * np.sin(tet) + tot[2] * np.cos(tet)
    bt = tot[0] * np.cos(tet) - tot[2] * np.sin(tet)
    return br, bt


print()
print('campo pela série contra Biot-Savart da corrente ligada:')
print('     r/R   theta      B_r série      B_r Biot-Savart    erro relativo')
for rr, tet in ((0.3 * R, 0.6), (0.7 * R, 2.1), (1.6 * R, 0.9), (3.0 * R, 1.4)):
    (_, _), (br_s, bt_s) = campos_serie(rr, tet)
    br_b, bt_b = campo_bs(rr, tet)
    print('   %5.2f   %5.2f   %+13.6e   %+13.6e     %.2e'
          % (rr / R, tet, br_s, br_b, abs(br_s - br_b) / abs(br_b)))

print()
print('verificações finais:')
(hr, ht), (br, bt) = campos_serie(0.5 * R, 0.8)
bz = br * np.cos(0.8) - bt * np.sin(0.8)
hz = hr * np.cos(0.8) - ht * np.sin(0.8)
print('  B dentro = %.6e T   previsto (2/3) mu0 M = %.6e T'
      % (bz, 2.0 / 3.0 * MU0 * M))
print('  H dentro = %.6e A/m previsto -M/3 = %.6e A/m' % (hz, -M / 3))

# ------------------------------------------------------------------- figura
z = np.linspace(-3 * R, 3 * R, 300)
bzs = []
for zz in z:
    r = abs(zz)
    tet = 0.0 if zz >= 0 else np.pi
    r = max(r, 1e-6)
    (_, _), (br, bt) = campos_serie(r, tet)
    bzs.append(br * np.cos(tet) - bt * np.sin(tet))

fig, eixo = plt.subplots(figsize=(7.2, 4.2))
eixo.plot(z / R, np.array(bzs) * 1e3, lw=2, label='série de Legendre')
pontos = np.linspace(-3 * R, 3 * R, 15)
vals = []
for zz in pontos:
    r = max(abs(zz), 1e-6)
    tet = 0.0 if zz >= 0 else np.pi
    br, bt = campo_bs(r, tet)
    vals.append((br * np.cos(tet) - bt * np.sin(tet)) * 1e3)
eixo.plot(pontos / R, vals, 'o', ms=5, label='Biot-Savart da corrente ligada')
eixo.axvspan(-1, 1, alpha=0.12)
eixo.set_xlabel('z / R')
eixo.set_ylabel('B_z no eixo (mT)')
eixo.set_title('Dois métodos independentes, o mesmo campo')
eixo.legend(frameon=False)
fig.tight_layout()
plt.show()
