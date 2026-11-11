# -*- coding: utf-8 -*-
"""A radiação de um dipolo oscilante, medida em vez de deduzida.

O QUE RESOLVE
    Monta os potenciais retardados EXATOS de uma antena curta (duas cargas
    oscilantes ligadas por um fio com corrente uniforme), obtém E e B por
    diferenças finitas, e integra o vetor de Poynting sobre esferas de vários
    raios. Compara com a potência média de Larmor para o dipolo,

        <P> = mu0 p0^2 omega^4 / (12 pi c).

    Nada da dedução analítica é usado no caminho: só as definições
    E = -grad V - dA/dt, B = rot A e S = E x B / mu0.

A FÍSICA
    Dos três pedaços do campo de um dipolo, o que cai com 1/r^3 (estático), o
    que cai com 1/r^2 (indução) e o que cai com 1/r (radiação), apenas o
    último sobrevive no infinito: a área da esfera cresce com r^2, de modo que
    só um campo que cai com 1/r mantém o fluxo constante. Perto da antena a
    energia vai e volta, sem se perder; longe dela, vai embora para sempre.

COMO CONFERIR SE ESTÁ CERTO
    1. A potência média que atravessa a esfera tem de ser a mesma para todos
       os raios na zona de radiação, e tem de bater com a fórmula de Larmor.
    2. O padrão angular tem de ser sen^2(theta): nulo no eixo da antena,
       máximo no plano equatorial.
    3. A média é a mesma em todo raio, inclusive na zona próxima, porque em
       regime estacionário a energia não se acumula em lugar nenhum. O que
       muda é a potência INSTANTÂNEA: perto da antena ela oscila com amplitude
       muito maior que a média, trocando energia de ida e volta; longe dela a
       oscilação fica da ordem da própria média, e o fluxo é sempre positivo.
    4. O campo na direção equatorial tem de passar de 1/r^3 (estático) para
       1/r (radiação) ao cruzar r ~ lambda.

Prof. Apiano Morais - LFCA/URCA - Eletromagnetismo III
"""

import numpy as np

C = 2.99792458e8
EPS0 = 8.8541878128e-12
MU0 = 1.0 / (EPS0 * C * C)

F = 100e6                     # frequencia, Hz
OMEGA = 2 * np.pi * F
LAMB = C / F                  # 3 m
D = 0.005 * LAMB              # antena curta: 0,5 % do comprimento de onda
Q0 = 1.0e-9                   # amplitude da carga, C
P0 = Q0 * D                   # momento de dipolo

NFIO = 161                    # pontos na integral ao longo do fio


def carga(t):
    return Q0 * np.cos(OMEGA * t)


def corrente(t):
    """I = dq/dt na carga de cima, com sinal tal que a carga de baixo perde."""
    return -Q0 * OMEGA * np.sin(OMEGA * t)


def potenciais(p, t):
    """V e A nos pontos p (n, 3), no instante t, por integração retardada."""
    zc = np.array([0.0, 0.0, D / 2])
    zb = np.array([0.0, 0.0, -D / 2])
    rc = np.linalg.norm(p - zc, axis=1)
    rb = np.linalg.norm(p - zb, axis=1)
    V = (carga(t - rc / C) / rc - carga(t - rb / C) / rb) / (4 * np.pi * EPS0)

    # o fio: corrente uniforme entre as duas cargas
    z = np.linspace(-D / 2, D / 2, NFIO)
    dz = z[1] - z[0]
    peso = np.full(NFIO, dz)
    peso[0] = peso[-1] = dz / 2                      # trapézio
    Az = np.zeros(p.shape[0])
    for zi, w in zip(z, peso):
        d = np.linalg.norm(p - np.array([0.0, 0.0, zi]), axis=1)
        Az += w * corrente(t - d / C) / d
    Az *= MU0 / (4 * np.pi)
    return V, Az


def campos(p, t, h=None, dt=None):
    """E e B por diferenças centrais a partir de V e A."""
    h = h if h is not None else LAMB / 4000
    dt = dt if dt is not None else 1.0 / (F * 4000)
    n = p.shape[0]
    gradV = np.zeros((n, 3))
    dAz = np.zeros((n, 3))                 # derivadas espaciais de Az
    for k in range(3):
        e = np.zeros(3)
        e[k] = h
        Vp, Ap = potenciais(p + e, t)
        Vm, Am = potenciais(p - e, t)
        gradV[:, k] = (Vp - Vm) / (2 * h)
        dAz[:, k] = (Ap - Am) / (2 * h)

    _, Af = potenciais(p, t + dt)
    _, Ai = potenciais(p, t - dt)
    dAdt = np.zeros((n, 3))
    dAdt[:, 2] = (Af - Ai) / (2 * dt)

    E = -gradV - dAdt
    # B = rot A, com A = Az z^:  Bx = dAz/dy, By = -dAz/dx, Bz = 0
    B = np.zeros((n, 3))
    B[:, 0] = dAz[:, 1]
    B[:, 1] = -dAz[:, 0]
    return E, B


