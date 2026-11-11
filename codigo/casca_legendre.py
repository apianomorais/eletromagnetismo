# -*- coding: utf-8 -*-
"""A casca girante pela expansão em polinômios de Legendre, conferida numericamente.

O QUE RESOLVE
    O potencial vetor de uma casca esférica de raio R, carga superficial sigma,
    girando com velocidade angular omega. A conta analítica usa a expansão

        1/|r - r'| = soma_l  (r_< ^l / r_> ^(l+1)) P_l(cos theta'),

    e o resultado é que SÓ o termo l = 1 sobrevive, o que dá

        A_phi = (mu0 sigma omega R / 3) r sen(theta),          r <= R
        A_phi = (mu0 sigma omega R^4 / 3) sen(theta) / r^2,    r >= R.

    O programa confere isso de três maneiras independentes.

A FÍSICA
    A corrente de superfície é K = sigma omega R sen(theta') phi', e a dependência
    em sen(theta') é exatamente a de um dipolo puro. Por isso a série colapsa:
    a integral angular projeta a fonte sobre P_1 e todos os outros coeficientes
    se anulam. Fora da casca não há quadrupolo, nem octupolo, nem nada.

COMO CONFERIR SE ESTÁ CERTO
    1. Os coeficientes c_l = integral de cos(theta') P_l(cos theta') têm de ser
       nulos para todo l diferente de 1, e valer 2/3 para l = 1.
    2. A integral de superfície feita por força bruta, sem nenhuma expansão,
       tem de reproduzir a fórmula fechada em pontos dentro e fora.
    3. O rotacional numérico de A tem de dar o campo uniforme (2/3) mu0 sigma
       omega R no interior, e um dipolo de momento (4/3) pi sigma omega R^4
       no exterior.

Prof. Apiano Morais - LFCA/URCA - Eletromagnetismo II
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import legendre as leg

MU0 = 4.0e-7 * np.pi

R = 0.10          # raio da casca, em metros
SIGMA = 1.0e-6    # densidade superficial de carga, em C/m^2
OMEGA = 50.0      # velocidade angular, em rad/s


def analitico(r, tet):
    """A_phi(r, theta) pela fórmula fechada, dentro e fora."""
    fora = MU0 * SIGMA * OMEGA * R ** 4 / 3.0 * np.sin(tet) / r ** 2
    dentro = MU0 * SIGMA * OMEGA * R / 3.0 * r * np.sin(tet)
    return np.where(r <= R, dentro, fora)


def forca_bruta(r, tet, nt=800, nf=800):
    """A_phi por integração direta da superfície, sem expansão nenhuma.

    O ponto de observação é posto no plano xz, onde phi^ coincide com y^, de
    modo que basta acumular a componente y do integrando.
    """
    # ponto de observação
    px, pz = r * np.sin(tet), r * np.cos(tet)
    t = (np.arange(nt) + 0.5) * np.pi / nt
    f = (np.arange(nf) + 0.5) * 2 * np.pi / nf
    tt, ff = np.meshgrid(t, f, indexing='ij')

    # pontos da casca e a corrente de superfície K = sigma (omega x r')
    x = R * np.sin(tt) * np.cos(ff)
    y = R * np.sin(tt) * np.sin(ff)
    z = R * np.cos(tt)
    kx = -SIGMA * OMEGA * y          # omega z^ x r' = omega (-y, x, 0)
    ky = SIGMA * OMEGA * x

    dist = np.sqrt((px - x) ** 2 + y ** 2 + (pz - z) ** 2)
    da = R ** 2 * np.sin(tt) * (np.pi / nt) * (2 * np.pi / nf)
    # só a componente y sobrevive à integração, e ela é a componente phi
    return MU0 / (4 * np.pi) * np.sum(ky / dist * da)


# --------------------------------------- 1. a série colapsa no termo de dipolo
print('coeficientes da fonte na base de Legendre:')
print('  c_l = (2l+1)/2 * integral de cos(t) P_l(cos t) d(cos t)')
u = np.linspace(-1, 1, 20001)
for l in range(7):
    c = np.zeros(l + 1)
    c[l] = 1.0
    pl = leg.legval(u, c)
    integral = np.trapezoid(u * pl, u) * (2 * l + 1) / 2
    print('    l = %d : %+.6f' % (l, integral))
print('  só l = 1 sobrevive, e é por isso que o campo externo é dipolo puro')

# ------------------------------- 2. a fórmula fechada contra a integral bruta
print()
print('A_phi: fórmula fechada contra integração direta da superfície')
print('     r/R    theta       fechada        bruta        erro relativo')
for rr, tet in ((0.4 * R, np.pi / 2), (0.7 * R, np.pi / 3),
                (1.5 * R, np.pi / 2), (3.0 * R, np.pi / 4)):
    a1 = analitico(np.array(rr), tet)
    a2 = forca_bruta(rr, tet)
    print('   %6.2f   %5.2f   %12.6e  %12.6e    %.2e'
          % (rr / R, tet, a1, a2, abs(a1 - a2) / abs(a1)))

# --------------------------------- 3. o campo, pelo rotacional de A em esféricas
def campo(r, tet, h=1e-4):
    """B = rot A, em esféricas, com A só na componente phi."""
    def a(rr, tt):
        return analitico(np.array(rr), tt)
    br = (a(r, tet + h) * np.sin(tet + h) - a(r, tet - h) * np.sin(tet - h))
    br = br / (r * np.sin(tet) * 2 * h)
    bt = -((r + h) * a(r + h, tet) - (r - h) * a(r - h, tet)) / (r * 2 * h)
    return br, bt


b_previsto = 2.0 / 3.0 * MU0 * SIGMA * OMEGA * R
print()
print('campo interno, previsto (2/3) mu0 sigma omega R = %.6e T' % b_previsto)
for rr, tet in ((0.3 * R, 0.7), (0.6 * R, 1.9), (0.9 * R, 2.6)):
    br, bt = campo(rr, tet)
    bz = br * np.cos(tet) - bt * np.sin(tet)
    bx = br * np.sin(tet) + bt * np.cos(tet)
    print('  em r = %.2f R, theta = %.2f : Bz = %.6e,  Bx = %+.2e,  erro = %.1e'
          % (rr / R, tet, bz, bx, abs(bz - b_previsto) / b_previsto))

m = 4.0 / 3.0 * np.pi * SIGMA * OMEGA * R ** 4
print()
print('momento de dipolo previsto m = (4/3) pi sigma omega R^4 = %.4e A m^2' % m)
for rr in (2.0 * R, 4.0 * R, 8.0 * R):
    br, _ = campo(rr, 0.3)
    br_dip = MU0 * m * 2 * np.cos(0.3) / (4 * np.pi * rr ** 3)
    print('  em r = %.0f R : B_r = %.4e,  dipolo = %.4e,  razão = %.6f'
          % (rr / R, br, br_dip, br / br_dip))

# ------------------------------------------------------------------- figura
r = np.linspace(0.02 * R, 4 * R, 400)
fig, eixo = plt.subplots(figsize=(7.2, 4.4))
eixo.plot(r / R, analitico(r, np.pi / 2) * 1e12, lw=2, label='série (só l = 1)')
pontos = np.linspace(0.1 * R, 4 * R, 14)
eixo.plot(pontos / R, [forca_bruta(x, np.pi / 2) * 1e12 for x in pontos],
          'o', ms=5, label='integração direta')
eixo.axvline(1.0, ls='--', lw=1)
eixo.set_xlabel('r / R')
eixo.set_ylabel('A_phi no equador (pT m)')
eixo.set_title('Potencial vetor da casca girante')
eixo.legend(frameon=False)
fig.tight_layout()
plt.show()
