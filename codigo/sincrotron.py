# -*- coding: utf-8 -*-
"""Quanto um acelerador perde irradiando.

O QUE RESOLVE
    Aplica a fórmula de Liénard (a versão relativística de Larmor) ao
    movimento circular e calcula a energia perdida por volta num anel de raio
    dado. Compara elétrons e prótons, reproduz a regra prática dos
    projetistas de aceleradores e mede o expoente com que a perda cresce com
    a energia.

A FÍSICA
    A potência irradiada por uma carga acelerada ganha, no caso relativístico,
    um fator gamma^6 (ou gamma^4, quando a aceleração é perpendicular à
    velocidade, que é o caso do movimento circular). Como gamma = E/mc^2, a
    perda por volta cresce com a QUARTA potência da energia e com a QUARTA
    potência inversa da massa. É por isso que o LEP, com elétrons, chegou ao
    seu limite em 104 GeV, e por que o mesmo túnel, com prótons, hospeda hoje
    o LHC a 7 TeV.

COMO CONFERIR SE ESTÁ CERTO
    1. A conta direta tem de reproduzir a regra prática
       Delta E [keV] = 88,46 E^4 [GeV] / rho [m], usada na engenharia de
       aceleradores de elétrons.
    2. O expoente medido da dependência com a energia tem de dar 4,00.
    3. A razão entre próton e elétron, na mesma energia e no mesmo anel, tem
       de ser (m_e/m_p)^4 = 8,8e-14.
    4. No limite não relativístico, a fórmula de Liénard tem de voltar à de
       Larmor: o teste final faz esse limite numericamente.

Prof. Apiano Morais - LFCA/URCA - Eletromagnetismo III
"""

import numpy as np

C = 2.99792458e8
EPS0 = 8.8541878128e-12
MU0 = 1.0 / (EPS0 * C * C)
E_C = 1.602176634e-19                 # carga elementar, C
ME = 9.1093837015e-31
MP = 1.67262192369e-27


def gama(energia_J, massa):
    """gamma a partir da energia TOTAL da partícula."""
    return energia_J / (massa * C * C)


def potencia_circular(q, massa, energia_J, raio):
    """Liénard para a + perpendicular a v: P = q^2 gamma^4 a^2 / (6 pi eps0 c^3).

    A aceleração própria do movimento circular é v^2/rho; o fator gamma^4 vem
    de a_perp entrar com gamma^4 na fórmula de Liénard.
    """
    g = gama(energia_J, massa)
    beta = np.sqrt(1.0 - 1.0 / g ** 2)
    v = beta * C
    a = v * v / raio
    return q * q * g ** 4 * a * a / (6 * np.pi * EPS0 * C ** 3)


def perda_por_volta(q, massa, energia_J, raio):
    """Energia perdida numa volta completa, em joules."""
    g = gama(energia_J, massa)
    beta = np.sqrt(1.0 - 1.0 / g ** 2)
    periodo = 2 * np.pi * raio / (beta * C)
    return potencia_circular(q, massa, energia_J, raio) * periodo


def larmor(q, a):
    return MU0 * q * q * a * a / (6 * np.pi * C)


GeV = 1e9 * E_C


def main():
    print('ENERGIA PERDIDA POR VOLTA')
    print()
    casos = [
        ('LEP-1   eletron    45,6 GeV', E_C, ME, 45.6, 3096.0),
        ('LEP-2   eletron   104,5 GeV', E_C, ME, 104.5, 3096.0),
        ('LHC     proton    7000  GeV', E_C, MP, 7000.0, 2803.95),
        ('Sirius  eletron     3,0 GeV', E_C, ME, 3.0, 29.0),
    ]
    print('  maquina                        perda/volta      regra 88,46 E^4/rho')
    for nome, q, m, egev, rho in casos:
        dE = perda_por_volta(q, m, egev * GeV, rho)
        dE_keV = dE / E_C / 1e3
        regra = 88.46 * egev ** 4 / rho if m == ME else float('nan')
        if np.isnan(regra):
            print('  %s    %12.4g keV        (regra so vale para eletrons)'
                  % (nome, dE_keV))
        else:
            print('  %s    %12.4g keV        %12.4g keV   (%.4f)'
                  % (nome, dE_keV, regra, dE_keV / regra))
    print()
    print('Para o LHC a perda e de alguns keV por volta, mas com 2808 pacotes')
    print('de 1,15e11 protons ela vira alguns quilowatts que precisam ser')
    print('retirados do criostato a 1,9 K: la, o problema nao e a energia')
    print('perdida pelo feixe, e a carga termica sobre o helio superfluido.')
    print()

    # ------------------------------------------------- expoente com a energia
    print('EXPOENTE DA DEPENDENCIA COM A ENERGIA (eletron, rho = 3096 m)')
    ant = None
    for egev in (10.0, 20.0, 40.0, 80.0, 160.0):
        dE = perda_por_volta(E_C, ME, egev * GeV, 3096.0)
        if ant is None:
            print('  E = %6.1f GeV    perda = %12.4e J' % (egev, dE))
        else:
            exp = np.log(dE / ant[1]) / np.log(egev / ant[0])
            print('  E = %6.1f GeV    perda = %12.4e J    expoente = %.4f'
                  % (egev, dE, exp))
        ant = (egev, dE)
    print()

    # ------------------------------------------------- a razao proton/eletron
    razao = (perda_por_volta(E_C, MP, 100 * GeV, 3096.0)
             / perda_por_volta(E_C, ME, 100 * GeV, 3096.0))
    print('RAZAO PROTON/ELETRON a 100 GeV no mesmo anel')
    print('  medida      = %.4e' % razao)
    print('  (m_e/m_p)^4 = %.4e' % (ME / MP) ** 4)
    print()

    # ------------------------------------------------- o limite nao relativistico
    print('LIMITE NAO RELATIVISTICO (Lienard tem de virar Larmor)')
    print('  v/c          Lienard/Larmor')
    for beta in (1e-4, 1e-3, 1e-2, 1e-1, 0.5):
        g = 1.0 / np.sqrt(1.0 - beta ** 2)
        energia = g * ME * C * C
        rho = 1.0
        a = (beta * C) ** 2 / rho
        print('  %.0e        %.8f'
              % (beta, potencia_circular(E_C, ME, energia, rho)
                 / larmor(E_C, a)))
    print()
    print('A razao tende a 1 quando beta tende a zero, e vale exatamente')
    print('gamma^4 em qualquer velocidade: e esse fator que torna a radiacao')
    print('de sincrotron, ao mesmo tempo, o limite dos colisores de eletrons')
    print('e a melhor fonte de raios X que existe.')


if __name__ == '__main__':
    main()
