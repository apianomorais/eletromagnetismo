# -*- coding: utf-8 -*-
"""Capítulo 7: eletrodinâmica.

O texto é escrito do zero. O Griffiths entra como referência de ordem e de
numeração de capítulo, nunca como fonte de frases, enunciados ou figuras:
os exemplos aqui são de nossa autoria, com contextos e números próprios.
"""
from molde import escreve, secoes_html
import exercicios
from lista_cap07 import LISTA

FE = 'https://apianomorais.github.io/fisica-estatistica'

S1 = r'''
<p>Os dois capítulos anteriores trataram de situações paradas: cargas que não
se movem e correntes que não mudam. Agora a corrente precisa começar, parar e
variar, e a primeira pergunta é a mais elementar de todas: o que mantém a carga
andando dentro de um fio.</p>

<p>Dentro de um condutor, a carga não anda por inércia. Ela colide, perde o que
ganhou e precisa ser empurrada de novo o tempo todo, de modo que o que
determina a corrente não é a aceleração, e sim o equilíbrio entre o empurrão e
o atrito. Escrevendo a força por unidade de carga como \(\vet{f}\), a
experiência diz que a densidade de corrente é proporcional a ela:</p>

\[ \boxed{\;\vet{J} = \sigma\vet{f},\qquad \sigma = \frac{1}{\rho}.\;} \]

<p>Esta é a lei de Ohm na forma que interessa à física, local e sem nenhum
circuito por perto. O \(\sigma\) é a condutividade do material e \(\rho\) a
resistividade, medida em ohm vezes metro. A faixa que ela cobre é a maior de
toda a física de materiais: o cobre tem \(1{,}7\times10^{-8}\ \Omega\cdot
\mathrm{m}\) e o quartzo fundido tem \(7{,}5\times10^{17}\), vinte e cinco
ordens de grandeza de diferença entre dois sólidos que cabem na mesma mão.</p>

<p>Na maioria dos casos a força por unidade de carga é só o campo elétrico,
\(\vet{f} = \vet{E}\), e aí \(\vet{J} = \sigma\vet{E}\). Mas não precisa ser:
pode ser a força magnética sobre uma carga que se move junto com o fio, pode
ser a força química dentro de uma pilha, pode ser a força de difusão numa
junção de semicondutores. Toda fonte de energia elétrica é, por definição, um
lugar onde \(\vet{f}\) <em>não</em> é eletrostática.</p>

<h3>Força eletromotriz</h3>

<p>Chamamos de força eletromotriz o trabalho por unidade de carga que a fonte
realiza para levar a carga uma volta inteira pelo circuito:</p>

\[ \boxed{\;\mathcal{E} = \oint \vet{f}_{\text{fonte}}\cdot d\vet{\ell}.\;} \]

<p>O nome é ruim, porque não se trata de força nem é medida em newtons: a fem
tem unidade de volt. O conceito, porém, é exato, e a razão de ele existir é que
a parte eletrostática do campo não pode fazer esse serviço. Para uma força
conservativa, \(\oint\vet{E}\cdot d\vet{\ell} = 0\), e um circuito movido só
por eletrostática não leva carga nenhuma por uma volta completa.</p>

<p>Numa fonte ideal, sem resistência interna, a força líquida sobre as cargas
dentro dela tem de ser nula, senão a corrente cresceria sem limite. Isso obriga
\(\vet{f}_{\text{fonte}} = -\vet{E}\) dentro da fonte, e a diferença de
potencial que aparece nos terminais vale</p>

\[ V = -\int_a^b \vet{E}\cdot d\vet{\ell} = \int_a^b
     \vet{f}_{\text{fonte}}\cdot d\vet{\ell} = \mathcal{E}. \]

<p>A fonte, então, não fabrica campo: ela empilha carga nos terminais até que o
campo eletrostático dessa carga equilibre exatamente a força que a move. Depois
disso, quem faz o trabalho no resto do circuito é esse campo eletrostático, e
quem o sustenta é a química lá dentro.</p>

<div class="destaque">
<p><strong>Exemplo trabalhado: qual resistência extrai mais potência.</strong>
Uma pilha de bancada tem \(\mathcal{E} = 9{,}0\ \mathrm{V}\) e resistência
interna \(r = 1{,}2\ \Omega\). Vamos ligar nela uma resistência de carga
\(R\) ajustável e perguntar qual valor entrega mais potência à carga.</p>

<p>Os dois resistores estão em série, de modo que a corrente é
\(I = \mathcal{E}/(r+R)\) e a potência dissipada na carga vale</p>

\[ \wp = R I^2 = \frac{\mathcal{E}^2 R}{(r+R)^2}. \]

<p>Derivando em relação a \(R\) e igualando a zero,</p>

\[ \frac{d\wp}{dR} = \frac{\mathcal{E}^2}{(r+R)^2}
   - \frac{2\mathcal{E}^2 R}{(r+R)^3} = 0
   \;\Longrightarrow\; (r+R) - 2R = 0 \;\Longrightarrow\; R = r. \]

<p>Com os números, \(R = 1{,}2\ \Omega\), corrente de \(3{,}75\ \mathrm{A}\) e
potência de \(16{,}9\ \mathrm{W}\) na carga. Repare no preço: nesse ponto a
própria pilha dissipa outros \(16{,}9\ \mathrm{W}\) internamente, de modo que o
rendimento é de exatamente 50 %. É por isso que casar resistências é a regra em
transmissão de sinal, onde o que importa é a potência entregue, e é proibido em
transmissão de energia, onde o que importa é não torrar metade dela no
caminho.</p>
</div>
'''

