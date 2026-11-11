# -*- coding: utf-8 -*-
"""Os campos de uma carga em movimento, por Liénard-Wiechert.

O QUE RESOLVE
    Para uma trajetória w(t) qualquer, resolve a condição de tempo retardado

        |r - w(t_r)| = c (t - t_r)

    por bisseção, monta os potenciais de Liénard-Wiechert e deriva os campos
    pela fórmula com as duas parcelas, de velocidade e de aceleração.

A FÍSICA
    A parcela de velocidade cai com 1/i^2 e acompanha a carga; a de aceleração
    cai com 1/i e é a radiação, a única que sobrevive longe. Em movimento
    uniforme a soma dá um campo que aponta para a posição PRESENTE da carga,
    achatado num disco perpendicular ao movimento.

COMO CONFERIR SE ESTÁ CERTO
    1. Com v pequeno, o campo tem de virar o de Coulomb.
    2. Em movimento uniforme, o campo tem de bater com a fórmula fechada
       q(1-b^2) / (4 pi eps0 R^2 (1 - b^2 sen^2 th)^(3/2)) e apontar para a
       posição presente.
    3. B tem de ser perpendicular a E, com B = E/c.
    4. Com aceleração, a potência que atravessa uma esfera grande tem de ser
       independente do raio, e igual à fórmula de Larmor.

Prof. Apiano Morais - LFCA/URCA - Eletromagnetismo III
"""

import numpy as np

C = 2.99792458e8
EPS0 = 8.8541878128e-12
MU0 = 1.0 / (EPS0 * C * C)
Q = 1.0e-9


def tempo_retardado(w, r, t, janela=1e-6, passos=200):
    """Acha t_r por bisseção em f(t_r) = |r - w(t_r)| - c (t - t_r).

    A função é monótona porque a carga é mais lenta que a luz, de modo que a
    bisseção é segura e converge sempre.
    """
    r = np.asarray(r, dtype=float)

    def f(tr):
        return np.linalg.norm(r - w(tr)) - C * (t - tr)

    lo, hi = t - janela, t
    while f(lo) > 0:
        janela *= 10
        lo = t - janela
    # f é negativa em lo e positiva em hi; a raiz fica entre as duas
    for _ in range(passos):
        meio = 0.5 * (lo + hi)
        if f(meio) > 0:
            hi = meio
        else:
            lo = meio
    return 0.5 * (lo + hi)


def campos(w, v, a, r, t):
    """E e B no ponto r, no instante t, para a trajetória w com v e a."""
    r = np.asarray(r, dtype=float)
    tr = tempo_retardado(w, r, t)
    vet_i = r - w(tr)
    i = np.linalg.norm(vet_i)
    u = C * vet_i / i - v(tr)
    iu = np.dot(vet_i, u)
    E = (Q / (4 * np.pi * EPS0)) * (i / iu ** 3) * (
        (C ** 2 - np.dot(v(tr), v(tr))) * u
        + np.cross(vet_i, np.cross(u, a(tr))))
    B = np.cross(vet_i / i, E) / C
    return E, B, tr


# ------------------------------------------------- 1. movimento uniforme
def uniforme(beta):
    vv = np.array([beta * C, 0.0, 0.0])

    def w(t):
        return vv * t

    def v(t):
        return vv

    def a(t):
        return np.zeros(3)
    return w, v, a


def exato_uniforme(beta, R, theta):
    """Fórmula fechada: R é medido da posição PRESENTE da carga."""
    return (Q / (4 * np.pi * EPS0)) * (1 - beta ** 2) / (
        (1 - beta ** 2 * np.sin(theta) ** 2) ** 1.5 * R ** 2)


print('carga em movimento uniforme: campo contra a fórmula fechada')
print('    beta    ângulo    |E| numérico     |E| exato      erro')
R = 1.0
for beta in (0.01, 0.5, 0.9):
    w, v, a = uniforme(beta)
    for theta in (np.pi / 2, np.pi / 4):
        t = 1e-9
        # ponto a uma distância R da posição PRESENTE, no ângulo theta
        alvo = w(t) + R * np.array([np.cos(theta), np.sin(theta), 0.0])
        E, B, tr = campos(w, v, a, alvo, t)
        ex = exato_uniforme(beta, R, theta)
        print('  %6.2f   %6.1f°   %13.6e   %13.6e   %.2e'
              % (beta, np.degrees(theta), np.linalg.norm(E), ex,
                 abs(np.linalg.norm(E) - ex) / ex))

