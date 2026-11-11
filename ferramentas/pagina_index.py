# -*- coding: utf-8 -*-
"""A página de entrada: o mapa das três disciplinas sobre os capítulos."""
import molde
from molde import CAPITULOS, DISCIPLINAS, escreve

EMENTAS = {
    'EM I': 'Eletrostática. Técnicas especiais na eletrostática. Campos elétricos '
            'na matéria.',
    'EM II': 'Magnetostática. Campos magnéticos na matéria. Eletrodinâmica.',
    'EM III': 'Leis de conservação. Ondas eletromagnéticas. Potenciais e campos. '
              'Radiação.',
}
SEMESTRE = {'EM I': '4º semestre', 'EM II': '5º semestre', 'EM III': '6º semestre'}
PRE = {'EM I': 'DF003, DM004', 'EM II': 'DF032', 'EM III': 'DF033'}

HERO = '''
  <section class="heroi">
    <img class="placa-logo" src="assets/img/logo.svg" alt="LFCA | URCA">
    <div>
      <h1>Eletromagnetismo</h1>
      <p class="subtitulo">As três disciplinas da sequência, numeradas pelos
      capítulos do Griffiths: o que se deduz no quadro, o que se resolve no papel
      e o que só sai no computador.</p>
      <p class="meta">Prof. Apiano Morais · Laboratório de Física Computacional
      Aplicada · Universidade Regional do Cariri</p>
    </div>
  </section>
'''


def cartoes_disciplinas():
    linhas = []
    for sigla, nome, codigo in DISCIPLINAS:
        caps = [c for c in CAPITULOS if c[4] == sigla]
        enc = sum(c[5] for c in caps)
        itens = '\n'.join(
            '        <li><a href="%s">%s</a> <small>%d encontro%s</small></li>'
            % (c[0], c[2].split(': ')[1].capitalize(), c[5], 's' if c[5] > 1 else '')
            for c in caps)
        linhas.append('''    <article class="cartao">
      <h3>%s <span class="etiqueta">%s</span></h3>
      <p class="ficha">%s · pré-requisito %s · 60 horas · %d encontros de duas horas</p>
      <p>%s</p>
      <ul>
%s
      </ul>
    </article>''' % (nome, codigo, SEMESTRE[sigla], PRE[sigla], enc,
                     EMENTAS[sigla], itens))
    return '  <div class="cartoes">\n%s\n  </div>\n' % '\n'.join(linhas)


CORPO = '''
  <h2 id="s1">1. As três disciplinas</h2>

  <p>A sequência tem uma lógica simples, e ela é a do livro: primeiro as cargas
  paradas, depois as cargas em movimento permanente, e por fim o que acontece
  quando tudo muda com o tempo. Cada disciplina ocupa três ou quatro capítulos
  do Griffiths, e as páginas deste site são numeradas por capítulo, não por
  aula, para o aluno abrir o livro e o site na mesma página.</p>

%s

  <h2 id="s2">2. Como as páginas são feitas</h2>

  <p>Cada capítulo tem a mesma estrutura. A teoria é deduzida do começo, sem
  pular passagem; os exemplos são resolvidos por extenso, com as contas à
  vista, e não com um "é fácil mostrar que"; e no fim há sempre um programa em
  Python que resolve o mesmo problema por outro caminho, para o aluno conferir
  o que fez no papel.</p>

  <div class="cartoes">
    <article class="cartao">
      <h3>Dedução</h3>
      <p>O caminho inteiro, do princípio físico até a fórmula, com as hipóteses
      ditas na hora em que são usadas.</p>
    </article>
    <article class="cartao">
      <h3>Exemplo resolvido</h3>
      <p>Um problema concreto, com a álgebra escrita linha a linha e o resultado
      checado em algum limite conhecido.</p>
    </article>
    <article class="cartao">
      <h3>Experimento na tela</h3>
      <p>Um widget na própria página para mexer nos parâmetros e ver o campo
      responder, sem instalar nada.</p>
    </article>
    <article class="cartao">
      <h3>Programa para rodar</h3>
      <p>Um arquivo <code>.py</code> comentado, para baixar e executar no Spyder,
      que reproduz e estende o que a página mostrou.</p>
    </article>
  </div>

  <h2 id="s3">3. O computador no eletromagnetismo</h2>

  <p>Boa parte do que esta disciplina pede não tem solução fechada. A equação de
  Laplace numa região de forma qualquer, o campo de uma distribuição que não é
  simétrica, a trajetória de uma carga num campo que varia: todos esses casos
  são triviais para um método numérico e impossíveis no papel. Os programas do
  site estão organizados por técnica, e não por capítulo, porque a mesma
  relaxação que resolve o capacitor resolve depois o guia de onda.</p>

  <p>Os códigos usam apenas <code>numpy</code>, <code>scipy</code> e
  <code>matplotlib</code>, rodam no Spyder sem configuração nenhuma, e cada um
  traz no cabeçalho o que resolve, o que imprime e como saber se acertou.
  <a href="codigo.html">A lista completa está na página do código.</a></p>

  <h2 id="s4">4. Bibliografia</h2>

  <div class="cartoes">
    <article class="cartao">
      <h3>Griffiths</h3>
      <p><em>Eletrodinâmica.</em> O livro-texto da sequência: a numeração deste
      site é a dele, e os exemplos e problemas citados são os seus.</p>
    </article>
    <article class="cartao">
      <h3>Machado</h3>
      <p><em>Teoria do Eletromagnetismo.</em> Em português, com mais detalhe
      algébrico nas passagens que o Griffiths resume.</p>
    </article>
    <article class="cartao">
      <h3>Reitz, Milford e Christy</h3>
      <p><em>Fundamentos da Teoria Eletromagnética.</em> O clássico das
      bibliotecas, forte em meios materiais.</p>
    </article>
    <article class="cartao">
      <h3>Jackson</h3>
      <p><em>Classical Electrodynamics.</em> Para quem for adiante: a referência
      das seções mais avançadas de Eletromagnetismo III.</p>
    </article>
  </div>
'''


def main():
    corpo = HERO + (CORPO % cartoes_disciplinas())
    escreve('index.html', corpo,
            secoes=['As três disciplinas', 'Como as páginas são feitas',
                    'O computador no eletromagnetismo', 'Bibliografia'],
            chapeu='', titulo_proprio=True)


if __name__ == '__main__':
    main()