S2 = r'''
<p>A lei de Ohm é empírica, e vale a pena ver de onde ela poderia vir. O modelo
mais simples é o de Drude, de 1900, que trata os elétrons de condução como um
gás de bolinhas que acelera no campo e colide de vez em quando com os íons da
rede, perdendo na colisão toda a memória do que ganhou.</p>

<p>Entre duas colisões separadas por um tempo médio \(\tau\), o elétron ganha
velocidade \(a\tau = eE\tau/m\). Como a colisão zera a média, a velocidade de
deriva é dessa ordem, e com \(n\) elétrons por unidade de volume,</p>

\[ \vet{J} = -n e \vet{v}_d = \frac{n e^2 \tau}{m}\vet{E}
   \;\Longrightarrow\;
   \boxed{\;\sigma = \frac{n e^2 \tau}{m}.\;} \]

<p>O modelo acerta a forma da lei de Ohm, e isso já é bastante: a corrente sai
proporcional ao campo, e não à sua integral no tempo, justamente porque a
colisão apaga a aceleração acumulada.</p>

<div class="destaque">
<p><strong>Exemplo trabalhado: a lentidão do elétron.</strong> Um fio de cobre
de \(1{,}0\ \mathrm{mm^2}\) de seção conduz \(10\ \mathrm{A}\). O cobre tem
\(n = 8{,}5\times10^{28}\ \mathrm{m^{-3}}\) elétrons de condução e
\(\sigma = 5{,}96\times10^{7}\ \mathrm{S/m}\). Qual a velocidade de deriva, e
qual o tempo entre colisões?</p>

<p>A densidade de corrente é \(J = I/A = 10/10^{-6} = 10^{7}\
\mathrm{A/m^2}\), e a velocidade de deriva sai de \(J = nev_d\):</p>

\[ v_d = \frac{J}{ne} = \frac{10^{7}}{8{,}5\times10^{28}\times1{,}6\times10^{-19}}
       = 7{,}4\times10^{-4}\ \mathrm{m/s}. \]

<p>Menos de um milímetro por segundo. Um elétron levaria perto de meia hora
para percorrer um fio de um metro, e no entanto a lâmpada acende assim que a
chave fecha, porque o que se propaga é o campo, e não o elétron. Já o tempo
entre colisões sai da condutividade:</p>

\[ \tau = \frac{m\sigma}{ne^2}
        = \frac{9{,}11\times10^{-31}\times5{,}96\times10^{7}}
               {8{,}5\times10^{28}\times(1{,}6\times10^{-19})^2}
        = 2{,}5\times10^{-14}\ \mathrm{s}. \]

<p>Vinte e cinco femtossegundos. Entre duas colisões o elétron anda alguns
nanômetros, dezenas de distâncias atômicas.</p>
</div>

<p>Até aqui tudo bem. O problema do modelo de Drude aparece quando se pergunta
pela <em>velocidade</em> com que o elétron anda entre colisões. Pelo teorema da
equipartição clássico, ela seria térmica, da ordem de \(10^{5}\ \mathrm{m/s}\) a
300 K, e cada elétron carregaria \(3\kB/2\) de calor específico. A medida diz
outra coisa: o calor específico eletrônico de um metal é cem vezes menor que
isso, e a velocidade relevante não é térmica, e sim a velocidade de Fermi, que
é da ordem de \(10^{6}\ \mathrm{m/s}\) e quase não depende da temperatura.</p>

<p>A correção é a mesma que já apareceu no capítulo anterior: o princípio de
exclusão. Quase todos os elétrons estão presos no fundo do mar de Fermi, sem
estados vazios por perto, e só a fração \(\sim T/T_F\) que está perto da
superfície de Fermi pode participar. A expressão de \(\sigma\) sobrevive quase
intacta, com \(m\) virando massa efetiva e \(\tau\) sendo o tempo de
espalhamento dos elétrons <em>da superfície de Fermi</em>, mas tudo o mais muda.
<a href="''' + FE + r'''/aula08.html">O gás de Fermi e o calor específico
eletrônico estão no Módulo 8 da Física Estatística</a>, e é lá que a conta
quântica é feita por inteiro.</p>

<p>Vale guardar a moral: a eletrodinâmica clássica deste capítulo é exata, e
continua valendo sem emenda. O que não é clássico é a resposta do material, isto
é, quanto valem \(\sigma\), \(\varepsilon\) e \(\mu\). Esses números são o
recado que a física estatística e a física do estado sólido entregam para a
eletrodinâmica usar.</p>
'''

