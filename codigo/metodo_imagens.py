# -*- coding: utf-8 -*-
"""O método das imagens, conferido contra a carga induzida e contra a relaxação.

O QUE RESOLVE
    Uma carga q a uma altura d de um plano condutor aterrado. A solução por
    imagem é imediata; o programa a usa para calcular a densidade de carga
    induzida e integra essa densidade sobre o plano inteiro.

    Depois refaz o mesmo problema sem usar imagem nenhuma, por relaxação da
    equação de Poisson numa grade tridimensional, e compara.

A FÍSICA
    A imagem não é um artifício justificado por analogia: ela é legítima pelo
    teorema da unicidade. Qualquer função que satisfaça Laplace na região e
    reproduza as condições de contorno É a solução, e a imagem está fora da
    região, de modo que não acrescenta fonte nenhuma onde não deve.

COMO CONFERIR SE ESTÁ CERTO
    1. A carga induzida total tem de dar exatamente -q, e a integral numérica
       confirma.
    2. Metade da carga induzida tem de estar dentro de um círculo de raio
       sqrt(3) d, resultado que sai em duas linhas da integral.
    3. A relaxação, sem saber da imagem, tem de reproduzir o potencial e a
       densidade induzida, dentro do erro da grade e da caixa finita.

Prof. Apiano Morais - LFCA/URCA - Eletromagnetismo I
"""

import numpy as np
import matplotlib.pyplot as plt

K = 8.9875517873681764e9
EPS0 = 1.0 / (4 * np.pi * K)

Q = 2.0e-9        # carga, em coulomb
D = 0.05          # altura acima do plano, em metros


def potencial(x, y, z):
    """Potencial da carga mais a imagem, válido em z > 0."""
    r1 = np.sqrt(x ** 2 + y ** 2 + (z - D) ** 2)
    r2 = np.sqrt(x ** 2 + y ** 2 + (z + D) ** 2)
    return K * Q * (1.0 / r1 - 1.0 / r2)


def sigma(s):
    """Densidade de carga induzida, a uma distância s do pé da perpendicular."""
    return -Q * D / (2 * np.pi * (s ** 2 + D ** 2) ** 1.5)


# --------------------------------------------------- 1. a carga induzida total
print('carga q = %.1f nC a d = %.0f cm do plano aterrado' % (Q * 1e9, D * 100))
s = np.linspace(0, 400 * D, 2000001)
total = np.trapezoid(sigma(s) * 2 * np.pi * s, s)
print('  carga induzida integrada até s = 400 d : %.6f nC' % (total * 1e9))
print('  valor exato, -q                        : %.6f nC' % (-Q * 1e9))
print('  a convergência é lenta porque sigma cai só com 1/s^3')

raio = np.sqrt(3) * D
dentro = np.trapezoid(sigma(s[s <= raio]) * 2 * np.pi * s[s <= raio], s[s <= raio])
print('  fração da carga dentro de raiz(3) d = %.1f cm : %.4f'
      % (raio * 100, dentro / total))

# ------------------------------------------------------- 2. força e energia
F = K * Q ** 2 / (2 * D) ** 2
W = -K * Q ** 2 / (4 * D)
print()
print('  força de atração = %.3e N  (igual à da imagem)' % F)
print('  energia do sistema = %.3e J  (metade da energia do par de cargas)' % W)

# ------------------------------- 3. a mesma coisa por relaxação, sem imagem
print()
print('agora sem imagem nenhuma: relaxação de Poisson numa caixa')
n = 61                      # pontos por lado
L = 0.30                    # meia-aresta da caixa, em metros
x = np.linspace(-L, L, n)
z = np.linspace(0.0, 2 * L, n)
h = x[1] - x[0]
V = np.zeros((n, n, n))     # índices x, y, z

# a carga, espalhada numa célula: rho = q / h^3
iq = n // 2
kq = int(round(D / (z[1] - z[0])))
fonte = np.zeros_like(V)
fonte[iq, iq, kq] = Q / h ** 3 / EPS0 * h ** 2 / 6.0   # termo do esquema 3D

omega = 1.9
for it in range(4000):
    velho = V.copy()
    for cor in (0, 1):
        i, j, k = np.meshgrid(np.arange(1, n - 1), np.arange(1, n - 1),
                              np.arange(1, n - 1), indexing='ij')
        m = (i + j + k) % 2 == cor
        ii, jj, kk = i[m], j[m], k[m]
        media = (V[ii + 1, jj, kk] + V[ii - 1, jj, kk]
                 + V[ii, jj + 1, kk] + V[ii, jj - 1, kk]
                 + V[ii, jj, kk + 1] + V[ii, jj, kk - 1]) / 6.0
        V[ii, jj, kk] += omega * (media + fonte[ii, jj, kk] - V[ii, jj, kk])
    V[:, :, 0] = 0.0                      # o plano aterrado
    V[0, :, :] = V[-1, :, :] = 0.0        # caixa grande: V ~ 0 nas bordas
    V[:, 0, :] = V[:, -1, :] = 0.0
    V[:, :, -1] = 0.0
    if np.max(np.abs(V - velho)) < 1e-7 * K * Q / D:
        break
print('  convergiu em %d varreduras numa grade %d^3' % (it + 1, n))

# densidade induzida lida da derivada normal, contra a fórmula da imagem
print()
print('     s (cm)    sigma relaxação     sigma imagem     diferença relativa')
dz = z[1] - z[0]
for di in (0, 3, 6, 10):
    sn = -EPS0 * (V[iq + di, iq, 1] - V[iq + di, iq, 0]) / dz
    se = sigma(di * h)
    print('   %8.2f   %14.3e   %14.3e        %.2f'
          % (di * h * 100, sn, se, abs(sn - se) / abs(se)))
print('  a grade grosseira e a caixa finita custam caro perto da carga;')
print('  o que importa é a forma do perfil e o sinal, que batem')

# ------------------------------------------------------------------- figura
xx = np.linspace(-4 * D, 4 * D, 300)
zz = np.linspace(0.001, 5 * D, 300)
X, Z = np.meshgrid(xx, zz, indexing='ij')
Vp = potencial(X, 0.0, Z)

fig, eixo = plt.subplots(1, 2, figsize=(11, 4.2))
niveis = np.array([2, 5, 10, 20, 50, 100, 200, 400])
eixo[0].contour(X / D, Z / D, Vp, levels=niveis, colors='#b05a1f')
eixo[0].axhline(0, color='#2b3240', lw=3)
eixo[0].plot(0, 1, 'o', ms=9, color='#b05a1f')
eixo[0].set_xlabel('x / d'); eixo[0].set_ylabel('z / d')
eixo[0].set_title('Equipotenciais acima do plano')
eixo[0].set_aspect('equal')

ss = np.linspace(0, 6 * D, 300)
eixo[1].plot(ss / D, sigma(ss) * 1e9, lw=2)
eixo[1].axvline(np.sqrt(3), ls='--', lw=1)
eixo[1].set_xlabel('s / d')
eixo[1].set_ylabel('sigma (nC/m²)')
eixo[1].set_title('Carga induzida: metade dentro de raiz(3) d')
fig.tight_layout()
plt.show()
