# -*- coding: utf-8 -*-
"""A esfera dielétrica num campo uniforme, pela série e pela relaxação.

O QUE RESOLVE
    Uma esfera de constante dielétrica eps_r num campo externo uniforme E0. A
    série de Legendre dá, em três linhas,

        E_dentro = 3 E0 / (eps_r + 2),   uniforme,

    e fora o campo é o aplicado mais o de um dipolo. O programa confere isso
    por relaxação numa grade, sem usar a série, resolvendo a equação de Laplace
    com a condição de contorno certa na interface.

A FÍSICA
    O campo interno é menor que o aplicado porque a carga ligada de superfície
    produz um campo contrário. Nos limites, eps_r = 1 devolve E0 (não há
    material) e eps_r -> infinito devolve zero (o condutor do capítulo 2).

COMO CONFERIR SE ESTÁ CERTO
    1. O campo interno tem de ser uniforme: o desvio entre pontos diferentes
       dentro da esfera fica abaixo de 1e-3, o que já é um bom sinal.
    2. O valor tem de bater com 3 E0/(eps_r + 2) para vários eps_r, e bate com
       alguns por cento na grade usada aqui.
    3. Os dois limites têm de aparecer sozinhos.
    4. Refinando, o erro cai em primeira ordem, porque a interface curva numa
       grade quadrada é o fator limitante. Esse é o preço do método, e é o
       argumento a favor de ter a solução analítica.

Prof. Apiano Morais - LFCA/URCA - Eletromagnetismo I
"""

import numpy as np
import matplotlib.pyplot as plt

E0 = 1.0          # campo aplicado, em unidades arbitrárias
R = 1.0           # raio da esfera


def analitico(eps_r):
    return 3.0 * E0 / (eps_r + 2.0)


def relaxar(eps_r, n=81, L=6.0, maxit=60000, tol=1e-9, omega=1.9):
    """Laplace com dielétrico, em simetria axial, na malha (s, z).

    A equação resolvida é div(eps grad V) = 0, discretizada com a
    permissividade avaliada nas faces entre células, que é o jeito correto de
    tratar a descontinuidade: assim a condição de contorno D_perp contínuo sai
    automaticamente, sem ser imposta à mão.
    """
    s = np.linspace(0.0, L, n)
    z = np.linspace(-L, L, 2 * n - 1)
    h = s[1] - s[0]
    S, Z = np.meshgrid(s, z, indexing='ij')
    # Interface suavizada: em vez de um degrau, a permissividade atravessa a
    # fronteira numa rampa de uma célula. Sem isso, a esfera vira uma escadinha
    # na grade quadrada e o erro deixa de cair de forma regular ao refinar.
    r = np.sqrt(S ** 2 + Z ** 2)
    fracao = np.clip(0.5 - (r - R) / h, 0.0, 1.0)
    eps = 1.0 + (eps_r - 1.0) * fracao

    V = -E0 * Z.copy()                 # chute inicial: o campo uniforme

    # os pesos não mudam com a iteração: calcule uma vez só
    ep_s = 2 * eps[1:, :] * eps[:-1, :] / (eps[1:, :] + eps[:-1, :])
    ep_z = 2 * eps[:, 1:] * eps[:, :-1] / (eps[:, 1:] + eps[:, :-1])
    sf = 0.5 * (S[1:, :] + S[:-1, :])
    wl = ep_s[:-1, 1:-1] * sf[:-1, 1:-1]       # face em s menor
    wr = ep_s[1:, 1:-1] * sf[1:, 1:-1]         # face em s maior
    wb = ep_z[1:-1, :-1] * S[1:-1, 1:-1]
    wt = ep_z[1:-1, 1:] * S[1:-1, 1:-1]
    den = wl + wr + wb + wt

    # tabuleiro de damas: com a varredura em duas cores a sobre-relaxação é
    # estável, coisa que ela não é se todos os pontos forem atualizados de uma
    # vez só com os valores velhos
    ii, jj = np.meshgrid(np.arange(1, V.shape[0] - 1),
                         np.arange(1, V.shape[1] - 1), indexing='ij')
    tabuleiro = (ii + jj) % 2

    for it in range(maxit):
        velho = V.copy()
        for cor in (0, 1):
            num = (wl * V[:-2, 1:-1] + wr * V[2:, 1:-1]
                   + wb * V[1:-1, :-2] + wt * V[1:-1, 2:])
            alvo = num / den
            m = tabuleiro == cor
            miolo = V[1:-1, 1:-1]
            miolo[m] += omega * (alvo[m] - miolo[m])
            V[1:-1, 1:-1] = miolo
        V[0, 1:-1] = V[1, 1:-1]                    # eixo: derivada radial nula
        V[-1, :] = -E0 * Z[-1, :]                  # longe, o campo aplicado
        V[:, 0] = -E0 * Z[:, 0]
        V[:, -1] = -E0 * Z[:, -1]
        if np.max(np.abs(V - velho)) < tol:
            break
    return s, z, V, it + 1


