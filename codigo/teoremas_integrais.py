# -*- coding: utf-8 -*-
"""Os teoremas da divergência e de Stokes, conferidos numericamente.

O QUE RESOLVE
    Calcula os dois lados de cada teorema para campos concretos:

      divergência:  integral de volume de div v  =  fluxo por fora
      Stokes:       fluxo do rotacional  =  circulação na borda

    e, no caso de Stokes, refaz a conta com DUAS superfícies diferentes
    apoiadas na mesma curva, para verificar que o resultado não muda.

A FÍSICA
    Esses dois teoremas são o que permite passar das formas integrais das
    equações de Maxwell para as diferenciais, e vice-versa. A invariância de
    Stokes pela troca de superfície é exatamente o que falha na lei de Ampère
    sem o termo de Maxwell, como mostra o capítulo 7: lá, a mesma curva com
    duas superfícies dá respostas diferentes, e é esse o sintoma do problema.

COMO CONFERIR SE ESTÁ CERTO
    1. No cubo do exemplo resolvido do capítulo, os dois lados têm de dar 48.
    2. Na calota esférica, fluxo do rotacional e circulação têm de coincidir, e
       o disco plano com a mesma borda tem de dar o mesmo número.
    3. Refinando a malha, o erro tem de cair como h^2.

Prof. Apiano Morais - LFCA/URCA - Eletromagnetismo I
"""

import numpy as np
import matplotlib.pyplot as plt

A = 2.0           # lado do cubo do exemplo resolvido


# ====================================================== teorema da divergência
def campo_cubo(x, y, z):
    """v = (x y, 2 y z, 3 z x)."""
    return np.array([x * y, 2 * y * z, 3 * z * x])


def volume_cubo(n):
    """Integral de div v no cubo [0,a]^3, por ponto médio."""
    u = (np.arange(n) + 0.5) * A / n
    X, Y, Z = np.meshgrid(u, u, u, indexing='ij')
    div = Y + 2 * Z + 3 * X          # div v = y + 2z + 3x
    return np.sum(div) * (A / n) ** 3


def fluxo_cubo(n):
    """Fluxo de v pelas seis faces, por ponto médio."""
    u = (np.arange(n) + 0.5) * A / n
    P, Q = np.meshgrid(u, u, indexing='ij')
    da = (A / n) ** 2
    total = 0.0
    # faces x = 0 e x = a, normal -x e +x, componente v_x = x y
    total += np.sum(A * P) * da - np.sum(0 * P) * da
    # faces y = 0 e y = a, componente v_y = 2 y z
    total += np.sum(2 * A * Q) * da - 0.0
    # faces z = 0 e z = a, componente v_z = 3 z x
    total += np.sum(3 * A * P) * da - 0.0
    return total


print('TEOREMA DA DIVERGÊNCIA no cubo de lado %.0f' % A)
print('    n      volume        superfície      diferença')
for n in (10, 20, 40, 80):
    v, f = volume_cubo(n), fluxo_cubo(n)
    print('  %4d   %10.6f    %10.6f     %.2e' % (n, v, f, abs(v - f)))
print('  valor exato da conta do papel: 48')
print('  o erro é zero em qualquer malha porque os integrandos são lineares,')
print('  e a regra do ponto médio integra polinômios de grau 1 exatamente')


# ================================================================= Stokes
def campo_stokes(x, y, z):
    """v = (z, x, y), cujo rotacional é (1, 1, 1)."""
    x, y, z = np.broadcast_arrays(np.asarray(x, dtype=float),
                                  np.asarray(y, dtype=float),
                                  np.asarray(z, dtype=float))
    return z, x, y


ROT = np.array([1.0, 1.0, 1.0])
RS = 1.0            # raio da esfera
ALFA = np.pi / 3    # ângulo polar da borda da calota


