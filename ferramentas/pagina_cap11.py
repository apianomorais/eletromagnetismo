# -*- coding: utf-8 -*-
"""Capítulo 11: radiação.

O texto é escrito do zero. O Griffiths entra como referência de ordem e de
numeração de capítulo, nunca como fonte de frases, enunciados ou figuras.

A seção 2 segue o caminho de J. J. Thomson, a partir do roteiro do professor
(conteudo/cap11_larmor_thomson.tex), com as correções anotadas no commit.
"""
from molde import escreve, secoes_html
import exercicios
from lista_cap11 import LISTA

S1 = r'''
<p>Uma carga parada tem campo, e esse campo guarda energia. Uma carga em
movimento uniforme tem campo, e esse campo carrega energia junto com ela. Em
nenhum dos dois casos alguma energia se perde: desligue o movimento e tudo
volta. Radiação é outra coisa, e vale a pena ser preciso sobre qual.</p>

<p>Tome uma esfera de raio \(r\) em volta da fonte e pergunte quanta energia
atravessa a sua superfície. O fluxo é a integral do vetor de Poynting, e a
área cresce com \(r^2\). Para que o resultado não desapareça quando a esfera
cresce, é preciso que</p>

\[ \oint\vet{S}\cdot d\vet{a} \sim S\,r^2 \sim E^2r^2 \]

<p>permaneça finito, e isso exige \(E \sim 1/r\). Essa é a definição
operacional: <strong>radiação é a parte do campo que cai com \(1/r\)</strong>.
Todo o resto, por mais intenso que seja perto da fonte, se dilui depressa
demais para chegar ao infinito.</p>

<p>O capítulo 10 já mostrou onde essa parte mora. Nos campos de uma carga
pontual em movimento qualquer, a parcela que vai com \(1/\imath^2\) depende
apenas da velocidade e acompanha a carga; a parcela que vai com \(1/\imath\)
é proporcional à <em>aceleração</em>. A conclusão é curta e tem uma
consequência enorme:</p>

<div class="bloco fisica">
<span class="rotulo">O critério</span>
<p>Carga parada não irradia. Carga em movimento uniforme não irradia. Carga
<em>acelerada</em> irradia, e a energia que ela perde não volta nunca
mais.</p>
</div>

<p>Resta calcular quanto. Há dois caminhos. Um parte dos potenciais de
Liénard-Wiechert, que o capítulo 10 construiu, e exige derivar expressões
desconfortáveis. O outro, mais curto e mais físico, é o que J. J. Thomson usou
em 1903, e é o que seguimos aqui.</p>
'''

