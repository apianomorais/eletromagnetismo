# -*- coding: utf-8 -*-
"""A onda plana posta à prova: ela satisfaz Maxwell mesmo?

O QUE RESOLVE
    Monta E e B de uma onda plana monocromática numa grade de espaço e tempo e
    verifica, por diferenças finitas, as quatro equações de Maxwell no vácuo.
    Depois calcula o vetor de Poynting, a intensidade média e a pressão de
    radiação.

A FÍSICA
    A onda plana não é uma solução qualquer: ela é transversal, tem E e B
    perpendiculares entre si, em fase, com B0 = E0/c, e transporta energia na
    direção de propagação. Cada uma dessas afirmações é consequência de uma das
    equações, e o programa confere uma por uma.

COMO CONFERIR SE ESTÁ CERTO
    1. Os dois divergentes têm de dar zero.
    2. rot E tem de ser igual a -dB/dt, e rot B a (1/c^2) dE/dt, ponto a ponto.
    3. As densidades de energia elétrica e magnética têm de ser IGUAIS, e a
       média de S tem de dar (1/2) c eps0 E0^2.

Prof. Apiano Morais - LFCA/URCA - Eletromagnetismo III
"""

import numpy as np
import matplotlib.pyplot as plt

C = 2.99792458e8
MU0 = 4.0e-7 * np.pi
EPS0 = 1.0 / (MU0 * C * C)

E0 = 1012.6            # amplitude, em V/m (a da luz solar, veja o exemplo)
LAMBDA = 550e-9        # comprimento de onda, em metros
K = 2 * np.pi / LAMBDA
OMEGA = C * K


def campos(x, y, z, t):
    """Onda plana polarizada em x, caminhando em +z."""
    fase = K * z - OMEGA * t
    Ex = E0 * np.cos(fase)
    By = E0 / C * np.cos(fase)
    zero = np.zeros_like(Ex)
    return (Ex, zero, zero), (zero, By, zero)


# grade pequena em torno de um ponto, para as derivadas
h = LAMBDA / 200
dt = 1.0 / (OMEGA * 200)
u = np.array([-h, 0.0, h])
X, Y, Z = np.meshgrid(u, u, u, indexing='ij')


def derivada_espacial(f, eixo):
    return np.gradient(f, h, axis=eixo, edge_order=2)[1, 1, 1]


t0 = 0.37e-15
E, B = campos(X, Y, Z, t0)
Ep, Bp = campos(X, Y, Z, t0 + dt)
Em, Bm = campos(X, Y, Z, t0 - dt)

divE = sum(derivada_espacial(E[i], i) for i in range(3))
divB = sum(derivada_espacial(B[i], i) for i in range(3))

rotE = np.array([
    derivada_espacial(E[2], 1) - derivada_espacial(E[1], 2),
    derivada_espacial(E[0], 2) - derivada_espacial(E[2], 0),
    derivada_espacial(E[1], 0) - derivada_espacial(E[0], 1)])
rotB = np.array([
    derivada_espacial(B[2], 1) - derivada_espacial(B[1], 2),
    derivada_espacial(B[0], 2) - derivada_espacial(B[2], 0),
    derivada_espacial(B[1], 0) - derivada_espacial(B[0], 1)])

dBdt = np.array([(Bp[i][1, 1, 1] - Bm[i][1, 1, 1]) / (2 * dt) for i in range(3)])
dEdt = np.array([(Ep[i][1, 1, 1] - Em[i][1, 1, 1]) / (2 * dt) for i in range(3)])

escala_E = E0 * K
escala_B = E0 / C * K

print('as quatro equações de Maxwell, medidas num ponto qualquer')
print('  div E            = %+.3e   (escala %.1e)  relativo %.1e'
      % (divE, escala_E, abs(divE) / escala_E))
print('  div B            = %+.3e   (escala %.1e)  relativo %.1e'
      % (divB, escala_B, abs(divB) / escala_B))
# cada resíduo é comparado com a escala do PRÓPRIO termo: rot E vai com
# E0 k, enquanto rot B vai com (E0/c) k. Dividir os dois pela mesma escala
# faria o primeiro parecer 1e8 vezes pior do que é.
err_f = np.max(np.abs(rotE + dBdt)) / escala_E
err_a = np.max(np.abs(rotB - dEdt / C ** 2)) / escala_B
print('  rot E + dB/dt    : erro relativo %.2e   (lei de Faraday)' % err_f)
print('  rot B - dE/dt/c² : erro relativo %.2e   (Ampère-Maxwell)' % err_a)

print()
print('a geometria da onda')
Ev = np.array([E[i][1, 1, 1] for i in range(3)])
Bv = np.array([B[i][1, 1, 1] for i in range(3)])
print('  E . B = %+.3e   (perpendiculares)' % float(np.dot(Ev, Bv)))
print('  E_z   = %+.3e   B_z = %+.3e   (transversal)' % (Ev[2], Bv[2]))
print('  |B|/|E| = %.6e   previsto 1/c = %.6e'
      % (np.linalg.norm(Bv) / np.linalg.norm(Ev), 1 / C))

print()
print('energia e momento')
t = np.linspace(0, 4 * np.pi / OMEGA, 20001)
Et = E0 * np.cos(-OMEGA * t)
ue = 0.5 * EPS0 * Et ** 2
ub = 0.5 * (Et / C) ** 2 / MU0
S = Et * (Et / C) / MU0
print('  densidade elétrica média  = %.6e J/m³' % np.mean(ue))
print('  densidade magnética média = %.6e J/m³' % np.mean(ub))
print('  são iguais: diferença relativa %.1e'
      % (abs(np.mean(ue) - np.mean(ub)) / np.mean(ue)))
I = np.mean(S)
print('  intensidade = %.4f W/m²   previsto (1/2) c eps0 E0² = %.4f'
      % (I, 0.5 * C * EPS0 * E0 ** 2))
print('  pressão de radiação: absorvida %.3e Pa, refletida %.3e Pa'
      % (I / C, 2 * I / C))
print('  numa vela de 100 m² refletora: F = %.3e N' % (2 * I / C * 100))

# ------------------------------------------------------------------- figura
z = np.linspace(0, 2 * LAMBDA, 400)
Ez = E0 * np.cos(K * z)
fig, eixo = plt.subplots(figsize=(7.6, 4.2))
eixo.plot(z * 1e9, Ez, lw=2, label='E_x (V/m)')
eixo.plot(z * 1e9, Ez / C * 1e6 * 300, lw=2, ls='--',
          label='B_y (µT, escala ×300)')
eixo.plot(z * 1e9, Ez * (Ez / C) / MU0 / 10, lw=1.4,
          label='S_z (W/m², escala ÷10)')
eixo.axhline(0, lw=0.8, color='0.6')
eixo.set_xlabel('z (nm)')
eixo.set_title('E e B em fase; S nunca é negativo')
eixo.legend(frameon=False, fontsize=9)
fig.tight_layout()
plt.show()