def esfera(raio, n=40):
    """Pontos, normais e pesos de área (Gauss-Legendre em cos(theta))."""
    u, w = np.polynomial.legendre.leggauss(n)
    phi = np.linspace(0.0, 2 * np.pi, 2 * n, endpoint=False)
    dphi = 2 * np.pi / (2 * n)
    U, P = np.meshgrid(u, phi, indexing='ij')
    W, _ = np.meshgrid(w, phi, indexing='ij')
    sen = np.sqrt(1.0 - U ** 2)
    dirs = np.stack([sen * np.cos(P), sen * np.sin(P), U],
                    axis=-1).reshape(-1, 3)
    return raio * dirs, dirs, (raio ** 2 * W * dphi).reshape(-1), U.reshape(-1)


def potencia(raio, nt=24, n=40):
    """Série temporal da potência que atravessa a esfera de raio dado."""
    p, nrm, da, _ = esfera(raio, n)
    serie = []
    for i in range(nt):
        t = i / (nt * F)
        E, B = campos(p, t)
        S = np.cross(E, B) / MU0
        serie.append(np.sum(np.sum(S * nrm, axis=1) * da))
    return np.array(serie)


def fluxo_radial(raio, graus=90.0, nt=24):
    """Fluxo médio por unidade de área numa direção, e o campo elétrico."""
    th = np.radians(graus)
    p = np.array([[raio * np.sin(th), 0.0, raio * np.cos(th)]])
    nrm = p / raio
    soma, emax = 0.0, 0.0
    for i in range(nt):
        t = i / (nt * F)
        E, B = campos(p, t)
        soma += float(np.sum(np.cross(E, B) / MU0 * nrm))
        emax = max(emax, float(np.linalg.norm(E)))
    return soma / nt, emax


def main():
    larmor = MU0 * P0 ** 2 * OMEGA ** 4 / (12 * np.pi * C)
    print('antena curta: f = %.0f MHz, lambda = %.2f m, d = %.3f m'
          % (F / 1e6, LAMB, D))
    print('p0 = %.3e C.m        <P> de Larmor = %.6e W' % (P0, larmor))
    print()

    print('  r/lambda     <P> medida (W)    razao com Larmor    oscilacao/media')
    for k in (0.02, 0.1, 0.5, 1.0, 3.0, 10.0):
        serie = potencia(k * LAMB)
        P = serie.mean()
        osc = (serie.max() - serie.min()) / abs(P)
        print('  %7.2f      %+.6e        %8.4f          %10.2f'
              % (k, P, P / larmor, osc))
    print()
    print('A media e a mesma em todo raio, como tem de ser: em regime')
    print('estacionario a energia nao se acumula em lugar nenhum. O que muda')
    print('e a oscilacao: perto da antena o fluxo instantaneo vai e volta com')
    print('amplitude centenas de vezes maior que a media, e so longe dela a')
    print('potencia escoa de maneira firme. Isso e a diferenca entre campo')
    print('reativo e radiacao.')
    print()

    # ---------------------------------------------------- o padrão angular
    r = 5 * LAMB
    base, _ = fluxo_radial(r, 90.0)
    print('Padrao angular em r = 5 lambda, normalizado pelo equador:')
    print('  theta      medido/equador      sen^2(theta)      razao')
    for graus in (0, 15, 30, 45, 60, 75, 90):
        med, _ = fluxo_radial(r, graus)
        s2 = np.sin(np.radians(graus)) ** 2
        razao = '    ---' if graus == 0 else '%8.5f' % (med / base / s2)
        print('  %5d        %10.6f        %10.6f   %s'
              % (graus, med / base, s2, razao))
    print()

    # ------------------------------------------- do campo proximo ao distante
    print('Como o campo equatorial cai com a distancia:')
    print('  r/lambda      |E| max (V/m)      expoente local')
    ant = None
    for k in (0.02, 0.05, 0.1, 0.3, 1.0, 3.0, 10.0):
        _, e = fluxo_radial(k * LAMB, 90.0, nt=12)
        if ant is None:
            exp = '   ---'
        else:
            exp = '%6.2f' % (np.log(e / ant[1]) / np.log(k / ant[0]))
        print('  %8.2f      %.6e       %s' % (k, e, exp))
        ant = (k, e)
    print()
    print('O expoente passa de -3 (campo estatico do dipolo) a -1 (radiacao),')
    print('com a transicao em torno de um comprimento de onda.')


if __name__ == '__main__':
    main()