S2 = r'''
<p>A ideia é começar pelo potencial vetor e descobrir que, para calcular
radiação, quase tudo o que torna o problema difícil é desnecessário.</p>

<h3>O ponto de partida</h3>

<p>No calibre de Lorenz, os potenciais satisfazem equações de onda com fonte,
cuja solução retardada o capítulo 10 obteve:</p>

\[ \vet{A}(\vet{r},t)
   = \frac{\mu_0}{4\pi}\int\frac{\vet{J}(\vet{r}',t_r)}{\left|\vet{r}
     -\vet{r}'\right|}\,d\tau',
   \qquad t_r = t - \frac{\left|\vet{r}-\vet{r}'\right|}{c}. \]

<p>Vamos impor duas condições, e são elas que fazem o problema desmoronar em
poucas linhas.</p>

<p><strong>Primeira:</strong> o observador está longe, muito mais longe que o
tamanho da fonte. Então \(\left|\vet{r}-\vet{r}'\right| \approx r\) no
denominador.</p>

<p><strong>Segunda:</strong> a fonte é pequena comparada ao comprimento de onda
da radiação que emite. Então o atraso <em>dentro</em> da fonte é desprezível, e
todos os pedaços dela contribuem com o mesmo tempo retardado,
\(t_r \approx t - r/c\). É a aproximação de dipolo, e é exatamente aquilo que
uma partícula não relativística satisfaz: ela anda muito menos que \(\lambda\)
em um período, justamente porque \(v \ll c\).</p>

<h3>A integral que sobra</h3>

<p>Com as duas condições,</p>

\[ \vet{A}(\vet{r},t) \approx \frac{\mu_0}{4\pi r}
   \int\vet{J}\!\left(\vet{r}',t-\tfrac{r}{c}\right)d\tau'. \]

<p>A integral da densidade de corrente sobre a fonte é uma quantidade
conhecida. Para uma distribuição qualquer,</p>

\[ \int\vet{J}\,d\tau' = \der{\vet{p}}{t},
   \qquad \vet{p} = \int\vet{r}'\rho\,d\tau', \]

<p>isto é, a derivada do momento de dipolo <em>elétrico</em>. Para uma única
carga pontual, \(\vet{p} = q\vet{w}(t)\) e a integral vale simplesmente
\(q\vet{v}\). O dipolo magnético e os multipolos de ordem mais alta aparecem só
no termo seguinte da expansão, aquele que guardamos no "aproximadamente", e
são menores por um fator \(v/c\). Logo</p>

\[ \boxed{\;\vet{A}(\vet{r},t)
   \approx \frac{\mu_0}{4\pi}\frac{q\,\vet{v}(t_r)}{r}
   = \frac{\mu_0}{4\pi}\frac{\dot{\vet{p}}(t_r)}{r}.\;} \]

<h3>Do potencial ao campo</h3>

<p>Falta tirar \(\vet{E}\) e \(\vet{B}\), e aqui entra de novo o critério da
seção anterior: só interessa o que cai com \(1/r\). Derivar \(1/r\) em relação
a \(r\) produz \(1/r^2\), que não interessa; derivar o argumento retardado
\(t_r = t-r/c\) produz um fator \(-1/c\) e mantém o \(1/r\), que interessa. A
regra prática é curta: <em>para radiação, derivar no espaço equivale a
derivar no tempo e multiplicar por \(-\vers{r}/c\)</em>.</p>

<p>Com ela, a parte de radiação do campo elétrico vem direto de
\(\vet{E} = -\nabla V - \partial\vet{A}/\partial t\). O gradiente do potencial
escalar contribui apenas com a parcela longitudinal, que cancela a componente
de \(\partial\vet{A}/\partial t\) ao longo de \(\vers{r}\), e o que sobra é a
parte <em>transversal</em>:</p>

\[ \vet{E}_{\text{rad}}
   = \frac{\mu_0 q}{4\pi r}
     \left[\vers{r}\cruz\left(\vers{r}\cruz\vet{a}(t_r)\right)\right]
   = -\frac{\mu_0 q}{4\pi r}\,\vet{a}_\perp(t_r), \]

<p>onde \(\vet{a}_\perp\) é a componente da aceleração perpendicular à direção
de observação. O campo magnético acompanha, como em qualquer onda:</p>

\[ \vet{B}_{\text{rad}} = \frac{1}{c}\,\vers{r}\cruz\vet{E}_{\text{rad}}. \]

<div class="bloco alerta">
<span class="rotulo">Três coisas para guardar</span>
<p>O campo de radiação é <em>transversal</em>, é proporcional à
<em>aceleração</em>, e é <em>retardado</em>: o que se mede aqui e agora é o
que a carga fez há \(r/c\) segundos. A última é a mais fácil de esquecer e a
mais importante: a informação de que a carga foi acelerada viaja, e a energia
viaja com ela.</p>
</div>
'''

