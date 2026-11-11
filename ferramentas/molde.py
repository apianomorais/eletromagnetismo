# -*- coding: utf-8 -*-
"""Escreve as páginas do site de eletromagnetismo.

Toda a navegação sai da lista CAPITULOS: mudando a ordem aqui, o menu do
topo, a barra lateral e as setas de rodapé de todas as páginas se
reorganizam sozinhos.

A numeração segue os capítulos do Griffiths, que é o livro que os alunos
têm na mão, e não o calendário. Cada capítulo diz de quantos encontros de
duas horas ele precisa, para o plano fechar as trinta aulas por disciplina.
"""
import io
import pathlib

RAIZ = pathlib.Path(__file__).resolve().parent.parent

# (arquivo, rótulo curto, título, subtítulo, disciplina, encontros)
CAPITULOS = [
    ('index.html', 'Início', 'Eletromagnetismo', '', '', 0),

    ('cap01.html', '1', 'Capítulo 1: análise vetorial',
     'A linguagem do curso inteiro: gradiente, divergente, rotacional, os teoremas '
     'integrais e a função delta. Sem isso, as equações de Maxwell são só símbolos.',
     'EM I', 4),
    ('cap02.html', '2', 'Capítulo 2: eletrostática',
     'Da lei de Coulomb ao potencial, passando pela lei de Gauss nas formas '
     'integral e diferencial, pela energia do campo e pelos condutores.',
     'EM I', 9),
    ('cap03.html', '3', 'Capítulo 3: potenciais e técnicas especiais',
     'Quando a carga não é dada de antemão: equação de Laplace, unicidade, método '
     'das imagens, separação de variáveis e expansão multipolar.',
     'EM I', 10),
    ('cap04.html', '4', 'Capítulo 4: campos elétricos na matéria',
     'Polarização, cargas ligadas, o deslocamento elétrico e os dielétricos '
     'lineares, com as condições de contorno que eles impõem.',
     'EM I', 7),

    ('cap05.html', '5', 'Capítulo 5: magnetostática',
     'Força de Lorentz, lei de Biot-Savart, lei de Ampère e o potencial vetor: a '
     'magnetostática montada em paralelo com a eletrostática.',
     'EM II', 10),
    ('cap06.html', '6', 'Capítulo 6: campos magnéticos na matéria',
     'Magnetização, correntes ligadas, o campo auxiliar H e os três tipos de '
     'resposta magnética: diamagnetismo, paramagnetismo e ferromagnetismo.',
     'EM II', 8),
    ('cap07.html', '7', 'Capítulo 7: eletrodinâmica',
     'Força eletromotriz, lei de Ohm, indução, a corrente de deslocamento e, no '
     'fim, as quatro equações de Maxwell reunidas.',
     'EM II', 12),

    ('cap08.html', '8', 'Capítulo 8: leis de conservação',
     'Continuidade, teorema de Poynting, momento do campo e o tensor das tensões '
     'de Maxwell: o campo como portador de energia e de momento.',
     'EM III', 6),
    ('cap09.html', '9', 'Capítulo 9: ondas eletromagnéticas',
     'A equação de onda saindo de Maxwell, polarização, propagação em meios '
     'lineares, absorção, dispersão e guias de onda.',
     'EM III', 10),
    ('cap10.html', '10', 'Capítulo 10: potenciais e campos',
     'Potencial escalar e vetor, transformações de calibre, Coulomb e Lorenz, '
     'potenciais retardados e os potenciais de Liénard-Wiechert.',
     'EM III', 7),
    ('cap11.html', '11', 'Capítulo 11: radiação',
     'Radiação de dipolo elétrico e magnético, a potência irradiada por uma carga '
     'acelerada e a reação de radiação.',
     'EM III', 7),

    ('formulario.html', 'Formulário', 'Formulário',
     'Tudo o que o curso usa, em uma página só: operadores, teoremas, as equações '
     'de Maxwell nas quatro formas e as condições de contorno.', '', 0),
    ('codigo.html', 'Código', 'Os programas',
     'Os scripts em Python para rodar no Spyder, um por técnica, com o que cada um '
     'resolve e como conferir se a resposta está certa.', '', 0),
]

DISCIPLINAS = [
    ('EM I', 'Eletromagnetismo I', 'DF032'),
    ('EM II', 'Eletromagnetismo II', 'DF033'),
    ('EM III', 'Eletromagnetismo III', 'DF053'),
]

