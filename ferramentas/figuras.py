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


# ---------------------------------------------------------------------------
def torque_na_espira():
    """A espira inclinada no campo uniforme: o binário e o braço b sen(theta)."""
    import math as _m
    p = []
    L, A = 940, 480
    tet = math.radians(38)

    def campo(x0, x1, cy, rotulo):
        """Fundo de campo uniforme: setas horizontais, bem claras."""
        q = []
        for j in range(5):
            y = cy - 152 + j * 76
            q.append(seta(x0, y, x1, y, BORDA, 2.2, 11))
        if rotulo:
            q.append(texto(x1 - 6, cy - 166, 'B', SUAVE, 21, anc='end', italico=True))
        return q

    # ---------------------------------------------------- painel 1: inclinada
    ox, oy = 250, 215
    p += campo(40, 470, oy, True)
    meia = 88.0
    dx, dy = _m.sin(tet), _m.cos(tet)            # direção do plano, visto de perfil
    x1, y1 = ox + meia * dx, oy + meia * dy      # ponta de baixo, corrente saindo
    x2, y2 = ox - meia * dx, oy - meia * dy      # ponta de cima, corrente entrando

    # as linhas de ação das duas forças, e o braço entre elas
    for xx in (x1, x2):
        p.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" '
                 'stroke-width="1.3" stroke-dasharray="6 6"/>'
                 % (xx, oy - 160, xx, oy + 176, SUAVE))
    p.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" '
             'stroke-width="1.6"/>' % (x2, oy + 174, x1, oy + 174, SUAVE))
    p.append(seta(x2 + 2, oy + 174, x2, oy + 174, SUAVE, 1.6, 9))
    p.append(seta(x1 - 2, oy + 174, x1, oy + 174, SUAVE, 1.6, 9))
    p.append(texto((x1 + x2) / 2, oy + 198, 'b sen θ', SUAVE, 18, italico=True))

    # a espira, de perfil
    p.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
             'stroke-width="5" stroke-linecap="round"/>' % (x1, y1, x2, y2, COBRE))
    p.append(texto((ox + x1) / 2 - 20, (oy + y1) / 2 + 14, 'b', COBRE, 19,
                   italico=True))
    p.append(entra(x2, y2, 11, COBRE))
    p.append(sai(x1, y1, 11, COBRE))
    p.append(texto(x2 - 26, y2 - 10, 'a', COBRE, 19, anc='end', italico=True))

    # o binário
    p.append(seta(x2, y2 - 16, x2, y2 - 92, VERDE, 3.4))
    p.append(texto(x2 - 10, y2 - 92, 'F = I a B', VERDE, 19, anc='end', italico=True))
    p.append(seta(x1, y1 + 16, x1, y1 + 92, VERDE, 3.4))
    p.append(texto(x1 + 10, y1 + 96, 'F', VERDE, 19, anc='start', italico=True))

    # o momento magnético e o ângulo até o campo
    mx, my = ox + 96 * _m.cos(tet), oy - 96 * _m.sin(tet)
    p.append(seta(ox, oy, mx, my, TINTA, 3.2))
    p.append(texto(mx + 10, my - 6, 'm', TINTA, 21, anc='start', italico=True))
    p.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" '
             'stroke-width="1.3" stroke-dasharray="6 6"/>'
             % (ox, oy, ox + 104, oy, SUAVE))
    r = 56
    p.append('<path d="M %.1f %.1f A %d %d 0 0 0 %.1f %.1f" fill="none" '
             'stroke="%s" stroke-width="1.6"/>'
             % (ox + r, oy, r, r, ox + r * _m.cos(tet), oy - r * _m.sin(tet), SUAVE))
    p.append(texto(ox + r + 16, oy - 14, 'θ', SUAVE, 19, anc='start', italico=True))
    p.append('<circle cx="%d" cy="%d" r="4" fill="%s"/>' % (ox, oy, TINTA))
    p.append(texto(250, oy + 236, 'braço b sen θ, torque τ = m B sen θ', SUAVE, 17))

    # ----------------------------------------------------- painel 2: alinhada
    ox2, oy2 = 730, 215
    p += campo(560, 900, oy2, False)
    p.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" '
             'stroke-width="1.3" stroke-dasharray="6 6"/>'
             % (ox2, oy2 - 150, ox2, oy2 + 150, SUAVE))
    p.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" '
             'stroke-width="5" stroke-linecap="round"/>'
             % (ox2, oy2 - meia, ox2, oy2 + meia, COBRE))
    p.append(entra(ox2, oy2 - meia, 11, COBRE))
    p.append(sai(ox2, oy2 + meia, 11, COBRE))
    p.append(seta(ox2, oy2 - meia - 16, ox2, oy2 - meia - 92, VERDE, 3.4))
    p.append(seta(ox2, oy2 + meia + 16, ox2, oy2 + meia + 92, VERDE, 3.4))
    p.append(seta(ox2, oy2, ox2 + 96, oy2, TINTA, 3.2))
    p.append(texto(ox2 + 106, oy2 - 8, 'm', TINTA, 21, anc='start', italico=True))
    p.append('<circle cx="%d" cy="%d" r="4" fill="%s"/>' % (ox2, oy2, TINTA))
    p.append(texto(ox2, oy2 + 236, 'θ = 0: braço nulo, torque nulo,', SUAVE, 17))
    p.append(texto(ox2, oy2 + 260, 'e é onde a espira para', SUAVE, 17))

    io.open(IMG / 'cap06_torque.svg', 'w', encoding='utf-8').write(
        svg(L, A, '\n'.join(p), 'Torque sobre uma espira num campo uniforme'))
    return 'cap06_torque.svg'


