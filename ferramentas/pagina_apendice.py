# -*- coding: utf-8 -*-
"""Apêndice: onde a teoria clássica termina.

Página de fechamento do curso, fora da numeração do Griffiths. Texto escrito
do zero; as remissões à Física Estatística apontam para as aulas 9 e 10.
"""
from molde import escreve, secoes_html

FE = 'https://apianomorais.github.io/fisica-estatistica'

S1 = r'''
<p>O curso termina com uma teoria em excelente estado de saúde. As equações de
Maxwell descrevem antenas, fibras ópticas, motores, guias de onda, dielétricos,
ímãs e luz, com precisão de muitos algarismos, e nada neste site precisou de
desculpas. Ainda assim, três momentos do curso apontaram para o mesmo lugar, e
vale juntá-los.</p>

<p>O capítulo 11 mostrou que a força de reação de radiação produz soluções
fugitivas e pré-aceleração, com um tempo característico
\(\tau = 6{,}3\times10^{-24}\ \mathrm{s}\), que é o tempo da luz atravessar o
raio clássico do elétron. O capítulo 12 mostrou que a eletrodinâmica de Weber,
construída sobre princípios inteiramente diferentes, produz massa efetiva
negativa em \(2r_e\). E o capítulo 2, lá atrás, já havia encontrado o problema
na sua forma mais simples: a energia do campo de uma carga pontual,</p>

\[ W = \frac{\varepsilon_0}{2}\int E^2\,d\tau
   = \frac{q^2}{8\pi\varepsilon_0}\int_0^\infty\frac{dr}{r^2}, \]

<p>diverge na origem.</p>

<div class="bloco alerta">
<span class="rotulo">A escala</span>
<p>Igualando a energia eletrostática à energia de repouso,
\(q^2/4\pi\varepsilon_0 r = mc^2\), sai</p>
\[ r_e = \frac{e^2}{4\pi\varepsilon_0mc^2}
   = 2{,}82\times10^{-15}\ \mathrm{m}. \]
<p>Não é o tamanho do elétron: experimentos de espalhamento mostram que ele é
pontual até pelo menos \(10^{-18}\) m. É a distância em que a eletrodinâmica
clássica deixa de saber do que está falando, qualquer que seja a versão dela
que se escolha.</p>
</div>

<p>Este apêndice percorre quatro direções em que a teoria clássica é
substituída por algo mais fundo. Nenhuma delas invalida o que o curso ensinou:
todas elas <em>contêm</em> o que o curso ensinou, como caso limite.</p>
'''

S2 = r'''
<p>O primeiro limite aparece quando o fóton fica energético demais, e o
capítulo 11 passou por ele sem parar.</p>

<p>A seção de choque de Thomson vale
\(\sigma_T = 6{,}65\times10^{-29}\ \mathrm{m^2}\) e não depende da frequência.
Isso é correto enquanto a energia do fóton for muito menor que a energia de
repouso do elétron,</p>

\[ mc^2 = 511\ \mathrm{keV}. \]

<p>Acima disso o espalhamento deixa de ser elástico: o elétron recua, o fóton
sai com comprimento de onda maior, e a seção de choque cai. A fórmula correta é
a de Klein-Nishina, de 1929, e o deslocamento do comprimento de onda é</p>

\[ \Delta\lambda = \lambda_C\left(1-\cos\theta\right),
   \qquad \lambda_C = \frac{h}{mc} = 2{,}43\times10^{-12}\ \mathrm{m}. \]

<p>Repare que \(\lambda_C\) é maior que \(r_e\) por um fator \(1/\alpha =
137\), e esse é o sinal de que a mecânica quântica chega <em>antes</em> do
muro clássico: muito antes de \(r_e\), já é preciso trocar de teoria.</p>

<h3>O que a eletrodinâmica quântica faz com a divergência</h3>

<p>A energia própria do elétron continua divergindo na teoria quântica, e a
solução encontrada nos anos 1940 é desconcertante e funciona: a massa que
aparece nas equações não é observável, apenas a soma dela com a energia do
campo próprio é. Absorvendo o infinito na redefinição da massa e da carga, o
que sobra para calcular é finito. É a <strong>renormalização</strong>.</p>

<div class="destaque">
<p><strong>O resultado que paga a conta.</strong> O momento magnético do
elétron, que a teoria de Dirac prevê com \(g = 2\) exatamente, ganha correções
da interação com o próprio campo. A previsão da eletrodinâmica quântica e a
medida mais recente, de 2023, são</p>

\[ \frac{g}{2} = 1{,}001\,159\,652\,180\,59\,(13), \]

<p>com incerteza de 0,13 parte por trilhão. É a previsão mais bem verificada
de toda a física, e o primeiro termo da correção,
\(\alpha/2\pi = 0{,}00116\), foi calculado por Schwinger em 1948 e está
gravado no túmulo dele.</p>
</div>

<p>A moral é que a teoria clássica não estava errada: ela estava
<em>incompleta</em>, e a maneira de completá-la preservou todas as suas
previsões de baixa energia, acrescentando correções em potências de
\(\alpha = 1/137\).</p>
'''

