# -*- coding: utf-8 -*-
"""Troca a paleta do site inteiro.

As cores do sítio moram em cinco variáveis do :root de estilo.css. Este
script reescreve as cinco de uma vez, de modo que experimentar uma paleta
nova não exige mexer em nenhuma página.

Uso:  python3 paleta.py nome_da_paleta
"""
import io
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
CSS = RAIZ / 'assets' / 'css' / 'estilo.css'

# nome: (principal, claro, pastel, destaque, secundária, papel alternativo, borda)
PALETAS = {
    # a do ímã do logo: navy e vermelho
    'ima': ('#1c2c60', '#3a4e8f', '#eceff8', '#a8181d', '#1d6b63',
            '#f7f8fc', '#d9ddea'),
    # violeta elétrico com laranja queimado
    'violeta': ('#4b2e83', '#7a5bbf', '#f1ecfa', '#c2410c', '#1f6f6b',
                '#f9f6fd', '#e2d9f0'),
    # grafite azulado com cobre: a cor do fio enrolado
    'cobre': ('#2b3240', '#4f5a6b', '#edf0f4', '#b05a1f', '#2c6e63',
              '#f7f8fa', '#dde2e8'),
    # bordô profundo com ouro velho
    'bordo': ('#6a1b2a', '#99394a', '#faecee', '#b5831f', '#2c5f6b',
              '#fdf7f8', '#ecd9dd'),
}


def aplica(nome):
    if nome not in PALETAS:
        raise SystemExit('paletas: %s' % ', '.join(sorted(PALETAS)))
    p, claro, pastel, destaque, sec, papel2, borda = PALETAS[nome]
    s = io.open(CSS, encoding='utf-8').read()
    pares = [('--azul', p), ('--azul-claro', claro), ('--azul-pastel', pastel),
             ('--vinho', destaque), ('--verde', sec),
             ('--papel-alt', papel2), ('--borda', borda)]
    for var, cor in pares:
        s = re.sub(r'(%s:)#[0-9a-fA-F]{6}' % var, r'\g<1>' + cor, s, count=1)
    io.open(CSS, 'w', encoding='utf-8').write(s)
    print('paleta %s aplicada: %s' % (nome, p))


if __name__ == '__main__':
    aplica(sys.argv[1] if len(sys.argv) > 1 else 'ima')