CABECA = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo} | Eletromagnetismo</title>
<link rel="icon" type="image/png" href="assets/img/favicon.png">
<link rel="stylesheet" href="assets/css/estilo.css">
<script src="assets/js/comum.js"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
</head>
<body>

<header class="topo">
  <div class="topo-interno">
    <a class="marca" href="index.html">Eletromagnetismo <span>· LFCA/URCA</span></a>
    <nav class="menu">
{menu}
    </nav>
  </div>
</header>

<div class="envoltorio">
{lateral}
<main class="conteudo">

{chapeu}
  <h1>{h1}</h1>
{subtitulo}
{corpo}

  <nav class="nav-aulas">
{nav}
  </nav>

</main>
</div>

<footer class="rodape">
  <img class="logo-rodape" src="assets/img/logo.png" alt="LFCA | URCA">
  <p><strong>Prof. Apiano Morais</strong> · <a href="mailto:apiano.morais@urca.br">apiano.morais@urca.br</a><br>
  Laboratório de Física Computacional Aplicada (LFCA) · Universidade Regional do Cariri</p>
</footer>

<script src="assets/js/widgets.js"></script>
</body>
</html>
'''


def menu(atual):
    partes = []
    disciplina_atual = None
    for arq, curto, titulo, _s, disc, _e in CAPITULOS:
        if curto in ('Início', 'Formulário', 'Código'):
            partes.append('      <a href="%s"%s>%s</a>'
                          % (arq, ' class="ativo"' if arq == atual else '', curto))
            continue
        if disc != disciplina_atual:
            disciplina_atual = disc
            partes.append('      <span class="grupo">%s</span>' % disc)
        cls = 'num ativo' if arq == atual else 'num'
        partes.append('      <a href="%s" class="%s" title="%s">%s</a>'
                      % (arq, cls, titulo, curto))
    return '\n'.join(partes)


def navegacao(atual):
    i = [c[0] for c in CAPITULOS].index(atual)
    saida = []
    if i > 0:
        saida.append('    <a href="%s"><small>Anterior</small>← %s</a>'
                     % (CAPITULOS[i - 1][0], CAPITULOS[i - 1][2]))
    if i < len(CAPITULOS) - 1:
        saida.append('    <a class="prox" href="%s"><small>Próximo</small>%s →</a>'
                     % (CAPITULOS[i + 1][0], CAPITULOS[i + 1][2]))
    return '\n'.join(saida)


def escreve(arquivo, corpo, secoes=None, chapeu=None, titulo_proprio=False):
    i = [c[0] for c in CAPITULOS].index(arquivo)
    _a, _c, titulo, sub, disc, enc = CAPITULOS[i]
    lateral = ''
    if secoes:
        itens = '\n'.join('    <li><a href="#s%d">%d. %s</a></li>' % (j + 1, j + 1, t)
                          for j, t in enumerate(secoes))
        lateral = ('\n<aside class="lateral">\n  <h4>Neste capítulo</h4>\n  <ol>\n%s\n'
                   '  </ol>\n</aside>\n' % itens)
    if chapeu is None and disc:
        chapeu = '%s · %d encontro%s de duas horas' % (disc, enc, 's' if enc > 1 else '')
    pag = CABECA.format(
        titulo=titulo, h1=titulo, menu=menu(arquivo), lateral=lateral,
        chapeu='  <p class="chapeu">%s</p>' % chapeu if chapeu else '',
        subtitulo='  <p class="subtitulo">%s</p>' % sub if sub else '',
        corpo=corpo, nav=navegacao(arquivo))
    if titulo_proprio:
        pag = pag.replace('  <h1>%s</h1>\n' % titulo, '', 1)
    (RAIZ / arquivo).write_text(pag, encoding='utf-8')
    print('%s escrito (%d caracteres)' % (arquivo, len(pag)))


def secoes_html(secoes):
    """secoes: lista de (titulo, html). Recua o HTML para encaixar no molde,
    deixando intactos os blocos <pre>: ali todo espaço conta."""
    saida = []
    for i, (titulo, html) in enumerate(secoes):
        saida.append('  <!-- ============================================== -->')
        saida.append('  <h2 id="s%d">%d. %s</h2>\n' % (i + 1, i + 1, titulo))
        dentro = False
        for linha in html.strip('\n').split('\n'):
            if '<pre' in linha:
                dentro = True
            saida.append(linha if dentro or not linha.strip() else '  ' + linha)
            if '</pre>' in linha:
                dentro = False
        saida.append('')
    return '\n'.join(saida)