print()
print('a direção do campo: ele aponta para a posição presente?')
beta = 0.8
w, v, a = uniforme(beta)
t = 1e-9
alvo = w(t) + np.array([0.0, 1.0, 0.0])
E, B, tr = campos(w, v, a, alvo, t)
dir_presente = (alvo - w(t)) / np.linalg.norm(alvo - w(t))
dir_retardada = (alvo - w(tr)) / np.linalg.norm(alvo - w(tr))
print('  cosseno com a direção presente  : %.8f' %
      np.dot(E / np.linalg.norm(E), dir_presente))
print('  cosseno com a direção retardada : %.8f' %
      np.dot(E / np.linalg.norm(E), dir_retardada))
print('  o campo aponta exatamente para onde a carga ESTÁ, e não para onde')
print('  ela estava quando a informação saiu')

print()
print('a relação entre B e E')
print('  E . B = %+.3e   (sempre perpendiculares)' % np.dot(E, B))
print('  |B| c / |E| = %.6f   em movimento uniforme, a %.1f c'
      % (np.linalg.norm(B) * C / np.linalg.norm(E), beta))
print('  NÃO é 1, e não tem de ser: B = (1/c) i^ x E, e aqui E não é')
print('  perpendicular à linha de visada retardada. O valor 1 vale só na zona')
print('  de radiação, onde E é transversal. Confira adiante, na carga')
print('  oscilante vista de longe.')

# ----------------------------------------- 2. carga acelerada: radiação
A0, OMEGA = 1e-3, 2 * np.pi * 1e9


def w_osc(t):
    return np.array([0.0, 0.0, A0 * np.cos(OMEGA * t)])


def v_osc(t):
    return np.array([0.0, 0.0, -A0 * OMEGA * np.sin(OMEGA * t)])


def a_osc(t):
    return np.array([0.0, 0.0, -A0 * OMEGA ** 2 * np.cos(OMEGA * t)])


E_far, B_far, _ = campos(w_osc, v_osc, a_osc,
                         np.array([30.0, 0.0, 0.0]), 5e-9 + 30.0 / C)
print('  na zona de radiação, a 30 m da carga oscilante:')
print('    |B| c / |E| = %.6f' % (np.linalg.norm(B_far) * C
                                  / np.linalg.norm(E_far)))
print()
print('carga oscilante: a potência que escapa não depende do raio')
print('   raio (m)    potência média (W)   Larmor médio (W)    razão')
larmor = MU0 * Q ** 2 * (A0 * OMEGA ** 2) ** 2 / (6 * np.pi * C) / 2
periodo = 2 * np.pi / OMEGA
for raio in (3.0, 10.0, 30.0):
    n = 40
    tet = (np.arange(n) + 0.5) * np.pi / n
    fi = (np.arange(2 * n) + 0.5) * 2 * np.pi / (2 * n)
    # média sobre um ciclo: a potência instantânea oscila, a média é Larmor
    media = 0.0
    instantes = 8
    for k in range(instantes):
        t = 5e-9 + k * periodo / instantes
        total = 0.0
        for th in tet:
            for ph in fi:
                nrm = np.array([np.sin(th) * np.cos(ph),
                                np.sin(th) * np.sin(ph), np.cos(th)])
                alvo = raio * nrm
                E, B, _ = campos(w_osc, v_osc, a_osc, alvo, t + raio / C)
                S = np.cross(E, B) / MU0
                total += np.dot(S, nrm) * raio ** 2 * np.sin(th) \
                    * (np.pi / n) * (2 * np.pi / (2 * n))
        media += total / instantes
    print('  %9.1f   %16.6e   %16.6e   %.4f'
          % (raio, media, larmor, media / larmor))
print('  a potência média é a mesma em qualquer esfera, e é a de Larmor: a')
print('  energia vai embora de verdade, e não volta')