# ---------------------------------------------------------------------------
def correntes_ligadas():
    """O empilhamento de espirinhas: o interior se cancela, a borda sobra."""
    p = []
    L, A = 940, 470
    x0, y0, cel, nc, nl = 60, 90, 86, 5, 3
    larg, alt = cel * nc, cel * nl

    p.append('<rect x="%d" y="%d" width="%d" height="%d" fill="%s" '
             'stroke="%s" stroke-width="1.6"/>' % (x0, y0, larg, alt, CLARO, BORDA))

    def circulacao(cx, cy, lado, cor, esp, tam):
        """Quatro setinhas no meio dos lados, girando no sentido anti-horário."""
        m = lado / 2.0 - 4
        d = lado * 0.3
        q = []
        q.append(seta(cx + m, cy + d, cx + m, cy - d, cor, esp, tam))   # sobe à direita
        q.append(seta(cx + d, cy - m, cx - d, cy - m, cor, esp, tam))   # vai à esquerda
        q.append(seta(cx - m, cy - d, cx - m, cy + d, cor, esp, tam))   # desce
        q.append(seta(cx - d, cy + m, cx + d, cy + m, cor, esp, tam))   # volta
        return q

    for i in range(nc):
        for j in range(nl):
            cx, cy = x0 + cel * (i + 0.5), y0 + cel * (j + 0.5)
            p.append('<rect x="%.1f" y="%.1f" width="%d" height="%d" fill="none" '
                     'stroke="%s" stroke-width="1" stroke-dasharray="4 4"/>'
                     % (cx - cel / 2, cy - cel / 2, cel, cel, BORDA))
            p += circulacao(cx, cy, cel, SUAVE, 1.8, 9)

    # a borda, que não tem com quem cancelar
    p += circulacao(x0 + larg / 2, y0 + alt / 2, 0, COBRE, 0, 0)[:0]
    cx, cy = x0 + larg / 2.0, y0 + alt / 2.0
    for xa, ya, xb, yb in ((x0 + larg, y0 + alt - 20, x0 + larg, y0 + 20),
                           (x0 + larg - 20, y0, x0 + 20, y0),
                           (x0, y0 + 20, x0, y0 + alt - 20),
                           (x0 + 20, y0 + alt, x0 + larg - 20, y0 + alt)):
        p.append(seta(xa, ya, xb, yb, COBRE, 4.0, 15))
    p.append(texto(x0 + larg / 2, y0 - 24,
                   'a corrente da borda contorna o objeto', COBRE, 18))
    p.append(texto(x0 + larg / 2, y0 + alt + 40,
                   'no interior, cada trecho encontra o do vizinho em sentido '
                   'oposto', SUAVE, 17))
    p.append(texto(x0 + larg / 2, y0 + alt + 64,
                   'e os dois se anulam', SUAVE, 17))

    # a ampliação de duas vizinhas
    zx, zy, z = 600, 120, 130
    p.append(texto(zx + z, zy - 26, 'duas vizinhas, de perto', SUAVE, 18))
    for k in (0, 1):
        q = zx + k * z
        p.append('<rect x="%d" y="%d" width="%d" height="%d" fill="%s" '
                 'stroke="%s" stroke-width="1.4"/>' % (q, zy, z, z, CLARO, BORDA))
        p += circulacao(q + z / 2, zy + z / 2, z, SUAVE, 2.4, 12)
    # o lado comum, com as duas setas opostas destacadas
    p.append('<rect x="%d" y="%d" width="32" height="%d" fill="%s"/>'
             % (zx + z - 16, zy + 10, z - 20, CLARO))
    p.append(seta(zx + z - 13, zy + z - 22, zx + z - 13, zy + 22, COBRE, 3.0, 13))
    p.append(seta(zx + z + 13, zy + 22, zx + z + 13, zy + z - 22, COBRE, 3.0, 13))
    p.append(texto(zx + z, zy + z + 36, 'no lado comum as correntes', COBRE, 17))
    p.append(texto(zx + z, zy + z + 60, 'são opostas: resultado nulo', COBRE, 17))

    io.open(IMG / 'cap06_ligadas.svg', 'w', encoding='utf-8').write(
        svg(L, A, '\n'.join(p), 'Cancelamento das correntes ligadas'))
    return 'cap06_ligadas.svg'


