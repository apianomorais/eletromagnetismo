# -*- coding: utf-8 -*-
"""Figuras dos exemplos resolvidos, em SVG.

São desenhos de geometria, não gráficos: o que o aluno precisa ver é onde
está cada coisa e para onde aponta cada vetor. SVG, porque escala sem perder
nitidez e porque o arquivo fica pequeno.

As cores vêm da paleta do site (grafite e cobre).
"""
import io
import math
import pathlib

RAIZ = pathlib.Path(__file__).resolve().parent.parent
IMG = RAIZ / 'assets' / 'img'

TINTA = '#2b3240'
SUAVE = '#4f5a6b'
COBRE = '#b05a1f'
VERDE = '#2c6e63'
CLARO = '#edf0f4'
BORDA = '#c9d2db'
FONTE = 'Iowan Old Style, Palatino Linotype, Palatino, Georgia, serif'


def svg(largura, altura, miolo, titulo):
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" '
            'width="%d" height="%d" font-family="%s" role="img" '
            'aria-label="%s">\n%s\n</svg>\n'
            % (largura, altura, largura, altura, FONTE, titulo, miolo))


def seta(x0, y0, x1, y1, cor=TINTA, esp=3.0, tam=13, tracejada=False):
    dx, dy = x1 - x0, y1 - y0
    n = math.hypot(dx, dy) or 1.0
    ux, uy = dx / n, dy / n
    xe, ye = x1 - tam * 0.9 * ux, y1 - tam * 0.9 * uy
    px, py = -uy, ux
    traco = ' stroke-dasharray="9 7"' if tracejada else ''
    return ('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
            'stroke-width="%.1f" stroke-linecap="round"%s/>'
            '<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="%s"/>'
            % (x0, y0, xe, ye, cor, esp, traco,
               x1, y1,
               x1 - tam * ux + tam * 0.42 * px, y1 - tam * uy + tam * 0.42 * py,
               x1 - tam * ux - tam * 0.42 * px, y1 - tam * uy - tam * 0.42 * py,
               cor))


def texto(x, y, s, cor=TINTA, tam=19, anc='middle', italico=False):
    return ('<text x="%.1f" y="%.1f" font-size="%d" fill="%s" '
            'text-anchor="%s"%s>%s</text>'
            % (x, y, tam, cor, anc, ' font-style="italic"' if italico else '', s))


def entra(x, y, r=9, cor=TINTA):
    """Símbolo de vetor entrando na tela: círculo com um xis."""
    k = r * 0.62
    return ('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="%s" '
            'stroke-width="2"/>'
            '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2"/>'
            '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2"/>'
            % (x, y, r, cor, x - k, y - k, x + k, y + k, cor,
               x + k, y - k, x - k, y + k, cor))


def sai(x, y, r=9, cor=TINTA):
    """Vetor saindo da tela: círculo com um ponto."""
    return ('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="%s" '
            'stroke-width="2"/><circle cx="%.1f" cy="%.1f" r="2.6" fill="%s"/>'
            % (x, y, r, cor, x, y, cor))