S3 = r'''
<p>A fonte não precisa ser química. Puxe um fio dentro de um campo magnético e
as cargas dentro dele sentem \(\vet{f} = \vet{v}\cruz\vet{B}\), que é uma força
por unidade de carga perfeitamente capaz de empurrar corrente. É isso, e nada
mais do que isso, que há dentro de um gerador.</p>

<p>O caso de bancada é uma espira retangular parcialmente dentro de uma região
de campo uniforme \(\vet{B}\), com uma barra de comprimento \(h\) que desliza
com velocidade \(\vet{v}\). Nas cargas da barra, a força por unidade de carga é
vertical e vale \(vB\), de modo que</p>

\[ \mathcal{E} = \oint \vet{f}\cdot d\vet{\ell} = vBh. \]

<p>Os outros três lados não contribuem: dois deles têm a força perpendicular ao
fio, e o quarto está fora do campo.</p>

<figure class="figura-exemplo" style="max-width:38rem">
  <img src="assets/img/cap07_barra.svg" alt="Barra deslizante nos trilhos">
  <figcaption>A barra desliza para a direita e a força magnética empurra as
  cargas dela para cima, fechando a corrente pelo resistor. Essa corrente, de
  volta no campo, produz uma força que aponta contra o movimento: é a lei de
  Lenz, e é o freio.</figcaption>
</figure>

<div data-widget="barra"></div>

<p class="legenda">Com força externa constante a velocidade não cresce sem
limite: ela tende ao valor terminal \(FR/(Bh)^2\), que é onde a força
magnética iguala a aplicada, com constante de tempo \(mR/(Bh)^2\).</p>

<p>Agora olhe o mesmo problema por outro ângulo. O fluxo do campo pela espira é
\(\Phi = Bhx\), com \(x\) a parte ainda dentro do campo, e ele diminui à medida
que a espira sai:</p>

\[ \frac{d\Phi}{dt} = Bh\frac{dx}{dt} = -Bhv
   \;\Longrightarrow\;
   \boxed{\;\mathcal{E} = -\frac{d\Phi}{dt}.\;} \]

<p>É a <strong>regra do fluxo</strong>, e ela é muito mais geral do que esta
dedução sugere. Vale para espira de qualquer forma, deformando-se de qualquer
jeito, com o campo variando de ponto a ponto.</p>

<h3>Por que a regra do fluxo vale sempre</h3>

<p>Considere a espira num instante \(t\) e no instante \(t+dt\). A diferença
entre os dois fluxos é o fluxo através da tira estreita varrida pela espira no
intervalo, cujo elemento de área é</p>

\[ d\vet{a} = \left(\vet{v}\cruz d\vet{\ell}\right)dt, \]

<p>de modo que</p>

\[ \frac{d\Phi}{dt} = \oint \vet{B}\cdot\left(\vet{v}\cruz d\vet{\ell}\right). \]

<p>Aqui entra o passo bonito. Chame de \(\vet{u}\) a velocidade da carga ao
longo do fio e de \(\vet{w} = \vet{u} + \vet{v}\) a velocidade total dela. Como
\(\vet{u}\) é paralela a \(d\vet{\ell}\), trocar \(\vet{v}\) por \(\vet{w}\) no
produto misto não muda nada, porque o termo extra tem dois vetores paralelos.
Então</p>

\[ \frac{d\Phi}{dt} = \oint \vet{B}\cdot\left(\vet{w}\cruz d\vet{\ell}\right)
   = -\oint \left(\vet{w}\cruz\vet{B}\right)\cdot d\vet{\ell}, \]

<p>e \(\vet{w}\cruz\vet{B}\) é exatamente a força magnética por unidade de carga
sentida pelas cargas do fio. Logo</p>

\[ \frac{d\Phi}{dt} = -\oint \vet{f}_m\cdot d\vet{\ell} = -\mathcal{E}. \]

<p>Repare no que a demonstração usou: apenas a força de Lorentz e a geometria.
Nenhuma lei nova entrou aqui. A fem de movimento <em>não</em> é a lei de
Faraday, é a força magnética disfarçada, e o fato de as duas darem a mesma
fórmula é, por enquanto, uma coincidência.</p>

<div class="destaque">
<p><strong>Exemplo trabalhado: o freio magnético.</strong> A barra do exemplo
tem \(h = 12\ \mathrm{cm}\), o campo vale \(B = 0{,}35\ \mathrm{T}\), o circuito
tem resistência total \(R = 0{,}50\ \Omega\) e alguém puxa a barra a
\(v = 2{,}0\ \mathrm{m/s}\) constantes. Quanta força é preciso fazer, e para
onde vai a energia?</p>

<p>A fem é \(\mathcal{E} = vBh = 2{,}0\times0{,}35\times0{,}12 = 0{,}084\
\mathrm{V}\), e a corrente \(I = \mathcal{E}/R = 0{,}168\ \mathrm{A}\). Essa
corrente, atravessando o campo, sente uma força \(F = IhB = 0{,}168\times
0{,}12\times0{,}35 = 7{,}1\times10^{-3}\ \mathrm{N}\), que pela lei de Lenz se
opõe ao movimento. Para manter a velocidade é preciso fazer exatamente essa
força, de modo que a potência mecânica gasta é</p>

\[ \wp_{\text{mec}} = Fv = 7{,}1\times10^{-3}\times2{,}0
   = 1{,}41\times10^{-2}\ \mathrm{W}, \]

<p>e a potência dissipada no resistor é</p>

\[ \wp_{\text{Joule}} = I^2R = (0{,}168)^2\times0{,}50
   = 1{,}41\times10^{-2}\ \mathrm{W}. \]

<p>São iguais, e tinham de ser. A força magnética não realiza trabalho, como
ficou demonstrado no capítulo 5: quem paga a conta é quem puxa a barra, e o
campo apenas transfere. É assim que funciona o freio eletromagnético de um
caminhão, e é por isso que um ímã forte cai devagar dentro de um tubo de
cobre.</p>
</div>
'''

