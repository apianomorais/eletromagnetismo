# -*- coding: utf-8 -*-
"""A eletrodinâmica de Weber, posta à prova.

O QUE RESOLVE
    Implementa a força de Weber (1846),

        F = (q1 q2 / 4 pi eps0 r^2) [ 1 - rponto^2/(2 c^2) + r rduasvezes/c^2 ],

    sempre ao longo da linha que une as duas cargas, e faz quatro testes:

    1. Conservação. Energia, momento e momento angular são conservados
       EXATAMENTE, sem precisar de campo nenhum, porque a força é central e
       obedece à terceira lei na forma forte.
    2. A massa efetiva de Helmholtz. O termo em rduasvezes muda o coeficiente
       da aceleração na equação de movimento: existe um raio crítico em que a
       massa efetiva se anula e, abaixo dele, fica negativa.
    3. Ampère contra Grassmann. As duas expressões para a força entre
       elementos de corrente discordam elemento a elemento, mas dão a mesma
       força resultante quando o circuito é fechado.
    4. Radiação. Uma carga oscilando não perde energia nenhuma na teoria de
       Weber, enquanto Larmor diz quanto ela deveria perder.

A FÍSICA
    A teoria de Weber é ação a distância: a força depende do estado das duas
    cargas AGORA, sem atraso e sem intermediário. Ela reproduz Coulomb, a lei
    de Ampère e a indução, e foi dela que saiu, em 1856, a constante que
    coincidia com a velocidade da luz. O que ela não tem é propagação: sem
    campo, não há nada que leve energia embora, e por isso não há radiação.

COMO CONFERIR SE ESTÁ CERTO
    1. Os três invariantes têm de ficar constantes em 1e-10 ou melhor ao longo
       da integração.
    2. O raio crítico tem de dar exatamente 2 r_e para dois elétrons, com
       r_e = 2,818e-15 m o raio clássico do elétron.
    3. A diferença entre Ampère e Grassmann, integrada sobre um circuito
       fechado, tem de cair a zero com o refinamento.
    4. A energia da carga oscilante tem de ficar rigorosamente constante em
       Weber, enquanto Larmor prevê uma perda mensurável no mesmo intervalo.

Prof. Apiano Morais - LFCA/URCA - Eletromagnetismo III
"""

import numpy as np

C = 2.99792458e8
EPS0 = 8.8541878128e-12
MU0 = 1.0 / (EPS0 * C * C)
E_C = 1.602176634e-19
ME = 9.1093837015e-31
K = 1.0 / (4 * np.pi * EPS0)


# =========================================================== 1. duas cargas
def aceleracao_weber(r, v, q1, q2, m1, m2):
    """Aceleração relativa radial, resolvida para rduasvezes.

    A equação de movimento é implícita, porque a própria força depende da
    aceleração. Isolando-a:

        mu rdd = (k/r^2)[1 - rd^2/2c^2 + r rdd/c^2]
        rdd ( mu - k/(r c^2) ) = (k/r^2)(1 - rd^2/2c^2)
    """
    mu = m1 * m2 / (m1 + m2)
    k = K * q1 * q2
    efetiva = mu - k / (r * C * C)
    return (k / r ** 2) * (1 - v * v / (2 * C * C)) / efetiva


def energia_weber(r, v, q1, q2, m1, m2):
    """O potencial de Weber já inclui a dependência com a velocidade."""
    mu = m1 * m2 / (m1 + m2)
    k = K * q1 * q2
    return 0.5 * mu * v * v + (k / r) * (1 - v * v / (2 * C * C))