# ---------------------------------------------------------------------------
def balanca_de_corrente():
    """A espira pendurada com um lado dentro do campo, e a massa no outro prato."""
    p = []
    L, A = 620, 420
    # peças polares
    p.append('<rect x="150" y="150" width="300" height="150" rx="6" fill="%s" '
             'stroke="%s" stroke-width="2"/>' % (CLARO, BORDA))
    for i in range(5):
        for j in range(2):
            p.append(entra(195 + i * 55, 195 + j * 60, 9, SUAVE))
    p.append(texto(300, 388, 'campo uniforme, entrando na tela', SUAVE, 17))

    # a espira
    p.append('<path d="M250,40 L250,260 L390,260 L390,40" fill="none" '
             'stroke="%s" stroke-width="5" stroke-linejoin="round"/>' % COBRE)
    p.append(seta(300, 260, 352, 260, COBRE, 3.2))
    p.append(texto(320, 288, 'I', COBRE, 21, italico=True))
    # cota do lado a
    p.append('<line x1="250" y1="320" x2="390" y2="320" stroke="%s" '
             'stroke-width="1.6"/>' % SUAVE)
    p.append(seta(252, 320, 250, 320, SUAVE, 1.6, 9))
    p.append(seta(388, 320, 390, 320, SUAVE, 1.6, 9))
    p.append(texto(320, 342, 'a', SUAVE, 19, italico=True))

    # a força magnética para cima
    p.append(seta(320, 252, 320, 172, VERDE, 3.4))
    p.append('<rect x="78" y="196" width="112" height="30" rx="5" '
             'fill="#ffffff" opacity="0.92"/>')
    p.append(texto(134, 218, 'F = I a B', VERDE, 19, italico=True))
    p.append('<line x1="192" y1="211" x2="306" y2="211" stroke="%s" '
             'stroke-width="1.4"/>' % VERDE)

    # o braço da balança e a massa
    p.append('<line x1="250" y1="40" x2="560" y2="40" stroke="%s" '
             'stroke-width="3"/>' % TINTA)
    p.append('<circle cx="405" cy="40" r="6" fill="%s"/>' % TINTA)
    p.append('<line x1="405" y1="40" x2="405" y2="26" stroke="%s" '
             'stroke-width="3"/>' % TINTA)
    p.append('<line x1="530" y1="40" x2="530" y2="95" stroke="%s" '
             'stroke-width="2"/>' % SUAVE)
    p.append('<rect x="498" y="95" width="64" height="44" rx="5" fill="%s" '
             'stroke="%s" stroke-width="2"/>' % (CLARO, TINTA))
    p.append(texto(530, 124, 'm', TINTA, 21, italico=True))
    p.append(seta(530, 145, 530, 205, TINTA, 3.0))
    p.append(texto(530, 230, 'mg', TINTA, 19, italico=True))

    io.open(IMG / 'cap05_balanca.svg', 'w', encoding='utf-8').write(
        svg(L, A, '\n'.join(p), 'Balança de corrente'))
    return 'cap05_balanca.svg'


# ---------------------------------------------------------------------------
def cabo_coaxial():
    """Corte do cabo, com as quatro regiões, e o perfil de B ao lado."""
    p = []
    L, A = 760, 400
    cx, cy = 200, 200
    a, b, c = 38, 92, 124

    p.append('<circle cx="%d" cy="%d" r="%d" fill="%s" stroke="%s" '
             'stroke-width="2"/>' % (cx, cy, c, CLARO, BORDA))
    p.append('<circle cx="%d" cy="%d" r="%d" fill="#ffffff" stroke="%s" '
             'stroke-width="2"/>' % (cx, cy, b, BORDA))
    p.append('<circle cx="%d" cy="%d" r="%d" fill="%s" stroke="%s" '
             'stroke-width="2"/>' % (cx, cy, a, COBRE, COBRE))
    p.append(sai(cx, cy, 11, '#ffffff'))
    p.append(texto(cx, cy + 58, 'I', '#ffffff', 20, italico=True))

    for k in range(10):
        ang = 2 * math.pi * k / 10 + 0.3
        rr = (b + c) / 2
        p.append(entra(cx + rr * math.cos(ang), cy + rr * math.sin(ang), 8, SUAVE))

    # raios cotados
    for r, rot, ang in ((a, 'a', -0.42), (b, 'b', -1.15), (c, 'c', -1.95)):
        xx, yy = cx + r * math.cos(ang), cy + r * math.sin(ang)
        p.append('<line x1="%d" y1="%d" x2="%.1f" y2="%.1f" stroke="%s" '
                 'stroke-width="1.4" stroke-dasharray="5 5"/>'
                 % (cx, cy, xx, yy, SUAVE))
        p.append('<circle cx="%.1f" cy="%.1f" r="3" fill="%s"/>' % (xx, yy, SUAVE))
        p.append(texto(xx + 13 * math.cos(ang), yy + 13 * math.sin(ang) + 6,
                       rot, SUAVE, 17, italico=True))
    p.append(texto(cx, cy + c + 34, 'corte do cabo', SUAVE, 17))

    # perfil de B(s)
    ox, oy, LW, AH = 400, 322, 320, 215
    p.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" '
             'stroke-width="2"/>' % (ox, oy, ox + LW, oy, SUAVE))
    p.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" '
             'stroke-width="2"/>' % (ox, oy, ox, oy - AH, SUAVE))
    p.append(texto(ox + LW - 4, oy + 26, 's', SUAVE, 18, anc='end', italico=True))
    p.append(texto(ox - 14, oy - AH + 4, 'B', SUAVE, 18, anc='end', italico=True))

    esc = LW / 170.0
    pico = AH * 0.78
    pts = []
    for i in range(0, 171):
        s = i
        if s <= 40:
            B = (s / 40.0)
        elif s <= 100:
            B = 40.0 / s
        elif s <= 140:
            B = (40.0 / s) * (140.0 ** 2 - s ** 2) / (140.0 ** 2 - 100.0 ** 2)
        else:
            B = 0.0
        pts.append('%.1f,%.1f' % (ox + s * esc, oy - B * pico))
    p.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="3.2" '
             'stroke-linejoin="round"/>' % (' '.join(pts), COBRE))
    for s, rot in ((40, 'a'), (100, 'b'), (140, 'c')):
        p.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" '
                 'stroke-width="1.2" stroke-dasharray="4 5"/>'
                 % (ox + s * esc, oy, ox + s * esc, oy - AH * 0.9, BORDA))
        p.append(texto(ox + s * esc, oy + 24, rot, SUAVE, 17, italico=True))
    p.append(texto(ox + LW * 0.52, oy - AH - 10,
                   'cresce, cai como 1/s, cai mais rápido, zera', SUAVE, 16))

    io.open(IMG / 'cap05_coaxial.svg', 'w', encoding='utf-8').write(
        svg(L, A, '\n'.join(p), 'Cabo coaxial'))
    return 'cap05_coaxial.svg'