S3 = r'''
<p>Com os campos em mãos, a potência sai de uma conta de duas linhas. O vetor
de Poynting de uma onda transversal vale</p>

\[ \vet{S} = \frac{1}{\mu_0}\vet{E}\cruz\vet{B}
   = \frac{E_{\text{rad}}^2}{\mu_0c}\,\vers{r}, \]

<p>e, escrevendo \(a_\perp = a\sen\theta\), com \(\theta\) medido a partir da
direção da aceleração,</p>

\[ S = \frac{1}{\mu_0c}\left(\frac{\mu_0qa\sen\theta}{4\pi r}\right)^2
   = \frac{\mu_0q^2a^2}{16\pi^2c}\frac{\sen^2\theta}{r^2}. \]

<figure class="figura-exemplo" style="max-width:44rem">
  <img src="assets/img/cap11_padrao.svg" alt="Padrão angular da radiação de dipolo">
  <figcaption>À esquerda, a superfície \(\sen^2\theta\): duas folhas simétricas
  em torno do eixo da aceleração, com um nó exato na direção de \(\vet{a}\) e
  máximo no plano perpendicular. À direita, a razão disso: o observador só
  "vê" a componente da aceleração perpendicular à sua linha de visada, e essa
  projeção vale \(a\sen\theta\). Na potência, que vai com o quadrado do campo,
  o seno vira \(\sen^2\theta\).</figcaption>
</figure>

<p>Repare que o \(r^2\) do denominador vai cancelar exatamente o \(r^2\) do
elemento de área: a potência que atravessa a esfera não depende do raio, como
tem de ser para algo que vai embora de verdade. Integrando,</p>

\[ P = \oint S\,r^2d\Omega
   = \frac{\mu_0q^2a^2}{16\pi^2c}\int_0^{2\pi}\!\!d\phi
     \int_0^{\pi}\sen^3\theta\,d\theta
   = \frac{\mu_0q^2a^2}{16\pi^2c}\cdot 2\pi\cdot\frac{4}{3}, \]

<p>isto é,</p>

\[ \boxed{\;P = \frac{\mu_0q^2a^2}{6\pi c}\;} \]

<p>que é a <strong>fórmula de Larmor</strong>. Em termos do dipolo, com
\(\ddot{\vet{p}} = q\vet{a}\) e uma oscilação harmônica
\(p(t) = p_0\cos\omega t\), a média temporal fica</p>

\[ \left\langle P\right\rangle
   = \frac{\mu_0p_0^2\omega^4}{12\pi c}. \]

<p>A quarta potência da frequência é o detalhe mais consequente de todo o
capítulo, e a seção 6 mostra por quê.</p>

<div class="destaque">
<p><strong>Exemplo trabalhado: a resistência de radiação de uma antena
curta.</strong> Uma antena de \(d = 30\ \mathrm{cm}\) opera em
\(100\ \mathrm{MHz}\), com corrente de amplitude \(I_0 = 1{,}0\ \mathrm{A}\).
Quanta potência ela irradia, e que resistência isso representa?</p>

<p><strong>O comprimento de onda</strong> é \(\lambda = c/f = 3{,}0\
\mathrm{m}\), de modo que \(d/\lambda = 0{,}10\): a antena é curta o bastante
para a aproximação de dipolo valer razoavelmente.</p>

<p><strong>O momento de dipolo.</strong> Se a corrente tem amplitude \(I_0\), a
carga que oscila nas pontas tem amplitude \(q_0 = I_0/\omega\), e</p>

\[ p_0 = q_0d = \frac{I_0d}{\omega}
   = \frac{1{,}0\times0{,}30}{2\pi\times10^{8}}
   = 4{,}77\times10^{-10}\ \mathrm{C\,m}. \]

<p><strong>A potência.</strong></p>

\[ \left\langle P\right\rangle = \frac{\mu_0p_0^2\omega^4}{12\pi c}
   = 3{,}95\ \mathrm{W}. \]

<p><strong>A resistência de radiação</strong> é definida por
\(\left\langle P\right\rangle = \frac12I_0^2R\), de onde</p>

\[ R = \frac{2\left\langle P\right\rangle}{I_0^2} = 7{,}90\ \Omega
   = 80\pi^2\left(\frac{d}{\lambda}\right)^2. \]

<p><strong>Honestidade sobre o modelo.</strong> Essa conta supõe a mesma
corrente em todo o comprimento da antena, o que é impossível: nas pontas a
corrente tem de ser nula, porque não há para onde a carga ir. Numa antena real
curta, o perfil é aproximadamente triangular, a corrente média cai pela
metade, e a potência, que vai com o quadrado, cai a um quarto:
\(R \approx 1{,}98\ \Omega\) e \(\left\langle P\right\rangle \approx
0{,}99\ \mathrm{W}\).</p>

<p>Ou seja: uma antena curta é um radiador ruim, e piora com o quadrado do
encurtamento. Casá-la a uma linha de 50 Ω exige uma rede de adaptação, e
qualquer perda ôhmica no condutor compete diretamente com esses poucos ohms de
resistência de radiação. É por isso que a antena de meia onda, com os seus
73 Ω, é o padrão: ela irradia bem e casa quase sozinha.</p>
</div>
'''

