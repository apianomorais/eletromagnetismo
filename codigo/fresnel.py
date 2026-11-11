# -*- coding: utf-8 -*-
"""As equações de Fresnel: reflexão, transmissão, Brewster e reflexão total.

O QUE RESOLVE
    Calcula os coeficientes de reflexão e transmissão de energia, para as duas
    polarizações, em função do ângulo de incidência, nos dois sentidos da
    interface (do meio menos denso para o mais denso e vice-versa).

A FÍSICA
    A lei de Snell vem só do casamento de fases na interface; as amplitudes
    exigem as condições de contorno dos campos. Dois fenômenos aparecem: o
    ângulo de Brewster, em que a polarização paralela não reflete nada, e o
    ângulo crítico, acima do qual tudo volta.

COMO CONFERIR SE ESTÁ CERTO
    1. R + T = 1 em todo ângulo e nas duas polarizações, que é conservação de
       energia.
    2. Em incidência normal, as duas polarizações têm de dar o mesmo R, e o
       valor tem de ser ((n1-n2)/(n1+n2))^2.
    3. R paralelo tem de zerar exatamente em arctan(n2/n1).
    4. Acima do ângulo crítico, R = 1 nas duas polarizações.

Prof. Apiano Morais - LFCA/URCA - Eletromagnetismo III
"""

import numpy as np
import matplotlib.pyplot as plt


def fresnel(n1, n2, theta_i):
    """Coeficientes de amplitude (r, t) para as duas polarizações.

    Usa cosseno complexo além do ângulo crítico, que é o jeito correto de
    descrever a onda evanescente.
    """
    ti = np.asarray(theta_i, dtype=complex)
    sin_t = n1 / n2 * np.sin(ti)
    cos_t = np.sqrt(1 - sin_t ** 2 + 0j)
    cos_i = np.cos(ti)
    # perpendicular ao plano de incidência (s)
    r_s = (n1 * cos_i - n2 * cos_t) / (n1 * cos_i + n2 * cos_t)
    t_s = 2 * n1 * cos_i / (n1 * cos_i + n2 * cos_t)
    # paralela ao plano de incidência (p)
    r_p = (n2 * cos_i - n1 * cos_t) / (n2 * cos_i + n1 * cos_t)
    t_p = 2 * n1 * cos_i / (n2 * cos_i + n1 * cos_t)
    return (r_s, t_s, r_p, t_p), cos_i, cos_t


def energia(n1, n2, theta_i):
    """R e T de energia, nas duas polarizações."""
    (r_s, t_s, r_p, t_p), cos_i, cos_t = fresnel(n1, n2, theta_i)
    fator = (n2 * cos_t) / (n1 * cos_i)
    R_s, R_p = np.abs(r_s) ** 2, np.abs(r_p) ** 2
    T_s = np.real(fator) * np.abs(t_s) ** 2
    T_p = np.real(fator) * np.abs(t_p) ** 2
    return R_s, T_s, R_p, T_p


N1, N2 = 1.0, 1.5

print('ar para vidro (n1 = %.1f, n2 = %.1f)' % (N1, N2))
print('  incidência normal: R = %.6f   previsto ((n1-n2)/(n1+n2))² = %.6f'
      % (energia(N1, N2, 0.0)[0], ((N1 - N2) / (N1 + N2)) ** 2))

print()
print('   ângulo    R_perp     T_perp     R_par      T_par     R+T (perp, par)')
for g in (0, 20, 40, 56.31, 70, 85):
    R_s, T_s, R_p, T_p = energia(N1, N2, np.radians(g))
    print('  %6.2f   %.6f   %.6f   %.6f   %.6f    %.8f %.8f'
          % (g, R_s, T_s, R_p, T_p, R_s + T_s, R_p + T_p))

brewster = np.degrees(np.arctan(N2 / N1))
R_s, T_s, R_p, T_p = energia(N1, N2, np.radians(brewster))
print()
print('ângulo de Brewster = arctan(n2/n1) = %.4f graus' % brewster)
print('  R paralelo ali = %.3e   (tem de ser zero)' % R_p)
print('  R perpendicular ali = %.6f   (a luz refletida fica toda polarizada)'
      % R_s)

print()
print('agora do vidro para o ar: reflexão interna total')
critico = np.degrees(np.arcsin(N1 / N2))
print('  ângulo crítico = arcsen(n_ar/n_vidro) = %.4f graus' % critico)
print('   ângulo    R_perp      R_par     T_perp     T_par')
for g in (0, 20, 41.0, critico, 45, 60, 80):
    R_s, T_s, R_p, T_p = energia(N2, N1, np.radians(g))
    print('  %6.2f   %.6f   %.6f   %.6f   %.6f' % (g, R_s, R_p, T_s, T_p))
print('  acima do crítico, R = 1 exatamente nas duas: nada atravessa, e a')
print('  energia que aparece do outro lado é a onda evanescente, que não')
print('  transporta fluxo médio')

# ------------------------------------------------------------------- figura
ang = np.linspace(0, 89.9, 600)
fig, eixo = plt.subplots(1, 2, figsize=(11, 4.2))
R_s, T_s, R_p, T_p = energia(N1, N2, np.radians(ang))
eixo[0].plot(ang, R_s, lw=2, label='R perpendicular')
eixo[0].plot(ang, R_p, lw=2, label='R paralela')
eixo[0].axvline(brewster, ls='--', lw=1)
eixo[0].set_title('ar → vidro: Brewster em %.1f°' % brewster)
R_s, T_s, R_p, T_p = energia(N2, N1, np.radians(ang))
eixo[1].plot(ang, R_s, lw=2, label='R perpendicular')
eixo[1].plot(ang, R_p, lw=2, label='R paralela')
eixo[1].axvline(critico, ls='--', lw=1)
eixo[1].set_title('vidro → ar: crítico em %.1f°' % critico)
for ax in eixo:
    ax.set_xlabel('ângulo de incidência (graus)')
    ax.set_ylabel('refletância')
    ax.set_ylim(-0.02, 1.02)
    ax.legend(frameon=False, fontsize=9)
fig.tight_layout()
plt.show()