S3 = r'''
<p>Em Maxwell, as equações são lineares: dois feixes de luz se atravessam sem
se perturbar, e o princípio da superposição vale exatamente. Na eletrodinâmica
quântica, não.</p>

<p>Um fóton pode, por um instante curtíssimo, virar um par elétron-pósitron, e
esse par sente outro campo. O resultado é que o vácuo se comporta como um meio
<em>não linear</em>, com uma permissividade que depende do campo aplicado. A
correção foi calculada por Euler e Heisenberg em 1936, e o campo em que ela se
torna importante é o <strong>campo crítico de Schwinger</strong>:</p>

\[ E_c = \frac{m^2c^3}{e\hbar} = 1{,}32\times10^{18}\ \mathrm{V/m},
   \qquad
   B_c = \frac{m^2c^2}{e\hbar} = 4{,}41\times10^{9}\ \mathrm{T}. \]

<p>São números absurdos para o laboratório, e por isso o efeito ficou setenta
anos sendo uma previsão de papel. Três coisas mudaram isso.</p>

<div class="bloco fisica">
<span class="rotulo">Luz espalhando luz</span>
<p>Em 2017, o experimento ATLAS observou dois fótons se espalhando um no outro,
em colisões de íons de chumbo no LHC. O truque é que um núcleo de chumbo com
82 prótons, movendo-se a \(0{,}9999c\), carrega um campo eletromagnético
achatado tão intenso que funciona como uma fonte de fótons quase reais, e dois
desses feixes podem colidir. É o capítulo 10 em ação: o achatamento relativo
do campo de uma carga rápida, do exercício 10.4, é o que torna o experimento
possível.</p>
</div>

<p><strong>Magnetares.</strong> Estrelas de nêutrons com campos de superfície
de \(10^{10}\) a \(10^{11}\) T, isto é, da ordem do campo crítico. Nessas
condições o vácuo é birrefringente: a luz polarizada paralela e
perpendicularmente ao campo viaja com velocidades diferentes. Em 2016 foi
publicada a primeira evidência observacional disso, na polarização da luz da
estrela RX J1856.5-3754.</p>

<p><strong>Lasers de petawatt.</strong> Focalizando pulsos de femtossegundo,
já se chega a \(10^{14}\ \mathrm{V/m}\), ainda quatro ordens abaixo do crítico.
Instalações em construção pretendem usar colisões entre um feixe de elétrons
relativístico e um laser intenso, em que o campo <em>no referencial do
elétron</em> é multiplicado por \(\gamma\), para alcançar o regime de
Schwinger.</p>

<p>O que está em jogo é a previsão mais estranha de todas: com campo elétrico
suficiente, o vácuo se torna instável e <strong>produz pares de partículas
espontaneamente</strong>. O espaço vazio quebra, como um dielétrico
atravessado pela tensão de ruptura. A analogia com o capítulo 4 é mais do que
retórica: é literalmente a rigidez dielétrica do nada.</p>
'''