S4 = r'''
<p>Faraday, em 1831, fez três experiências que parecem a mesma coisa e não são.
Na primeira ele puxou a espira para fora do campo, e apareceu corrente: é a fem
de movimento da seção anterior, explicada pela força magnética. Na segunda ele
deixou a espira parada e puxou o <em>ímã</em>, e apareceu a mesma corrente. Na
terceira ele deixou tudo parado e variou a intensidade do campo, e a corrente
apareceu de novo.</p>

<p>A segunda experiência é a que incomoda. Com a espira parada, as cargas dela
estão paradas, e carga parada não sente força magnética nenhuma. Alguma coisa
precisa empurrar essas cargas, e essa coisa só pode ser um campo elétrico. A
conclusão de Faraday foi direta: <strong>campo magnético que varia no tempo
produz campo elétrico</strong>.</p>

<p>O resultado quantitativo é que a mesma regra do fluxo governa os três casos,
e no segundo e no terceiro a fem é a circulação de um campo elétrico de verdade:</p>

\[ \oint \vet{E}\cdot d\vet{\ell} = -\frac{d\Phi}{dt}. \]

<p>Com a espira parada, só o campo varia, e a derivada entra na integral:</p>

\[ \oint \vet{E}\cdot d\vet{\ell}
   = -\iint \pder{\vet{B}}{t}\cdot d\vet{a}, \]

<p>e aplicando o teorema de Stokes ao lado esquerdo, como a curva é arbitrária,
os integrandos têm de ser iguais ponto a ponto:</p>

\[ \boxed{\;\rot{\vet{E}} = -\pder{\vet{B}}{t}.\;} \]

<p>Esta é a lei de Faraday na forma diferencial, e é a terceira das quatro
equações de Maxwell. Note o que ela faz com a eletrostática: o campo elétrico
deixa de ser conservativo. A integral de \(\vet{E}\) por um caminho fechado só é
nula enquanto nada variar no tempo, e a ideia de potencial escalar, que foi o
pilar do primeiro semestre, precisa ser revista. Faremos isso no capítulo
10.</p>

<div class="bloco fisica">
<span class="rotulo">A coincidência que ninguém engoliu</span>
<p>Repare na estrutura do que acabou de acontecer. No caso da espira que se
move, a explicação é a força magnética \(q\vet{v}\cruz\vet{B}\) sobre as cargas.
No caso do ímã que se move, a explicação é um campo elétrico induzido. São dois
mecanismos distintos, com duas fórmulas distintas, e ainda assim eles dão
sempre o mesmo número, porque só o movimento relativo importa.</p>
<p>Nenhuma experiência distingue os dois casos, e é exatamente com essa
assimetria que Einstein abre o artigo de 1905 que funda a relatividade restrita.
A resposta é que \(\vet{E}\) e \(\vet{B}\) não são dois campos, e sim duas
faces do mesmo objeto, vistas de referenciais diferentes.
<a href="index.html#s1">A história completa está na página de entrada</a>, e a
conta, em Eletromagnetismo III.</p>
</div>
'''

S5 = r'''
<p>A lei de Faraday determina o campo elétrico induzido do mesmo jeito que a
lei de Ampère determina o campo magnético de uma corrente. A comparação é
literal, e vale a pena colocá-la lado a lado:</p>

<div class="cartoes">
  <article class="cartao">
    <h3>Magnetostática</h3>
    \[ \rot{\vet{B}} = \mu_0\vet{J},\qquad \divg{\vet{B}} = 0 \]
    <p>Com simetria suficiente, \(\oint\vet{B}\cdot d\vet{\ell} =
    \mu_0 I_{\text{enl}}\) resolve de cabeça.</p>
  </article>
  <article class="cartao">
    <h3>Campo induzido</h3>
    \[ \rot{\vet{E}} = -\pder{\vet{B}}{t},\qquad \divg{\vet{E}} = 0 \]
    <p>Sem cargas por perto, \(\oint\vet{E}\cdot d\vet{\ell} = -d\Phi/dt\)
    resolve do mesmo jeito.</p>
  </article>
</div>

<p>A correspondência é exata com a troca \(\mu_0\vet{J} \to -\partial
\vet{B}/\partial t\). Isso significa que todo resultado de magnetostática pode
ser reaproveitado: onde havia corrente uniforme, ponha \(-\partial B/\partial t\)
uniforme, e o campo elétrico induzido terá a forma do campo magnético daquela
corrente.</p>

<div class="destaque">
<p><strong>Exemplo trabalhado: o campo elétrico dentro de um solenoide que
liga.</strong> Um solenoide longo de raio \(R = 4{,}0\ \mathrm{cm}\) tem o campo
interno crescendo à taxa constante \(dB/dt = 0{,}25\ \mathrm{T/s}\). Qual o
campo elétrico induzido dentro e fora?</p>

<p>Por simetria, \(\vet{E}\) é azimutal e só depende da distância \(s\) ao eixo,
exatamente como o campo magnético de um fio grosso com corrente uniforme. Tome
uma curva circular de raio \(s\) centrada no eixo. Dentro do solenoide
(\(s \lt R\)), o fluxo enlaçado é \(B\pi s^2\), e</p>

\[ E\,(2\pi s) = -\frac{d}{dt}\left(B\pi s^2\right)
   \;\Longrightarrow\;
   \vet{E} = -\frac{s}{2}\pder{B}{t}\,\vers{\phi}. \]

<p>Fora (\(s \gt R\)), o fluxo enlaçado não cresce mais com \(s\), porque não há
campo fora do solenoide, e</p>

\[ E\,(2\pi s) = -\pi R^2\pder{B}{t}
   \;\Longrightarrow\;
   \vet{E} = -\frac{R^2}{2s}\pder{B}{t}\,\vers{\phi}. \]

<p>Com os números, na borda do solenoide \(E = (0{,}04/2)\times0{,}25 =
5{,}0\ \mathrm{mV/m}\), e a dez centímetros do eixo cai para
\(2{,}0\ \mathrm{mV/m}\). Pouco, mas mensurável, e perfeitamente capaz de
mover carga.</p>

<figure class="figura-exemplo" style="max-width:30rem">
  <img src="assets/img/cap07_induzido.svg" alt="Campo elétrico induzido">
  <figcaption>As linhas de \(\vet{E}\) são circunferências, como as de
  \(\vet{B}\) em torno de um fio grosso. Dentro da região de campo elas
  crescem com \(s\); fora, onde o campo magnético é nulo, elas continuam
  existindo e caem com \(1/s\).</figcaption>
</figure>

<p>O sinal negativo é a lei de Lenz escrita em símbolos: o campo elétrico
induzido empurra a carga no sentido que criaria um campo magnético <em>contra</em>
a variação. E note o que o resultado de fora significa: existe campo elétrico
numa região onde o campo magnético é rigorosamente nulo, e onde ele sempre foi
nulo. O que chega até ali não é o campo magnético, é a sua variação no
tempo.</p>
</div>

<p>Esse é o princípio do bétatron, acelerador em que elétrons dão voltas numa
câmara em anel enquanto um eletroímã central aumenta o fluxo: o campo elétrico
induzido acelera, o campo magnético da própria máquina curva, e as duas coisas
são ajustadas para que o raio da órbita não mude.</p>
'''

