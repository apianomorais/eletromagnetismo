# -*- coding: utf-8 -*-
"""A corrente de deslocamento num capacitor carregando.

O QUE RESOLVE
    Um capacitor de placas circulares de raio R é carregado através de um
    circuito RC. O programa acompanha a carga, o campo elétrico entre as
    placas, a corrente de condução no fio e a corrente de deslocamento, e
    calcula o campo magnético em torno do eixo, dentro e fora da borda da
    placa.

A FÍSICA
    A lei de Ampère sem o termo de Maxwell é ambígua: duas superfícies
    apoiadas na mesma curva, uma atravessada pelo fio e outra passando entre
    as placas, dão correntes enlaçadas diferentes. Com o termo de
    deslocamento, eps0 dPhi_E/dt, as duas voltam a concordar, e é esse o
    conteúdo da conta abaixo.

        s < R :  B = mu0 I s / (2 pi R^2)
        s > R :  B = mu0 I / (2 pi s)

COMO CONFERIR SE ESTÁ CERTO
    1. A corrente de deslocamento através de um disco de raio maior que R tem
       de ser igual, em todo instante, à corrente de condução no fio. O
       programa imprime a diferença.
    2. As duas expressões de B têm de coincidir em s = R: o campo é contínuo
       na borda da placa.
    3. No circuito RC, a carga tem de tender a C V0 e a corrente a zero, com
       a constante de tempo RC.

Prof. Apiano Morais - LFCA/URCA - Eletromagnetismo II
"""

import numpy as np
import matplotlib.pyplot as plt

EPS0 = 8.8541878128e-12
MU0 = 4.0e-7 * np.pi

RP = 0.050        # raio das placas, em metros
GAP = 1.0e-3      # separação entre as placas, em metros
RES = 2.0e3       # resistência do circuito, em ohm
V0 = 12.0         # tensão da fonte, em volt

CAP = EPS0 * np.pi * RP ** 2 / GAP       # capacitância de placas paralelas
TAU = RES * CAP

print('capacitor de placas circulares')
print('  C = eps0 pi R^2 / g = %.4e F' % CAP)
print('  constante de tempo RC = %.4e s' % TAU)


def estado(t):
    """Carga, corrente e campo elétrico entre as placas, no instante t."""
    q = CAP * V0 * (1.0 - np.exp(-t / TAU))
    i = (V0 / RES) * np.exp(-t / TAU)
    e = q / (EPS0 * np.pi * RP ** 2)
    return q, i, e


def deslocamento(t, s, dt=1e-9):
    """Corrente de deslocamento através de um disco de raio s, por diferença
    finita central do fluxo elétrico: eps0 dPhi_E/dt."""
    area = np.pi * min(s, RP) ** 2           # fora da placa não há campo
    fluxo = lambda tt: EPS0 * estado(tt)[2] * area
    return (fluxo(t + dt) - fluxo(t - dt)) / (2 * dt)


def campo_magnetico(s, i):
    """B(s) no plano médio entre as placas, para a corrente i no fio."""
    s = np.asarray(s, dtype=float)
    return np.where(s < RP,
                    MU0 * i * s / (2 * np.pi * RP ** 2),
                    MU0 * i / (2 * np.pi * s))


# ------------------------------------- 1. as duas superfícies, instante a instante
print()
print('corrente de condução contra corrente de deslocamento (disco com s > R):')
print('      t (ns)    I_cond (mA)    I_desl (mA)    diferença relativa')
for t in (0.05 * TAU, 0.3 * TAU, 1.0 * TAU, 2.5 * TAU):
    _, i, _ = estado(t)
    idesl = deslocamento(t, 2 * RP)
    print('   %9.2f   %12.6f   %12.6f    %.2e'
          % (t * 1e9, i * 1e3, idesl * 1e3, abs(i - idesl) / i))
print('  a diferença que sobra é truncamento da diferença central, e cai com dt^2:')
for dt in (4e-9, 2e-9, 1e-9):
    t = TAU
    _, i, _ = estado(t)
    err = abs(i - deslocamento(t, 2 * RP, dt=dt)) / i
    print('    dt = %.0e s : erro = %.3e' % (dt, err))

# --------------------------------------------- 2. continuidade na borda da placa
t0 = 0.5 * TAU
_, i0, e0 = estado(t0)
b_dentro = MU0 * i0 * RP / (2 * np.pi * RP ** 2)
b_fora = MU0 * i0 / (2 * np.pi * RP)
print()
print('no instante t = 0,5 RC, com I = %.4f mA:' % (i0 * 1e3))
print('  B na borda pela expressão de dentro = %.6e T' % b_dentro)
print('  B na borda pela expressão de fora   = %.6e T' % b_fora)
print('  diferença relativa = %.2e' % (abs(b_dentro - b_fora) / b_fora))
print('  campo elétrico entre as placas = %.4e V/m' % e0)

# -------------------------------------------------- 3. o circuito faz o esperado
tf = 6 * TAU
qf, i_f, _ = estado(tf)
print()
print('em t = 6 RC: carga = %.4e C (prevista C V0 = %.4e C), corrente = %.2e A'
      % (qf, CAP * V0, i_f))

# ------------------------------------------------------------------- figura
s = np.linspace(1e-4, 2.5 * RP, 400)
fig, eixo = plt.subplots(1, 2, figsize=(11, 4.2))

eixo[0].plot(s / RP, campo_magnetico(s, i0) * 1e9, lw=2)
eixo[0].axvline(1.0, ls='--', lw=1)
eixo[0].set_xlabel('s / R')
eixo[0].set_ylabel('B (nT)')
eixo[0].set_title('Campo magnético entre as placas')

t = np.linspace(0, 5 * TAU, 400)
q, i, e = estado(t)
eixo[1].plot(t / TAU, i * 1e3, lw=2, label='corrente de condução')
eixo[1].plot(t / TAU, [deslocamento(tt, 2 * RP) * 1e3 for tt in t],
             ls='--', lw=1.6, label='corrente de deslocamento')
eixo[1].set_xlabel('t / RC')
eixo[1].set_ylabel('corrente (mA)')
eixo[1].set_title('As duas superfícies dão o mesmo')
eixo[1].legend(frameon=False, fontsize=9)

fig.tight_layout()
plt.show()
