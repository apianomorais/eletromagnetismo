# -*- coding: utf-8 -*-
"""A barra que desliza nos trilhos: fem de movimento e balanço de energia.

O QUE RESOLVE
    Integra o movimento de uma barra condutora de massa m e comprimento h que
    desliza sem atrito sobre dois trilhos fechados por um resistor R, dentro de
    um campo magnético uniforme B perpendicular ao plano. A fem induzida é
    vBh, a corrente é vBh/R, e a força magnética sobre a barra se opõe ao
    movimento.

A FÍSICA
    A equação de movimento é

        m dv/dt = F_ext - (B h)^2 v / R,

    isto é, um atrito viscoso de origem puramente eletromagnética, com
    constante de tempo tau = mR/(Bh)^2. Note que a força magnética NÃO realiza
    trabalho: quem gasta energia é quem puxa a barra, e o campo apenas
    transfere essa energia para o resistor. O programa verifica isso.

COMO CONFERIR SE ESTÁ CERTO
    1. Com força externa constante, a velocidade tem de tender ao valor
       terminal v_t = F R / (B h)^2, quando a força externa iguala a magnética.
    2. Sem força externa, partindo de v0, a velocidade tem de decair como
       v0 exp(-t/tau), e a energia cinética perdida tem de aparecer inteira
       como calor no resistor.
    3. Em qualquer caso, o balanço W_ext = Delta_Ec + Q tem de fechar em todo
       instante, até o erro do integrador.

Prof. Apiano Morais - LFCA/URCA - Eletromagnetismo II
"""

import numpy as np
import matplotlib.pyplot as plt

B = 0.35          # campo magnético, em tesla
H = 0.12          # comprimento da barra entre os trilhos, em metros
R = 0.50          # resistência total do circuito, em ohm
M = 0.020         # massa da barra, em quilogramas

K = (B * H) ** 2 / R          # constante do atrito magnético
TAU = M / K                   # tempo característico


def integrar(v0, f_ext, t_final, n=20001):
    """Runge-Kutta 4 para m dv/dt = F(t) - K v, com os acumuladores de energia."""
    t = np.linspace(0.0, t_final, n)
    dt = t[1] - t[0]
    v = np.zeros(n)
    x = np.zeros(n)
    w_ext = np.zeros(n)        # trabalho da força externa
    calor = np.zeros(n)        # energia dissipada no resistor
    v[0] = v0

    def a(tt, vv):
        return (f_ext(tt) - K * vv) / M

    for i in range(n - 1):
        k1 = a(t[i], v[i])
        k2 = a(t[i] + dt / 2, v[i] + dt / 2 * k1)
        k3 = a(t[i] + dt / 2, v[i] + dt / 2 * k2)
        k4 = a(t[i] + dt, v[i] + dt * k3)
        v[i + 1] = v[i] + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        vm = 0.5 * (v[i] + v[i + 1])
        x[i + 1] = x[i] + vm * dt
        w_ext[i + 1] = w_ext[i] + f_ext(t[i] + dt / 2) * vm * dt
        calor[i + 1] = calor[i] + K * vm * vm * dt     # I^2 R = K v^2
    return t, v, x, w_ext, calor


print('constantes do circuito')
print('  atrito magnético K = (Bh)^2/R = %.5f N s/m' % K)
print('  tempo característico tau = mR/(Bh)^2 = %.4f s' % TAU)

# ----------------------------------------------- 1. força externa constante
F0 = 7.1e-3
t, v, x, w, q = integrar(0.0, lambda tt: F0, 12 * TAU)
v_term = F0 / K
print()
print('FORÇA CONSTANTE de %.4f N' % F0)
print('  velocidade terminal prevista  v_t = F R/(Bh)^2 = %.5f m/s' % v_term)
print('  velocidade final da integração                = %.5f m/s' % v[-1])
print('  fem terminal = v_t B h = %.5f V,  corrente = %.5f A'
      % (v_term * B * H, v_term * B * H / R))

# ------------------------------------------- 2. sem força: decaimento puro
V0 = 2.0
t2, v2, x2, w2, q2 = integrar(V0, lambda tt: 0.0, 6 * TAU)
previsto = V0 * np.exp(-t2 / TAU)
print()
print('SEM FORÇA EXTERNA, partindo de %.1f m/s' % V0)
print('  erro máximo contra v0 exp(-t/tau): %.3e m/s'
      % np.max(np.abs(v2 - previsto)))
ec_perdida = 0.5 * M * (V0 ** 2 - v2[-1] ** 2)
print('  energia cinética perdida = %.6e J' % ec_perdida)
print('  calor dissipado no resistor = %.6e J' % q2[-1])
print('  diferença relativa = %.2e'
      % (abs(ec_perdida - q2[-1]) / ec_perdida))

# ------------------------------------------------ 3. balanço instante a instante
ec = 0.5 * M * v ** 2
desvio = np.max(np.abs(w - (ec - ec[0]) - q)) / max(w[-1], 1e-30)
print()
print('BALANÇO W_ext = Delta_Ec + Q, com força constante')
print('  desvio relativo máximo ao longo de toda a integração: %.2e' % desvio)

# ------------------------------------------------------------------- figura
fig, eixo = plt.subplots(1, 2, figsize=(11, 4.2))

eixo[0].plot(t / TAU, v, lw=2, label='com força constante')
eixo[0].plot(t2 / TAU, v2, lw=2, label='sem força externa')
eixo[0].axhline(v_term, ls='--', lw=1)
eixo[0].set_xlabel('t / tau')
eixo[0].set_ylabel('velocidade (m/s)')
eixo[0].set_title('O campo freia como um atrito viscoso')
eixo[0].legend(frameon=False, fontsize=9)

eixo[1].plot(t / TAU, w * 1e3, lw=2, label='trabalho externo')
eixo[1].plot(t / TAU, (ec - ec[0]) * 1e3, lw=2, label='energia cinética')
eixo[1].plot(t / TAU, q * 1e3, lw=2, label='calor no resistor')
eixo[1].set_xlabel('t / tau')
eixo[1].set_ylabel('energia (mJ)')
eixo[1].set_title('Quem paga a conta é quem puxa')
eixo[1].legend(frameon=False, fontsize=9)

fig.tight_layout()
plt.show()