# ---------------------------------------------------------------------------
def laco_de_histerese():
    """O laço com os três números, e a comparação entre material doce e duro."""
    p = []
    L, A = 940, 480

    def eixos(ox, oy, lx, ly, rh, rb):
        q = [seta(ox - lx, oy, ox + lx, oy, SUAVE, 1.8, 11),
             seta(ox, oy + ly, ox, oy - ly, SUAVE, 1.8, 11),
             texto(ox + lx + 4, oy + 22, rh, SUAVE, 19, anc='end', italico=True),
             texto(ox + 18, oy - ly + 4, rb, SUAVE, 19, anc='start', italico=True)]
        return q

    def curva(pontos, cor, esp=2.6, traco=False):
        d = ' '.join('%.1f,%.1f' % (x, y) for x, y in pontos)
        t = ' stroke-dasharray="7 6"' if traco else ''
        return ('<polyline points="%s" fill="none" stroke="%s" stroke-width="%.1f" '
                'stroke-linejoin="round" stroke-linecap="round"%s/>' % (d, cor, esp, t))

    def ramo(ox, oy, ex, ey, hc, larg, sentido):
        """Um ramo do laço: B = tanh((H -+ Hc)/larg), já em coordenadas de tela."""
        pts = []
        n = 160
        for i in range(n + 1):
            h = -1.6 + 3.2 * i / n
            b = math.tanh((h - sentido * hc) / larg)
            pts.append((ox + h * ex, oy - b * ey))
        return pts if sentido > 0 else pts[::-1]

    # ------------------------------------------------- painel 1: os três números
    ox, oy, ex, ey = 240, 230, 118, 112
    hc, larg = 0.42, 0.34
    p += eixos(ox, oy, 180, 160, 'H', 'B')
    sobe = ramo(ox, oy, ex, ey, hc, larg, +1)
    desce = ramo(ox, oy, ex, ey, hc, larg, -1)
    p.append(curva(sobe, COBRE))
    p.append(curva(desce, COBRE))
    # a curva virgem, do material nunca magnetizado
    # A curva virgem tem de ficar DENTRO do laço: ela parte da origem e
    # encosta na saturação sem nunca cruzar nenhum dos dois ramos. A média
    # dos dois ramos satisfaz isso por construção, e é o que se mede.
    def primeira(h):
        return 0.5 * (math.tanh((h - hc) / larg) + math.tanh((h + hc) / larg))
    virgem = [(ox + h * ex, oy - primeira(h) * ey)
              for h in [1.6 * i / 120 for i in range(121)]]
    p.append(curva(virgem, VERDE, 2.2, True))
    p.append(texto(ox + 176, oy + 80, 'curva virgem, do material', VERDE, 17, anc='end'))
    p.append(texto(ox + 176, oy + 100, 'nunca magnetizado', VERDE, 17, anc='end'))

    br = math.tanh(hc / larg)
    p.append('<circle cx="%d" cy="%.1f" r="4.5" fill="%s"/>' % (ox, oy - br * ey, TINTA))
    p.append(texto(ox - 12, oy - br * ey - 10, 'remanência', TINTA, 17, anc='end'))
    p.append('<circle cx="%.1f" cy="%d" r="4.5" fill="%s"/>' % (ox - hc * ex, oy, TINTA))
    p.append(texto(ox - hc * ex - 10, oy + 26, 'coercividade', TINTA, 17, anc='end'))
    p.append(texto(ox + 176, oy - 68, 'saturação', TINTA, 17, anc='end'))
    # o sentido de percurso
    p.append(seta(ox + 30 * 1.0, oy - 104, ox + 62, oy - 108, COBRE, 2.4, 11))
    p.append(seta(ox - 30, oy + 104, ox - 62, oy + 108, COBRE, 2.4, 11))
    p.append(texto(ox, oy + 216, 'o caminho de ida não é o de volta', SUAVE, 17))

    # ---------------------------------------------- painel 2: doce contra duro
    ox2 = 700
    p += eixos(ox2, oy, 180, 160, 'H', 'B')
    for hcx, cor, rot, dy in ((0.08, VERDE, 'doce: transformador', 150),
                              (0.78, COBRE, 'duro: ímã permanente', 174)):
        p.append(curva(ramo(ox2, oy, ex, ey, hcx, larg, +1), cor, 2.4))
        p.append(curva(ramo(ox2, oy, ex, ey, hcx, larg, -1), cor, 2.4))
        p.append(texto(ox2 - 176, oy + dy, rot, cor, 17, anc='start'))
    p.append(texto(ox2, oy + 216, 'a área do laço é a energia perdida por ciclo',
                   SUAVE, 17))

    io.open(IMG / 'cap06_histerese.svg', 'w', encoding='utf-8').write(
        svg(L, A, '\n'.join(p), 'Laço de histerese'))
    return 'cap06_histerese.svg'