S6 = r'''
<p>Duas espiras paradas, uma ao lado da outra. Passe uma corrente estacionária
\(I_1\) pela primeira: pela lei de Biot-Savart o campo que ela cria é
proporcional a \(I_1\), e portanto o fluxo dele através da segunda também é:</p>

\[ \Phi_2 = M_{21} I_1. \]

<p>A constante \(M_{21}\) é a <strong>indutância mútua</strong>, e ela depende
só da geometria das duas espiras e da posição relativa entre elas. Escrevendo o
fluxo pelo potencial vetor, que é onde a conta fica bonita,</p>

\[ \Phi_2 = \iint \left(\rot{\vet{A}_1}\right)\cdot d\vet{a}_2
          = \oint \vet{A}_1\cdot d\vet{\ell}_2, \]

<p>e substituindo a expressão do potencial vetor de uma espira,</p>

\[ \boxed{\;M_{21} = \frac{\mu_0}{4\pi}\oint\oint
   \frac{d\vet{\ell}_1\cdot d\vet{\ell}_2}
        {\left|\vet{r}_2-\vet{r}_1\right|}.\;} \]

<p>É a fórmula de Neumann, e o que ela tem de notável não é o seu valor
prático, que é pequeno, e sim a sua <em>simetria</em>. Trocar as duas espiras de
papel troca \(d\vet{\ell}_1\) com \(d\vet{\ell}_2\) e deixa o resto idêntico,
de modo que</p>

\[ M_{12} = M_{21} \equiv M. \]

<p>Pare um momento nisso. Uma espira enorme e uma espira minúscula, uma
quadrada e uma redonda, uma perto e outra longe: seja qual for a geometria, o
fluxo que a primeira manda na segunda por ampère é igual ao fluxo que a segunda
manda na primeira por ampère. Não há razão intuitiva para isso, e a conta
direta em qualquer caso concreto costuma ser horrorosa. A fórmula de Neumann
mostra que é inevitável.</p>

<div class="destaque">
<p><strong>Exemplo trabalhado: o solenoide curto dentro do longo.</strong> Um
solenoide curto, de comprimento \(\ell = 3{,}0\ \mathrm{cm}\), raio
\(a = 8{,}0\ \mathrm{mm}\) e \(n_1 = 2000\) espiras por metro, está no eixo de
um solenoide muito longo, de raio \(b = 2{,}5\ \mathrm{cm}\) e \(n_2 = 800\)
espiras por metro. Qual a indutância mútua?</p>

<p>Calcular o fluxo que o solenoide curto manda no longo é um pesadelo: o campo
dele é bagunçado fora das suas extremidades. Calcular o contrário é trivial.
Ligue \(I\) no solenoide <em>longo</em>: o campo dentro dele é uniforme e vale
\(\mu_0 n_2 I\), e o fluxo através de cada espira do solenoide curto é
\(\mu_0 n_2 I \pi a^2\). Como o solenoide curto tem \(n_1\ell\) espiras,</p>

\[ \Phi = \mu_0 n_2 n_1 \ell\,\pi a^2 I
   \;\Longrightarrow\;
   M = \mu_0 n_1 n_2 \ell\,\pi a^2. \]

<p>Com os números,</p>

\[ M = 4\pi\times10^{-7}\times2000\times800\times0{,}030
       \times\pi\times(8{,}0\times10^{-3})^2
     = 1{,}21\times10^{-5}\ \mathrm{H}, \]

<p>isto é, 12 microhenries. E, pela simetria, esse mesmo número responde à
pergunta original, que era o fluxo no solenoide longo. <strong>É este o uso
prático da reciprocidade</strong>: calcular o lado fácil e ler a resposta do
lado difícil.</p>
</div>

<h3>Autoindutância e a oposição à mudança</h3>

<p>A espira também enlaça o próprio campo, e o fluxo que ela manda em si mesma
é proporcional à sua corrente:</p>

\[ \Phi = L I,\qquad \mathcal{E} = -L\der{I}{t}. \]

<p>O \(L\) é a autoindutância, medida em henry, e é sempre positivo. O sinal
negativo da fem é a lei de Lenz mais uma vez, e aqui ela ganha um nome
sugestivo: a autoindutância é a <em>inércia</em> elétrica do circuito. Ela não
impede que a corrente mude, ela se opõe a que a corrente mude depressa, do mesmo
jeito que a massa não impede que um corpo acelere.</p>

<p>Para um solenoide de \(N\) espiras, comprimento \(\ell\) e área \(A\), o
campo interno é \(\mu_0 N I/\ell\), o fluxo total enlaçado é \(N\) vezes o fluxo
de uma espira, e</p>

\[ L = \frac{\mu_0 N^2 A}{\ell}. \]

<p>O quadrado em \(N\) é o que faz um indutor de bancada ser possível: dobrar o
número de voltas quadruplica a indutância, porque cada volta contribui para o
campo e cada volta enlaça o campo de todas as outras.</p>
'''

