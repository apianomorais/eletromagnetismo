# -*- coding: utf-8 -*-
"""A equação de Laplace por relaxação: o método que resolve qualquer geometria.

O QUE RESOLVE
    Dada uma grade com valores fixos na fronteira, acha V no interior
    substituindo repetidamente cada ponto pela média dos quatro vizinhos, até
    que nada mais mude. É a tradução direta da propriedade da média do capítulo
    3, e funciona para contorno de qualquer forma.

A FÍSICA
    A propriedade da média não é um truque numérico: é equivalente à equação de
    Laplace. Discretizando as segundas derivadas por diferenças centrais,

        (V[i+1,j] + V[i-1,j] + V[i,j+1] + V[i,j-1] - 4 V[i,j]) / h^2 = 0,

    o que é exatamente "o valor é a média dos vizinhos". O método de
    Gauss-Seidel com sobre-relaxação (SOR) faz a mesma coisa, só que mais
    depressa, empurrando cada correção um pouco além.

COMO CONFERIR SE ESTÁ CERTO
    1. No duto quadrado com três paredes aterradas e uma em V0, o centro tem de
       dar exatamente V0/4, por um argumento de simetria que não usa série
       nenhuma. Atenção: isso vale também na grade discreta, que tem a mesma
       simetria, de modo que o centro NÃO serve para medir erro de truncamento.
    2. Num ponto sem simetria, o erro contra a série de Fourier tem de cair
       como h^2.
    3. A solução tem de satisfazer a propriedade da média em todo ponto
       interior, que é o que o método impõe por construção.

Prof. Apiano Morais - LFCA/URCA - Eletromagnetismo I
"""

import numpy as np
import matplotlib.pyplot as plt

V0 = 100.0        # potencial da parede de cima, em volts


def serie(x, y, a=1.0, termos=40):
    """Solução analítica do duto, pela série de Fourier."""
    s = np.zeros_like(x, dtype=float)
    for n in range(1, 2 * termos, 2):
        s += (1.0 / n) * np.sinh(n * np.pi * y / a) / np.sinh(n * np.pi) \
             * np.sin(n * np.pi * x / a)
    return 4 * V0 / np.pi * s


def relaxar(n, omega=None, tol=1e-10, maxit=200000):
    """Resolve o duto numa grade (n+1)x(n+1) por SOR. Devolve V e as iterações."""
    V = np.zeros((n + 1, n + 1))
    V[:, -1] = V0                      # parede de cima, em y = a
    if omega is None:
        # valor ótimo conhecido para o retângulo: converge em O(n) iterações
        omega = 2.0 / (1.0 + np.sin(np.pi / n))
    for it in range(maxit):
        velho = V.copy()
        # varredura de Gauss-Seidel vetorizada em duas cores (xadrez)
        for cor in (0, 1):
            i, j = np.meshgrid(np.arange(1, n), np.arange(1, n), indexing='ij')
            m = (i + j) % 2 == cor
            ii, jj = i[m], j[m]
            media = 0.25 * (V[ii + 1, jj] + V[ii - 1, jj]
                            + V[ii, jj + 1] + V[ii, jj - 1])
            V[ii, jj] += omega * (media - V[ii, jj])
        if np.max(np.abs(V - velho)) < tol * V0:
            return V, it + 1
    return V, maxit