# ---------------------------------------------------------------------------
def condicoes_de_contorno():
    """O que salta e o que não salta ao atravessar uma folha de corrente."""
    p = []
    L, A = 940, 460
    cy = 215

    def folha(x0, x1, com_rotulo):
        q = ['<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" '
             'stroke-width="4" stroke-linecap="round"/>' % (x0, cy, x1, cy, COBRE)]
        n = int((x1 - x0) / 62)
        for i in range(n + 1):
            q.append(entra(x0 + 31 + i * 62, cy, 9, COBRE))
        if com_rotulo:
            q.append(texto(x1 - 4, cy - 18, 'K', COBRE, 20, anc='end', italico=True))
        return q

    # ------------------------------------------- painel 1: a componente normal
    ax0, ax1 = 40, 440
    p += folha(ax0, ax1, True)
    cx = (ax0 + ax1) // 2
    p.append('<rect x="%d" y="%d" width="150" height="54" rx="4" fill="none" '
             'stroke="%s" stroke-width="1.6" stroke-dasharray="7 6"/>'
             % (cx - 75, cy - 27, SUAVE))
    p.append(texto(cx - 92, cy + 46, 'tijolo achatado', SUAVE, 17, anc='end'))
    for dx in (-40, 40):
        p.append(seta(cx + dx, cy + 112, cx + dx, cy + 32, VERDE, 3.2))
        p.append(seta(cx + dx, cy - 32, cx + dx, cy - 112, VERDE, 3.2))
    perp = ('<tspan font-style="italic">B</tspan>'
            '<tspan font-size="14" dy="4">\u22a5</tspan>')
    p.append(texto(cx - 52, cy - 104, perp, VERDE, 20, anc='end'))
    p.append(texto(cx - 52, cy + 120, perp, VERDE, 20, anc='end'))
    p.append(texto(cx, cy + 176, 'o que entra por baixo sai por cima:', SUAVE, 17))
    p.append(texto(cx, cy + 200, 'a componente normal não salta', SUAVE, 17))

    # --------------------------------------- painel 2: a componente tangencial
    bx0, bx1 = 500, 900
    p += folha(bx0, bx1, True)
    dx = (bx0 + bx1) // 2
    p.append('<rect x="%d" y="%d" width="170" height="110" rx="4" fill="none" '
             'stroke="%s" stroke-width="1.6" stroke-dasharray="7 6"/>'
             % (dx - 85, cy - 55, SUAVE))
    p.append(texto(dx + 100, cy + 40, 'curva amperiana', SUAVE, 17, anc='start'))
    # o sentido de percurso, coerente com a corrente que entra na tela
    for xa, ya, xb, yb in ((dx - 85, cy + 20, dx - 85, cy - 20),
                           (dx - 20, cy - 55, dx + 20, cy - 55),
                           (dx + 85, cy - 20, dx + 85, cy + 20),
                           (dx + 20, cy + 55, dx - 20, cy + 55)):
        p.append(seta(xa, ya, xb, yb, SUAVE, 1.8, 10))
    # o campo da própria folha: para a direita em cima, para a esquerda embaixo
    p.append(seta(dx - 70, cy - 90, dx + 70, cy - 90, VERDE, 3.2))
    p.append(texto(dx, cy - 102, 'μ₀K/2', VERDE, 18))
    p.append(seta(dx + 70, cy + 90, dx - 70, cy + 90, VERDE, 3.2))
    p.append(texto(dx, cy + 118, 'μ₀K/2', VERDE, 18))
    p.append(texto(dx, cy + 176, 'a corrente enlaçada muda o lado esquerdo:', SUAVE, 17))
    p.append(texto(dx, cy + 200, 'a componente paralela salta de μ₀K', SUAVE, 17))

    io.open(IMG / 'cap05_contorno.svg', 'w', encoding='utf-8').write(
        svg(L, A, '\n'.join(p), 'Condições de contorno do campo magnético'))
    return 'cap05_contorno.svg'