S7 = r'''
<p>Para estabelecer uma corrente é preciso vencer a fem de autoindução, e o
trabalho gasto nisso fica guardado em algum lugar. Seguindo a conta: o trabalho
por unidade de carga contra a fem induzida é \(-\mathcal{E}\), e passam
\(I = dq/dt\) cargas por unidade de tempo, de modo que</p>

\[ \frac{dW}{dt} = -\mathcal{E}I = L I\der{I}{t}
   \;\Longrightarrow\;
   \boxed{\;W = \frac{1}{2}LI^2.\;} \]

<p>Não há nada de misterioso até aqui: é a mesma estrutura de \(\frac12 mv^2\) e
de \(\frac12 CV^2\). A pergunta interessante é <em>onde</em> essa energia está, e
a resposta é a mesma da eletrostática: ela está no campo. Para chegar lá,
escreva o fluxo pelo potencial vetor,</p>

\[ W = \frac{1}{2}I\oint \vet{A}\cdot d\vet{\ell}
     = \frac{1}{2}\iiint \left(\vet{A}\cdot\vet{J}\right)d\tau, \]

<p>troque \(\vet{J}\) pela lei de Ampère, \(\mu_0\vet{J} = \rot{\vet{B}}\), e use
a identidade \(\divg{\left(\vet{A}\cruz\vet{B}\right)} =
\vet{B}\cdot\left(\rot{\vet{A}}\right) - \vet{A}\cdot\left(\rot{\vet{B}}\right)\),
que com \(\rot{\vet{A}} = \vet{B}\) deixa</p>

\[ W = \frac{1}{2\mu_0}\iiint B^2\,d\tau
     - \frac{1}{2\mu_0}\oiint \left(\vet{A}\cruz\vet{B}\right)\cdot d\vet{a}. \]

<p>O volume de integração pode ser qualquer um que contenha toda a corrente, e
escolhendo-o cada vez maior o termo de superfície some, porque \(\vet{A}\) e
\(\vet{B}\) caem com a distância mais depressa do que a área cresce. Sobra</p>

\[ \boxed{\;W = \frac{1}{2\mu_0}\iiint B^2\,d\tau,\qquad
   u_B = \frac{B^2}{2\mu_0}.\;} \]

<p>Compare com a eletrostática, \(u_E = \tfrac12\varepsilon_0E^2\). As duas
densidades de energia são irmãs, e no capítulo 8 elas vão aparecer juntas no
teorema de Poynting, que é onde o balanço de energia do campo fica completo.</p>

<div class="destaque">
<p><strong>Exemplo trabalhado: quanta energia cabe num indutor.</strong> O
solenoide da seção anterior, com \(n = 2000\) espiras por metro, raio
\(a = 8{,}0\ \mathrm{mm}\) e comprimento \(\ell = 3{,}0\ \mathrm{cm}\), conduz
\(I = 1{,}5\ \mathrm{A}\). Vamos calcular a energia pelos dois caminhos e
conferir.</p>

<p><strong>Pela indutância.</strong> Com \(N = n\ell = 60\) espiras e
\(A = \pi a^2 = 2{,}01\times10^{-4}\ \mathrm{m^2}\),</p>

\[ L = \frac{\mu_0 N^2 A}{\ell}
     = \frac{4\pi\times10^{-7}\times3600\times2{,}01\times10^{-4}}{0{,}030}
     = 3{,}03\times10^{-5}\ \mathrm{H}, \]

\[ W = \tfrac12 L I^2 = \tfrac12\times3{,}03\times10^{-5}\times2{,}25
     = 3{,}41\times10^{-5}\ \mathrm{J}. \]

<p><strong>Pelo campo.</strong> O campo interno vale \(B = \mu_0 n I =
4\pi\times10^{-7}\times2000\times1{,}5 = 3{,}77\ \mathrm{mT}\), o volume é
\(A\ell = 6{,}03\times10^{-6}\ \mathrm{m^3}\), e</p>

\[ W = \frac{B^2}{2\mu_0}A\ell
     = \frac{(3{,}77\times10^{-3})^2}{2\times4\pi\times10^{-7}}
       \times6{,}03\times10^{-6}
     = 3{,}41\times10^{-5}\ \mathrm{J}. \]

<p>Os dois batem, como tinham de bater. E repare na ordem de grandeza: trinta e
quatro microjoules, menos do que uma formiga gasta para subir um degrau. Guardar
energia em campo magnético é notoriamente ineficiente, e é por isso que ninguém
alimenta um carro com indutor. O que se guarda bem em campo magnético não é
energia, é <em>corrente</em>, e é disso que vivem as fontes chaveadas.</p>
</div>
'''

