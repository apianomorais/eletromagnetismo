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
      <p class="subtitulo">Da pedra que atrai o ferro até a luz que é campo: as
      três disciplinas da sequência, com o que se deduz no quadro, o que se
      resolve no papel e o que só sai no computador.</p>
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
  <h2 id="s1">1. De onde isso tudo veio</h2>

  <p>Dois fatos esquisitos chegaram até nós da Antiguidade, e por quase dois mil
  anos ninguém desconfiou que tivessem qualquer parentesco. Um pedaço de
  <a href="https://pt.wikipedia.org/wiki/%C3%82mbar">âmbar</a> atritado em lã
  atrai palha, folha seca, fiapo de qualquer coisa leve, e os gregos chamavam
  essa resina de <em>élektron</em>. Uma pedra escura achada na região da
  Magnésia, a <a href="https://pt.wikipedia.org/wiki/Magnetita">magnetita</a>,
  atrai ferro sem precisar ser atritada, e sempre aponta na mesma direção quando
  pendurada por um fio. Atração sem contato, nos dois casos, e nenhuma pista do
  que estivesse acontecendo no meio.</p>

  <p>A separação cuidadosa das duas coisas é trabalho de
  <a href="https://en.wikipedia.org/wiki/William_Gilbert_(physicist)">William
  Gilbert</a>, médico da corte inglesa, que em 1600 publicou o <em>De
  Magnete</em>. Ele mostra, com experimento atrás de experimento, que a atração
  do âmbar aparece em dezenas de outros materiais e some com a umidade, enquanto
  a da magnetita é exclusiva de poucos minerais, não some, e tem dois polos que
  não se deixam separar. E arrisca a tese que até hoje se ensina na quinta
  série: a Terra inteira é um ímã, e é por isso que a bússola funciona.</p>

  <p>O século XVIII passou inteiro produzindo eletricidade e quase nenhuma
  teoria. Máquinas de atrito, garrafas de Leiden, faíscas de palmo, demonstrações
  de salão em que uma fila de monges levava choque ao mesmo tempo, e a pipa de
  Franklin na tempestade. O que faltava era medida, e ela vem com
  <a href="https://pt.wikipedia.org/wiki/Charles-Augustin_de_Coulomb">Coulomb</a>,
  em 1785, numa balança de torção tão sensível que o deslocamento angular de uma
  agulha de palha traduz a força entre duas bolinhas carregadas. O resultado é
  uma lei do inverso do quadrado, idêntica em forma à da gravitação, e daí em
  diante a eletrostática é assunto de matemática.</p>

  <p>Faltava a corrente, e ela chega em 1800 com a pilha de
  <a href="https://pt.wikipedia.org/wiki/Alessandro_Volta">Volta</a>: discos de
  zinco e cobre alternados, separados por papelão em salmoura, fornecendo um
  escoamento contínuo de carga em vez do estouro de uma garrafa de Leiden. Vinte
  anos depois, numa aula em Copenhague,
  <a href="https://pt.wikipedia.org/wiki/Hans_Christian_%C3%98rsted">Ørsted</a>
  nota que a agulha de uma bússola deitada perto de um fio ligado à pilha gira.
  Não é um detalhe de laboratório: a agulha não aponta nem para o fio nem ao
  longo dele, e sim perpendicularmente aos dois, coisa que nenhuma força
  conhecida fazia. Em poucos meses
  <a href="https://pt.wikipedia.org/wiki/Andr%C3%A9-Marie_Amp%C3%A8re">Ampère</a>
  e a dupla
  <a href="https://pt.wikipedia.org/wiki/Lei_de_Biot-Savart">Biot e Savart</a>
  tinham transformado o espanto em fórmula.</p>

  <p>Se a corrente faz campo magnético, o inverso deveria valer, e a busca por
  esse inverso ocupou
  <a href="https://pt.wikipedia.org/wiki/Michael_Faraday">Faraday</a> por dez
  anos. A resposta, em 1831, é que o ímã parado não faz nada, e o que gera
  corrente é a variação: aproximar, afastar, ligar, desligar. Faraday, que não
  tinha formação matemática, pensava em linhas de força preenchendo o espaço, e
  essa imagem de campo, que os continentais achavam ingênua,
  <a href="https://pt.wikipedia.org/wiki/James_Clerk_Maxwell">Maxwell</a>
  traduziu em equações. Ao fazê-lo, percebeu que a lei de Ampère estava
  incompleta, acrescentou o termo que faltava, e o sistema devolveu uma equação
  de onda cuja velocidade, calculada a partir de duas constantes medidas em
  bancada, dava a velocidade da luz. A conclusão está escrita no artigo de 1865
  (<a href="https://doi.org/10.1098/rstl.1865.0008">doi:10.1098/rstl.1865.0008</a>):
  a luz é uma onda eletromagnética.</p>

  <p>A previsão ficou no papel por vinte anos, até
  <a href="https://pt.wikipedia.org/wiki/Heinrich_Hertz">Hertz</a> produzir essas
  ondas com um centelhador e detectá-las do outro lado da sala com um anel de
  fio, medindo-lhes o comprimento e a velocidade. Hertz morreu antes de ver o
  que fizeram com isso. E ainda havia uma pedra no sapato: a lei de indução dava
  a mesma corrente quer se movesse o ímã, quer se movesse a espira, mas por duas
  explicações diferentes. É exatamente com essa assimetria que
  <a href="https://pt.wikipedia.org/wiki/Albert_Einstein">Einstein</a> abre o
  artigo de 1905
  (<a href="https://doi.org/10.1002/andp.19053221004">doi:10.1002/andp.19053221004</a>),
  intitulado, não por acaso, <em>Sobre a eletrodinâmica dos corpos em
  movimento</em>. O eletromagnetismo não é uma teoria encerrada no século XIX:
  é a porta de entrada da relatividade.</p>

  <div class="cartoes">
    <article class="cartao"><h3>1600</h3>
      <p>Gilbert separa o elétrico do magnético e propõe a Terra como ímã.</p></article>
    <article class="cartao"><h3>1785</h3>
      <p>Coulomb mede a força entre cargas e acha o inverso do quadrado.</p></article>
    <article class="cartao"><h3>1800</h3>
      <p>Volta empilha zinco e cobre, e nasce a corrente contínua.</p></article>
    <article class="cartao"><h3>1820</h3>
      <p>Ørsted vê a agulha girar perto do fio, perpendicularmente a ele.</p></article>
    <article class="cartao"><h3>1831</h3>
      <p>Faraday descobre que campo que varia no tempo gera corrente.</p></article>
    <article class="cartao"><h3>1865</h3>
      <p>Maxwell fecha as equações e identifica a luz com a onda do campo.</p></article>
    <article class="cartao"><h3>1887</h3>
      <p>Hertz fabrica e detecta a onda prevista, numa sala de aula.</p></article>
    <article class="cartao"><h3>1905</h3>
      <p>Einstein parte de uma assimetria da indução e chega à relatividade.</p></article>
  </div>

  <h2 id="s2">2. As três disciplinas</h2>

  <p>A ordem em que as coisas foram descobertas não é a ordem em que elas se
  aprendem, e tentar ensinar pela história custa caro: o aluno gastaria um
  semestre com fluidos elétricos e linhas de força antes de escrever a primeira
  divergência. A sequência segue então a ordem lógica, que é a do livro do
  Griffiths: primeiro as cargas paradas, depois as cargas em movimento
  permanente, e por fim o que acontece quando tudo muda com o tempo. Cada
  disciplina ocupa três ou quatro capítulos, e as páginas deste site são
  numeradas por capítulo, não por aula, para o aluno abrir o livro e o site na
  mesma página.</p>

<!--CARTOES-->

  <h2 id="s3">3. Como as páginas são feitas</h2>

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

  <h2 id="s4">4. O computador no eletromagnetismo</h2>

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

  <h2 id="s5">5. Bibliografia</h2>

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
    corpo = HERO + CORPO.replace('<!--CARTOES-->', cartoes_disciplinas())
    escreve('index.html', corpo,
            secoes=['De onde isso tudo veio', 'As três disciplinas',
                    'Como as páginas são feitas',
                    'O computador no eletromagnetismo', 'Bibliografia'],
            chapeu='', titulo_proprio=True)


if __name__ == '__main__':
    main()
