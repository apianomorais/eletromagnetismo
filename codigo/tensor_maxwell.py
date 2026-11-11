# -*- coding: utf-8 -*-
"""A força entre duas cargas, sem usar a lei de Coulomb.

O QUE RESOLVE
    Calcula a força sobre uma carga pontual integrando o tensor de tensões de
    Maxwell sobre uma superfície fechada que a envolve:

        F_i = integral de T_ij n_j da,
        T_ij = eps0 (E_i E_j - delta_ij E^2 / 2).

    O campo E na superfície é a soma dos campos das duas cargas. A lei de
    Coulomb só aparece no fim, para conferir.

A FÍSICA
    O tensor de tensões transforma uma força num fluxo pela fronteira: não é
    preciso saber o que há dentro da superfície, basta medir o campo nela. É o
    mesmo raciocínio usado para calcular a força num fluido pela pressão nas
    paredes, e é o que torna possível falar de momento guardado no campo.

COMO CONFERIR SE ESTÁ CERTO
    1. O resultado tem de reproduzir Coulomb, com erro só de quadratura.
    2. O resultado tem de ser o MESMO para superfícies de formas e tamanhos
       diferentes (esfera, cubo, esfera deslocada), desde que envolvam a mesma
       carga e nenhuma outra. Isso é o conteúdo do teorema, e é a verificação
       que importa.
    3. As componentes x e y têm de dar zero, por simetria em torno do eixo.
    4. Refinando a malha, o erro cai depressa na esfera (o integrando é suave)
       e mais devagar no cubo (as quinas).

Prof. Apiano Morais - LFCA/URCA - Eletromagnetismo III
"""

import numpy as np

EPS0 = 8.8541878128e-12
K = 1.0 / (4 * np.pi * EPS0)

Q1 = 1.0e-9           # carga envolvida pela superficie, na origem
Q2 = -2.0e-9          # a outra carga, em z = D
D = 0.10              # separacao, m


def campo(p):
    """Campo das duas cargas num conjunto de pontos p, de forma (n, 3)."""
    E = np.zeros_like(p)
    for q, centro in ((Q1, np.array([0.0, 0.0, 0.0])),
                      (Q2, np.array([0.0, 0.0, D]))):
        r = p - centro
        d = np.linalg.norm(r, axis=1)[:, None]
        E += K * q * r / d ** 3
    return E


def forca(p, n, da):
    """Integra T.da sobre os pontos p, com normais n e elementos de area da."""
    E = campo(p)
    En = np.sum(E * n, axis=1)
    E2 = np.sum(E * E, axis=1)
    # T_ij n_j = eps0 ( E_i (E.n) - n_i E^2 / 2 )
    t = EPS0 * (E * En[:, None] - 0.5 * n * E2[:, None])
    return np.sum(t * da[:, None], axis=0)


# ---------------------------------------------------- superficies de teste
def esfera(raio, centro=(0.0, 0.0, 0.0), n=120):
    """Esfera, com Gauss-Legendre em cos(theta) e trapezio em phi."""
    u, w = np.polynomial.legendre.leggauss(n)        # u = cos(theta)
    phi = np.linspace(0.0, 2 * np.pi, 2 * n, endpoint=False)
    dphi = 2 * np.pi / (2 * n)
    U, P = np.meshgrid(u, phi, indexing='ij')
    W, _ = np.meshgrid(w, phi, indexing='ij')
    sen = np.sqrt(1.0 - U ** 2)
    dir = np.stack([sen * np.cos(P), sen * np.sin(P), U], axis=-1).reshape(-1, 3)
    pontos = np.array(centro) + raio * dir
    da = (raio ** 2 * W * dphi).reshape(-1)
    return pontos, dir, da


def cubo(meio, n=160):
    """Cubo de semilado 'meio' centrado na origem, com ponto medio por face."""
    t = (np.arange(n) + 0.5) / n * (2 * meio) - meio
    A, B = np.meshgrid(t, t, indexing='ij')
    A = A.reshape(-1)
    B = B.reshape(-1)
    passo = (2 * meio / n) ** 2
    pontos, normais = [], []
    for eixo in range(3):
        for sinal in (-1.0, 1.0):
            p = np.zeros((A.size, 3))
            outros = [i for i in range(3) if i != eixo]
            p[:, eixo] = sinal * meio
            p[:, outros[0]] = A
            p[:, outros[1]] = B
            nrm = np.zeros((A.size, 3))
            nrm[:, eixo] = sinal
            pontos.append(p)
            normais.append(nrm)
    pontos = np.concatenate(pontos)
    normais = np.concatenate(normais)
    da = np.full(pontos.shape[0], passo)
    return pontos, normais, da


def main():
    coulomb = K * Q1 * Q2 / D ** 2
    # vetor unitario de q2 para q1 e -z, de modo que a forca sobre q1 e:
    fz_exato = -coulomb
    print('q1 = %+.1f nC na origem, q2 = %+.1f nC em z = %.2f m'
          % (Q1 * 1e9, Q2 * 1e9, D))
    print('Coulomb: F_z sobre q1 = %+.6e N' % fz_exato)
    print()

    print('  superficie                        F_x         F_y         F_z        erro')
    testes = [
        ('esfera  R = 1 cm      ', esfera(0.01)),
        ('esfera  R = 3 cm      ', esfera(0.03)),
        ('esfera  R = 4,9 cm    ', esfera(0.049)),
        ('esfera  R = 2 cm, desl', esfera(0.02, centro=(0.005, 0.0, -0.01))),
        ('cubo    semilado 1 cm ', cubo(0.01)),
        ('cubo    semilado 4 cm ', cubo(0.04)),
    ]
    for nome, (p, n, da) in testes:
        F = forca(p, n, da)
        erro = abs(F[2] - fz_exato) / abs(fz_exato)
        print('  %s  %+9.2e  %+9.2e  %+.6e   %7.1e'
              % (nome, F[0], F[1], F[2], erro))

    print()
    print('Nenhuma dessas contas usou a lei de Coulomb para a forca: todas')
    print('mediram o campo na fronteira e somaram tensoes. A superficie pode')
    print('ter qualquer forma, desde que envolva q1 e deixe q2 de fora.')
    print()
    print('Convergencia no cubo (as quinas atrapalham):')
    for n in (40, 80, 160, 320):
        F = forca(*cubo(0.01, n=n))
        print('   n = %4d por face   F_z = %+.6e   erro = %7.1e'
              % (n, F[2], abs(F[2] - fz_exato) / abs(fz_exato)))


if __name__ == '__main__':
    main()
