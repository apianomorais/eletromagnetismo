# -*- coding: utf-8 -*-
"""Espalhamento Thomson, e por que o céu é azul.

O QUE RESOLVE
    Usa a fórmula de Larmor para calcular duas seções de choque:

    1. Thomson: um elétron LIVRE, sacudido por uma onda, irradia; a razão
       entre a potência irradiada e a intensidade incidente é uma área.
    2. Rayleigh: um elétron LIGADO, muito abaixo da frequência de ressonância,
       responde com amplitude proporcional a omega^2, e a potência irradiada
       passa a crescer com omega^4. Daí o azul do céu.

    Depois aplica o resultado à atmosfera, usando o índice de refração do ar
    para obter a seção de choque das moléculas, e calcula a transmissão em
    várias cores ao meio-dia e no poente.

A FÍSICA
    Nos dois casos a radiação espalhada é a radiação de dipolo do capítulo:
    a onda incidente acelera a carga, e a carga acelerada irradia. O que muda
    é só a amplitude da aceleração. A dependência com omega^4 é o motivo de o
    céu ser azul, de o Sol poente ser vermelho e de a luz do céu ser
    polarizada a 90 graus do Sol.

COMO CONFERIR SE ESTÁ CERTO
    1. A seção de choque de Thomson calculada pela potência tem de dar
       6,652e-29 m^2, independente da intensidade e da frequência usadas.
    2. A seção de choque de Rayleigh calculada a partir do índice de refração
       do ar tem de reproduzir a profundidade óptica medida da atmosfera,
       em torno de 0,2 no azul e 0,05 no vermelho.
    3. O expoente medido da dependência com o comprimento de onda tem de dar
       -4,00.

Prof. Apiano Morais - LFCA/URCA - Eletromagnetismo III
"""

import numpy as np

C = 2.99792458e8
EPS0 = 8.8541878128e-12
MU0 = 1.0 / (EPS0 * C * C)
E_C = 1.602176634e-19
ME = 9.1093837015e-31

# atmosfera
N_AR = 2.546899e25            # moléculas por m^3 nas condições normais
COLUNA = 2.15e29              # moléculas por m^2 numa atmosfera vertical


def thomson_pela_potencia(I, lamb):
    """Seção de choque de Thomson, obtida de Larmor, sem usar a fórmula."""
    E0 = np.sqrt(2 * I / (C * EPS0))          # amplitude do campo incidente
    a0 = E_C * E0 / ME                        # amplitude da aceleração
    P = MU0 * E_C ** 2 * (a0 ** 2 / 2) / (6 * np.pi * C)   # media: <a^2> = a0^2/2
    return P / I


def raio_classico():
    return E_C ** 2 / (4 * np.pi * EPS0 * ME * C ** 2)


def indice_do_ar(lamb_um):
    """Índice de refração do ar (fórmula de Ciddor simplificada, seca, 15 C)."""
    s2 = 1.0 / lamb_um ** 2
    n_menos_1 = (5792105.0 / (238.0185 - s2) + 167917.0 / (57.362 - s2)) * 1e-8
    return 1.0 + n_menos_1


def rayleigh_molecular(lamb):
    """Seção de choque por molécula de ar, a partir do índice de refração."""
    n = indice_do_ar(lamb * 1e6)
    fator = (n ** 2 - 1) / (n ** 2 + 2)
    return 24 * np.pi ** 3 * fator ** 2 / (lamb ** 4 * N_AR ** 2)


def main():
    print('ESPALHAMENTO THOMSON')
    re = raio_classico()
    sigma_T = 8 * np.pi / 3 * re ** 2
    print('  raio classico do eletron   r_e = %.6e m' % re)
    print('  (8 pi / 3) r_e^2               = %.6e m^2' % sigma_T)
    print()
    print('  mesma secao, obtida da potencia irradiada:')
    print('    I (W/m^2)    lambda (nm)      sigma (m^2)        razao')
    for I in (1e2, 1e6, 1e12):
        for lamb in (500e-9, 1e-10):
            s = thomson_pela_potencia(I, lamb)
            print('    %9.0e      %8.3f      %.6e      %.6f'
                  % (I, lamb * 1e9, s, s / sigma_T))
    print()
    print('A secao nao depende nem da intensidade nem da frequencia: o eletron')
    print('livre espalha tudo igualmente. Isso vale enquanto a energia do foton')
    print('for muito menor que m c^2 = 511 keV; acima disso o recuo do eletron')
    print('entra na conta e o resultado vira a formula de Klein-Nishina.')
    print()

    print('ESPALHAMENTO RAYLEIGH NA ATMOSFERA')
    print('  cor                 n - 1       sigma (m^2)    prof. optica  transmissao')
    cores = [('violeta', 400e-9), ('azul', 450e-9), ('verde', 550e-9),
             ('amarelo', 580e-9), ('vermelho', 650e-9), ('IV proximo', 800e-9)]
    taus = {}
    for nome, lamb in cores:
        s = rayleigh_molecular(lamb)
        tau = s * COLUNA
        taus[nome] = tau
        print('  %-11s %4.0f nm   %.3e   %.4e      %7.4f      %7.4f'
              % (nome, lamb * 1e9, indice_do_ar(lamb * 1e6) - 1,
                 s, tau, np.exp(-tau)))
    print()
    print('  medida real da profundidade optica de Rayleigh: 0,23 no azul e')
    print('  0,05 no vermelho, ao nivel do mar. A conta acima usa apenas o')
    print('  indice de refracao do ar e a densidade de moleculas.')
    print()

    # ------------------------------------------------------- o expoente
    print('  EXPOENTE DA DEPENDENCIA COM O COMPRIMENTO DE ONDA')
    ant = None
    for lamb in (400e-9, 500e-9, 600e-9, 700e-9, 800e-9):
        s = rayleigh_molecular(lamb)
        if ant is not None:
            exp = np.log(s / ant[1]) / np.log(lamb / ant[0])
            print('    %4.0f nm    sigma = %.4e    expoente local = %6.3f'
                  % (lamb * 1e9, s, exp))
        else:
            print('    %4.0f nm    sigma = %.4e' % (lamb * 1e9, s))
        ant = (lamb, s)
    print()
    print('  O expoente fica um pouco alem de -4 porque o indice de refracao')
    print('  do ar tambem depende da cor: a dispersao reforca o efeito.')
    print()

    # ------------------------------------------------------- o poente
    print('O POENTE')
    print('  no horizonte a luz atravessa cerca de 38 atmosferas')
    print('  cor          meio-dia     poente       razao poente/meio-dia')
    for nome, lamb in cores:
        tau = rayleigh_molecular(lamb) * COLUNA
        meio, poente = np.exp(-tau), np.exp(-38 * tau)
        print('  %-10s   %7.4f     %.3e        %.2e'
              % (nome, meio, poente, poente / meio))
    print()
    razao = (np.exp(-38 * rayleigh_molecular(650e-9) * COLUNA)
             / np.exp(-38 * rayleigh_molecular(450e-9) * COLUNA))
    print('  No poente chega %.0f vezes mais vermelho que azul: o Sol fica' % razao)
    print('  laranja nao porque ganhe vermelho, e sim porque perde o resto.')


if __name__ == '__main__':
    main()
