# -*- coding: utf-8 -*-
"""Campo magnético de um circuito fechado qualquer, pela lei de Biot-Savart.

O QUE RESOLVE
    B(r) = (mu0 I / 4 pi) * integral( dl x r_hat / r^2 ), para um circuito
    descrito por uma lista de pontos. Funciona para espira circular, quadrada,
    retangular, helicoidal, bobina de Helmholtz ou qualquer curva que você
    souber parametrizar.

COMO CONFERIR SE ESTÁ CERTO
    1. Espira circular no eixo: compare com B = mu0 I R^2 / 2 (R^2 + z^2)^(3/2).
       O programa faz essa comparação e imprime o erro.
    2. O erro cai com o quadrado do número de segmentos: dobre n_seg e veja o
       erro cair por um fator quatro. Isso é a regra do trapézio em ação.
    3. Longe da espira, o campo tem de virar o de um dipolo, caindo com 1/z^3.

CUIDADO
    A integral diverge em cima do fio, onde r -> 0. O programa recusa pontos
    mais próximos do que meio segmento, em vez de devolver um número enorme
    sem sentido.

Prof. Apiano Morais - LFCA/URCA - Eletromagnetismo II
"""

import numpy as np
import matplotlib.pyplot as plt

MU0 = 4.0e-7 * np.pi


# ------------------------------------------------------------------ CIRCUITOS
def espira_circular(R=1.0, z0=0.0, n_seg=400):
    """Devolve os vértices de uma espira circular de raio R, no plano z = z0."""
    phi = np.linspace(0.0, 2.0 * np.pi, n_seg + 1)
    return np.column_stack([R * np.cos(phi), R * np.sin(phi),
                            np.full_like(phi, z0)])


def espira_quadrada(a=1.0, z0=0.0, n_lado=100):
    """Quadrado de lado a centrado na origem, no plano z = z0."""
    t = np.linspace(-a / 2, a / 2, n_lado + 1)
    um = np.full_like(t, a / 2)
    lados = [np.column_stack([t, -um, np.full_like(t, z0)]),
             np.column_stack([um, t, np.full_like(t, z0)]),
             np.column_stack([t[::-1], um, np.full_like(t, z0)]),
             np.column_stack([-um, t[::-1], np.full_like(t, z0)])]
    return np.vstack([lados[0]] + [l[1:] for l in lados[1:]])


# ------------------------------------------------------------------ O CÁLCULO
def campo(pontos, corrente, alvos):
    """Campo B nos pontos `alvos` produzido pelo circuito `pontos`.

    O circuito é uma poligonal fechada: cada segmento contribui com
    dl x r_hat / r^2, avaliado no ponto médio do segmento. Isso equivale à
    regra do ponto médio, cujo erro cai com o quadrado do comprimento do
    segmento.
    """
    alvos = np.atleast_2d(alvos)
    dl = pontos[1:] - pontos[:-1]                  # vetores dos segmentos
    meio = 0.5 * (pontos[1:] + pontos[:-1])        # pontos médios
    passo = np.linalg.norm(dl, axis=1).mean()

    B = np.zeros_like(alvos, dtype=float)
    for i, alvo in enumerate(alvos):
        rr = alvo - meio                           # do segmento ao alvo
        r = np.linalg.norm(rr, axis=1)
        if r.min() < 0.5 * passo:
            raise ValueError('ponto muito próximo do fio: a integral diverge '
                             'ali. Afaste o alvo ou refine o circuito.')
        integrando = np.cross(dl, rr) / r[:, None] ** 3
        B[i] = MU0 * corrente / (4.0 * np.pi) * integrando.sum(axis=0)
    return B


# ------------------------------------------------------------------ EXEMPLO
if __name__ == '__main__':
    I = 1.0
    R = 1.0
    espira = espira_circular(R=R, n_seg=400)

    z = np.linspace(0.05, 4.0, 160)
    alvos = np.column_stack([np.zeros_like(z), np.zeros_like(z), z])
    Bnum = campo(espira, I, alvos)[:, 2]
    Bexato = MU0 * I * R ** 2 / (2.0 * (R ** 2 + z ** 2) ** 1.5)

    erro = np.abs(Bnum - Bexato) / Bexato
    print('espira circular, 400 segmentos')
    print('  erro relativo máximo no eixo: %.2e' % erro.max())

    for n in (50, 100, 200, 400):
        e = campo(espira_circular(R=R, n_seg=n), I, [[0, 0, 0.5]])[0, 2]
        ex = MU0 * I * R ** 2 / (2.0 * (R ** 2 + 0.25) ** 1.5)
        print('  n = %3d  erro = %.3e' % (n, abs(e - ex) / ex))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.4))
    ax1.plot(z, Bexato * 1e6, lw=2.4, color='#1c2c60', label='analítico')
    ax1.plot(z[::6], Bnum[::6] * 1e6, 'o', ms=5, color='#a8181d',
             label='Biot-Savart numérico')
    ax1.set_xlabel('$z$ [m]'); ax1.set_ylabel(r'$B_z$ [$\mu$T]')
    ax1.set_title('campo no eixo da espira')
    ax1.legend(frameon=False)

    # o campo no plano que contém o eixo
    y = np.linspace(-2.2, 2.2, 41)
    zz = np.linspace(-2.2, 2.2, 41)
    Y, Z = np.meshgrid(y, zz)
    alvos2 = np.column_stack([np.zeros(Y.size), Y.ravel(), Z.ravel()])
    dist = np.hypot(np.abs(Y.ravel()) - R, Z.ravel())
    bons = dist > 0.18
    By = np.zeros(Y.size); Bz = np.zeros(Y.size)
    Bf = campo(espira, I, alvos2[bons])
    By[bons] = Bf[:, 1]; Bz[bons] = Bf[:, 2]
    ax2.streamplot(Y, Z, By.reshape(Y.shape), Bz.reshape(Y.shape),
                   color='#1c2c60', density=1.1, linewidth=0.9,
                   arrowsize=0.9)
    ax2.plot([-R, R], [0, 0], 'o', color='#a8181d', ms=8)
    ax2.set_xlabel('$y$ [m]'); ax2.set_ylabel('$z$ [m]')
    ax2.set_title('linhas de campo da espira')
    ax2.set_aspect('equal')

    fig.tight_layout()
    plt.show()
