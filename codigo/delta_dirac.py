# -*- coding: utf-8 -*-
"""A função delta: o limite, a filtragem, e a divergência que mora na origem.

O QUE RESOLVE
    Três coisas, nesta ordem:
    (1) mostra a delta como limite de gaussianas de largura decrescente, todas
        com área um;
    (2) testa a propriedade de filtragem, integral de f(x) delta(x-a) = f(a),
        medindo como o erro cai com a largura;
    (3) calcula o fluxo do campo r^/r^2 por esferas de vários raios e o seu
        divergente fora da origem, que é o par de resultados aparentemente
        contraditório da seção 5 do capítulo.

A FÍSICA
    O campo de uma carga pontual é r^/r^2 a menos de constantes. O divergente
    dele é nulo em toda parte menos num ponto, e mesmo assim o fluxo por
    qualquer superfície que contenha esse ponto vale 4 pi. A única maneira de
    escrever isso é div(r^/r^2) = 4 pi delta^3(r), e é dessa identidade que sai
    a lei de Gauss na forma diferencial para cargas pontuais.

COMO CONFERIR SE ESTÁ CERTO
    1. A área sob cada gaussiana tem de ser 1, qualquer que seja a largura.
    2. O erro da filtragem tem de cair como epsilon^2, porque a correção de
       ordem epsilon some por simetria.
    3. O fluxo tem de dar 4 pi = 12,566 para TODOS os raios, e o divergente
       numérico fora da origem tem de ser nulo.

Prof. Apiano Morais - LFCA/URCA - Eletromagnetismo I
"""

import numpy as np
import matplotlib.pyplot as plt


def gaussiana(x, eps):
    """Delta nascente de largura eps, com área unitária."""
    return np.exp(-(x / eps) ** 2) / (eps * np.sqrt(np.pi))


def f(x):
    """Função de teste qualquer, suave."""
    return np.cos(x) + 0.5 * x ** 2


A = 1.3            # ponto onde a delta está centrada

print('1. área sob a gaussiana nascente (tem de ser 1 para toda largura)')
x = np.linspace(-20, 20, 2000001)
for eps in (1.0, 0.3, 0.1, 0.03):
    area = np.trapezoid(gaussiana(x, eps), x)
    print('   eps = %.2f : área = %.10f' % (eps, area))

print()
print('2. propriedade de filtragem: integral de f(x) d_eps(x-a) -> f(a)')
print('   f(a) = %.10f' % f(A))
anterior = None
for eps in (0.4, 0.2, 0.1, 0.05, 0.025):
    val = np.trapezoid(f(x) * gaussiana(x - A, eps), x)
    err = abs(val - f(A))
    linha = '   eps = %.3f : %.10f   erro = %.3e' % (eps, val, err)
    if anterior:
        linha += '   razão = %.2f' % (anterior / err)
    anterior = err
    print(linha)
print('   razão 4 por divisão ao meio: o erro vai com eps^2, como previsto')

print()
print('3. o campo r^/r^2: fluxo e divergente')
print('   raio da esfera      fluxo numérico     4 pi')
for raio in (0.1, 1.0, 5.0, 100.0):
    n = 400
    t = (np.arange(n) + 0.5) * np.pi / n
    p = (np.arange(n) + 0.5) * 2 * np.pi / n
    T, P = np.meshgrid(t, p, indexing='ij')
    # v . da = (1/r^2) r^ . r^ r^2 sen t dt dp = sen t dt dp
    da = raio ** 2 * np.sin(T) * (np.pi / n) * (2 * np.pi / n)
    fluxo = np.sum((1.0 / raio ** 2) * da)
    print('   %12.1f      %14.9f   %10.6f' % (raio, fluxo, 4 * np.pi))

# divergente numérico longe da origem
n = 121
u = np.linspace(-3, 3, n)
h = u[1] - u[0]
X, Y, Z = np.meshgrid(u, u, u, indexing='ij')
r = np.sqrt(X ** 2 + Y ** 2 + Z ** 2)
r[r < 1e-9] = 1e-9
vx, vy, vz = X / r ** 3, Y / r ** 3, Z / r ** 3
div = (np.gradient(vx, h, axis=0) + np.gradient(vy, h, axis=1)
       + np.gradient(vz, h, axis=2))
longe = r > 1.0
print()
print('   divergente numérico para r > 1 : máximo |div| = %.3e' % np.max(np.abs(div[longe])))
print('   divergente no ponto central    : %.3e' % div[n // 2, n // 2, n // 2])
print('   nulo fora, infinito no ponto: é a delta, e a sua integral vale 4 pi')

# ------------------------------------------------------------------- figura
xx = np.linspace(-1.5, 1.5, 2000)
fig, eixo = plt.subplots(1, 2, figsize=(11, 4.2))
for eps in (0.5, 0.25, 0.12, 0.06):
    eixo[0].plot(xx, gaussiana(xx, eps), lw=2, label='eps = %.2f' % eps)
eixo[0].set_xlabel('x')
eixo[0].set_ylabel('delta nascente')
eixo[0].set_title('Mais alta e mais estreita, área sempre 1')
eixo[0].legend(frameon=False, fontsize=9)

epsilons = np.array([0.4, 0.2, 0.1, 0.05, 0.025, 0.0125])
erros = [abs(np.trapezoid(f(x) * gaussiana(x - A, e), x) - f(A)) for e in epsilons]
eixo[1].loglog(epsilons, erros, 'o-', lw=2)
eixo[1].loglog(epsilons, erros[0] * (epsilons / epsilons[0]) ** 2, ls='--', lw=1.2,
               label='inclinação 2')
eixo[1].set_xlabel('largura eps')
eixo[1].set_ylabel('erro da filtragem')
eixo[1].set_title('O erro cai com eps ao quadrado')
eixo[1].legend(frameon=False, fontsize=9)
fig.tight_layout()
plt.show()
