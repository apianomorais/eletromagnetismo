# -*- coding: utf-8 -*-
"""Exercícios propostos, com solução recolhível, para as páginas dos capítulos.

O enunciado fica sempre visível e a solução abre num <details>, de modo que a
mesma página serve para estudar e para imprimir: a folha de impressão abre
todas as soluções, pela regra de @media print do estilo.

Cada exercício é uma tupla (rótulo, enunciado, solução), e a função bloco()
devolve o HTML da seção inteira.
"""


def bloco(lista):
    """Monta a seção de exercícios a partir da lista de tuplas."""
    partes = ['<p>Os enunciados são nossos, e as soluções estão aqui mesmo, '
              'recolhidas. Resolva antes de abrir: ler solução pronta dá a '
              'sensação de ter entendido, que é diferente de ter entendido.</p>']
    for rotulo, enunciado, solucao in lista:
        partes.append(
            '<div class="bloco ex">\n'
            '  <span class="rotulo">%s</span>\n'
            '  <p>%s</p>\n'
            '  <details class="solucao"><summary>Ver solução</summary>\n'
            '  <div class="corpo-solucao">\n%s\n  </div>\n'
            '  </details>\n'
            '</div>' % (rotulo, enunciado, solucao))
    return '\n\n'.join(partes) + '\n'
