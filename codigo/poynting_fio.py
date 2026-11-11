# -*- coding: utf-8 -*-
"""Por onde entra a energia que aquece um fio.

O QUE RESOLVE
    Monta os campos E e B em volta de um fio cilíndrico com corrente contínua,
    integra o vetor de Poynting sobre superfícies cilíndricas de vários raios
    e compara o fluxo com a potência dissipada, I^2 R.

A FÍSICA
    A energia que aquece o fio não viaja dentro dele, empurrada pelos elétrons.
    Ela viaja no campo, no espaço em volta, e entra radialmente pela superfície
    lateral. O fio é um sorvedouro, não um cano. Essa leitura, que parece
    apenas filosófica num fio de cobre com corrente contínua, é o que explica
    por que um guia de onda oco funciona sem condutor central e por que, em
    alta frequência, a qualidade do dielétrico importa mais que a do cobre.

COMO CONFERIR SE ESTÁ CERTO
    1. O fluxo para dentro tem de dar exatamente I^2 R, com erro só de
       integração numérica.
    2. O resultado não pode depender do raio da superfície escolhida, desde
       que ela envolva o fio: fora dele não há dissipação, e o que entra por
       uma superfície sai pela de dentro.
    3. S tem de apontar para dentro em todos os pontos: o produto E x B, com E
       ao longo do fio e B em volta dele, é radial e negativo.
    4. Dentro do fio, o fluxo através de um cilindro de raio s < a tem de dar a
       potência dissipada apenas no miolo, que vai com s^2.

Prof. Apiano Morais - LFCA/URCA - Eletromagnetismo III
"""

import numpy as np

MU0 = 4 * np.pi * 1e-7

A = 1.0e-3            # raio do fio, m
L = 1.0               # comprimento, m
I = 10.0              # corrente, A
RHO = 1.68e-8         # resistividade do cobre, ohm.m


def resistencia():
    return RHO * L / (np.pi * A * A)


def campos(s):
    """E (longitudinal) e B (azimutal) a uma distancia s do eixo.

    Dentro do condutor a corrente e uniforme, de modo que B cresce com s; o
    campo eletrico e o mesmo dentro e fora da superficie, porque e a queda de
    tensao dividida pelo comprimento.
    """
    E = I * resistencia() / L
    B = np.where(s < A,
                 MU0 * I * s / (2 * np.pi * A * A),
                 MU0 * I / (2 * np.pi * np.maximum(s, 1e-30)))
    return E, B


def fluxo(s, n=20000):
    """Potencia que ENTRA por um cilindro de raio s e comprimento L.

    Integra numericamente sobre a superficie, em vez de usar a simetria, para
    que o resultado nao seja uma tautologia: a malha cobre phi e z.
    """
    phi = np.linspace(0.0, 2 * np.pi, n, endpoint=False)
    z = np.linspace(0.0, L, 200, endpoint=False)
    dphi = phi[1] - phi[0]
    dz = z[1] - z[0]
    E, B = campos(np.array([s]))
    S = E * B[0] / MU0                 # modulo; o sentido e para dentro
    da = s * dphi * dz
    return S * da * len(phi) * len(z)


def dissipada_ate(s):
    """Potencia dissipada no material contido dentro do raio s."""
    s = min(s, A)
    fracao = (s / A) ** 2              # fracao da corrente, e da secao
    j = I / (np.pi * A * A)
    return RHO * j * j * (np.pi * s * s * L)


def main():
    R = resistencia()
    E, B = campos(np.array([A]))
    print('fio de cobre: a = %.1f mm, L = %.2f m, I = %.1f A' % (A * 1e3, L, I))
    print('R = %.3f mohm     I^2 R = %.4f W' % (R * 1e3, I * I * R))
    print('na superficie: E = %.4e V/m   B = %.4e T   S = %.2f W/m^2'
          % (E, B[0], E * B[0] / MU0))
    print()

    print('  s (mm)    fluxo para dentro (W)     esperado (W)      erro')
    for s in [0.25e-3, 0.5e-3, A, 2 * A, 10 * A, 1.0]:
        f = fluxo(s)
        esp = dissipada_ate(s) if s < A else I * I * R
        print('  %7.3f        %12.6f        %12.6f     %8.1e'
              % (s * 1e3, f, esp, abs(f - esp) / esp))

    print()
    print('Fora do fio o fluxo nao depende do raio: toda a energia que entra')
    print('por uma superficie larga atravessa a estreita e cai no condutor.')
    print('Dentro, o fluxo acompanha a dissipacao do miolo, que vai com s^2.')


if __name__ == '__main__':
    main()