S4 = r'''
<p>O termo que descartamos na expansão não é zero, apenas menor. Vale a pena
saber o quanto, e o que aparece lá.</p>

<p>Mantendo a ordem seguinte no atraso interno da fonte,</p>

\[ \vet{J}\!\left(\vet{r}',t_r\right)
   \approx \vet{J}\!\left(\vet{r}',t-\tfrac{r}{c}\right)
   + \frac{\vers{r}\cdot\vet{r}'}{c}\,\pder{\vet{J}}{t} + \cdots, \]

<p>e a integral do segundo termo se separa em duas partes, uma antissimétrica e
outra simétrica na troca dos índices. A antissimétrica dá o <strong>dipolo
magnético</strong>, \(\vet{m}\); a simétrica dá o <strong>quadrupolo
elétrico</strong>. Para uma espira de corrente oscilante,</p>

\[ P_{\text{mag}} = \frac{\mu_0 m_0^2\omega^4}{12\pi c^3}, \]

<p>que tem a mesma cara da fórmula do dipolo elétrico, com \(p_0\) trocado por
\(m_0/c\). Essa é a chave da comparação.</p>

<div class="bloco fisica">
<span class="rotulo">Por que a radiação magnética é tão mais fraca</span>
<p>Para uma espira de raio \(R\) com corrente \(I_0\), \(m_0 = I_0\pi R^2\);
para um dipolo elétrico do mesmo tamanho, \(p_0 = q_0R \sim I_0R/\omega\). A
razão das potências é</p>
\[ \frac{P_{\text{mag}}}{P_{\text{elé}}}
   \sim \left(\frac{m_0}{cp_0}\right)^2
   \sim \left(\frac{\omega R}{c}\right)^2
   \sim \left(\frac{R}{\lambda}\right)^2. \]
<p>Como a aproximação de dipolo já exigiu \(R \ll \lambda\), a radiação de
dipolo magnético é automaticamente pequena. A hierarquia continua: cada ordem
seguinte perde mais um fator \(R/\lambda\). Por isso quase toda antena prática
é um radiador de dipolo elétrico, e por isso as transições atômicas de dipolo
elétrico são milhões de vezes mais rápidas que as de dipolo magnético, que os
espectroscopistas chamam de proibidas.</p>
</div>

<p>Há uma exceção importante. Quando o dipolo elétrico é nulo por simetria, a
ordem seguinte deixa de ser uma correção e passa a ser o efeito inteiro. É o
que acontece numa espira fechada com corrente alternada, numa transição atômica
entre estados de mesma paridade, e na radiação gravitacional, em que o
equivalente do dipolo é nulo por conservação do momento e a primeira ordem
observável é o quadrupolo.</p>
'''

