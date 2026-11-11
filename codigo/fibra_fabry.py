# -*- coding: utf-8 -*-
"""A fibra monomodo e o filtro Fabry-Perot, com as contas que o capítulo 9 faz.

O QUE RESOLVE
    Duas coisas, nos dois extremos do capítulo:

    (1) a fibra: calcula o número V, resolve numericamente a equação
        transcendental dos modos de um guia dielétrico plano e conta quantos
        modos sobrevivem em cada comprimento de onda;

    (2) o Fabry-Perot: monta a função de Airy, mede o intervalo espectral
        livre, a finesse e a largura dos picos direto da curva, e compara com
        as fórmulas.

A FÍSICA
    Os dois são problemas de autovalor, e é por isso que estão no mesmo
    arquivo. Na fibra, o casamento entre a oscilação no núcleo e o decaimento
    na casca só é possível para certos beta; no Fabry-Perot, a interferência
    das infinitas idas e voltas só é construtiva para certas frequências.

COMO CONFERIR SE ESTÁ CERTO
    1. A fibra plana tem de ser monomodo quando V < pi/2 (no caso plano) e a
       fibra cilíndrica quando V < 2,405; o programa conta os modos e mostra
       isso acontecendo.
    2. O número de modos a V grande tem de se aproximar de V/(pi/2) no caso
       plano.
    3. O FSR medido na curva de Airy tem de dar c/2nL, e a finesse medida tem
       de dar pi raiz(R)/(1-R).

Prof. Apiano Morais - LFCA/URCA - Eletromagnetismo III
"""

import numpy as np
from scipy.optimize import brentq

C = 2.99792458e8

# ===================================================================== fibra
A_NUCLEO = 4.1e-6
N1, N2 = 1.4504, 1.4447
NA = np.sqrt(N1 ** 2 - N2 ** 2)


def numero_v(lam, a=A_NUCLEO):
    return 2 * np.pi * a / lam * NA


def modos_guia_plano(V):
    """Raízes de tan(u) = sqrt(V^2 - u^2)/u, os modos pares do guia plano.

    É a versão unidimensional do problema da fibra: dentro, oscilação com
    número de onda transversal u; fora, decaimento. A equação sai de casar as
    duas soluções e as suas derivadas na interface.
    """
    raizes = []
    m = 0
    while True:
        lo = m * np.pi + 1e-9
        hi = min((m + 0.5) * np.pi - 1e-9, V - 1e-12)
        if lo >= hi:
            break

        def f(u):
            return np.tan(u) - np.sqrt(max(V ** 2 - u ** 2, 0.0)) / u

        if f(lo) * f(hi) < 0:
            raizes.append(brentq(f, lo, hi, xtol=1e-12))
        m += 1
    return raizes


print('FIBRA: núcleo de %.1f µm, n1 = %.4f, n2 = %.4f' % (A_NUCLEO * 1e6, N1, N2))
print('  abertura numérica NA = %.4f' % NA)
print('  comprimento de onda de corte (V = 2,405) = %.0f nm'
      % (2 * np.pi * A_NUCLEO * NA / 2.405 * 1e9))
print()
print('  a coluna do guia plano é o análogo unidimensional, resolvido de')
print('  verdade aqui; a coluna "monomodo" usa o critério V < 2,405, que é o')
print('  da fibra cilíndrica. Os dois modelos têm critérios diferentes, e a')
print('  comparação serve para ver a mesma física em duas geometrias.')
print()
print('   lambda (nm)      V       modos pares do guia plano   monomodo?')
for lam in (650e-9, 850e-9, 1310e-9, 1550e-9):
    V = numero_v(lam)
    r = modos_guia_plano(V)
    print('   %9.0f   %7.3f   %18d          %s'
          % (lam * 1e9, V, len(r), 'sim' if V < 2.405 else 'não'))

print()
print('contagem de modos do guia plano contra a estimativa V/(pi/2):')
for V in (1.0, 3.0, 10.0, 30.0, 100.0):
    r = modos_guia_plano(V)
    print('   V = %6.1f : %3d modos pares   estimativa %5.1f'
          % (V, len(r), V / np.pi))
print('  (só os modos pares são contados; os ímpares dobram o total)')

# =============================================================== Fabry-Perot
L = 0.010
R = 0.99
N_MEIO = 1.0


def airy(f, R=R, L=L, n=N_MEIO):
    delta = 4 * np.pi * n * L * f / C
    F = 4 * R / (1 - R) ** 2
    return 1.0 / (1.0 + F * np.sin(delta / 2) ** 2)


print()
print('FABRY-PEROT: L = %.0f cm, R = %.2f, em 1550 nm' % (L * 100, R))
fsr_teorico = C / (2 * N_MEIO * L)
finesse_teorica = np.pi * np.sqrt(R) / (1 - R)
print('  previsto: FSR = %.4f GHz, finesse = %.1f, largura = %.3f MHz'
      % (fsr_teorico / 1e9, finesse_teorica,
         fsr_teorico / finesse_teorica / 1e6))

# mede tudo direto da curva, sem usar as fórmulas
f0 = C / 1550e-9
f = np.linspace(f0 - 2 * fsr_teorico, f0 + 2 * fsr_teorico, 4000001)
T = airy(f)
eh_pico = (T[1:-1] > T[:-2]) & (T[1:-1] > T[2:])
picos = f[1:-1][eh_pico]
fsr_medido = np.mean(np.diff(picos))
# largura a meia altura do pico central
pico = picos[len(picos) // 2]
perto = np.abs(f - pico) < fsr_teorico / 2
acima = f[perto][T[perto] > 0.5]
largura = acima.max() - acima.min()
print('  medido  : FSR = %.4f GHz, largura = %.3f MHz, finesse = %.1f'
      % (fsr_medido / 1e9, largura / 1e6, fsr_medido / largura))
print('  erro relativo: FSR %.1e, finesse %.1e'
      % (abs(fsr_medido - fsr_teorico) / fsr_teorico,
         abs(fsr_medido / largura - finesse_teorica) / finesse_teorica))
print('  Q = f0 / largura = %.3e' % (f0 / largura))

print()
print('como a finesse depende do espelho:')
print('    R        finesse     largura (MHz)        Q')
for Rr in (0.5, 0.9, 0.99, 0.999):
    Fn = np.pi * np.sqrt(Rr) / (1 - Rr)
    larg = fsr_teorico / Fn
    print('   %.3f   %10.1f   %12.3f   %.2e' % (Rr, Fn, larg / 1e6, f0 / larg))
print('  a finesse explode quando R se aproxima de 1, e é por isso que')
print('  espelhos de cavidade óptica são feitos com dezenas de camadas')