# ---------------------------------------------------------------------------
def casca_girante():
    """A casca esférica girante: campo uniforme dentro, dipolo fora."""
    p = []
    L, A = 640, 430
    cx, cy, R = 300, 215, 130

    # linhas de dipolo, do lado de fora
    for f in (1.35, 1.75, 2.25):
        rr = R * f
        p.append('<path d="M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f" '
                 'fill="none" stroke="%s" stroke-width="2" opacity="0.55"/>'
                 % (cx, cy - R + 4, cx + rr, cy - rr * 0.65,
                    cx + rr, cy + rr * 0.65, cx, cy + R - 4, SUAVE))
        p.append('<path d="M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f" '
                 'fill="none" stroke="%s" stroke-width="2" opacity="0.55"/>'
                 % (cx, cy - R + 4, cx - rr, cy - rr * 0.65,
                    cx - rr, cy + rr * 0.65, cx, cy + R - 4, SUAVE))

    p.append('<circle cx="%d" cy="%d" r="%d" fill="%s" stroke="%s" '
             'stroke-width="3"/>' % (cx, cy, R, CLARO, TINTA))

    # campo interno uniforme
    for dx in (-62, -21, 20, 61):
        p.append(seta(cx + dx, cy + 74, cx + dx, cy - 74, COBRE, 3.0, 12))
    p.append('<rect x="%d" y="%d" width="150" height="54" rx="6" fill="#ffffff" '
             'opacity="0.93"/>' % (cx + R + 36, cy - 96))
    p.append(texto(cx + R + 48, cy - 72, 'B uniforme', COBRE, 18, anc='start'))
    p.append(texto(cx + R + 48, cy - 50, 'dentro da casca', COBRE, 17, anc='start'))
    p.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" '
             'stroke-width="1.4"/>' % (cx + R + 34, cy - 66, cx + 72, cy - 40, COBRE))

    # eixo e rotação
    p.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" '
             'stroke-width="1.6" stroke-dasharray="8 6"/>'
             % (cx, cy - R - 58, cx, cy + R + 44, SUAVE))
    arco = []
    for k in range(41):
        t = -2.5 + 5.0 * k / 40
        arco.append('%.1f,%.1f' % (cx + 46 * math.sin(t) * 0.9,
                                   cy - R - 30 + 16 * math.cos(t)))
    p.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="3"/>'
             % (' '.join(arco), VERDE))
    p.append(seta(cx + 34, cy - R - 42, cx + 46, cy - R - 28, VERDE, 3, 11))
    p.append(texto(cx - 74, cy - R - 28, 'ω', VERDE, 22, italico=True))

    # corrente de superfície
    for ang, lado in ((0.6, -1), (2.54, 1)):
        x = cx + (R + 13) * math.cos(ang)
        y = cy + (R + 13) * math.sin(ang)
        p.append(sai(x, y, 9, VERDE) if lado > 0 else entra(x, y, 9, VERDE))
    p.append(texto(cx + 150, cy + 96, 'K = σ v', VERDE, 18, anc='start',
                   italico=True))
    p.append(texto(cx, cy + R + 72, 'casca de raio R, carga Q, girando', SUAVE, 17))

    io.open(IMG / 'cap05_casca.svg', 'w', encoding='utf-8').write(
        svg(L, A, '\n'.join(p), 'Casca esférica girante'))
    return 'cap05_casca.svg'