# ---------------------------------------------------------------------------
def barra_nos_trilhos():
    """A barra deslizante: fem de movimento, corrente e freio magnético."""
    p = []
    L, A = 700, 460
    cy, meia = 210, 86
    x_res, x_barra, x_fim = 110, 380, 620

    # a região de campo
    p.append('<rect x="%d" y="%d" width="%d" height="%d" rx="6" fill="%s" '
             'stroke="%s" stroke-width="1.6"/>'
             % (x_res - 20, cy - meia - 40, x_fim - x_res + 60, 2 * meia + 80,
                CLARO, BORDA))
    for i in range(7):
        for j in range(3):
            xx = x_res + 12 + i * 78
            yy = cy - meia + 4 + j * (meia - 4)
            if abs(xx - x_barra) > 20:
                p.append(entra(xx, yy, 8, SUAVE))
    p.append(texto(L / 2, cy + meia + 64, 'campo uniforme B, entrando na tela',
                   SUAVE, 17))

    # a faixa varrida no intervalo dt
    p.append('<rect x="%d" y="%d" width="62" height="%d" fill="%s" '
             'opacity="0.5"/>' % (x_barra, cy - meia, 2 * meia, '#e6d3c2'))
    p.append(texto(x_barra + 31, cy - meia - 14, 'v dt', COBRE, 17, italico=True))

    # trilhos e resistor
    for yy in (cy - meia, cy + meia):
        p.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" '
                 'stroke-width="3.4"/>' % (x_res, yy, x_fim, yy, TINTA))
    p.append('<path d="M %d %d L %d %d L %d %d L %d %d L %d %d L %d %d L %d %d" '
             'fill="none" stroke="%s" stroke-width="3.4" stroke-linejoin="round"/>'
             % (x_res, cy - meia, x_res, cy - 48,
                x_res - 16, cy - 32, x_res + 16, cy - 8,
                x_res - 16, cy + 16, x_res + 16, cy + 40,
                x_res, cy + meia, TINTA))
    p.append(texto(x_res - 30, cy + 8, 'R', TINTA, 20, anc='end', italico=True))

    # a barra e a velocidade
    p.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" '
             'stroke-width="6" stroke-linecap="round"/>'
             % (x_barra, cy - meia, x_barra, cy + meia, COBRE))
    p.append(texto(x_barra - 16, cy + 48, 'h', COBRE, 20, anc='end', italico=True))
    p.append(seta(x_barra + 70, cy - meia - 26, x_barra + 150, cy - meia - 26,
                  TINTA, 3.2))
    p.append(texto(x_barra + 160, cy - meia - 20, 'v', TINTA, 21, anc='start',
                   italico=True))

    # a corrente: sobe na barra, volta pelo circuito
    p.append(seta(x_barra, cy + 40, x_barra, cy - 40, COBRE, 3.0))
    p.append(texto(x_barra + 16, cy - 10, 'I', COBRE, 20, anc='start', italico=True))
    p.append(seta(x_barra - 60, cy - meia, x_barra - 130, cy - meia, COBRE, 2.6))
    p.append(seta(x_res + 130, cy + meia, x_res + 200, cy + meia, COBRE, 2.6))

    # a força magnética sobre a barra, contra o movimento
    p.append(seta(x_barra - 8, cy + meia + 30, x_barra - 92, cy + meia + 30,
                  VERDE, 3.4))
    p.append(texto(x_barra - 100, cy + meia + 36, 'F = I h B', VERDE, 19,
                   anc='end', italico=True))

    p.append(texto(L / 2, cy + meia + 112,
                   'a fem vale v B h, e a força magnética freia:', SUAVE, 17))
    p.append(texto(L / 2, cy + meia + 136,
                   'quem gasta energia é quem puxa', SUAVE, 17))

    io.open(IMG / 'cap07_barra.svg', 'w', encoding='utf-8').write(
        svg(L, A, '\n'.join(p), 'Barra deslizante nos trilhos'))
    return 'cap07_barra.svg'


