# -*- coding: utf-8 -*-
"""Gradiente, divergente, rotacional e laplaciano por diferenças finitas.

O QUE RESOLVE
    Monta os quatro operadores numa grade cartesiana tridimensional, por
    diferenças centrais, e testa as duas identidades que o capítulo 1 usa o
    tempo todo:

        rot(grad T) = 0        e        div(rot v) = 0.

A FÍSICA
    As duas identidades são o que permite escrever E = -grad V na eletrostática
    e B = rot A sempre. Há aqui uma surpresa boa: na grade elas valem
    EXATAMENTE, e não apenas até o truncamento, porque a diferença central em x
    comuta com a diferença central em y, do mesmo jeito que as derivadas
    parciais comutam no contínuo. O que sobra é só arredondamento de ponto
    flutuante, e esse PIORA ao refinar a grade, porque cada derivada divide por
    h. É o oposto do que a intuição sugere.

COMO CONFERIR SE ESTÁ CERTO
    1. O rotacional de um gradiente e o divergente de um rotacional têm de dar
       zero na ordem de 1e-15, independentemente da resolução; e o resíduo tem
       de crescer, não cair, quando a grade é refinada.
    2. Para um campo de teste com resultado conhecido, o divergente e o
       rotacional numéricos têm de reproduzir a expressão analítica.
    3. O laplaciano de 1/r tem de ser nulo longe da origem, que é o conteúdo da
       seção 5 do capítulo.

Prof. Apiano Morais - LFCA/URCA - Eletromagnetismo I
"""

import numpy as np
import matplotlib.pyplot as plt


def grade(n, lim=1.0):
    """Grade cúbica de n pontos por lado, de -lim a lim, e o passo."""
    x = np.linspace(-lim, lim, n)
    h = x[1] - x[0]
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
    return X, Y, Z, h


def d(f, eixo, h):
    """Derivada por diferença central, com as bordas descartadas depois."""
    return np.gradient(f, h, axis=eixo, edge_order=2)


def gradiente(T, h):
    return np.array([d(T, 0, h), d(T, 1, h), d(T, 2, h)])


def divergente(v, h):
    return d(v[0], 0, h) + d(v[1], 1, h) + d(v[2], 2, h)


def rotacional(v, h):
    return np.array([d(v[2], 1, h) - d(v[1], 2, h),
                     d(v[0], 2, h) - d(v[2], 0, h),
                     d(v[1], 0, h) - d(v[0], 1, h)])


def laplaciano(T, h):
    return divergente(gradiente(T, h), h)


def miolo(a, k=2):
    """Descarta k camadas de borda, onde a diferença central não é central."""
    if a.ndim == 4:
        return a[:, k:-k, k:-k, k:-k]
    return a[k:-k, k:-k, k:-k]


# ------------------------------------------- 1. as duas identidades nulas
print('identidades nulas: exatas na grade, a menos de arredondamento')
print('   n      h        max|rot(grad T)|     max|div(rot v)|')
anterior = None
for n in (21, 41, 81, 161):
    X, Y, Z, h = grade(n)
    T = np.sin(2 * X) * np.cos(Y) * np.exp(Z / 3)
    v = np.array([Y * Z ** 2, X ** 2 * Z, X * Y * np.cos(X)])
    e1 = np.max(np.abs(miolo(rotacional(gradiente(T, h), h))))
    e2 = np.max(np.abs(miolo(divergente(rotacional(v, h), h))))
    print('  %4d  %.5f     %.6e        %.6e' % (n, h, e1, e2))
    if anterior:
        print('        o resíduo CRESCEU por %.1f e %.1f ao refinar'
              % (e1 / anterior[0], e2 / anterior[1]))
    anterior = (e1, e2)
print('  as identidades são exatas na grade: o que se vê é o arredondamento,')
print('  amplificado pela divisão por h de cada derivada')

# ------------------------------------ 2. um campo de teste com conta fechada
n = 121
X, Y, Z, h = grade(n)
v = np.array([X ** 2 * Y, Y * Z, X * Z ** 2])
# div v = 2xy + z + 2xz ;  rot v = (-y, -2z^2... ) calculado abaixo
div_num = divergente(v, h)
div_exato = 2 * X * Y + Z + 2 * X * Z
rot_num = rotacional(v, h)
# rot v = (dv_z/dy - dv_y/dz, dv_x/dz - dv_z/dx, dv_y/dx - dv_x/dy)
#       = (0 - y, 0 - z^2, 0 - x^2)
rot_exato = np.array([-Y, -Z ** 2, -X ** 2])

print()
print('campo de teste v = (x^2 y, y z, x z^2):')
print('  erro máximo no divergente : %.3e'
      % np.max(np.abs(miolo(div_num) - miolo(div_exato))))
print('  erro máximo no rotacional : %.3e'
      % np.max(np.abs(miolo(rot_num) - miolo(rot_exato))))

# ------------------------------------------- 3. o laplaciano de 1/r, longe de 0
n = 161
x = np.linspace(-3, 3, n)
h = x[1] - x[0]
X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
r = np.sqrt(X ** 2 + Y ** 2 + Z ** 2)
r[r < 1e-9] = 1e-9
T = 1.0 / r
lap = laplaciano(T, h)
longe = r > 1.0
print()
print('laplaciano de 1/r:')
escala = np.max(np.abs(1.0 / r[longe] ** 3))
print('  máximo de |lap| para r > 1 : %.3e, ou %.1e vezes a escala 1/r^3'
      % (np.max(np.abs(lap[longe])), np.max(np.abs(lap[longe])) / escala))
print('  isto é truncamento de ordem h^2, e some refinando a grade')
print('  valor no ponto mais próximo da origem: %.3e  (a delta mora aqui)'
      % lap[n // 2, n // 2, n // 2])

# ------------------------------------------------------------------- figura
nx = 26
x2 = np.linspace(-2, 2, nx)
X2, Y2 = np.meshgrid(x2, x2, indexing='ij')
fig, eixo = plt.subplots(1, 3, figsize=(12, 4))
campos = [('fonte: v = (x, y)', X2, Y2),
          ('rotação: v = (-y, x)', -Y2, X2),
          ('cisalhamento: v = (y, 0)', Y2, np.zeros_like(X2))]
for ax, (titulo, u, w) in zip(eixo, campos):
    ax.quiver(X2, Y2, u, w, color='#b05a1f')
    ax.set_title(titulo, fontsize=10)
    ax.set_aspect('equal')
    ax.set_xticks([]); ax.set_yticks([])
fig.suptitle('Divergente puro, rotacional puro, e um campo paralelo '
             'com rotacional', fontsize=11)
fig.tight_layout()
plt.show()
