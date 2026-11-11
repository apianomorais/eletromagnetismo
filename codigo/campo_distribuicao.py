# -*- coding: utf-8 -*-
"""Campo e potencial de distribuições contínuas, por integração numérica.

O QUE RESOLVE
    Discretiza três distribuições clássicas em pedaços pequenos, soma a
    contribuição de cada um e compara com a fórmula fechada:

        fio de comprimento 2L,  E_z = Q / (4 pi eps0 z sqrt(L^2+z^2))
        anel de raio a,         E_z = Q z / (4 pi eps0 (a^2+z^2)^(3/2))
        disco de raio a,        E_z = (sigma/2eps0)[1 - z/sqrt(a^2+z^2)]

A FÍSICA
    O princípio da superposição é o que autoriza somar pedaços. Ele não é uma
    necessidade lógica, é um fato experimental, e é ele que torna todo este
    capítulo possível: sem linearidade, a soma de duas soluções não seria
    solução e cada problema teria de ser resolvido do zero.

COMO CONFERIR SE ESTÁ CERTO
    1. O erro contra a fórmula fechada tem de cair como 1/n^2 ao aumentar o
       número de pedaços (regra do ponto médio).
    2. Os limites têm de aparecer sozinhos: longe, carga pontual; perto, fio
       infinito ou plano infinito, conforme o caso.
    3. O campo obtido derivando o potencial numérico tem de bater com o campo
       integrado diretamente, que é um teste independente dos dois.

Prof. Apiano Morais - LFCA/URCA - Eletromagnetismo I
"""

import numpy as np
import matplotlib.pyplot as plt

K = 8.9875517873681764e9      # 1/4 pi eps0, em N m^2 / C^2
EPS0 = 1.0 / (4 * np.pi * K)

Q = 1.0e-9        # carga total, em coulomb
L = 0.20          # semicomprimento do fio, em metros
A = 0.10          # raio do anel e do disco, em metros


# ----------------------------------------------------- distribuições em pedaços
def fio(n):
    """Pedaços do bastão no eixo x, de -L a L. Devolve posições e cargas."""
    x = (np.arange(n) + 0.5) * (2 * L) / n - L
    p = np.column_stack([x, np.zeros(n), np.zeros(n)])
    return p, np.full(n, Q / n)


def anel(n):
    f = (np.arange(n) + 0.5) * 2 * np.pi / n
    p = np.column_stack([A * np.cos(f), A * np.sin(f), np.zeros(n)])
    return p, np.full(n, Q / n)


def disco(n):
    """n anéis vezes n setores, com área correta em cada pedaço."""
    s = (np.arange(n) + 0.5) * A / n
    f = (np.arange(n) + 0.5) * 2 * np.pi / n
    S, F = np.meshgrid(s, f, indexing='ij')
    p = np.column_stack([(S * np.cos(F)).ravel(), (S * np.sin(F)).ravel(),
                         np.zeros(S.size)])
    da = (S * (A / n) * (2 * np.pi / n)).ravel()
    sigma = Q / (np.pi * A ** 2)
    return p, sigma * da


def campo(pontos, cargas, alvo):
    """E e V no alvo, somando as contribuições de cada pedaço."""
    d = alvo - pontos
    r = np.sqrt((d ** 2).sum(axis=1))
    E = K * np.sum((cargas / r ** 3)[:, None] * d, axis=0)
    V = K * np.sum(cargas / r)
    return E, V


# ------------------------------------------- fórmulas fechadas, para comparar
def fio_exato(z):
    return K * Q / (z * np.sqrt(L ** 2 + z ** 2))


def anel_exato(z):
    return K * Q * z / (A ** 2 + z ** 2) ** 1.5


def disco_exato(z):
    sigma = Q / (np.pi * A ** 2)
    return sigma / (2 * EPS0) * (1 - z / np.sqrt(A ** 2 + z ** 2))


print('convergência contra a fórmula fechada, em z = 0,15 m')
z = 0.15
alvo = np.array([0.0, 0.0, z])
for nome, gerador, exato in (('fio', fio, fio_exato), ('anel', anel, anel_exato),
                             ('disco', disco, disco_exato)):
    print('  %s, valor exato = %.8e V/m' % (nome, exato(z)))
    anterior = None
    for n in (10, 20, 40, 80):
        p, q = gerador(n)
        E, _ = campo(p, q, alvo)
        err = abs(E[2] - exato(z)) / exato(z)
        linha = '    n = %3d (%6d pedaços) : erro = %.3e' % (n, len(q), err)
        if anterior:
            linha += '   razão = %.2f' % (anterior / err)
        anterior = err
        print(linha)
    if nome == 'anel':
        print('    o anel dá erro de máquina já com 10 pedaços: no eixo, todos')
        print('    os pedaços estão à mesma distância, e a soma é exata')

# ------------------------------------------------------- os limites conhecidos
print()
print('limites do fio, contra carga pontual e fio infinito')
print('      z (m)     numérico      pontual      fio infinito')
p, q = fio(4000)
lam = Q / (2 * L)
for z in (0.01, 0.05, 0.5, 5.0):
    E, _ = campo(p, q, np.array([0.0, 0.0, z]))
    pontual = K * Q / z ** 2
    infinito = lam / (2 * np.pi * EPS0 * z)
    print('   %8.2f  %.4e   %.4e   %.4e' % (z, E[2], pontual, infinito))
print('  perto, o numérico segue o fio infinito; longe, segue a carga pontual')

# -------------------------------------- o campo como derivada do potencial
print()
print('teste independente: E_z contra -dV/dz, no disco')
p, q = disco(120)
h = 1e-4
print('      z (m)    E_z integrado   -dV/dz numérico   diferença relativa')
for z in (0.03, 0.08, 0.20):
    E, _ = campo(p, q, np.array([0.0, 0.0, z]))
    _, vmais = campo(p, q, np.array([0.0, 0.0, z + h]))
    _, vmenos = campo(p, q, np.array([0.0, 0.0, z - h]))
    deriv = -(vmais - vmenos) / (2 * h)
    print('   %8.2f    %.6e     %.6e      %.2e'
          % (z, E[2], deriv, abs(E[2] - deriv) / abs(E[2])))

# ------------------------------------------------------------------- figura
zs = np.linspace(0.005, 0.6, 300)
p, q = fio(4000)
num = [campo(p, q, np.array([0.0, 0.0, z]))[0][2] for z in zs]

fig, eixo = plt.subplots(figsize=(7.2, 4.4))
eixo.loglog(zs, num, lw=2, label='bastão, numérico')
eixo.loglog(zs, K * Q / zs ** 2, ls='--', lw=1.4, label='carga pontual')
eixo.loglog(zs, lam / (2 * np.pi * EPS0 * zs), ls=':', lw=1.6,
            label='fio infinito')
eixo.axvline(L, lw=1, color='0.6')
eixo.set_xlabel('distância z (m)')
eixo.set_ylabel('campo no eixo (V/m)')
eixo.set_title('O mesmo bastão, dois regimes')
eixo.legend(frameon=False)
fig.tight_layout()
plt.show()