S5 = r'''
<p>A fórmula de Larmor supõe \(v \ll c\), e as máquinas mais interessantes do
mundo violam essa hipótese por muitas ordens de grandeza. A generalização
relativística é a <strong>fórmula de Liénard</strong>:</p>

\[ P = \frac{\mu_0q^2\gamma^6}{6\pi c}
   \left[a^2 - \left|\frac{\vet{v}\cruz\vet{a}}{c}\right|^2\right],
   \qquad \gamma = \frac{1}{\sqrt{1-v^2/c^2}}. \]

<p>Dois casos extremos organizam tudo o que vem depois.</p>

<p><strong>Aceleração paralela à velocidade</strong>, como num acelerador
linear: o colchete vira \(a^2\) e sobra \(\gamma^6\).</p>

<p><strong>Aceleração perpendicular à velocidade</strong>, como num anel: o
colchete vira \(a^2(1-v^2/c^2) = a^2/\gamma^2\) e sobra \(\gamma^4\).</p>

<p>Parece que o caso linear é pior, mas é o contrário, e a razão é que as duas
situações não são comparáveis diretamente. Num acelerador linear a aceleração
que importa é a que um campo elétrico consegue dar, e ela é limitada; num anel,
a aceleração centrípeta \(v^2/\rho\) é imposta pela geometria e não tem como
ser reduzida sem aumentar o anel. O resultado prático é que a radiação é o
limite dos anéis, não dos lineares.</p>

<div class="destaque">
<p><strong>Exemplo trabalhado: o LEP, o LHC e o mesmo túnel.</strong> Entre 1989
e 2000, o anel de 27 km do CERN acelerou elétrons e pósitrons. Desde 2008, o
mesmo túnel abriga prótons. A diferença entre as duas máquinas é, em boa
medida, esta seção.</p>

<p><strong>A perda por volta.</strong> Com \(\vet{a}\perp\vet{v}\),
\(a = v^2/\rho\) e \(\gamma = E/mc^2\), a energia perdida numa volta é</p>

\[ \Delta E = \frac{q^2\gamma^4\beta^3}{3\varepsilon_0\rho}, \]

<p>que para elétrons se escreve, em unidades práticas,</p>

\[ \Delta E\,[\mathrm{keV}]
   = 88{,}46\,\frac{E^4\,[\mathrm{GeV}]}{\rho\,[\mathrm{m}]}. \]

<p><strong>Os números</strong>, com \(\rho = 3096\ \mathrm{m}\) no LEP:</p>

<div class="tabela-rolavel">
<table>
<thead><tr><th>máquina</th><th>partícula</th><th>energia</th>
<th>perda por volta</th></tr></thead>
<tbody>
<tr><td>LEP-1</td><td>elétron</td><td>45,6 GeV</td><td>124 MeV</td></tr>
<tr><td>LEP-2</td><td>elétron</td><td>104,5 GeV</td><td>3,4 GeV</td></tr>
<tr><td>LHC</td><td>próton</td><td>7000 GeV</td><td>6,7 keV</td></tr>
</tbody>
</table>
</div>

<p><strong>A leitura.</strong> No LEP-2, cada elétron precisava receber, a cada
volta, 3,4 GeV só para não desacelerar. Era preciso encher o anel de cavidades
supercondutoras de radiofrequência apenas para repor a radiação, e foi esse
custo, crescendo com \(E^4\), que encerrou a máquina: dobrar a energia exigiria
dezesseis vezes mais potência.</p>

<p><strong>E o LHC?</strong> O próton é 1836 vezes mais pesado, e a perda vai
com \(1/m^4\), isto é, \(1{,}1\times10^{13}\) vezes menor na mesma energia.
Mesmo a 7 TeV, uma energia 67 vezes maior que a do LEP-2, a perda por volta é
de 6,7 keV, um milhão de vezes menor. Ela ainda importa, porque o feixe tem
\(3\times10^{14}\) prótons e os ímãs estão a 1,9 K: alguns quilowatts
depositados no hélio superfluido são um problema de criogenia, não de
energia.</p>

<p><strong>E a volta por cima.</strong> O que matou o LEP sustenta uma
indústria inteira. Um anel pequeno de elétrons, projetado justamente <em>para
irradiar</em>, é uma fonte de luz síncrotron, e a radiação que o projetista de
colisores combate é exatamente o produto que o usuário quer: raios X
intensos, colimados e sintonizáveis. O Sirius, em Campinas, é uma dessas
máquinas.</p>
</div>
'''

