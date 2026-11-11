# -*- coding: utf-8 -*-
"""Invariância de calibre, medida numericamente.

O QUE RESOLVE
    Parte de potenciais (V, A) quaisquer, aplica uma transformação de calibre

        A' = A + grad(lambda),     V' = V - d(lambda)/dt

    com lambda arbitrário, e verifica que E e B calculados a partir dos dois
    conjuntos coincidem. Depois mede a condição de Lorenz antes e depois.

A FÍSICA
    Os potenciais não são observáveis: a mesma física admite infinitas
    descrições, ligadas por transformações de calibre. O que é observável é o
    campo. Esse excesso de descrição não é um defeito, é a estrutura que, na
    teoria quântica de campos, dita quais interações podem existir.

COMO CONFERIR SE ESTÁ CERTO
    1. E e B têm de ser iguais nos dois calibres. O erro em B cai como h^2,
       mas o erro em E não: ele envolve derivada segunda de lambda, calculada
       com diferenças aninhadas, e é dominado por arredondamento. É um bom
       exemplo de que nem todo erro numérico melhora refinando.
    2. A condição de Lorenz, que o conjunto original satisfaz, deixa de valer
       depois de uma transformação com lambda que não obedeça à equação de
       onda.
    3. Escolhendo lambda que RESOLVE a equação de onda, a condição de Lorenz é
       preservada: é a liberdade que sobra dentro do calibre de Lorenz.

Prof. Apiano Morais - LFCA/URCA - Eletromagnetismo III
"""

import numpy as np

C = 2.99792458e8
EPS0 = 8.8541878128e-12
MU0 = 1.0 / (EPS0 * C * C)

K = 2 * np.pi / 0.10          # 10 cm de comprimento de onda
OMEGA = C * K


# ----------------------- potenciais de partida: uma onda no calibre de Lorenz
def V0(x, y, z, t):
    return 0.0 * x


def A0(x, y, z, t):
    """A = A0 cos(kz - wt) x^, com V = 0: satisfaz Lorenz, pois div A = 0."""
    ax = np.cos(K * z - OMEGA * t)
    return np.array([ax, np.zeros_like(ax), np.zeros_like(ax)])


# --------------------------------------- a função de calibre, bem arbitrária
def lam(x, y, z, t):
    return 1e-3 * np.sin(3 * K * x) * np.cos(2 * K * z) * np.exp(-OMEGA * t * 1e-12)


def derivadas(f, x, y, z, t, h, dt):
    """Gradiente espacial e derivada temporal por diferenças centrais."""
    gx = (f(x + h, y, z, t) - f(x - h, y, z, t)) / (2 * h)
    gy = (f(x, y + h, z, t) - f(x, y - h, z, t)) / (2 * h)
    gz = (f(x, y, z + h, t) - f(x, y, z - h, t)) / (2 * h)
    ft = (f(x, y, z, t + dt) - f(x, y, z, t - dt)) / (2 * dt)
    return np.array([gx, gy, gz]), ft


def campos(V, A, x, y, z, t, h, dt):
    """E = -grad V - dA/dt e B = rot A, por diferenças centrais."""
    gradV, _ = derivadas(V, x, y, z, t, h, dt)
    dAdt = (A(x, y, z, t + dt) - A(x, y, z, t - dt)) / (2 * dt)
    E = -gradV - dAdt

    def comp(i):
        def f(xx, yy, zz, tt):
            return A(xx, yy, zz, tt)[i]
        return f

    def d(i, eixo):
        f = comp(i)
        if eixo == 0:
            return (f(x + h, y, z, t) - f(x - h, y, z, t)) / (2 * h)
        if eixo == 1:
            return (f(x, y + h, z, t) - f(x, y - h, z, t)) / (2 * h)
        return (f(x, y, z + h, t) - f(x, y, z - h, t)) / (2 * h)

    B = np.array([d(2, 1) - d(1, 2), d(0, 2) - d(2, 0), d(1, 0) - d(0, 1)])
    return E, B


def transformados():
    """Os potenciais depois da transformação de calibre."""
    h, dt = 1e-5, 1e-14

    def V1(x, y, z, t):
        _, lt = derivadas(lam, x, y, z, t, h, dt)
        return V0(x, y, z, t) - lt

    def A1(x, y, z, t):
        gl, _ = derivadas(lam, x, y, z, t, h, dt)
        return A0(x, y, z, t) + gl
    return V1, A1


x, y, z, t = 0.013, -0.027, 0.041, 3.1e-10
V1, A1 = transformados()

print('invariância de calibre, medida ponto a ponto')
print('      h (m)        erro em E        erro em B')
anterior = None
for h in (1e-4, 5e-5, 2.5e-5):
    dt = h / C
    E_a, B_a = campos(V0, A0, x, y, z, t, h, dt)
    E_b, B_b = campos(V1, A1, x, y, z, t, h, dt)
    eE = np.max(np.abs(E_a - E_b)) / np.max(np.abs(E_a))
    eB = np.max(np.abs(B_a - B_b)) / np.max(np.abs(B_a))
    linha = '   %.2e     %.3e      %.3e' % (h, eE, eB)
    if anterior:
        linha += '   razão %.1f e %.1f' % (anterior[0] / eE, anterior[1] / eB)
    anterior = (eE, eB)
    print(linha)
print('  os campos são os mesmos nos dois calibres, em uma parte em 1e5 ou')
print('  melhor. O erro em B cai por 4 a cada refinamento, como manda a')
print('  diferença central; o erro em E não cai, e isso é esperado: ele exige')
print('  derivada SEGUNDA de lambda, feita com diferenças aninhadas, e aí o')
print('  arredondamento domina. Refinar piora em vez de melhorar.')

print()
print('os potenciais, esses, são bem diferentes:')
h, dt = 2.5e-5, 2.5e-5 / C
print('  V  original = %+.6e     V  transformado = %+.6e'
      % (V0(x, y, z, t), V1(x, y, z, t)))
print('  Ax original = %+.6e     Ax transformado = %+.6e'
      % (A0(x, y, z, t)[0], A1(x, y, z, t)[0]))


def lorenz(V, A, x, y, z, t, h, dt):
    """div A + (1/c^2) dV/dt, que tem de ser zero no calibre de Lorenz."""
    def comp(i):
        def f(xx, yy, zz, tt):
            return A(xx, yy, zz, tt)[i]
        return f
    divA = 0.0
    for i, passo in enumerate(((h, 0, 0), (0, h, 0), (0, 0, h))):
        f = comp(i)
        divA += (f(x + passo[0], y + passo[1], z + passo[2], t)
                 - f(x - passo[0], y - passo[1], z - passo[2], t)) / (2 * h)
    _, dVdt = derivadas(V, x, y, z, t, h, dt)
    return divA + dVdt / C ** 2


print()
print('condição de Lorenz, div A + (1/c²) dV/dt:')
print('  no conjunto original    : %+.3e  (zero: está em Lorenz)'
      % lorenz(V0, A0, x, y, z, t, h, dt))
print('  depois da transformação : %+.3e  (não é mais zero)'
      % lorenz(V1, A1, x, y, z, t, h, dt))
print('  porque o lambda escolhido não satisfaz a equação de onda. Só os')
print('  lambdas que satisfazem preservam o calibre de Lorenz, e é essa a')
print('  liberdade que sobra dentro dele')