print('duto quadrado: três paredes aterradas, a de cima em %.0f V' % V0)
print('  o valor exato no centro é V0/4 = %.4f V' % (V0 / 4))
print()
print('  e a grade discreta tem a mesma simetria, de modo que o centro sai')
print('  exato em qualquer resolução: para medir truncamento é preciso um')
print('  ponto sem simetria, e usamos (x, y) = (0,25; 0,50)')
print()
print('     n       h        centro      V(0,25; 0,50)   erro contra a série')
anterior = None
for n in (20, 40, 80, 160):
    V, it = relaxar(n)
    centro = V[n // 2, n // 2]
    ponto = V[n // 4, n // 2]
    exato = float(serie(np.array(0.25), np.array(0.50)))
    err = abs(ponto - exato)
    linha = ('  %4d   %.5f   %10.6f   %12.6f   %10.3e'
             % (n, 1.0 / n, centro, ponto, err))
    if anterior:
        linha += '   razão %.2f' % (anterior / err)
    anterior = err
    print(linha)
print('  razão 4 por refinamento: o erro vai com h^2, como manda a diferença')
print('  central de segunda ordem')

# ------------------------------------------- contra a série, ponto a ponto
n = 120
V, it = relaxar(n)
x = np.linspace(0, 1, n + 1)
X, Y = np.meshgrid(x, x, indexing='ij')
Vs = serie(X, Y)
# longe da parede de cima, onde a série tem o salto nos cantos e converge mal
longe = (slice(1, -1), slice(1, int(0.8 * n)))
err = np.max(np.abs(V[longe] - Vs[longe])) / V0
err_tudo = np.max(np.abs(V[1:-1, 1:-1] - Vs[1:-1, 1:-1])) / V0
print()
print('contra a série de Fourier, grade %d x %d:' % (n, n))
print('  erro máximo relativo até y = 0,8 a : %.3e' % err)
print('  erro máximo incluindo a faixa junto à tampa: %.3e' % err_tudo)
print('  a diferença é dos cantos, onde V salta de 0 para V0 e tanto a série')
print('  quanto a grade têm dificuldade: é a região de Gibbs')
print('  convergiu em %d varreduras' % it)

# ------------------------------------------ a propriedade da média, medida
print()
print('propriedade da média, num ponto qualquer do interior:')
for (i, j) in ((30, 40), (60, 60), (90, 25)):
    media = 0.25 * (V[i + 1, j] + V[i - 1, j] + V[i, j + 1] + V[i, j - 1])
    print('  V(%3d,%3d) = %10.6f    média dos vizinhos = %10.6f   dif = %.1e'
          % (i, j, V[i, j], media, abs(V[i, j] - media)))

# -------------------------------- uma geometria que a série não resolve
print()
print('o mesmo método numa geometria sem solução fechada:')
m = 120
W = np.zeros((m + 1, m + 1))
W[:, -1] = V0
# um bloco condutor aterrado, quadrado, no meio do duto
bloco = (slice(18, 44), slice(30, 56))
mascara = np.zeros_like(W, dtype=bool)
mascara[bloco] = True
omega = 2.0 / (1.0 + np.sin(np.pi / m))
for it in range(40000):
    velho = W.copy()
    for cor in (0, 1):
        i, j = np.meshgrid(np.arange(1, m), np.arange(1, m), indexing='ij')
        msk = ((i + j) % 2 == cor) & (~mascara[1:m, 1:m])
        ii, jj = i[msk], j[msk]
        media = 0.25 * (W[ii + 1, jj] + W[ii - 1, jj]
                        + W[ii, jj + 1] + W[ii, jj - 1])
        W[ii, jj] += omega * (media - W[ii, jj])
    W[mascara] = 0.0
    if np.max(np.abs(W - velho)) < 1e-10 * V0:
        break
print('  duto com um bloco aterrado no interior: convergiu em %d varreduras' % (it + 1))
print('  V no centro do duto, agora: %.4f V (era %.4f sem o bloco)'
      % (W[m // 2, m // 2], V0 / 4))
print('  nenhuma série de Fourier resolve isso, e a relaxação não se incomoda')

# ------------------------------------------------------------------- figura
fig, eixo = plt.subplots(1, 2, figsize=(11, 4.4))
for ax, campo, titulo in ((eixo[0], V, 'duto vazio'),
                          (eixo[1], W, 'duto com bloco aterrado')):
    im = ax.contourf(X, Y, campo, levels=24, cmap='copper')
    ax.contour(X, Y, campo, levels=12, colors='k', linewidths=0.5, alpha=0.4)
    ax.set_aspect('equal')
    ax.set_title(titulo, fontsize=11)
    ax.set_xlabel('x / a'); ax.set_ylabel('y / a')
fig.colorbar(im, ax=eixo, label='V (volts)', fraction=0.04)
plt.show()