S6 = r'''
<p>A radiação de dipolo tem uma aplicação que não é sobre antenas nem sobre
aceleradores: espalhamento. A ideia é simples de enunciar. Uma onda chega a uma
carga, a carga é acelerada pelo campo da onda, e a carga acelerada irradia. A
luz que sai em outras direções foi "espalhada", e nada além de Larmor é
necessário para calculá-la.</p>

<h3>Carga livre: Thomson</h3>

<p>Para um elétron livre, a aceleração é \(a = eE_0\cos\omega t/m\), e a
potência média sai de Larmor. Dividindo pela intensidade incidente,
\(I = \frac12c\varepsilon_0E_0^2\), obtém-se uma área, que é a seção de choque:</p>

\[ \sigma_T = \frac{8\pi}{3}r_e^2,
   \qquad r_e = \frac{e^2}{4\pi\varepsilon_0mc^2}
   = 2{,}818\times10^{-15}\ \mathrm{m}, \]

<p>numericamente \(6{,}65\times10^{-29}\ \mathrm{m^2}\). O campo
\(E_0\) se cancela, e a frequência também: <strong>um elétron livre espalha
todas as cores igualmente</strong>. É por isso que o interior do Sol, onde os
elétrons estão livres, é opaco de modo acromático, e é por isso que \(\sigma_T\)
aparece em toda conta de astrofísica, do limite de Eddington ao desacoplamento
da radiação cósmica de fundo.</p>

<h3>Carga ligada: Rayleigh</h3>

<p>Num átomo ou numa molécula, o elétron não está livre: está preso por uma
força restauradora, com frequência natural \(\omega_0\) no ultravioleta. Para
luz visível, \(\omega \ll \omega_0\), e o oscilador forçado responde com
amplitude praticamente estática,</p>

\[ x_0 \approx \frac{eE_0}{m\omega_0^2}, \]

<p>de modo que a aceleração vale \(\omega^2x_0\) e a potência irradiada, que vai
com o quadrado da aceleração, cresce com \(\omega^4\):</p>

\[ \sigma \approx \sigma_T\left(\frac{\omega}{\omega_0}\right)^4
   \propto \frac{1}{\lambda^4}. \]

<p>Essa é a lei de Rayleigh, e ela explica a cor do céu de uma vez só. A luz
azul, de comprimento de onda menor, é espalhada muito mais que a vermelha; o
que chega aos olhos vindo de uma direção qualquer do céu é essa luz espalhada,
e é azul.</p>

<div class="destaque">
<p><strong>Exemplo trabalhado: o céu, o poente e um número.</strong> O script
<code>espalhamento.py</code> calcula a seção de choque de uma molécula de ar a
partir do índice de refração do ar, sem nenhum parâmetro ajustado, e multiplica
pela densidade de colunas da atmosfera (\(2{,}15\times10^{29}\) moléculas por
metro quadrado). O resultado é a profundidade óptica \(\tau\), e a transmissão
é \(e^{-\tau}\).</p>

<div class="tabela-rolavel">
<table>
<thead><tr><th>cor</th><th>σ por molécula</th><th>τ no zênite</th>
<th>transmissão ao meio-dia</th><th>no poente (38 atmosferas)</th></tr></thead>
<tbody>
<tr><td>violeta, 400 nm</td><td>1,59×10⁻³⁰ m²</td><td>0,342</td>
    <td>71 %</td><td>0,0002 %</td></tr>
<tr><td>azul, 450 nm</td><td>9,78×10⁻³¹ m²</td><td>0,210</td>
    <td>81 %</td><td>0,03 %</td></tr>
<tr><td>verde, 550 nm</td><td>4,30×10⁻³¹ m²</td><td>0,093</td>
    <td>91 %</td><td>3,0 %</td></tr>
<tr><td>vermelho, 650 nm</td><td>2,18×10⁻³¹ m²</td><td>0,047</td>
    <td>95 %</td><td>17 %</td></tr>
</tbody>
</table>
</div>

<p><strong>Confira contra a medida.</strong> A profundidade óptica de Rayleigh
medida ao nível do mar vale cerca de 0,23 no azul e 0,05 no vermelho. A conta,
feita apenas com o índice de refração do ar, acerta as duas.</p>

<p><strong>O poente.</strong> Com o Sol no horizonte, a luz atravessa cerca de
38 vezes mais atmosfera. O vermelho ainda chega com 17 % da intensidade; o azul
chega com 0,03 %, isto é, 500 vezes menos. O Sol poente não fica laranja porque
ganha vermelho, e sim porque perde todo o resto.</p>

<p><strong>E por que não violeta?</strong> Se o espalhamento cresce com
\(1/\lambda^4\), o céu deveria ser violeta, que é espalhado ainda mais que o
azul. Duas razões: o espectro solar já tem menos violeta que azul, e os cones
do olho humano são bem menos sensíveis nessa faixa. O céu é azul por causa de
Rayleigh, mas é <em>desse</em> azul por causa da fisiologia.</p>
</div>

<div class="bloco ex">
<span class="rotulo">Um teste de dois segundos</span>
<p>A luz espalhada a 90° do Sol é fortemente polarizada, porque o dipolo
induzido nas moléculas não irradia ao longo da sua própria direção. Olhe para
um trecho de céu a noventa graus do Sol através de um óculos polarizado e gire
a cabeça: o azul escurece e clareia. O padrão \(\sen^2\theta\) da figura da
seção 3 é visível a olho nu, de dentro de um carro.</p>
</div>
'''