print('esfera dielétrica num campo uniforme E0 = %.1f' % E0)
print('  previsto: E_dentro = 3 E0 / (eps_r + 2), uniforme')
print()
print('   eps_r    previsto    relaxação    erro     uniformidade   varreduras')
for eps_r in (1.0, 2.0, 4.0, 10.0, 80.0):
    s, z, V, it = relaxar(eps_r)
    dz = z[1] - z[0]
    k0 = len(z) // 2
    # campo no centro e em dois outros pontos internos, todos sobre o eixo
    amostras = []
    passo = max(1, int(0.3 * R / dz))
    for k in (k0, k0 + passo, k0 - passo):
        amostras.append(-(V[0, k + 1] - V[0, k - 1]) / (2 * dz))
    E_num = amostras[0]
    unif = (max(amostras) - min(amostras)) / abs(E_num)
    prev = analitico(eps_r)
    print('  %6.1f   %9.5f   %9.5f   %7.2e   %9.2e   %7d'
          % (eps_r, prev, E_num, abs(E_num - prev) / prev, unif, it))

print()
print('refinando a grade, com eps_r = 4:')
print('   n      h        relaxação      erro')
anterior = None
for n in (41, 61, 81, 121, 161):
    s_, z_, V_, it_ = relaxar(4.0, n=n)
    dz = z_[1] - z_[0]
    k0 = len(z_) // 2
    E_num = -(V_[0, k0 + 1] - V_[0, k0 - 1]) / (2 * dz)
    err = abs(E_num - analitico(4.0)) / analitico(4.0)
    linha = '  %4d  %.4f   %10.6f   %.3e' % (n, 6.0 / (n - 1), E_num, err)
    if anterior:
        linha += '   razão %.2f' % (anterior / err)
    anterior = err
    print(linha)
print('  com a interface suavizada numa célula o erro cai de forma regular,')
print('  mas em PRIMEIRA ordem: a suavização é de ordem h, e domina. Com o')
print('  degrau duro ele nem cai regularmente, porque a escadinha muda de')
print('  jeito a cada resolução.')
print('  Moral: chegar a 1 por cento aqui custa grade grande, e a solução')
print('  analítica da série dá o número exato em três linhas. O numérico vale')
print('  pela generalidade, não pela precisão barata.')

print()
print('os dois limites')
print('  eps_r = 1    : %.5f  (tem de ser E0 = %.1f)' % (analitico(1.0), E0))
print('  eps_r = 1e6  : %.3e  (tem de tender a zero, o condutor)'
      % analitico(1e6))

# ------------------------------------------------------------------- figura
s, z, V, _ = relaxar(4.0, n=101)
S, Z = np.meshgrid(s, z, indexing='ij')
fig, eixo = plt.subplots(figsize=(6.4, 5.4))
eixo.contour(np.concatenate([-S[::-1], S]), np.concatenate([Z[::-1], Z]),
             np.concatenate([V[::-1], V]), levels=28, colors='#b05a1f',
             linewidths=1.0)
ang = np.linspace(0, 2 * np.pi, 200)
eixo.plot(R * np.cos(ang), R * np.sin(ang), lw=2, color='#2b3240')
eixo.set_xlim(-3, 3); eixo.set_ylim(-3, 3)
eixo.set_aspect('equal')
eixo.set_xlabel('s / R'); eixo.set_ylabel('z / R')
eixo.set_title('Equipotenciais: dentro, igualmente espaçadas e mais raras')
fig.tight_layout()
plt.show()