# ---------------------------------------------------------------------------
def campo_induzido():
    """A região de campo crescente e as linhas de E, dentro e fora."""
    p = []
    L, A = 620, 580
    cx, cy, R = 310, 268, 105

    p.append('<circle cx="%d" cy="%d" r="%d" fill="%s" stroke="%s" '
             'stroke-width="2"/>' % (cx, cy, R, CLARO, BORDA))
    for ang, raio in ((0.4, 58), (1.9, 58), (3.4, 58), (4.9, 58),
                      (1.0, 0), (2.5, 95), (5.6, 95), (4.0, 95)):
        p.append(sai(cx + raio * math.cos(ang), cy + raio * math.sin(ang), 9, SUAVE))
    legenda_topo = (cx, cy - 1.6 * R - 44)

    # linhas de E: dentro proporcional a s, fora caindo como 1/s
    def circulo(raio, cor, esp, traco=False):
        t = ' stroke-dasharray="7 6"' if traco else ''
        return ('<circle cx="%d" cy="%d" r="%.1f" fill="none" stroke="%s" '
                'stroke-width="%.1f"%s/>' % (cx, cy, raio, cor, esp, t))

    for raio, esp in ((0.45 * R, 2.0), (0.8 * R, 2.4), (1.25 * R, 2.0),
                      (1.6 * R, 1.6)):
        p.append(circulo(raio, COBRE, esp, raio > R))
        # a ponta, no topo do círculo: sentido horário (lei de Lenz)
        p.append(seta(cx - 12, cy - raio, cx + 14, cy - raio, COBRE, esp))
    p.append(texto(cx + 0.8 * R + 14, cy + 6, 'E', COBRE, 20, anc='start',
                   italico=True))

    p.append(texto(legenda_topo[0], legenda_topo[1] - 24,
                   'B crescendo, saindo da tela,', SUAVE, 17))
    p.append(texto(legenda_topo[0], legenda_topo[1],
                   'dentro do círculo de raio R', SUAVE, 17))
    p.append(texto(cx, cy + 1.6 * R + 56,
                   'dentro, E cresce com s; fora, cai com 1/s', SUAVE, 17))
    p.append(texto(cx, cy + 1.6 * R + 80,
                   'há campo elétrico onde o magnético é nulo', SUAVE, 17))

    io.open(IMG / 'cap07_induzido.svg', 'w', encoding='utf-8').write(
        svg(L, A, '\n'.join(p), 'Campo elétrico induzido'))
    return 'cap07_induzido.svg'