S8 = r'''
<p>Reúna o que existe até este ponto do curso:</p>

\[ \divg{\vet{E}} = \frac{\rho}{\varepsilon_0},\qquad
   \divg{\vet{B}} = 0,\qquad
   \rot{\vet{E}} = -\pder{\vet{B}}{t},\qquad
   \rot{\vet{B}} = \mu_0\vet{J}. \]

<p>As três primeiras estão certas. A quarta está errada, e o jeito de ver isso
não exige nenhuma experiência nova: basta tomar o divergente dos dois lados. O
divergente de um rotacional é identicamente nulo, de modo que a lei de Ampère,
como está, exige \(\divg{\vet{J}} = 0\) sempre. Mas a equação da continuidade
diz</p>

\[ \divg{\vet{J}} = -\pder{\rho}{t}, \]

<p>que só é nulo quando a carga não se acumula em lugar nenhum. A lei de Ampère,
portanto, é incompatível com a conservação da carga fora da magnetostática. Foi
Maxwell quem notou e quem consertou.</p>

<p>O conserto é quase forçado. Substitua \(\rho\) pela lei de Gauss:</p>

\[ \divg{\vet{J}} + \pder{}{t}\left(\varepsilon_0\divg{\vet{E}}\right)
   = \divg{\left(\vet{J} + \varepsilon_0\pder{\vet{E}}{t}\right)} = 0. \]

<p>A combinação entre parênteses tem divergente nulo <em>sempre</em>, e é ela,
portanto, que deve aparecer no lugar de \(\vet{J}\):</p>

\[ \boxed{\;\rot{\vet{B}} = \mu_0\vet{J}
   + \mu_0\varepsilon_0\pder{\vet{E}}{t}.\;} \]

<p>O termo novo tem dimensão de densidade de corrente e por isso ganhou o nome
de <strong>corrente de deslocamento</strong>, \(\vet{J}_d = \varepsilon_0
\partial\vet{E}/\partial t\). O nome é infeliz, porque não há nada se
deslocando: é campo elétrico variando, e só.</p>

<div class="destaque">
<p><strong>Exemplo trabalhado: o capacitor que carrega, e as duas
superfícies.</strong> Um capacitor de placas paralelas circulares de raio
\(R = 5{,}0\ \mathrm{cm}\) é carregado por um fio que conduz \(I = 0{,}30\
\mathrm{A}\). Aplique a lei de Ampère a um círculo de raio \(s\) em torno do
fio, à altura do espaço entre as placas.</p>

<p>A lei de Ampère permite apoiar na curva <em>qualquer</em> superfície. Escolha
primeiro a superfície plana, que o fio atravessa: a corrente enlaçada é \(I\), e
o campo dá \(B = \mu_0 I/2\pi s\). Escolha agora a superfície em forma de saco,
que passa entre as placas sem tocar no fio: a corrente enlaçada é
<em>zero</em>, e o campo daria zero. A mesma curva, duas respostas. É aqui que a
lei de Ampère sem emenda morre.</p>

<figure class="figura-exemplo" style="max-width:38rem">
  <img src="assets/img/cap07_superficies.svg" alt="As duas superfícies amperianas">
  <figcaption>As duas superfícies se apoiam na mesma curva e têm todo o direito
  de ser usadas. O fio atravessa a primeira e não a segunda, de modo que, sem o
  termo de Maxwell, a lei de Ampère não seria nem bem definida.</figcaption>
</figure>

<p>Com a correção de Maxwell, a segunda superfície não enlaça corrente nenhuma,
mas enlaça campo elétrico variando. Entre as placas, \(E = \sigma/\varepsilon_0
= Q/\varepsilon_0\pi R^2\), e</p>

\[ \varepsilon_0\pder{E}{t}\,\pi R^2
   = \varepsilon_0\,\frac{1}{\varepsilon_0\pi R^2}\der{Q}{t}\,\pi R^2 = I. \]

<p>A corrente de deslocamento através do saco vale exatamente a corrente de
condução através do plano. As duas superfícies voltam a concordar, e é por isso
que o termo de Maxwell não é um ajuste cosmético: sem ele a lei de Ampère nem
sequer é bem definida.</p>

<p>Para \(s \lt R\), entre as placas, a mesma conta dá o campo magnético
<em>dentro</em> do capacitor,</p>

\[ B = \frac{\mu_0 I s}{2\pi R^2}, \]

<p>que na borda da placa vale \(\mu_0 I/2\pi R = 1{,}2\ \mu\mathrm{T}\), e casa
continuamente com o campo do fio. Existe campo magnético entre as placas de um
capacitor carregando, mesmo sem nenhuma carga passando por ali.</p>
</div>

<h3>As equações de Maxwell</h3>

<p>Com a correção no lugar, o conjunto fecha:</p>

\[ \divg{\vet{E}} = \frac{\rho}{\varepsilon_0},\qquad
   \divg{\vet{B}} = 0, \]

\[ \rot{\vet{E}} = -\pder{\vet{B}}{t},\qquad
   \rot{\vet{B}} = \mu_0\vet{J} + \mu_0\varepsilon_0\pder{\vet{E}}{t}. \]

<p>Junto com a força de Lorentz \(\vet{F} = q(\vet{E} + \vet{v}\cruz\vet{B})\) e
com a conservação da carga, elas contêm toda a eletrodinâmica clássica. Tudo o
que vem depois, no resto desta sequência e em qualquer curso adiante, é
consequência: as ondas do capítulo 9, a radiação do capítulo 11, a óptica
inteira, a relatividade.</p>

<p>Vale notar a assimetria que sobrou. O campo elétrico tem fonte escalar
(\(\rho\)) e o magnético não tem (\(\divg{\vet{B}} = 0\)), porque nunca se achou
monopolo magnético. Se um dia aparecer, as equações acomodam sem nenhum estrago:
basta acrescentar \(\rho_m\) na segunda e \(\vet{J}_m\) na terceira, e a simetria
fica completa.</p>

<h3>Na matéria</h3>

<p>Dentro de um material, convém separar o que é livre do que é ligado. Os
capítulos 4 e 6 já deram dois dos três pedaços: a polarização produz carga
ligada e a magnetização produz corrente ligada,</p>

\[ \rho_b = -\divg{\vet{P}},\qquad
   \sigma_b = \vet{P}\cdot\vers{n},\qquad
   \vet{J}_b = \rot{\vet{M}}. \]

<p>Falta o terceiro, que é novo e só aparece agora que as coisas variam no
tempo. Se a polarização aumenta, a carga ligada acumulada nas faces aumenta, e
para chegar lá ela teve de atravessar o material. Isso é uma corrente, e não é
nem livre nem de magnetização:</p>

\[ \boxed{\;\vet{J}_p = \pder{\vet{P}}{t}.\;} \]

<p>Com os três pedaços, a carga total é \(\rho = \rho_f + \rho_b\) e a corrente
total é \(\vet{J} = \vet{J}_f + \vet{J}_b + \vet{J}_p\). Substituindo nas
equações e agrupando, aparecem \(\vet{D} = \varepsilon_0\vet{E} + \vet{P}\) e
\(\vet{H} = \vet{B}/\mu_0 - \vet{M}\), já conhecidos dos capítulos 4 e 6, e as
equações na matéria ficam</p>

\[ \divg{\vet{D}} = \rho_f,\qquad
   \divg{\vet{B}} = 0, \]

\[ \rot{\vet{E}} = -\pder{\vet{B}}{t},\qquad
   \rot{\vet{H}} = \vet{J}_f + \pder{\vet{D}}{t}. \]

<p>Elas têm exatamente a mesma forma das do vácuo, com \(\vet{D}\) e \(\vet{H}\)
no lugar de \(\vet{E}\) e \(\vet{B}\) e só a carga e a corrente livres à vista.
Isso é uma conveniência enorme e uma armadilha: o sistema só fecha quando se
acrescenta a resposta do material, \(\vet{D} = \varepsilon\vet{E}\) e
\(\vet{H} = \vet{B}/\mu\), que não vem da eletrodinâmica e nem sempre é linear.
De onde vêm \(\varepsilon\) e \(\mu\) é assunto da matéria condensada, e o
capítulo 6 já mostrou um caso em que a relação não é função nenhuma: a
histerese.</p>
'''