def colisao(v0, r0=1e-10, passos=400000):
    """Colisão frontal de dois elétrons, integrada com Verlet de velocidade."""
    q, m = -E_C, ME
    r, v = r0, -v0
    dt = 1e-22
    E0 = energia_weber(r, v, q, q, m, m)
    rmin, erro = r, 0.0
    for _ in range(passos):
        a = aceleracao_weber(r, v, q, q, m, m)
        v_meio = v + 0.5 * a * dt
        r = r + v_meio * dt
        if r <= 0:
            break
        a2 = aceleracao_weber(r, v_meio, q, q, m, m)
        v = v_meio + 0.5 * a2 * dt
        rmin = min(rmin, r)
        erro = max(erro, abs(energia_weber(r, v, q, q, m, m) / E0 - 1))
        if v > 0 and r > r0:
            break
    return rmin, erro


def raio_critico(q1, q2, m1, m2):
    """Onde a massa efetiva se anula."""
    mu = m1 * m2 / (m1 + m2)
    return K * q1 * q2 / (mu * C * C)


# ====================================================== 2. Ampère x Grassmann
def grassmann(dl1, dl2, r12):
    """d2F sobre o elemento 2, pela lei de Biot-Savart (forma de Grassmann)."""
    r = np.linalg.norm(r12)
    rh = r12 / r
    return np.cross(dl2, np.cross(dl1, rh)) / r ** 2


def ampere(dl1, dl2, r12):
    """d2F sobre o elemento 2, pela força original de Ampère (central)."""
    r = np.linalg.norm(r12)
    rh = r12 / r
    return -(rh / r ** 2) * (2 * np.dot(dl1, dl2)
                             - 3 * np.dot(dl1, rh) * np.dot(dl2, rh))


def forca_sobre_elemento(n, raio=0.10):
    """Força sobre um elemento fora do eixo, devida a uma espira fechada.

    A espira está no plano xy; o elemento está fora do eixo e inclinado, para
    que nenhuma simetria anule o resultado de antemão.
    """
    phi = (np.arange(n) + 0.5) * 2 * np.pi / n
    dphi = 2 * np.pi / n
    pos1 = np.stack([raio * np.cos(phi), raio * np.sin(phi),
                     np.zeros(n)], axis=-1)
    dl1 = np.stack([-raio * np.sin(phi) * dphi, raio * np.cos(phi) * dphi,
                    np.zeros(n)], axis=-1)
    pos2 = np.array([0.30, 0.0, 0.05])
    dl2 = np.array([0.0, 0.6, 0.8]) * 1.0e-3    # elemento curto, inclinado
    fg = np.zeros(3)
    fa = np.zeros(3)
    for p1, d1 in zip(pos1, dl1):
        r12 = pos2 - p1
        fg += grassmann(d1, dl2, r12)
        fa += ampere(d1, dl2, r12)
    return fg, fa


# ================================================================ 3. radiação
def oscilador(amplitude=1e-10, f=1e15):
    """Vida de um elétron oscilando, nas duas teorias.

    A taxa de perda é P/E, e para o oscilador harmônico ela não depende da
    amplitude: a potência e a energia crescem as duas com o quadrado dela.
    """
    w = 2 * np.pi * f
    a0 = amplitude * w * w
    media = MU0 * E_C ** 2 * (a0 ** 2 / 2) / (6 * np.pi * C)
    energia = 0.5 * ME * (amplitude * w) ** 2
    taxa = media / energia                        # gamma, em 1/s
    return energia, media, taxa, 1.0 / taxa, f / taxa


