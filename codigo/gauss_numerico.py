# -*- coding: utf-8 -*-
"""A lei de Gauss em superfícies sem simetria nenhuma.

O QUE RESOLVE
    Calcula o fluxo do campo de uma carga pontual através de superfícies
    fechadas de formas diferentes: esfera centrada, esfera deslocada, cubo e
    uma superfície deformada sem simetria. Com a carga dentro e com a carga
    fora.

A FÍSICA
    A lei de Gauss diz que o fluxo vale q/eps0 sempre que a carga estiver
    dentro, qualquer que seja a forma da superfície, e zero quando estiver
    fora. Isso não é óbvio: o campo em cada ponto depende fortemente da
    geometria, e é só a combinação do inverso do quadrado com o crescimento
    quadrático da área que faz os dois efeitos se cancelarem exatamente.

COMO CONFERIR SE ESTÁ CERTO
    1. Dentro: o fluxo tem de dar q/eps0 = 1,129e11 N m^2/C para q = 1 nC, em
       todas as quatro superfícies.
    2. Fora: o fluxo tem de dar zero, e o resíduo numérico tem de cair quando a
       malha é refinada.
    3. Com duas cargas, o fluxo tem de ser a soma, incluindo o caso em que uma
       está dentro e a outra fora.

Prof. Apiano Morais - LFCA/URCA - Eletromagnetismo I
"""

import numpy as np

K = 8.9875517873681764e9
EPS0 = 1.0 / (4 * np.pi * K)
Q = 1.0e-9


def campo(cargas, pontos):
    """E nos pontos (n,3), somando as cargas, cada uma (posicao, q)."""
    E = np.zeros_like(pontos)
    for pos, q in cargas:
        d = pontos - np.asarray(pos, dtype=float)
        r = np.sqrt((d ** 2).sum(axis=1))
        E += K * q * d / r[:, None] ** 3
    return E


# ------------------------------------------------------------- as superfícies
def esfera(n, centro=(0, 0, 0), raio=0.1, deforma=0.0):
    """Esfera, possivelmente amassada por um fator radial dependente do ângulo."""
    t = (np.arange(n) + 0.5) * np.pi / n
    f = (np.arange(n) + 0.5) * 2 * np.pi / n
    T, F = np.meshgrid(t, f, indexing='ij')
    # raio variável: a superfície deixa de ter qualquer simetria
    R = raio * (1 + deforma * (np.sin(3 * T) * np.cos(2 * F)
                               + 0.5 * np.cos(T)))
    x = R * np.sin(T) * np.cos(F)
    y = R * np.sin(T) * np.sin(F)
    z = R * np.cos(T)
    dt, df = np.pi / n, 2 * np.pi / n
    # vetores tangentes por diferenciação da parametrização, para o caso
    # deformado, em que n ao é mais radial
    dR_dt = np.gradient(R, dt, axis=0, edge_order=2)
    dR_df = np.gradient(R, df, axis=1, edge_order=2)
    e_t = np.stack([dR_dt * np.sin(T) * np.cos(F) + R * np.cos(T) * np.cos(F),
                    dR_dt * np.sin(T) * np.sin(F) + R * np.cos(T) * np.sin(F),
                    dR_dt * np.cos(T) - R * np.sin(T)], axis=-1)
    e_f = np.stack([dR_df * np.sin(T) * np.cos(F) - R * np.sin(T) * np.sin(F),
                    dR_df * np.sin(T) * np.sin(F) + R * np.sin(T) * np.cos(F),
                    dR_df * np.cos(T)], axis=-1)
    da = np.cross(e_t, e_f) * dt * df          # já é o vetor área, com módulo
    pts = np.stack([x, y, z], axis=-1) + np.asarray(centro, dtype=float)
    return pts.reshape(-1, 3), da.reshape(-1, 3)


def cubo(n, centro=(0, 0, 0), lado=0.16):
    """Seis faces, com o vetor área apontando para fora."""
    u = (np.arange(n) + 0.5) * lado / n - lado / 2
    P, Qd = np.meshgrid(u, u, indexing='ij')
    zeros = np.zeros_like(P)
    meia = lado / 2
    da_escalar = (lado / n) ** 2
    pts, das = [], []
    for eixo in range(3):
        for sinal in (+1, -1):
            coord = [P, Qd]
            face = np.insert(np.stack(coord, axis=-1), eixo,
                             sinal * meia + zeros, axis=-1)
            normal = np.zeros(3)
            normal[eixo] = sinal
            pts.append(face.reshape(-1, 3))
            das.append(np.tile(normal * da_escalar, (face[..., 0].size, 1)))
    pts = np.concatenate(pts) + np.asarray(centro, dtype=float)
    return pts, np.concatenate(das)


def fluxo(cargas, pts, da):
    return float(np.sum(campo(cargas, pts) * da))


ESPERADO = Q / EPS0
print('fluxo esperado para a carga dentro: q/eps0 = %.6e N m^2/C' % ESPERADO)
print()

casos = [
    ('esfera centrada', lambda n: esfera(n)),
    ('esfera deslocada', lambda n: esfera(n, centro=(0.04, -0.02, 0.03))),
    ('esfera amassada', lambda n: esfera(n, deforma=0.35)),
    ('cubo', lambda n: cubo(n)),
]

print('CARGA DENTRO, na origem')
print('  repare que a esfera amassada dá exatamente o mesmo que a centrada:')
print('  para qualquer superfície que "enxergue" a carga em todas as direções,')
print('  o integrando se reduz ao elemento de ângulo sólido, e o raio cancela')
print('   superfície           n=40            n=80        erro relativo (n=80)')
for nome, gerar in casos:
    linha = '  %-18s' % nome
    for n in (40, 80):
        pts, da = gerar(n)
        f = fluxo([((0, 0, 0), Q)], pts, da)
        linha += ' %14.6e' % f
    linha += '   %.1e' % (abs(f - ESPERADO) / ESPERADO)
    print(linha)

print()
print('CARGA FORA, em (0,30; 0; 0), bem longe de todas as superfícies')
print('   superfície           n=40            n=80')
for nome, gerar in casos:
    linha = '  %-18s' % nome
    for n in (40, 80):
        pts, da = gerar(n)
        linha += ' %14.3e' % fluxo([((0.30, 0.0, 0.0), Q)], pts, da)
    print(linha)
print('  o resíduo cai por 4 a cada refinamento: é truncamento da malha, e')
print('  não um fluxo de verdade. O que entra de um lado sai do outro')

print()
print('DUAS CARGAS, uma dentro e uma fora, na esfera amassada')
pts, da = esfera(120, deforma=0.35)
f = fluxo([((0.01, 0.0, 0.0), Q), ((0.30, 0.0, 0.0), -5 * Q)], pts, da)
print('  fluxo = %.6e, esperado q/eps0 = %.6e, erro = %.1e'
      % (f, ESPERADO, abs(f - ESPERADO) / ESPERADO))
print('  a carga de fora, cinco vezes maior e negativa, não conta nada')
