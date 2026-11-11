# -*- coding: utf-8 -*-
"""Monta assets/js/widgets.js: o preâmbulo comum mais os widgets do curso.

O preâmbulo (utilitários de DOM, deslizantes, cartões numéricos, seta e
rótulo com halo) é o mesmo dos outros sites do laboratório, e fica em
partes/preambulo.js. Cada widget mora no seu arquivo em partes/.
"""
import io
import pathlib

RAIZ = pathlib.Path(__file__).resolve().parent.parent
PARTES = RAIZ / 'ferramentas' / 'partes'

ORDEM = ['preambulo.js', 'trajetoria.js', 'esferamag.js', 'rodape.js']


def main():
    pedacos = [io.open(PARTES / n, encoding='utf-8').read() for n in ORDEM]
    alvo = RAIZ / 'assets' / 'js' / 'widgets.js'
    alvo.write_text('\n'.join(pedacos), encoding='utf-8')
    print('widgets.js: %d partes, %d caracteres'
          % (len(ORDEM), len(alvo.read_text(encoding='utf-8'))))


if __name__ == '__main__':
    main()
