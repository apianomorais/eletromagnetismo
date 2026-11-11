# -*- coding: utf-8 -*-
"""Modos de um guia de onda, por autovalores do laplaciano discreto.

O QUE RESOLVE
    Acha as frequências de corte e os padrões transversais dos modos de um guia
    metálico oco, resolvendo o problema de autovalores

        -(d²/dx² + d²/dy²) psi = k_c² psi

    na seção transversal, com condição de Dirichlet (modos TM, E_z = 0 nas
    paredes) ou de Neumann (modos TE, derivada normal de B_z nula).

A FÍSICA
    A frequência de corte é f_c = c k_c / 2 pi: abaixo dela beta é imaginário e
    a onda não propaga. O método não sabe nada de retângulos, de modo que
    funciona para qualquer seção, inclusive as que não têm solução fechada.
    É a mesma técnica da relaxação do capítulo 3, agora como autovalor.

COMO CONFERIR SE ESTÁ CERTO
    1. No retângulo, os cortes têm de reproduzir c pi sqrt(m²/a² + n²/b²), com
       m,n >= 1 para TM e m,n >= 0 (não ambos nulos) para TE.
    2. Para o WR-90 (a = 22,86 mm, b = 10,16 mm), o TE10 tem de dar 6,557 GHz.
    3. Uma seção em L, sem fórmula fechada, tem de ter corte MENOR que o do
       retângulo que a contém, porque ela é "maior" no sentido que importa.

Prof. Apiano Morais - LFCA/URCA - Eletromagnetismo III
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import eigsh

C = 2.99792458e8


def laplaciano(mascara, hx, hy, neumann=False):
    """Monta -laplaciano nos pontos de 'mascara' (True = dentro do guia).

    Dirichlet: fora da máscara o campo é zero, e simplesmente não há vizinho.
    Neumann: o vizinho de fora é substituído pelo próprio ponto, que é a
    discretização de derivada normal nula.
    """
    idx = -np.ones(mascara.shape, dtype=int)
    pontos = np.argwhere(mascara)
    for n, (i, j) in enumerate(pontos):
        idx[i, j] = n
    N = len(pontos)
    A = lil_matrix((N, N))
    px, py = 1.0 / hx ** 2, 1.0 / hy ** 2
    for n, (i, j) in enumerate(pontos):
        A[n, n] = 2 * px + 2 * py
        for di, dj, peso in ((1, 0, px), (-1, 0, px), (0, 1, py), (0, -1, py)):
            ii, jj = i + di, j + dj
            dentro = (0 <= ii < mascara.shape[0] and 0 <= jj < mascara.shape[1]
                      and mascara[ii, jj])
            if dentro:
                A[n, idx[ii, jj]] = -peso
            elif neumann:
                A[n, n] -= peso         # vizinho espelhado
    return A.tocsr(), idx, pontos


def cortes(a, b, n=60, quantos=6, neumann=False, recorte=None):
    """Frequências de corte de um guia de seção a x b, com recorte opcional.

    Dois cuidados com a malha, e os dois mudam o resultado em por cento:
    (1) com Neumann os pontos ficam nos centros das células, h = a/n, mas com
    Dirichlet eles são interiores e as paredes caem entre pontos, h = a/(n+1);
    (2) os espaçamentos em x e em y são calculados separadamente, senão a
    seção representada não tem as dimensões pedidas e o corte sai errado pela
    razão entre o b verdadeiro e o b da grade.
    """
    m = max(2, int(round(n * b / a)))
    if neumann:
        hx, hy = a / n, b / m
    else:
        hx, hy = a / (n + 1), b / (m + 1)
    mascara = np.ones((n, m), dtype=bool)
    if recorte is not None:
        i0, i1, j0, j1 = recorte
        mascara[i0:i1, j0:j1] = False
    A, idx, pontos = laplaciano(mascara, hx, hy, neumann)
    vals, vecs = eigsh(A, k=quantos, sigma=1e-6 if neumann else 0.0,
                       which='LM')
    vals = np.clip(vals, 0, None)
    return C * np.sqrt(vals) / (2 * np.pi), vecs, mascara, idx


A_WR90, B_WR90 = 22.86e-3, 10.16e-3


def analitico(a, b, m, n):
    return C / 2 * np.sqrt((m / a) ** 2 + (n / b) ** 2)


print('guia WR-90 (banda X): a = %.2f mm, b = %.2f mm'
      % (A_WR90 * 1e3, B_WR90 * 1e3))
print()
print('modos TE (Neumann), frequências de corte em GHz')
f, _, _, _ = cortes(A_WR90, B_WR90, n=70, quantos=6, neumann=True)
previsto = sorted([analitico(A_WR90, B_WR90, m, n)
                   for m in range(3) for n in range(3)
                   if not (m == 0 and n == 0)])
print('   numérico   analítico    (m,n)        erro')
rotulos = ['(1,0)', '(2,0)', '(0,1)', '(1,1)', '(2,1)', '(3,0)']
for num, prev, rot in zip(sorted(f)[1:], previsto, rotulos):
    print('   %8.4f   %8.4f    %s   %.2e'
          % (num / 1e9, prev / 1e9, rot, abs(num - prev) / prev))
print('  o primeiro autovalor numérico é zero (o modo constante, que não')
print('  corresponde a modo propagante nenhum) e foi descartado')

print()
print('modos TM (Dirichlet), em GHz')
f, _, _, _ = cortes(A_WR90, B_WR90, n=70, quantos=4)
previsto = sorted([analitico(A_WR90, B_WR90, m, n)
                   for m in range(1, 4) for n in range(1, 4)])
for num, prev in zip(sorted(f), previsto):
    print('   %8.4f   %8.4f    erro %.2e' % (num / 1e9, prev / 1e9,
                                             abs(num - prev) / prev))
print('  o TM mais baixo é o TM11, bem acima do TE10: por isso o guia é')
print('  monomodo na faixa de operação')

print()
print('convergência do TE10 com a malha')
for n in (30, 50, 70, 100):
    f, _, _, _ = cortes(A_WR90, B_WR90, n=n, quantos=3, neumann=True)
    fte = sorted(f)[1]
    print('   n = %3d : %10.5f GHz   erro %.2e'
          % (n, fte / 1e9, abs(fte - analitico(A_WR90, B_WR90, 1, 0))
             / analitico(A_WR90, B_WR90, 1, 0)))

print()
print('uma seção que nenhuma fórmula resolve: guia em L')
n = 70
m = int(round(n * B_WR90 / A_WR90))
f, vecs, mascara, idx = cortes(A_WR90, B_WR90, n=n, quantos=4,
                               recorte=(n // 2, n, 0, m // 2))
print('   corte TM mais baixo, em L     : %.4f GHz' % (sorted(f)[0] / 1e9))
f2, _, _, _ = cortes(A_WR90, B_WR90, n=n, quantos=4)
print('   corte TM mais baixo, retângulo: %.4f GHz' % (sorted(f2)[0] / 1e9))
print('   o L tem corte MAIOR: recortar um pedaço aperta a seção, e apertar')
print('   sobe a frequência de corte, como a corda mais curta soa mais agudo')

# ------------------------------------------------------------------- figura
f, vecs, mascara, idx = cortes(A_WR90, B_WR90, n=70, quantos=4)
ordem = np.argsort(f)
fig, eixo = plt.subplots(1, 3, figsize=(12, 3.6))
for ax, k in zip(eixo, ordem[:3]):
    campo = np.full(mascara.shape, np.nan)
    campo[mascara] = vecs[:, k]
    ax.imshow(campo.T, origin='lower', cmap='copper',
              extent=[0, A_WR90 * 1e3, 0, B_WR90 * 1e3])
    ax.set_title('TM, corte %.2f GHz' % (f[k] / 1e9), fontsize=10)
    ax.set_xlabel('x (mm)'); ax.set_ylabel('y (mm)')
fig.tight_layout()
plt.show()
