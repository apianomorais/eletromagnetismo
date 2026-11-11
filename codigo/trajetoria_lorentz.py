# -*- coding: utf-8 -*-
"""Trajetória de uma carga em campos elétrico e magnético, pelo método de Boris.

O QUE RESOLVE
    A equação de movimento m dv/dt = q (E + v x B), para E e B uniformes ou
    dados por funções da posição. Devolve e desenha a trajetória.

POR QUE BORIS, E NÃO RUNGE-KUTTA
    A força magnética não realiza trabalho: |v| tem de ser constante quando
    E = 0. Um integrador comum erra um pouquinho a cada passo sempre para o
    mesmo lado, a energia deriva, e depois de algumas centenas de voltas o
    círculo virou espiral. O método de Boris implementa a parte magnética como
    uma ROTAÇÃO, que preserva |v| por construção: o erro vai para a fase, e
    não para a energia.

COMO CONFERIR SE ESTÁ CERTO
    1. Com E = 0, o raio medido tem de bater com R = m v / (q B) e NÃO pode
       crescer com o tempo. O programa imprime os dois e o desvio.
    2. Com campos cruzados e partida do repouso, o centro da órbita caminha
       com velocidade E/B, independentemente de q e de m. Troque a carga de
       sinal e veja que a deriva não muda de sentido.
    3. O período tem de ser T = 2 pi m / (q B), qualquer que seja a velocidade.

COMO RODAR
    No Spyder: abra e aperte F5. Mexa no bloco PARÂMETROS e rode de novo.

Prof. Apiano Morais - LFCA/URCA - Eletromagnetismo II
"""

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------------- PARÂMETROS
q = 1.0            # carga, em unidades arbitrárias
m = 1.0            # massa
E = np.array([0.0, 0.0, 1.0])     # campo elétrico (aponta em z)
B = np.array([1.0, 0.0, 0.0])     # campo magnético (aponta em x)
v0 = np.array([0.0, 0.0, 0.0])    # velocidade inicial
r0 = np.array([0.0, 0.0, 0.0])    # posição inicial
dt = 0.01          # passo de tempo
n_passos = 4000


# ----------------------------------------------------------------- O MÉTODO
def boris(r0, v0, q, m, E, B, dt, n):
    """Integra n passos e devolve as trajetórias r(t) e v(t).

    Cada passo tem três partes:
      1. meio empurrão do campo elétrico,
      2. rotação pura em torno de B, feita pela fórmula de Boris, que é
         equivalente a uma rotação de ângulo -q B dt / m,
      3. o outro meio empurrão elétrico.
    """
    r = np.zeros((n + 1, 3))
    v = np.zeros((n + 1, 3))
    r[0], v[0] = r0, v0

    t_vec = (q * B / m) * (dt / 2.0)          # vetor t da fórmula de Boris
    t2 = np.dot(t_vec, t_vec)
    s_vec = 2.0 * t_vec / (1.0 + t2)          # vetor s

    for i in range(n):
        v_menos = v[i] + (q * E / m) * (dt / 2.0)      # 1. meio empurrão
        v_linha = v_menos + np.cross(v_menos, t_vec)   # 2. rotação, parte 1
        v_mais = v_menos + np.cross(v_linha, s_vec)    #    rotação, parte 2
        v[i + 1] = v_mais + (q * E / m) * (dt / 2.0)   # 3. meio empurrão
        r[i + 1] = r[i] + v[i + 1] * dt
    return r, v


# ------------------------------------------------------------------ CÁLCULO
r, v = boris(r0, v0, q, m, E, B, dt, n_passos)
t = np.arange(n_passos + 1) * dt

Bmod = np.linalg.norm(B)
omega = q * Bmod / m
periodo = 2.0 * np.pi / omega
deriva = np.linalg.norm(np.cross(E, B)) / Bmod ** 2

print('frequência de cíclotron  omega = %.4f rad/s' % omega)
print('período                      T = %.4f s' % periodo)
print('deriva E x B / B^2            = %.4f (unidades de comprimento por s)' % deriva)

# conferência 1: a energia cinética só pode variar por causa de E
energia = 0.5 * m * np.sum(v ** 2, axis=1)
if np.linalg.norm(E) == 0:
    desvio = (energia.max() - energia.min()) / energia[0] if energia[0] else 0.0
    print('variação relativa da energia cinética: %.2e  (deveria ser ~0)' % desvio)
    R_teorico = m * np.linalg.norm(v0) / (q * Bmod)
    R_medido = (r[:, 1].max() - r[:, 1].min()) / 2.0
    print('raio teórico %.4f   raio medido %.4f   erro %.2f %%'
          % (R_teorico, R_medido, 100 * abs(R_medido - R_teorico) / R_teorico))
else:
    # conferência 2: o centro de guia caminha com E/B
    y_final = r[-1, 1]
    print('deslocamento médio em y: %.4f   previsto: %.4f'
          % (y_final / t[-1], deriva))

# ------------------------------------------------------------------ GRÁFICO
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.6))

ax1.plot(r[:, 1], r[:, 2], lw=1.6, color='#1c2c60')
ax1.plot(r[0, 1], r[0, 2], 'o', color='#b5831f', ms=7, label='início')
if np.linalg.norm(E) > 0:
    ax1.plot(t * deriva, np.full_like(t, r[:, 2].mean()), '--',
             color='#a8181d', lw=1.2, label='deriva $E/B$')
ax1.set_xlabel('$y$'); ax1.set_ylabel('$z$')
ax1.set_title('trajetória no plano perpendicular a $B$')
ax1.set_aspect('equal', adjustable='datalim')
ax1.legend(frameon=False)

ax2.plot(t, energia, lw=1.6, color='#1c2c60')
ax2.set_xlabel('$t$'); ax2.set_ylabel('energia cinética')
ax2.set_title('o que a força magnética não faz')

fig.tight_layout()
plt.show()
