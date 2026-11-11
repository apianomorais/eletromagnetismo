# -*- coding: utf-8 -*-
"""Histerese a partir do campo médio de Weiss.

O QUE RESOLVE
    Resolve a equação de campo médio, em variáveis adimensionais,

        m = tanh[ (m + h) * Tc / T ],

    varrendo o campo externo h para cima e para baixo, e mostra que abaixo de
    Tc o laço abre sozinho, sem que nenhuma histerese tenha sido posta na mão.

A FÍSICA
    Weiss supõe que cada momento sente, além do campo externo, um campo
    proporcional à magnetização média dos vizinhos. Abaixo de Tc a equação
    passa a ter três soluções para h pequeno: duas estáveis, de sinais
    opostos, e uma instável no meio. O sistema não escolhe a de menor energia,
    ele fica na que estava, e só pula quando a solução em que estava deixa de
    existir. Esse salto é o campo coercivo deste modelo.

    Note o que isto NÃO é: a histerese de um ímã real vem de paredes de
    domínio presas em defeitos, e não da multiplicidade de soluções do campo
    médio. O laço daqui é o esqueleto do fenômeno, não o fenômeno.

COMO CONFERIR SE ESTÁ CERTO
    1. Acima de Tc o laço tem de fechar: ida e volta sobre a mesma curva.
       O programa mede a área e ela tem de ser desprezível.
    2. Em h = 0 e T -> 0 a magnetização tem de saturar em m = 1.
    3. A susceptibilidade inicial acima de Tc tem de seguir Curie-Weiss,
       chi = 1 / (T - Tc). O programa ajusta log(chi) contra log(T - Tc) e
       imprime o expoente, que tem de dar -1.

Prof. Apiano Morais - LFCA/URCA - Eletromagnetismo II
"""

import numpy as np
import matplotlib.pyplot as plt

TC = 1.0          # temperatura crítica, em unidades próprias
TOL = 1e-12
MAX_IT = 20000


def resolve(h, t, chute):
    """Ponto fixo amortecido de m = tanh[(m + h)/t], partindo de 'chute'.

    O amortecimento é o que impede a iteração de oscilar entre as duas
    soluções simétricas quando t fica bem abaixo de Tc.
    """
    m = chute
    for _ in range(MAX_IT):
        novo = np.tanh((m + h) * TC / t)
        passo = 0.5 * (novo - m)
        m += passo
        if abs(passo) < TOL:
            break
    return m


def laco(t, h_max=0.6, n=601):
    """Varre h de -h_max a +h_max e de volta, sempre partindo de onde parou."""
    subida = np.linspace(-h_max, h_max, n)
    descida = subida[::-1]
    m_sobe, m_desce = [], []
    m = -1.0
    for h in subida:
        m = resolve(h, t, m)
        m_sobe.append(m)
    m = +1.0
    for h in descida:
        m = resolve(h, t, m)
        m_desce.append(m)
    return subida, np.array(m_sobe), descida, np.array(m_desce)


def area(h, m_sobe, m_desce):
    """Área do laço, que é a energia dissipada por ciclo."""
    return np.trapezoid(m_desce[::-1] - m_sobe, h)


# ------------------------------------------------------- 1. os laços e a área
print('área do laço (energia por ciclo), em unidades próprias:')
temperaturas = [0.5, 0.8, 0.95, 1.2]
guardado = {}
for t in temperaturas:
    h, ms, hd, md = laco(t)
    guardado[t] = (h, ms, hd, md)
    a = area(h, ms, md)
    estado = 'ferro, laço aberto' if t < TC else 'para, laço fechado'
    print('  T/Tc = %.2f : área = %.3e   (%s)' % (t, a, estado))

# ------------------------------------- 2. remanência e coercividade em T = 0,5
h, ms, hd, md = guardado[0.5]
remanencia = np.interp(0.0, h, ms)
troca = np.where(np.diff(np.sign(ms)))[0]
coerciva = h[troca[0]] if len(troca) else float('nan')
print()
print('em T/Tc = 0,50:  m(h=0) na subida = %+.4f   campo coercivo = %+.4f'
      % (remanencia, coerciva))

# -------------------------------------------- 3. Curie-Weiss acima da crítica
dh = 1e-4
ts = TC + np.array([0.02, 0.05, 0.1, 0.2, 0.4, 0.8])
chi = np.array([(resolve(dh, t, 0.0) - resolve(-dh, t, 0.0)) / (2 * dh)
                for t in ts])
coef = np.polyfit(np.log(ts - TC), np.log(chi), 1)
print()
print('susceptibilidade acima de Tc: chi ~ (T - Tc)^(%.4f), previsto -1'
      % coef[0])
for t, c in zip(ts, chi):
    print('  T - Tc = %.2f : chi = %8.3f   1/(T-Tc) = %8.3f' % (t - TC, c, 1 / (t - TC)))

# ------------------------------------------------------------------- 4. figura
fig, eixo = plt.subplots(1, 2, figsize=(11, 4.4))

for t in temperaturas:
    h, ms, hd, md = guardado[t]
    linha, = eixo[0].plot(h, ms, lw=2, label='T/Tc = %.2f' % t)
    eixo[0].plot(hd, md, lw=2, color=linha.get_color())
eixo[0].axhline(0, lw=0.8, color='0.6')
eixo[0].axvline(0, lw=0.8, color='0.6')
eixo[0].set_xlabel('campo externo h')
eixo[0].set_ylabel('magnetização m')
eixo[0].set_title('O laço abre abaixo de Tc')
eixo[0].legend(frameon=False, fontsize=9)

tt = np.linspace(0.02, 1.6, 300)
m0 = np.array([resolve(0.0, t, 0.9) for t in tt])
eixo[1].plot(tt, np.abs(m0), lw=2)
eixo[1].axvline(TC, ls='--', lw=1)
eixo[1].set_xlabel('T / Tc')
eixo[1].set_ylabel('magnetização espontânea |m|')
eixo[1].set_title('Some em Tc, com expoente 1/2')

fig.tight_layout()
plt.show()
