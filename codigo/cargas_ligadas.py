# -*- coding: utf-8 -*-
"""Cargas ligadas: cálculo, soma zero e o campo que elas produzem.

O QUE RESOLVE
    Dada uma polarização P(r) qualquer dentro de uma esfera, calcula

        rho_b = -div P     (volume)
        sigma_b = P . n    (superfície)

    numericamente, integra as duas e mostra que a soma é zero. Depois monta o
    campo dessas cargas por integração direta e compara com o resultado
    analítico no caso da polarização uniforme.

A FÍSICA
    Carga ligada não é artifício: é o que sobra quando as pontas dos dipolos
    vizinhos não se cancelam. Por isso a soma tem de ser rigorosamente nula,
    seja qual for P: polarizar desloca carga, não cria.

COMO CONFERIR SE ESTÁ CERTO
    1. Q_volume + Q_superficie = 0 para toda polarização testada.
    2. Para P uniforme, o campo dentro tem de dar -P/3eps0, uniforme, e fora
       tem de ser dipolar com p = P vezes o volume.
    3. Para P = k r r^, o campo dentro tem de dar -P/eps0 e fora, zero.

Prof. Apiano Morais - LFCA/URCA - Eletromagnetismo I
"""

import numpy as np

EPS0 = 8.8541878128e-12
R = 0.05          # raio da esfera, em metros
P0 = 1.0e-6       # escala de polarização, em C/m^2


# ------------------------------------------------- as polarizações de teste
def uniforme(x, y, z):
    """P = P0 z^."""
    return np.zeros_like(x), np.zeros_like(y), np.full_like(z, P0)


def radial(x, y, z):
    """P = (P0/R) r r^, que cresce do centro para a borda."""
    k = P0 / R
    return k * x, k * y, k * z


def torcida(x, y, z):
    """P = P0 (y, -x, 0) / R, azimutal: tem rotacional, divergente nulo."""
    return P0 * y / R, -P0 * x / R, np.zeros_like(z)


def divergente(campo, n=161):
    """div P numa grade cúbica que contém a esfera, por diferenças centrais."""
    u = np.linspace(-1.4 * R, 1.4 * R, n)
    h = u[1] - u[0]
    X, Y, Z = np.meshgrid(u, u, u, indexing='ij')
    Px, Py, Pz = campo(X, Y, Z)
    d = (np.gradient(Px, h, axis=0, edge_order=2)
         + np.gradient(Py, h, axis=1, edge_order=2)
         + np.gradient(Pz, h, axis=2, edge_order=2))
    dentro = (X ** 2 + Y ** 2 + Z ** 2) < R ** 2
    return -d, dentro, h


def carga_superficie(campo, n=600):
    """Integral de P . n sobre a esfera."""
    t = (np.arange(n) + 0.5) * np.pi / n
    f = (np.arange(n) + 0.5) * 2 * np.pi / n
    T, F = np.meshgrid(t, f, indexing='ij')
    nx = np.sin(T) * np.cos(F)
    ny = np.sin(T) * np.sin(F)
    nz = np.cos(T)
    Px, Py, Pz = campo(R * nx, R * ny, R * nz)
    sig = Px * nx + Py * ny + Pz * nz
    da = R ** 2 * np.sin(T) * (np.pi / n) * (2 * np.pi / n)
    return float(np.sum(sig * da)), sig, T


print('carga ligada total, volume mais superfície')
print('   polarização        Q_volume (C)     Q_superfície (C)      soma')
for nome, campo in (('uniforme', uniforme), ('radial', radial),
                    ('azimutal', torcida)):
    rho, dentro, h = divergente(campo)
    qv = float(np.sum(rho[dentro]) * h ** 3)
    qs, _, _ = carga_superficie(campo)
    print('  %-16s  %+14.6e   %+14.6e   %+9.2e' % (nome, qv, qs, qv + qs))
print('  a soma é nula em todos os casos, a menos do erro da grade')

print()
print('densidades, comparadas com a conta analítica')
rho_u, dentro, h = divergente(uniforme)
print('  uniforme : rho_b médio dentro = %+.3e C/m^3  (previsto 0)'
      % float(np.mean(rho_u[dentro])))
rho_r, dentro, h = divergente(radial)
print('  radial   : rho_b médio dentro = %+.3e C/m^3  (previsto -3P0/R = %+.3e)'
      % (float(np.mean(rho_r[dentro])), -3 * P0 / R))
_, sig_u, T = carga_superficie(uniforme)
print('  uniforme : sigma_b no polo = %+.3e C/m^2  (previsto P0 = %+.3e)'
      % (float(sig_u[0, 0]), P0))

# ----------------------- o campo das cargas ligadas, para a esfera uniforme
print()
print('campo no centro da esfera uniformemente polarizada')


def campo_das_cargas(alvo, n=400):
    """Soma o campo da carga de superfície sigma_b = P0 cos(theta)."""
    t = (np.arange(n) + 0.5) * np.pi / n
    f = (np.arange(n) + 0.5) * 2 * np.pi / n
    T, F = np.meshgrid(t, f, indexing='ij')
    x = R * np.sin(T) * np.cos(F)
    y = R * np.sin(T) * np.sin(F)
    z = R * np.cos(T)
    sig = P0 * np.cos(T)
    da = R ** 2 * np.sin(T) * (np.pi / n) * (2 * np.pi / n)
    dx = alvo[0] - x
    dy = alvo[1] - y
    dz = alvo[2] - z
    r3 = (dx ** 2 + dy ** 2 + dz ** 2) ** 1.5
    k = 1.0 / (4 * np.pi * EPS0)
    return (float(k * np.sum(sig * da * dx / r3)),
            float(k * np.sum(sig * da * dy / r3)),
            float(k * np.sum(sig * da * dz / r3)))


previsto = -P0 / (3 * EPS0)
for alvo in ((0.0, 0.0, 0.0), (0.0, 0.0, 0.4 * R), (0.3 * R, 0.2 * R, -0.1 * R)):
    Ex, Ey, Ez = campo_das_cargas(alvo)
    print('  em (%.3f, %.3f, %.3f) : Ez = %+.5e  (previsto %+.5e)  erro %.1e'
          % (alvo[0], alvo[1], alvo[2], Ez, previsto, abs(Ez - previsto)
             / abs(previsto)))
print('  uniforme em módulo e direção, como manda a série de Legendre')

p_dip = P0 * 4 / 3 * np.pi * R ** 3
for d in (2 * R, 4 * R):
    Ex, Ey, Ez = campo_das_cargas((0.0, 0.0, d))
    dip = 2 * p_dip / (4 * np.pi * EPS0 * d ** 3)
    print('  fora, em z = %.0f R : Ez = %+.4e  dipolo = %+.4e  razão %.5f'
          % (d / R, Ez, dip, Ez / dip))