S4 = r'''
<p>O capítulo 6 montou toda a magnetostática da matéria: magnetização,
correntes ligadas, o campo \(\vet{H}\), a susceptibilidade, os três tipos de
comportamento magnético. O que ele não conseguiu, e deixou dito, foi explicar
de onde vêm os valores. A razão é forte: <em>nenhuma</em> teoria clássica
consegue.</p>

<div class="bloco alerta">
<span class="rotulo">O teorema de Bohr-van Leeuwen</span>
<p>A magnetização de equilíbrio de qualquer sistema clássico de cargas é
exatamente zero, a qualquer temperatura e em qualquer campo. A prova é curta:
o campo entra na mecânica clássica pela substituição
\(\vet{p}\to\vet{p}-q\vet{A}\), e na integral da função de partição sobre todo
o espaço de momentos essa substituição é só uma translação, com jacobiano 1 e
limites inalterados. Logo \(Z\) não depende de \(\vet{A}\), e portanto
\(M = -\partial F/\partial B = 0\).</p>
<p>Diamagnetismo, paramagnetismo e ferromagnetismo são, os três, efeitos
quânticos. <a href="%(FE)s/aula09.html#s1">A demonstração completa está na
aula 9 de Física Estatística.</a></p>
</div>

<p>O que substitui a conta clássica são três mecanismos, todos quânticos, e
todos tratados do lado da Física Estatística:</p>

<div class="cartoes">
  <article class="cartao">
    <h3><a href="%(FE)s/aula09.html#s2">Paramagnetismo de Pauli</a></h3>
    <p>Num metal, só os elétrons a menos de \(k_BT\) do nível de Fermi podem
    virar o spin, e isso reduz a susceptibilidade de Curie por um fator
    \(T/T_F \sim 10^{-2}\). O resultado é uma susceptibilidade pequena e
    <em>independente da temperatura</em>, que é o que se mede nos metais
    alcalinos.</p>
  </article>
  <article class="cartao">
    <h3><a href="%(FE)s/aula09.html#s3">Diamagnetismo de Landau</a></h3>
    <p>A quantização das órbitas ciclotrônicas em níveis de Landau produz uma
    contribuição diamagnética que vale exatamente \(-1/3\) da de Pauli, para
    elétrons livres. Dela saem as oscilações de De Haas-van Alphen, que são
    hoje a principal ferramenta para mapear superfícies de Fermi.</p>
  </article>
  <article class="cartao">
    <h3><a href="%(FE)s/aula09.html#s5">A integral de troca</a></h3>
    <p>O alinhamento ferromagnético não vem de força magnética nenhuma: vem da
    repulsão de Coulomb filtrada pelo princípio de exclusão. É por isso que a
    temperatura de Curie do ferro é de 1043 K, e não dos poucos kelvins que a
    interação dipolo-dipolo daria.</p>
  </article>
  <article class="cartao">
    <h3><a href="%(FE)s/aula10.html">Supercondutividade</a></h3>
    <p>O diamagnetismo perfeito do efeito Meissner não é a "resistência zero"
    aplicada à lei de Faraday: é um estado quântico macroscópico, descrito pela
    equação de London e, no fundo, pelo pareamento de BCS.</p>
  </article>
</div>

<p>Vale enunciar a conclusão sem suavizar: o capítulo 6 deste curso é uma
descrição fenomenológica correta e sem poder explicativo. Ele diz o que um
material faz com o campo, e não tem como dizer por quê. A resposta mora na
estatística quântica, e é por isso que as duas disciplinas aparecem ligadas
neste site.</p>
''' % {'FE': FE}