S9 = r'''
<p>Três programas, no mesmo padrão dos capítulos anteriores: cada um resolve
por via numérica algo que a página resolveu no papel, e cada um traz no
cabeçalho como conferir se acertou.</p>

<div class="cartoes">
  <article class="cartao">
    <h3><a href="codigo/barra_deslizante.py">barra_deslizante.py</a></h3>
    <p>Integra o circuito da barra que desliza, com a equação de movimento
    acoplada à corrente, e acompanha o balanço de energia instante a instante.</p>
    <p><strong>Confira assim:</strong> com força externa constante a velocidade
    tem de tender ao valor terminal \(F R/(Bh)^2\); e, em queda livre sem força
    externa, o trabalho mecânico tem de bater com a energia dissipada no
    resistor em todo instante. O programa imprime a diferença.</p>
  </article>
  <article class="cartao">
    <h3><a href="codigo/indutancia_mutua.py">indutancia_mutua.py</a></h3>
    <p>Calcula a indutância mútua de duas espiras pela fórmula de Neumann, por
    integração dupla sobre os dois contornos, para qualquer posição relativa.</p>
    <p><strong>Confira assim:</strong> \(M_{12}\) e \(M_{21}\) têm de dar o
    mesmo número até o erro de truncamento, mesmo com espiras de tamanhos muito
    diferentes; e, para espiras coaxiais distantes, \(M\) tem de tender a
    \(\mu_0\pi a^2 b^2/2d^3\). O programa compara os três.</p>
  </article>
  <article class="cartao">
    <h3><a href="codigo/capacitor_deslocamento.py">capacitor_deslocamento.py</a></h3>
    <p>Monta o campo magnético em torno de um capacitor que carrega, somando a
    corrente de condução e a de deslocamento, e varre o raio por dentro e por
    fora da placa.</p>
    <p><strong>Confira assim:</strong> as duas superfícies apoiadas na mesma
    curva têm de dar a mesma corrente enlaçada, e o campo tem de ser contínuo na
    borda da placa, onde as duas expressões se encontram.</p>
  </article>
</div>

<p>O primeiro programa é também o widget desta página, de modo que dá para
brincar com os parâmetros antes de baixar o código e mexer nele.</p>
'''

SECOES = [
    ('O que empurra a carga', S1),
    ('Ohm, Drude e o que o clássico erra', S2),
    ('Fem de movimento e a regra do fluxo', S3),
    ('A lei de Faraday', S4),
    ('O campo elétrico induzido', S5),
    ('Indutância', S6),
    ('A energia no campo magnético', S7),
    ('A corrente de deslocamento', S8),
    ('No Spyder', S9),
]


SECOES.append(('Exercícios propostos', exercicios.bloco(LISTA)))


def main():
    titulos = [t for t, _ in SECOES]
    escreve('cap07.html', secoes_html(SECOES), secoes=titulos)


if __name__ == '__main__':
    main()