S7 = r'''
<p>Falta uma pergunta incômoda, e ela fecha o curso. Se a carga acelerada perde
energia irradiando, alguma força tem de estar fazendo esse trabalho negativo
sobre ela. Que força é essa?</p>

<p>A resposta é que a carga sente o seu <em>próprio</em> campo. Cada pedaço da
distribuição de carga empurra os outros, e numa configuração acelerada esses
empurrões não se cancelam, porque chegam com atrasos diferentes. Impondo que o
trabalho dessa força, ao longo de um ciclo, seja igual à energia irradiada,
chega-se à <strong>fórmula de Abraham-Lorentz</strong>:</p>

\[ \vet{F}_{\text{rad}} = \frac{\mu_0q^2}{6\pi c}\,\dot{\vet{a}}, \]

<p>proporcional à <em>derivada</em> da aceleração. É um resultado
desconfortável por pelo menos três motivos, e vale enfrentá-los em vez de
escondê-los.</p>

<p><strong>Primeiro: soluções fugitivas.</strong> Para uma partícula livre, a
equação \(m\dot{v} = \tau m\ddot{v}\), com
\(\tau = \mu_0q^2/6\pi mc\), admite \(a(t) = a_0e^{t/\tau}\). Uma partícula
sozinha no universo começaria a acelerar sem causa, exponencialmente, para
sempre.</p>

<p><strong>Segundo: pré-aceleração.</strong> Descartando as soluções fugitivas
com a condição de contorno adequada, aparece outra patologia: a partícula
começa a acelerar <em>antes</em> de a força ser aplicada, com uma antecedência
da ordem de \(\tau\). Para o elétron, \(\tau = 6{,}3\times10^{-24}\) s, o tempo
que a luz leva para atravessar o raio clássico do elétron. É pouco, mas é
causalidade violada.</p>

<p><strong>Terceiro: o caso de aceleração constante.</strong> Com \(\vet{a}\)
constante, \(\dot{\vet{a}} = 0\) e a força de reação é nula, embora a carga
esteja irradiando. De onde sai a energia? Essa é a situação, ainda discutida,
de uma carga em repouso num campo gravitacional uniforme.</p>

<div class="bloco alerta">
<span class="rotulo">Onde isso para</span>
<p>Os três problemas apontam para o mesmo lugar: o conceito de carga pontual.
A energia do campo de uma carga pontual diverge, a massa eletromagnética
diverge, e a reação de radiação herda a doença. A eletrodinâmica clássica é
uma teoria excelente que não sabe o que é um elétron, e as suas patologias
aparecem exatamente na escala \(r_e = 2{,}8\times10^{-15}\ \mathrm{m}\), em
que ela já deveria ter sido substituída pela eletrodinâmica quântica. Lá, a
divergência é tratada por renormalização, e o resultado, o momento magnético
do elétron, é a previsão mais bem verificada da física.</p>
</div>

<p>Vale terminar olhando para trás. O curso começou com uma carga parada e a
lei de Coulomb, passou por correntes, matéria polarizada e magnetizada,
indução, as quatro equações reunidas, as leis de conservação e as ondas, e
termina com uma carga acelerada que irradia e com uma teoria que não consegue
descrever consistentemente a sua própria fonte. Não é um fracasso: é a maneira
usual como uma teoria física indica, com precisão, onde ela termina e onde
começa a próxima.</p>
'''