S5 = r'''
<p>O capítulo 10 introduziu \(V\) e \(\vet{A}\) como artifícios de cálculo, e
insistiu que eles não são observáveis: o calibre pode ser mudado à vontade, e
só \(\vet{E}\) e \(\vet{B}\) são medidos. Essa afirmação é verdadeira na
mecânica clássica e <em>falsa</em> na mecânica quântica, de um jeito que
demorou trinta anos para ser notado.</p>

<h3>O efeito Aharonov-Bohm</h3>

<p>Aharonov e Bohm propuseram, em 1959, o seguinte. Tome um solenoide longo e
fino, com campo magnético confinado inteiramente no seu interior, e faça um
feixe de elétrons passar <em>fora</em> dele, por dois caminhos que o contornam
por lados opostos e depois se reencontram. Na região percorrida pelos elétrons,
\(\vet{B} = 0\) em toda parte, e a força de Lorentz é identicamente nula.</p>

<p>Mesmo assim, a figura de interferência se desloca quando a corrente do
solenoide muda. A fase acumulada por cada caminho é</p>

\[ \varphi = \frac{q}{\hbar}\int\vet{A}\cdot d\vet{\ell}, \]

<p>e a diferença entre os dois caminhos é</p>

\[ \Delta\varphi = \frac{q}{\hbar}\oint\vet{A}\cdot d\vet{\ell}
   = \frac{q\Phi}{\hbar}, \]

<p>proporcional ao fluxo <em>envolvido</em>, que o elétron nunca visitou. A
confirmação experimental definitiva é de Tonomura e colaboradores, em 1986,
com o solenoide substituído por um toro supercondutor minúsculo, para que não
sobrasse nenhum campo de fuga a que se pudesse atribuir o efeito.</p>

<div class="bloco fisica">
<span class="rotulo">O que exatamente é observável</span>
<p>Não é \(\vet{A}\) ponto a ponto: esse continua dependendo do calibre. É a
<em>integral de \(\vet{A}\) ao longo de um caminho fechado</em>, que é
invariante de calibre e igual ao fluxo. O potencial não é uma ficção
matemática nem um campo observável: é um objeto geométrico cuja circulação tem
significado físico.</p>
</div>

<h3>O fluxo é quantizado</h3>

<p>Num anel supercondutor, a função de onda macroscópica tem de ser unívoca, e
isso força a fase acumulada numa volta a ser múltiplo de \(2\pi\). Com a carga
dos pares de Cooper, \(q = 2e\), sai</p>

\[ \Phi = n\Phi_0,
   \qquad \Phi_0 = \frac{h}{2e} = 2{,}068\times10^{-15}\ \mathrm{Wb}. \]

<p>Esse número foi medido em 1961, e o fator 2 no denominador foi uma das
primeiras confirmações diretas de que os portadores de carga num supercondutor
são <em>pares</em>. É também o princípio do SQUID, o magnetômetro mais
sensível que existe, capaz de detectar o campo magnético do cérebro humano,
da ordem de \(10^{-13}\ \mathrm{T}\).</p>

<h3>E se existisse monopolo</h3>

<p>A equação \(\divg{\vet{B}} = 0\) é a única das quatro sem fonte, e nada na
estrutura da teoria exige isso. Dirac mostrou, em 1931, que a existência de um
único monopolo magnético em algum lugar do universo <em>forçaria</em> a
quantização da carga elétrica, porque a fase de Aharonov-Bohm em volta da
corda de Dirac precisa ser invisível:</p>

\[ qg = nh
   \;\Longrightarrow\;
   g_{\min} = \frac{h}{e} = 4{,}14\times10^{-15}\ \mathrm{Wb} = 2\Phi_0. \]

<p>O menor monopolo possível carrega exatamente dois quanta de fluxo
supercondutor, e a carga elétrica ser sempre um múltiplo de \(e\), fato
observado e não explicado, ganharia uma razão de ser. Nenhum monopolo foi
encontrado até hoje, apesar de buscas em aceleradores, em raios cósmicos e em
rochas lunares. Vale lembrar o argumento: basta <em>um</em>, em qualquer lugar,
em qualquer época.</p>
'''

S6 = r'''
<p>Depois de tudo isso, o que sobra do curso?</p>

<p>Sobra tudo, com uma mudança de estatuto. As equações de Maxwell não são
mais a teoria fundamental do eletromagnetismo: são o <strong>limite de baixa
energia</strong> da eletrodinâmica quântica, válido quando os campos são muito
menores que o crítico de Schwinger, as distâncias muito maiores que o
comprimento de onda Compton e os fótons muito menos energéticos que
\(mc^2\). Dentro dessas condições, que cobrem toda a engenharia elétrica, toda
a óptica, toda a eletrônica e quase toda a astrofísica, elas são exatas para
qualquer propósito prático.</p>

<p>E sobra mais uma coisa, que talvez seja a mais importante e que o curso
encontrou sem anunciar. A liberdade de calibre, que apareceu no capítulo 10
como uma conveniência de cálculo, acabou se revelando o princípio organizador
de toda a física de partículas. Exigir que a teoria seja invariante sob uma
mudança de fase local da função de onda <em>força</em> a existência do campo
eletromagnético, com todas as propriedades que ele tem. Trocando o grupo de
simetria de \(U(1)\) por \(SU(2)\) e \(SU(3)\), o mesmo raciocínio produz a
interação fraca e a forte.</p>

<div class="bloco ex">
<span class="rotulo">Onde isso deixa o curso</span>
<p>O eletromagnetismo é a primeira teoria de calibre, e foi a única por
oitenta anos sem que ninguém percebesse que era uma. Quem entende por que
\(\vet{A}\) pode ser mudado sem mudar \(\vet{B}\), e por que a circulação dele
não pode, já entendeu a estrutura de que o Modelo Padrão é feito. Não é pouco
para uma disciplina que começa com duas bolinhas carregadas se repelindo.</p>
</div>
'''