# ---------------------------------------------------------------------------
def forca_de_lorentz():
    """Para onde aponta qv x B: o caso positivo, o negativo e a regra da mão."""
    p = []
    L, A = 960, 420
    cy = 180

    def painel(x0, sinal):
        """Campo entrando na tela, velocidade para a direita, força vertical."""
        q = []
        cx = x0 + 140
        q.append('<rect x="%d" y="%d" width="260" height="210" rx="8" '
                 'fill="%s" stroke="%s" stroke-width="1.6"/>'
                 % (x0 + 10, cy - 100, CLARO, BORDA))
        for i in range(4):
            for j in range(3):
                q.append(entra(x0 + 45 + i * 62, cy - 72 + j * 72, 8, SUAVE))
        # a carga, com o sinal dentro
        q.append('<circle cx="%d" cy="%d" r="17" fill="#ffffff" stroke="%s" '
                 'stroke-width="2.6"/>' % (cx, cy, COBRE))
        q.append(texto(cx, cy + 8, '+' if sinal > 0 else '−', COBRE, 24))
        # velocidade, sempre para a direita
        q.append(seta(cx + 20, cy, cx + 104, cy, TINTA, 3.2))
        q.append(texto(cx + 112, cy + 7, 'v', TINTA, 21, anc='start', italico=True))
        # força: para cima se a carga é positiva, para baixo se é negativa
        ya, yb = (cy - 22, cy - 96) if sinal > 0 else (cy + 22, cy + 96)
        q.append(seta(cx, ya, cx, yb, VERDE, 3.4))
        q.append(texto(cx + 14, yb + (6 if sinal > 0 else 16),
                       'F', VERDE, 21, anc='start', italico=True))
        rot = 'carga positiva' if sinal > 0 else 'carga negativa'
        q.append(texto(cx, cy + 142, rot, SUAVE, 17))
        if sinal < 0:
            q.append(texto(cx, cy + 166, 'com os mesmos v e B', SUAVE, 17))
        return q

    p += painel(10, +1)
    p += painel(330, -1)
    p.append(texto(150, cy - 120, 'B entrando na tela', SUAVE, 17))
    p.append(texto(470, cy - 120, 'B entrando na tela', SUAVE, 17))

    # ------------------------------------------------ o caso geral, em espaço
    ox, oy = 740, cy + 30
    p.append(seta(ox, oy, ox + 96, oy + 28, TINTA, 3.2))
    p.append(texto(ox + 104, oy + 40, 'v', TINTA, 21, anc='start', italico=True))
    p.append(seta(ox, oy, ox - 58, oy - 40, SUAVE, 3.2))
    p.append(texto(ox - 70, oy - 46, 'B', SUAVE, 21, anc='end', italico=True))
    p.append(seta(ox, oy, ox, oy - 104, VERDE, 3.4))
    p.append(texto(ox + 12, oy - 104, 'F = q v × B', VERDE, 19,
                   anc='start', italico=True))
    p.append('<circle cx="%d" cy="%d" r="4.5" fill="%s"/>' % (ox, oy, COBRE))
    p.append(texto(ox + 20, cy + 142, 'os dedos ao longo de v,', SUAVE, 17))
    p.append(texto(ox + 20, cy + 166, 'dobrando para B: o polegar dá F',
                   SUAVE, 17))

    io.open(IMG / 'cap05_lorentz.svg', 'w', encoding='utf-8').write(
        svg(L, A, '\n'.join(p), 'Orientação da força magnética'))
    return 'cap05_lorentz.svg'


def main():
    IMG.mkdir(parents=True, exist_ok=True)
    for fn in (forca_de_lorentz, balanca_de_corrente, cabo_coaxial, casca_girante):
        print('  ' + fn())


if __name__ == '__main__':
    main()