S8 = r'''
<div class="cartoes">
  <article class="cartao">
    <h3><a href="codigo/radiacao_dipolo.py">radiacao_dipolo.py</a></h3>
    <p>Monta os potenciais retardados exatos de uma antena curta, obtém
    \(\vet{E}\) e \(\vet{B}\) por diferenças finitas e integra o fluxo de
    energia sobre esferas de vários raios.</p>
    <p><strong>Confira assim:</strong> a potência média tem de bater com
    Larmor e ser a mesma em todo raio; o padrão angular tem de ser
    \(\sen^2\theta\); e o expoente com que o campo cai tem de passar de
    \(-3\) a \(-1\) ao cruzar um comprimento de onda.</p>
  </article>
  <article class="cartao">
    <h3><a href="codigo/sincrotron.py">sincrotron.py</a></h3>
    <p>Aplica a fórmula de Liénard ao movimento circular e calcula a energia
    perdida por volta no LEP, no LHC e no Sirius.</p>
    <p><strong>Confira assim:</strong> a conta direta tem de reproduzir a regra
    prática \(88{,}46\,E^4/\rho\); o expoente com a energia tem de dar 4,00; e
    a razão próton/elétron tem de ser \((m_e/m_p)^4\).</p>
  </article>
  <article class="cartao">
    <h3><a href="codigo/espalhamento.py">espalhamento.py</a></h3>
    <p>Obtém a seção de choque de Thomson a partir de Larmor e a de Rayleigh a
    partir do índice de refração do ar, e calcula a transmissão da atmosfera
    cor por cor.</p>
    <p><strong>Confira assim:</strong> \(\sigma_T\) tem de dar
    \(6{,}65\times10^{-29}\ \mathrm{m^2}\) para qualquer intensidade e
    frequência; e a profundidade óptica calculada tem de bater com a medida,
    0,21 no azul contra 0,05 no vermelho.</p>
  </article>
  <article class="cartao">
    <h3><a href="codigo/lienard_wiechert.py">lienard_wiechert.py</a></h3>
    <p>Do capítulo 10, e vale revisitar aqui: ele separa as parcelas de
    velocidade e de aceleração do campo de uma carga em movimento qualquer.</p>
    <p><strong>Confira assim:</strong> a potência média que atravessa qualquer
    esfera é a de Larmor, e some quando a aceleração é desligada.</p>
  </article>
</div>
'''

SECOES = [
    ('O que escapa para o infinito', S1),
    ('O método de Thomson', S2),
    ('Larmor, e o padrão sen²θ', S3),
    ('A hierarquia: dipolo magnético e o resto', S4),
    ('Cargas rápidas: Liénard e o síncrotron', S5),
    ('Espalhamento: Thomson, Rayleigh e o céu', S6),
    ('A reação de radiação, e onde a teoria clássica termina', S7),
    ('No Spyder', S8),
]

SECOES.append(('Exercícios propostos', exercicios.bloco(LISTA)))


def main():
    titulos = [t for t, _ in SECOES]
    escreve('cap11.html', secoes_html(SECOES), secoes=titulos)


if __name__ == '__main__':
    main()