# ---------------------------------------------------------------------------
def duas_superficies():
    """O capacitor carregando e as duas superfícies apoiadas na mesma curva."""
    p = []
    L, A = 880, 470
    cy = 210
    xa, xb = 470, 520          # placas

    # o saco vai por baixo de tudo, senão esconde o fio e as placas
    p.append('<path d="M 320 %d C 330 %d, 700 %d, 700 %d C 700 %d, 330 %d, 320 %d" '
             'fill="%s" opacity="0.34" stroke="%s" stroke-width="2" '
             'stroke-dasharray="8 6"/>'
             % (cy - 100, cy - 186, cy - 186, cy,
                cy + 186, cy + 186, cy + 100, '#e6d3c2', COBRE))

    # o fio e as placas
    p.append('<line x1="60" y1="%d" x2="%d" y2="%d" stroke="%s" '
             'stroke-width="4"/>' % (cy, xa, cy, TINTA))
    p.append('<line x1="%d" y1="%d" x2="820" y2="%d" stroke="%s" '
             'stroke-width="4"/>' % (xb, cy, cy, TINTA))
    for x, sinal in ((xa, '+'), (xb, '\u2212')):
        p.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" '
                 'stroke-width="6" stroke-linecap="round"/>'
                 % (x, cy - 74, x, cy + 74, COBRE))
        p.append(texto(x + (-18 if sinal == '+' else 18), cy - 92, sinal,
                       COBRE, 22))
    for j in range(5):
        yy = cy - 56 + j * 28
        p.append(seta(xa + 8, yy, xb - 8, yy, VERDE, 2.0, 9))
    p.append(texto((xa + xb) / 2, cy + 104, 'E crescendo', VERDE, 17))
    p.append(seta(150, cy - 24, 230, cy - 24, TINTA, 3.0))
    p.append(texto(190, cy - 36, 'I', TINTA, 20, italico=True))

    # a curva amperiana vista de perfil, e a superfície plana apoiada nela
    p.append('<ellipse cx="320" cy="%d" rx="26" ry="100" fill="%s" '
             'opacity="0.55" stroke="%s" stroke-width="2.4" '
             'stroke-dasharray="8 6"/>' % (cy, '#cfe0d8', COBRE))
    p.append(texto(320, cy - 122, 'a mesma curva', COBRE, 17))

    p.append(texto(236, cy + 156, 'superfície plana:', VERDE, 17, anc='end'))
    p.append(texto(236, cy + 180, 'o fio a atravessa, enlaça I', VERDE, 17,
                   anc='end'))
    p.append('<line x1="244" y1="%d" x2="302" y2="%d" stroke="%s" '
             'stroke-width="1.4"/>' % (cy + 150, cy + 96, VERDE))

    p.append(texto(700, cy + 156, 'superfície em saco:', COBRE, 17))
    p.append(texto(700, cy + 180, 'passa entre as placas, não enlaça corrente',
                   COBRE, 17))

    p.append(texto(L / 2, cy + 232,
                   'sem o termo de Maxwell as duas dariam respostas diferentes',
                   SUAVE, 17))

    io.open(IMG / 'cap07_superficies.svg', 'w', encoding='utf-8').write(
        svg(L, A, '\n'.join(p), 'As duas superfícies amperianas'))
    return 'cap07_superficies.svg'