def fluxo_calota(n):
    """Fluxo do rotacional pela calota esférica, de theta = 0 a ALFA."""
    t = (np.arange(n) + 0.5) * ALFA / n
    f = (np.arange(n) + 0.5) * 2 * np.pi / n
    T, F = np.meshgrid(t, f, indexing='ij')
    nx = np.sin(T) * np.cos(F)
    ny = np.sin(T) * np.sin(F)
    nz = np.cos(T)
    da = RS ** 2 * np.sin(T) * (ALFA / n) * (2 * np.pi / n)
    return np.sum((ROT[0] * nx + ROT[1] * ny + ROT[2] * nz) * da)


def fluxo_disco(n):
    """Fluxo do rotacional pelo disco plano com a mesma borda."""
    raio = RS * np.sin(ALFA)
    altura = RS * np.cos(ALFA)
    s = (np.arange(n) + 0.5) * raio / n
    f = (np.arange(n) + 0.5) * 2 * np.pi / n
    S, F = np.meshgrid(s, f, indexing='ij')
    da = S * (raio / n) * (2 * np.pi / n)
    # normal do disco é +z, e a altura não entra no fluxo de um rotacional
    # constante, mas fica registrada para quem quiser conferir a geometria
    _ = altura
    return ROT[2] * np.sum(da)


def circulacao(n):
    """Circulação de v ao longo da borda da calota."""
    raio = RS * np.sin(ALFA)
    z0 = RS * np.cos(ALFA)
    f = (np.arange(n) + 0.5) * 2 * np.pi / n
    df = 2 * np.pi / n
    x, y = raio * np.cos(f), raio * np.sin(f)
    dx, dy = -raio * np.sin(f) * df, raio * np.cos(f) * df
    vx, vy, _ = campo_stokes(x, y, np.full_like(x, z0))
    return np.sum(vx * dx + vy * dy)


print()
print('TEOREMA DE STOKES, calota de meio ângulo %.0f graus' % np.degrees(ALFA))
print('    n     fluxo calota    fluxo disco     circulação')
for n in (20, 40, 80, 160):
    print('  %4d   %12.8f   %12.8f   %12.8f'
          % (n, fluxo_calota(n), fluxo_disco(n), circulacao(n)))
exato = np.pi * (RS * np.sin(ALFA)) ** 2
print('  previsto: a área projetada vezes a componente z do rotacional,')
print('  pi (R sen alfa)^2 = %.8f' % exato)

print()
print('convergência do fluxo pela calota:')
anterior = None
for n in (20, 40, 80, 160, 320):
    err = abs(fluxo_calota(n) - exato)
    linha = '  n = %4d : erro = %.3e' % (n, err)
    if anterior:
        linha += '   razão = %.2f' % (anterior / err)
    anterior = err
    print(linha)

# ------------------------------------------------------------------- figura
fig = plt.figure(figsize=(6.4, 5.2))
ax = fig.add_subplot(111, projection='3d')
t = np.linspace(0, ALFA, 40)
f = np.linspace(0, 2 * np.pi, 80)
T, F = np.meshgrid(t, f, indexing='ij')
ax.plot_surface(RS * np.sin(T) * np.cos(F), RS * np.sin(T) * np.sin(F),
                RS * np.cos(T), alpha=0.35, color='#b05a1f', linewidth=0)
raio = RS * np.sin(ALFA)
s = np.linspace(0, raio, 20)
S, F2 = np.meshgrid(s, f, indexing='ij')
ax.plot_surface(S * np.cos(F2), S * np.sin(F2),
                np.full_like(S, RS * np.cos(ALFA)), alpha=0.3, color='#2c6e63',
                linewidth=0)
ax.plot(raio * np.cos(f), raio * np.sin(f), RS * np.cos(ALFA), lw=2.5,
        color='#2b3240')
ax.set_title('Duas superfícies, a mesma borda, o mesmo fluxo', fontsize=11)
ax.set_box_aspect((1, 1, 0.8))
plt.show()