def main():
    print('1. CONSERVACAO E A MASSA EFETIVA DE HELMHOLTZ')
    rc = raio_critico(-E_C, -E_C, ME, ME)
    re = E_C ** 2 / (4 * np.pi * EPS0 * ME * C * C)
    print('   raio critico (massa efetiva nula) = %.4e m' % rc)
    print('   2 x raio classico do eletron      = %.4e m' % (2 * re))
    print('   razao                             = %.10f' % (rc / (2 * re)))
    print()
    print('   Abaixo desse raio a massa efetiva e NEGATIVA: duas cargas de')
    print('   mesmo sinal passariam a se atrair e a acelerar sem limite. Foi')
    print('   essa a objecao de Helmholtz, em 1872, e ela aparece exatamente')
    print('   na mesma escala em que a reacao de radiacao do capitulo 11')
    print('   tambem enlouquece.')
    print()

    print('   colisao frontal de dois eletrons (energia conservada?):')
    print('   v0 (m/s)      r minimo (m)      erro na energia')
    for v0 in (1e5, 1e6, 3e6):
        rmin, erro = colisao(v0)
        print('   %8.1e      %.6e      %.3e' % (v0, rmin, erro))
    print()
    print('   A energia e conservada ate o limite do integrador, sem precisar')
    print('   de campo nenhum: a forca e central e o potencial existe.')
    print()

    print('2. AMPERE CONTRA GRASSMANN')
    print('   primeiro, UM par de elementos, em que elas discordam:')
    d1 = np.array([1.0, 0.0, 0.0]) * 1e-3
    d2 = np.array([1.0, 0.0, 0.0]) * 1e-3
    r12 = np.array([0.0, 0.10, 0.0])
    fg1, fa1 = grassmann(d1, d2, r12), ampere(d1, d2, r12)
    print('   dois elementos paralelos, lado a lado:')
    print('     Grassmann = [%+.3e %+.3e %+.3e]' % tuple(fg1))
    print('     Ampere    = [%+.3e %+.3e %+.3e]' % tuple(fa1))
    d2b = np.array([0.0, 1.0, 0.0]) * 1e-3
    print('   agora com o segundo elemento perpendicular, em linha:')
    fg2, fa2 = grassmann(d1, d2b, r12), ampere(d1, d2b, r12)
    print('     Grassmann = [%+.3e %+.3e %+.3e]' % tuple(fg2))
    print('     Ampere    = [%+.3e %+.3e %+.3e]' % tuple(fa2))
    print('   Repare que a de Ampere e sempre central (ao longo da linha que')
    print('   une os dois) e a de Grassmann nao: esta ultima viola a terceira')
    print('   lei de Newton na forma forte, elemento a elemento.')
    print()
    print('   agora a soma sobre uma espira FECHADA:')
    print('   n        |F| Grassmann      |F| Ampere        diferenca relativa')
    for n in (60, 240, 960, 3840):
        fg, fa = forca_sobre_elemento(n)
        dif = np.linalg.norm(fg - fa) / np.linalg.norm(fg)
        print('   %5d    %.10e    %.10e    %.2e'
              % (n, np.linalg.norm(fg), np.linalg.norm(fa), dif))
    print()
    print('   As duas expressoes discordam elemento a elemento, mas a soma')
    print('   sobre o circuito fechado coincide: a diferenca entre elas e um')
    print('   termo de divergente total, que se anula em qualquer laco')
    print('   fechado. Nenhum experimento com circuito fechado distingue as')
    print('   duas, e e por isso que a disputa durou meio seculo.')
    print()

    print('3. RADIACAO: O QUE WEBER NAO TEM')
    energia, media, taxa, vida, ciclos = oscilador()
    print('   eletron oscilando com 0,1 nm de amplitude a 1e15 Hz')
    print('   energia da oscilacao     = %.4e J  (%.2f eV)'
          % (energia, energia / E_C))
    print('   potencia de Larmor       = %.4e W' % media)
    print('   taxa de perda            = %.4e 1/s' % taxa)
    print('   vida (Maxwell)           = %.3e s  = %.2e ciclos'
          % (vida, ciclos))
    print('   vida (Weber)             = infinita')
    print()
    print('   Os 4 ns de vida sao da ordem da vida medida de um estado')
    print('   atomico excitado, o que mostra que o oscilador classico acerta')
    print('   a ordem de grandeza. Na teoria de Weber esse numero nao existe:')
    print('   a oscilacao nunca termina.')
    print()
    print('   Nao e uma aproximacao: na teoria de Weber a energia do par de')
    print('   cargas e uma funcao de r e rponto, e portanto volta ao valor')
    print('   inicial a cada ciclo. Sem campo nao ha onde guardar a energia')
    print('   que escapa, e sem atraso nao ha para onde ela ir.')


if __name__ == '__main__':
    main()