# ---------------------------------------------------------------------------
def cargas_ligadas():
    """Os dipolos alinhados: o interior se cancela, as faces sobram."""
    p = []
    L, A = 880, 430
    x0, y0, cel, nc, nl = 70, 80, 80, 7, 3
    larg, alt = cel * nc, cel * nl

    p.append('<rect x="%d" y="%d" width="%d" height="%d" rx="4" fill="%s" '
             'stroke="%s" stroke-width="1.6"/>'
             % (x0, y0, larg, alt, CLARO, BORDA))

    # cada dipolo: um par de cargas, a negativa à esquerda e a positiva à direita
    for i in range(nc):
        for j in range(nl):
            cx = x0 + cel * (i + 0.5)
            cy = y0 + cel * (j + 0.5)
            p.append('<circle cx="%.1f" cy="%.1f" r="13" fill="#ffffff" '
                     'stroke="%s" stroke-width="2"/>' % (cx - 20, cy, SUAVE))
            p.append(texto(cx - 20, cy + 7, '−', SUAVE, 20))
            p.append('<circle cx="%.1f" cy="%.1f" r="13" fill="#ffffff" '
                     'stroke="%s" stroke-width="2"/>' % (cx + 20, cy, COBRE))
            p.append(texto(cx + 20, cy + 7, '+', COBRE, 20))
            p.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" '
                     'stroke="%s" stroke-width="2"/>'
                     % (cx - 7, cy, cx + 7, cy, SUAVE))

    # os pares internos que se cancelam
    for i in range(nc - 1):
        for j in range(nl):
            cx = x0 + cel * (i + 1)
            cy = y0 + cel * (j + 0.5)
            p.append('<ellipse cx="%.1f" cy="%.1f" rx="34" ry="19" fill="none" '
                     'stroke="%s" stroke-width="1.6" stroke-dasharray="6 5"/>'
                     % (cx, cy, VERDE))
    p.append(texto(x0 + larg / 2, y0 + alt + 36,
                   'dentro, cada + encosta num − e os dois somam zero',
                   VERDE, 17))

    # as faces, que sobram
    p.append('<rect x="%d" y="%d" width="26" height="%d" fill="%s" '
             'opacity="0.22"/>' % (x0 - 4, y0, alt, SUAVE))
    p.append('<rect x="%d" y="%d" width="26" height="%d" fill="%s" '
             'opacity="0.22"/>' % (x0 + larg - 22, y0, alt, COBRE))
    p.append(texto(x0 + 9, y0 - 20, '−σ', SUAVE, 21))
    p.append(texto(x0 + larg - 9, y0 - 20, '+σ', COBRE, 21))
    p.append(texto(x0 + larg / 2, y0 - 22,
                   'nas faces não há vizinho para cancelar', SUAVE, 17))

    # a polarização
    p.append(seta(x0 + larg / 2 - 60, y0 + alt + 76,
                  x0 + larg / 2 + 60, y0 + alt + 76, TINTA, 3.2))
    p.append(texto(x0 + larg / 2 + 72, y0 + alt + 82, 'P', TINTA, 21,
                   anc='start', italico=True))

    io.open(IMG / 'cap04_ligadas.svg', 'w', encoding='utf-8').write(
        svg(L, A, '\n'.join(p), 'Cargas ligadas num dielétrico polarizado'))
    return 'cap04_ligadas.svg'


def main():
    IMG.mkdir(parents=True, exist_ok=True)
    for fn in (forca_de_lorentz, balanca_de_corrente, cabo_coaxial,
               casca_girante, torque_na_espira, correntes_ligadas,
               laco_de_histerese, condicoes_de_contorno,
               barra_nos_trilhos, campo_induzido, duas_superficies,
               cargas_ligadas):
        print('  ' + fn())


if __name__ == '__main__':
    main()