S7 = r'''
<p>Os artigos originais de cada um dos tópicos acima, para quem quiser ir à
fonte:</p>

<ul>
<li><strong>Efeito Aharonov-Bohm.</strong> Y. Aharonov e D. Bohm,
<em>Significance of electromagnetic potentials in the quantum theory</em>,
Phys. Rev. <strong>115</strong>, 485 (1959).
<a href="https://doi.org/10.1103/PhysRev.115.485">doi:10.1103/PhysRev.115.485</a></li>

<li><strong>Confirmação experimental.</strong> A. Tonomura <em>et al.</em>,
Phys. Rev. Lett. <strong>56</strong>, 792 (1986).
<a href="https://doi.org/10.1103/PhysRevLett.56.792">doi:10.1103/PhysRevLett.56.792</a></li>

<li><strong>Monopolo e quantização da carga.</strong> P. A. M. Dirac,
<em>Quantised singularities in the electromagnetic field</em>, Proc. R. Soc.
Lond. A <strong>133</strong>, 60 (1931).
<a href="https://doi.org/10.1098/rspa.1931.0130">doi:10.1098/rspa.1931.0130</a></li>

<li><strong>Quantização do fluxo.</strong> B. S. Deaver e W. M. Fairbank,
Phys. Rev. Lett. <strong>7</strong>, 43 (1961).
<a href="https://doi.org/10.1103/PhysRevLett.7.43">doi:10.1103/PhysRevLett.7.43</a></li>

<li><strong>Vácuo não linear.</strong> W. Heisenberg e H. Euler,
<em>Folgerungen aus der Diracschen Theorie des Positrons</em>, Z. Phys.
<strong>98</strong>, 714 (1936).
<a href="https://doi.org/10.1007/BF01343663">doi:10.1007/BF01343663</a></li>

<li><strong>Luz espalhando luz.</strong> Colaboração ATLAS, <em>Evidence for
light-by-light scattering in heavy-ion collisions</em>, Nature Physics
<strong>13</strong>, 852 (2017).
<a href="https://doi.org/10.1038/nphys4208">doi:10.1038/nphys4208</a></li>

<li><strong>O momento magnético do elétron.</strong> X. Fan <em>et al.</em>,
Phys. Rev. Lett. <strong>130</strong>, 071801 (2023).
<a href="https://doi.org/10.1103/PhysRevLett.130.071801">doi:10.1103/PhysRevLett.130.071801</a></li>
</ul>

<p>E, do lado da Física Estatística, as duas aulas que continuam a conversa:
<a href="%(FE)s/aula09.html">magnetismo</a> e
<a href="%(FE)s/aula10.html">supercondutividade</a>.</p>
''' % {'FE': FE}

SECOES = [
    ('O muro de 10⁻¹⁵ metros', S1),
    ('Altas energias: de Thomson a Compton, e a renormalização', S2),
    ('O vácuo não é vazio', S3),
    ('O magnetismo é quântico, sem exceção', S4),
    ('Os potenciais são reais', S5),
    ('O que fica de pé', S6),
    ('Para ler na fonte', S7),
]


def main():
    titulos = [t for t, _ in SECOES]
    escreve('apendice.html', secoes_html(SECOES), secoes=titulos,
            chapeu='Fechamento do curso')


if __name__ == '__main__':
    main()
