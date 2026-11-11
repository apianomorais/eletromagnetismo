# -*- coding: utf-8 -*-
"""A expansão multipolar: quando ela serve, e quanto erra.

O QUE RESOLVE
    Dada uma distribuição de cargas pontuais, calcula o monopolo, o dipolo e o
    quadrupolo, monta a série truncada em cada ordem e compara com o potencial
    exato, em função da distância e da direção.

A FÍSICA
    A expansão não é uma aproximação qualquer: cada ordem cai com uma potência
    diferente de 1/r, de modo que longe o suficiente o primeiro termo não nulo
    domina sozinho. Daí a regra prática: carga total não nula, tudo é monopolo;
    carga nula, procure o dipolo; dipolo nulo por simetria, procure o
    quadrupolo.

COMO CONFERIR SE ESTÁ CERTO
    1. O erro relativo da série truncada na ordem n tem de cair como 1/r^(n+1)
       em relação ao termo dominante, e o programa mede o expoente.
    2. Mudando a origem, o momento de dipolo muda de p para p - Q a, e isso só
       deixa de acontecer quando a carga total é nula.
    3. Para um quadrupolo puro (quatro cargas alternadas), o monopolo e o
       dipolo têm de dar zero, e sobra o 1/r^3 no potencial.

Prof. Apiano Morais - LFCA/URCA - Eletromagnetismo I
"""

import numpy as np

K = 8.9875517873681764e9


def exato(cargas, alvo):
    """Potencial exato da coleção de cargas pontuais."""
    v = 0.0
    for pos, q in cargas:
        v += K * q / np.linalg.norm(np.asarray(alvo, float) - np.asarray(pos, float))
    return v


def momentos(cargas, origem=(0, 0, 0)):
    """Carga total, vetor dipolo e tensor quadrupolo (sem traço)."""
    o = np.asarray(origem, dtype=float)
    Q = sum(q for _, q in cargas)
    p = sum(q * (np.asarray(pos, float) - o) for pos, q in cargas)
    Qij = np.zeros((3, 3))
    for pos, q in cargas:
        r = np.asarray(pos, float) - o
        Qij += q * (3 * np.outer(r, r) - np.dot(r, r) * np.eye(3))
    return Q, np.asarray(p, dtype=float), Qij


def serie(cargas, alvo, ordem, origem=(0, 0, 0)):
    """Série multipolar truncada: ordem 0 monopolo, 1 dipolo, 2 quadrupolo."""
    o = np.asarray(origem, dtype=float)
    r = np.asarray(alvo, float) - o
    d = np.linalg.norm(r)
    n = r / d
    Q, p, Qij = momentos(cargas, origem)
    v = K * Q / d
    if ordem >= 1:
        v += K * np.dot(p, n) / d ** 2
    if ordem >= 2:
        v += K * 0.5 * np.dot(n, Qij @ n) / d ** 3
    return v


# --------------------------------------------- 1. um dipolo, com carga total
A = 0.02
dipolo = [((0, 0, +A), +1.0e-9), ((0, 0, -A), -1.0e-9)]

print('dipolo puro: duas cargas opostas separadas por %.0f cm' % (2 * A * 100))
Q, p, Qij = momentos(dipolo)
print('  carga total = %.2e C,  |p| = %.4e C m  (previsto q d = %.4e)'
      % (Q, np.linalg.norm(p), 1e-9 * 2 * A))
print()
print('     r/d      exato (V)     ordem 1 (V)    erro relativo   expoente')
anterior = None
for mult in (3, 6, 12, 24, 48):
    r = mult * 2 * A
    alvo = (0.0, 0.0, r)
    ex = exato(dipolo, alvo)
    s1 = serie(dipolo, alvo, 1)
    err = abs(s1 - ex) / abs(ex)
    linha = '  %6.0f   %12.6f   %12.6f    %.3e' % (mult, ex, s1, err)
    if anterior:
        linha += '      %.2f' % (np.log(anterior / err) / np.log(2.0))
    anterior = err
    print(linha)
print('  expoente 2: o erro do dipolo cai como 1/r^2 em relação ao termo')
print('  dominante, porque o primeiro termo omitido é o quadrupolo')

# ------------------------------------------- 2. a origem muda o dipolo
print()
print('dependência da origem')
for nome, cargas in (('carga total nula (dipolo)', dipolo),
                     ('carga total não nula', dipolo + [((0, 0, 0), 3.0e-9)])):
    _, p0, _ = momentos(cargas, (0, 0, 0))
    _, p1, _ = momentos(cargas, (0.05, 0, 0))
    print('  %-26s p(origem) = %.4e   p(deslocada) = %.4e'
          % (nome, np.linalg.norm(p0), np.linalg.norm(p1)))
print('  com carga total nula o dipolo não depende da origem; com carga total')
print('  não nula ele depende, e por isso não tem significado próprio')

# --------------------------------------------------- 3. um quadrupolo puro
B = 0.02
quad = [((+B, 0, 0), +1.0e-9), ((-B, 0, 0), +1.0e-9),
        ((0, +B, 0), -1.0e-9), ((0, -B, 0), -1.0e-9)]
Q, p, Qij = momentos(quad)
print()
print('quatro cargas alternadas em cruz: quadrupolo puro')
print('  carga total = %.1e C,  |p| = %.1e C m  (ambos nulos)'
      % (Q, np.linalg.norm(p)))
print('  traço do tensor quadrupolo = %.1e  (nulo por construção)' % np.trace(Qij))
print()
print('     r/a      exato (V)     ordem 2 (V)    erro relativo   expoente')
anterior = None
for mult in (4, 8, 16, 32):
    r = mult * B
    # sobre o eixo x, onde o quadrupolo não se anula por simetria
    alvo = (r, 0.0, 0.0)
    ex = exato(quad, alvo)
    s2 = serie(quad, alvo, 2)
    err = abs(s2 - ex) / abs(ex)
    linha = '  %6.0f   %12.6e   %12.6e    %.3e' % (mult, ex, s2, err)
    if anterior:
        linha += '       %.2f' % (np.log(anterior / err) / np.log(2.0))
    anterior = err
    print(linha)
print('  o potencial cai como 1/r^3, e a série de ordem 2 já o acompanha')
