# -*- coding: utf-8 -*-
"""Capítulo 9: ondas eletromagnéticas.

O texto é escrito do zero. O Griffiths entra como referência de ordem e de
numeração de capítulo, nunca como fonte de frases, enunciados ou figuras:
os exemplos aqui são de nossa autoria, com contextos e números próprios.
A seção de guias de onda não vem de slide nenhum: foi escrita para cá.
"""
from molde import escreve, secoes_html
import exercicios
from lista_cap09 import LISTA

S1 = r'''
<p>No vácuo, longe de qualquer carga e corrente, as equações de Maxwell ficam
com uma simetria notável:</p>

\[ \divg{\vet{E}} = 0,\qquad \divg{\vet{B}} = 0, \]

\[ \rot{\vet{E}} = -\pder{\vet{B}}{t},\qquad
   \rot{\vet{B}} = \mu_0\varepsilon_0\pder{\vet{E}}{t}. \]

<p>Cada rotacional alimenta a derivada temporal do outro campo, e é dessa
realimentação que sai a onda. Para ver, tome o rotacional da terceira:</p>

\[ \rot{\left(\rot{\vet{E}}\right)}
   = \nabla\left(\divg{\vet{E}}\right) - \nabla^2\vet{E}
   = -\nabla^2\vet{E}, \]

<p>usando a identidade do capítulo 1 e o fato de o divergente ser nulo. Pelo
outro lado,</p>

\[ \rot{\left(-\pder{\vet{B}}{t}\right)}
   = -\pder{}{t}\left(\rot{\vet{B}}\right)
   = -\mu_0\varepsilon_0\frac{\partial^2\vet{E}}{\partial t^2}. \]

<p>Igualando,</p>

\[ \boxed{\;\nabla^2\vet{E}
   = \mu_0\varepsilon_0\frac{\partial^2\vet{E}}{\partial t^2},\;} \]

<p>e o mesmo para \(\vet{B}\). É a equação de onda, com velocidade</p>

\[ v = \frac{1}{\sqrt{\mu_0\varepsilon_0}}
     = \frac{1}{\sqrt{4\pi\times10^{-7}\times8{,}854\times10^{-12}}}
     = 3{,}00\times10^{8}\ \mathrm{m/s}. \]

<div class="bloco fisica">
<span class="rotulo">O que aconteceu aqui</span>
<p>Duas constantes medidas em bancada, uma com balança de torção e cargas
paradas, outra com fios e correntes estacionárias, combinaram-se para dar a
velocidade da luz. Nenhuma das duas medidas tem nada a ver com óptica.</p>
<p>É difícil exagerar o tamanho disso. Até 1865 a luz era assunto de uma
disciplina, e eletricidade e magnetismo de outra; depois do artigo de Maxwell,
são a mesma coisa. Foi a primeira das grandes unificações da física, e o modelo
de todas as que vieram depois.</p>
</div>

<p>Vale notar que o termo responsável é a corrente de deslocamento do capítulo
7. Sem ele, \(\rot{\vet{B}} = 0\) no vácuo, a realimentação não fecha e não há
onda nenhuma. O termo que Maxwell acrescentou por consistência matemática é o
que faz a luz existir.</p>
'''

S2 = r'''
<p>A solução mais simples da equação de onda é a onda plana monocromática.
Escolhendo a propagação em \(z\) e usando notação complexa,</p>

\[ \tilde{\vet{E}}(z,t) = \tilde{\vet{E}}_0\,e^{i(kz-\omega t)},
   \qquad
   \tilde{\vet{B}}(z,t) = \tilde{\vet{B}}_0\,e^{i(kz-\omega t)}, \]

<p>com a parte real sendo o campo físico. Substituindo na equação de onda sai a
relação de dispersão \(\omega = ck\), e com ela o conjunto de nomes que vale
fixar de uma vez:</p>

\[ k = \frac{2\pi}{\lambda},\qquad
   \omega = 2\pi f,\qquad
   T = \frac{1}{f},\qquad
   c = \lambda f. \]

<h3>O que as equações de Maxwell impõem</h3>

<p>A equação de onda sozinha não determina tudo. Voltando às equações
originais com a forma de onda plana, \(\divg{\vet{E}} = 0\) dá
\(ik\,\tilde{E}_{0z} = 0\), ou seja</p>

<p><strong>1. A onda é transversal.</strong> Nem \(\vet{E}\) nem \(\vet{B}\)
têm componente na direção de propagação.</p>

<p>E a lei de Faraday, \(\rot{\vet{E}} = -\partial\vet{B}/\partial t\), aplicada
à forma plana, dá \(\tilde{\vet{B}}_0 = \frac{k}{\omega}\left(\vers{z}\cruz
\tilde{\vet{E}}_0\right)\), isto é</p>

<p><strong>2. \(\vet{B}\) é perpendicular a \(\vet{E}\)</strong>, e os dois são
perpendiculares à direção de propagação, formando um triedro direto com ela.</p>

<p><strong>3. Os dois estão em fase</strong>, e as amplitudes reais obedecem</p>

\[ \boxed{\;B_0 = \frac{E_0}{c}.\;} \]

<p>Esse último ponto costuma causar a impressão de que o campo magnético de uma
onda é desprezível, porque \(B_0\) é \(3\times10^{8}\) vezes menor em unidades
do SI. É uma ilusão de unidades: as duas contribuem <em>igualmente</em> para a
energia, como a próxima seção mostra, porque a densidade magnética traz
\(1/\mu_0\) e a elétrica traz \(\varepsilon_0\).</p>

<div class="bloco def">
<span class="rotulo">Por que a notação complexa compensa</span>
<p>Trabalhar com \(e^{i(kz-\omega t)}\) em vez de cossenos não é preguiça:
derivar vira multiplicar por \(ik\) ou por \(-i\omega\), e as equações
diferenciais viram equações algébricas. O preço é lembrar de tomar a parte real
no fim, e de que produtos de campos (energia, Poynting) <em>não</em> podem ser
calculados com os complexos diretamente: aí é preciso usar
\(\frac12\mathrm{Re}(\tilde{\vet{A}}\cdot\tilde{\vet{B}}^*)\) ou voltar aos
reais.</p>
</div>
'''

S3 = r'''
<p>A densidade de energia do campo, somando as duas parcelas dos capítulos 2 e
7,</p>

\[ u = \frac{\varepsilon_0}{2}E^2 + \frac{1}{2\mu_0}B^2, \]

<p>e para uma onda plana, com \(B = E/c\) e \(c^2 = 1/\mu_0\varepsilon_0\), as
duas parcelas são <em>iguais</em>:</p>

\[ \frac{B^2}{2\mu_0} = \frac{E^2/c^2}{2\mu_0}
   = \frac{\varepsilon_0 E^2}{2}
   \;\Longrightarrow\;
   u = \varepsilon_0 E^2. \]

<p>A energia viaja, e quem contabiliza o transporte é o <strong>vetor de
Poynting</strong>,</p>

\[ \boxed{\;\vet{S} = \frac{1}{\mu_0}\left(\vet{E}\cruz\vet{B}\right),\;} \]

<p>que é energia por unidade de área e de tempo, em watts por metro quadrado.
Para a onda plana, \(\vet{S} = c\,u\,\vers{z}\): a energia caminha com a onda, à
velocidade da luz, como era de esperar.</p>

<p>Tomando a média temporal de \(\cos^2\), que vale \(1/2\), a
<strong>intensidade</strong> é</p>

\[ I = \langle S\rangle = \frac{1}{2}c\varepsilon_0E_0^2. \]

<h3>Momento e pressão</h3>

<p>A onda carrega também momento, na razão</p>

\[ \vet{g} = \frac{\vet{S}}{c^2}
   \;\Longrightarrow\;
   P_{\text{rad}} = \frac{I}{c}\ \text{(absorvida)},\qquad
   \frac{2I}{c}\ \text{(refletida)}. \]

<div class="destaque">
<p><strong>Exemplo trabalhado: o Sol empurra?</strong> A constante solar, acima
da atmosfera, vale \(I = 1361\ \mathrm{W/m^2}\). Calcule o campo elétrico da
luz solar, a pressão de radiação sobre uma superfície negra e sobre um espelho,
e a força sobre uma vela solar de \(100\ \mathrm{m^2}\).</p>

<p><strong>O campo.</strong> De \(I = \frac12 c\varepsilon_0E_0^2\),</p>

\[ E_0 = \sqrt{\frac{2I}{c\varepsilon_0}}
   = \sqrt{\frac{2\times1361}{3{,}00\times10^{8}\times8{,}85\times10^{-12}}}
   = 1{,}0\times10^{3}\ \mathrm{V/m}, \]

<p>e \(B_0 = E_0/c = 3{,}4\ \mu\mathrm{T}\), que é um quinze avos do campo
magnético da Terra. A luz do Sol tem campo elétrico de mil volts por metro, e
ninguém sente nada, porque ele oscila \(10^{15}\) vezes por segundo.</p>

<p><strong>A pressão.</strong></p>

\[ P = \frac{I}{c} = \frac{1361}{3{,}00\times10^{8}}
   = 4{,}5\ \mu\mathrm{Pa}, \]

<p>e o dobro num espelho, \(9{,}1\ \mu\mathrm{Pa}\). Comparando: a pressão
atmosférica é \(10^{5}\) Pa, vinte bilhões de vezes maior.</p>

<p><strong>A vela.</strong> Com \(100\ \mathrm{m^2}\) refletindo,
\(F = 9{,}1\times10^{-6}\times100 = 9{,}1\times10^{-4}\ \mathrm{N}\), menos de
um milinewton. Parece nada, mas é constante e não gasta combustível: aplicada a
uma sonda de 10 kg, dá uma aceleração de \(9\times10^{-5}\ \mathrm{m/s^2}\), que
em um ano de voo acumula \(2{,}9\ \mathrm{km/s}\) de variação de velocidade.
É assim que a IKAROS e a LightSail navegaram de verdade.</p>
</div>
'''

S4 = r'''
<p>Dentro de um meio linear, sem carga nem corrente livres, as equações têm a
mesma forma com \(\varepsilon\) e \(\mu\) no lugar de \(\varepsilon_0\) e
\(\mu_0\). A conta se repete palavra por palavra e dá</p>

\[ v = \frac{1}{\sqrt{\varepsilon\mu}} = \frac{c}{n},
   \qquad n \equiv \sqrt{\frac{\varepsilon\mu}{\varepsilon_0\mu_0}}
   \approx \sqrt{\varepsilon_r}, \]

<p>com a última aproximação valendo porque quase todo material transparente tem
\(\mu \approx \mu_0\).</p>

<div class="bloco alerta">
<span class="rotulo">O paradoxo da água</span>
<p>A água tem \(\varepsilon_r = 80\), o que daria \(n = 8{,}9\). O índice de
refração medido da água é 1,33.</p>
<p>Não há erro: as duas medidas são feitas em frequências diferentes. O valor 80
é estático, e vem do giro das moléculas polares; na frequência da luz visível,
\(10^{15}\ \mathrm{Hz}\), a molécula não consegue girar a tempo, aquele mecanismo
some, e sobra apenas a deformação eletrônica. É o primeiro aviso de que
\(\varepsilon\) depende da frequência, e é esse o assunto da dispersão.</p>
</div>

<h3>Incidência normal</h3>

<p>Uma onda vinda do meio 1 encontra o meio 2 em \(z=0\). As condições de
contorno do capítulo 7, com as componentes tangenciais de \(\vet{E}\) e
\(\vet{H}\) contínuas, levam a um sistema de duas equações para as amplitudes
refletida e transmitida. O resultado, para \(\mu_1 = \mu_2\), é</p>

\[ \boxed{\;\tilde{E}_{0R} = \frac{n_1-n_2}{n_1+n_2}\tilde{E}_{0I},
   \qquad
   \tilde{E}_{0T} = \frac{2n_1}{n_1+n_2}\tilde{E}_{0I}.\;} \]

<p>Em termos de energia, com \(R = |E_{0R}/E_{0I}|^2\) e
\(T = \frac{n_2}{n_1}|E_{0T}/E_{0I}|^2\),</p>

\[ R = \left(\frac{n_1-n_2}{n_1+n_2}\right)^2,\qquad R + T = 1. \]

<div class="destaque">
<p><strong>Exemplo trabalhado: por que a vitrine reflete.</strong> Luz vai do ar
(\(n_1=1\)) para o vidro (\(n_2=1{,}5\)), incidindo perpendicularmente. Quanto
reflete?</p>

\[ R = \left(\frac{1-1{,}5}{1+1{,}5}\right)^2
   = \left(\frac{-0{,}5}{2{,}5}\right)^2 = 0{,}04. \]

<p>Quatro por cento, e \(T = 96\%\). O sinal negativo de \(\tilde{E}_{0R}\) diz
que a onda refletida sai invertida de fase, o que acontece sempre que a luz vai
de um meio menos denso para um mais denso.</p>

<p><strong>E por que isso importa.</strong> Uma lente tem duas superfícies, de
modo que perde 8 %; uma objetiva com seis elementos tem doze superfícies e
perderia 38 % da luz, além de produzir reflexos fantasmas. É por isso que toda
óptica séria é tratada com camadas antirreflexo, que usam interferência para
cancelar justamente esses 4 %.</p>

<p><strong>O caso extremo.</strong> Para um metal, \(n\) é complexo e grande, e
\(R\) tende a 1: é por isso que metal polido é espelho. A parte imaginária
descreve a absorção, e aparece na seção dos condutores.</p>
</div>
'''

S5 = r'''
<p>Com a onda chegando em ângulo, a álgebra cresce mas a estrutura é a mesma.
Impor que as três ondas (incidente, refletida, transmitida) casem na interface
<em>para todo ponto e todo instante</em> obriga que os fatores de fase
coincidam ali, e isso sozinho dá duas leis, antes de qualquer conta de
amplitude:</p>

\[ \theta_R = \theta_I \qquad\text{(reflexão especular)}, \]

\[ \boxed{\;n_1\sen\theta_I = n_2\sen\theta_T\;}
   \qquad\text{(lei de Snell)}. \]

<p>Vale a pena reparar: a lei de Snell não veio da dinâmica, veio de
<em>cinemática de fases</em>. Qualquer onda, de qualquer natureza, obedece a ela
na fronteira entre dois meios com velocidades diferentes.</p>

<h3>As equações de Fresnel</h3>

<p>As amplitudes exigem as condições de contorno completas, e o resultado
depende da polarização. Para a polarização paralela ao plano de incidência,</p>

\[ \frac{\tilde{E}_{0R}}{\tilde{E}_{0I}} = \frac{\alpha-\beta}{\alpha+\beta},
   \qquad
   \frac{\tilde{E}_{0T}}{\tilde{E}_{0I}} = \frac{2}{\alpha+\beta}, \]

<p>com \(\alpha = \cos\theta_T/\cos\theta_I\) e \(\beta = n_2/n_1\) (tomando
\(\mu_1=\mu_2\)). Para a polarização perpendicular, a forma é a mesma com
\(\alpha\) trocado de lugar.</p>

<h3>Brewster, e por que o óculos polarizado funciona</h3>

<p>Na polarização paralela existe um ângulo em que \(\alpha = \beta\) e a
reflexão <strong>se anula</strong>. É o ângulo de Brewster:</p>

\[ \tg\theta_B = \frac{n_2}{n_1}. \]

<p>Para o vidro, \(\theta_B = \arctan 1{,}5 = 56{,}3^\circ\); para a água,
\(53{,}1^\circ\). Nesse ângulo, a luz refletida é <em>inteiramente</em>
polarizada perpendicular ao plano de incidência, porque a outra componente
simplesmente não reflete.</p>

<p>O reflexo de uma estrada molhada ou de um lago vem de uma superfície
horizontal, de modo que a luz refletida é polarizada horizontalmente. Um óculos
com o eixo de transmissão vertical corta exatamente essa componente, e é por
isso que ele mata o brilho sem escurecer o resto da cena.</p>

<h3>Reflexão interna total</h3>

<p>Indo do meio mais denso para o menos denso (\(n_1 \gt n_2\)), a lei de Snell
pede \(\sen\theta_T = (n_1/n_2)\sen\theta_I\), que passa de 1 quando</p>

\[ \theta_I \gt \theta_c = \arcsen\frac{n_2}{n_1}. \]

<p>Para o vidro, \(\theta_c = 41{,}8^\circ\). Acima disso não há onda
transmitida de verdade, e toda a energia volta. O campo não é rigorosamente
nulo do outro lado: existe uma onda evanescente que decai exponencialmente em
poucas dezenas de nanômetros, e é ela que permite acoplar luz entre duas fibras
encostadas sem nenhum contato elétrico.</p>

<p>A reflexão interna total é o que faz a fibra óptica funcionar, e repare que
ela é <em>total</em> mesmo: não há 4 %, não há perda por reflexão. A atenuação
de uma fibra moderna, de 0,2 dB por quilômetro, vem de espalhamento no vidro, e
não da reflexão nas paredes.</p>
'''

S6 = r'''
<p>Até aqui \(n\) foi um número. Medir com cuidado mostra que ele depende da
frequência, e é por isso que o prisma separa cores. O modelo que explica isso em
primeira aproximação é mecânico, e tem mais de cem anos.</p>

<p>Trate cada elétron ligado como preso ao átomo por uma mola de frequência
natural \(\omega_0\), com um atrito \(\gamma\) que representa a perda de
energia. A onda o sacode:</p>

\[ m\dder{x}{t} + m\gamma\der{x}{t} + m\omega_0^2x = qE_0e^{-i\omega t}. \]

<p>É o oscilador forçado de toda a mecânica, cuja solução estacionária é</p>

\[ \tilde{x} = \frac{q/m}{\omega_0^2-\omega^2-i\gamma\omega}\,
   \tilde{E}. \]

<p>O momento de dipolo é \(q\tilde{x}\), a polarização é \(N\) vezes isso, e a
susceptibilidade sai direto:</p>

\[ \tilde{\varepsilon}_r = 1 + \frac{Nq^2}{m\varepsilon_0}
   \sum_j\frac{f_j}{\omega_j^2-\omega^2-i\gamma_j\omega}, \]

<p>com a soma sobre as frequências de ressonância do material. Três leituras
imediatas:</p>

<div class="cartoes">
  <article class="cartao">
    <h3>Dispersão normal</h3>
    <p>Longe das ressonâncias, \(n\) cresce com a frequência: o azul é mais
    desviado que o vermelho. É o caso do vidro na faixa visível.</p>
  </article>
  <article class="cartao">
    <h3>Absorção</h3>
    <p>A parte imaginária é grande perto de \(\omega_j\), e ali o material é
    opaco. Cada banda de absorção é uma ressonância.</p>
  </article>
  <article class="cartao">
    <h3>Dispersão anômala</h3>
    <p>Dentro da banda de absorção, \(n\) <em>cai</em> com a frequência. É
    real, e foi uma surpresa quando medida.</p>
  </article>
</div>

<p>Escrevendo o número de onda como complexo, \(\tilde{k} = k + i\kappa/2\), a
onda fica</p>

\[ E = E_0e^{-\kappa z/2}\cos(kz-\omega t), \]

<p>e a intensidade decai como \(e^{-\kappa z}\), que é a lei de Beer. A
distância \(1/\kappa\) é a profundidade de penetração.</p>

<h3>Condutores: a profundidade de pele</h3>

<p>Num condutor, a corrente livre entra na conta e o resultado é que o campo
decai exponencialmente ao penetrar, com</p>

\[ \delta = \sqrt{\frac{2}{\omega\mu\sigma}}. \]

<div class="destaque">
<p><strong>Exemplo trabalhado: por que o fio grosso não adianta em alta
frequência.</strong> Para o cobre, \(\sigma = 5{,}96\times10^{7}\
\mathrm{S/m}\). Calcule a profundidade de pele a 60 Hz e a 1 GHz.</p>

\[ \delta(60\ \mathrm{Hz}) = \sqrt{\frac{2}
   {2\pi\times60\times4\pi\times10^{-7}\times5{,}96\times10^{7}}}
   = 8{,}4\ \mathrm{mm}, \]

\[ \delta(1\ \mathrm{GHz}) = 2{,}1\ \mu\mathrm{m}. \]

<p><strong>O que isso significa.</strong> Na rede elétrica, 8 mm é mais que o
raio da maioria dos fios, de modo que a corrente usa a seção toda e o efeito
quase não importa. Em 1 GHz, a corrente anda numa casca de dois micrômetros:
engrossar o condutor não serve para nada, e o que vale é aumentar a
<em>superfície</em>. Daí os condutores chatos e as fitas trançadas em
radiofrequência, e daí também fazer sentido dourar a superfície de um guia de
onda, já que a corrente nem chega a ver o metal de baixo.</p>
</div>
'''

S7 = r'''
<p>Esta seção não está nos slides da disciplina e foi escrita para cá, porque
sem ela o capítulo fica sem a aplicação que mais aparece em laboratório e em
telecomunicações.</p>

<p>Até agora, a onda viajava no espaço livre. Ponha-a dentro de um tubo metálico
oco, de seção retangular \(a \times b\), com paredes condutoras perfeitas. As
condições de contorno mudam tudo: nas paredes, a componente tangencial de
\(\vet{E}\) tem de se anular.</p>

<p>Procurando soluções que caminhem ao longo do tubo,</p>

\[ \vet{E}(x,y,z,t) = \vet{E}_0(x,y)\,e^{i(\beta z-\omega t)}, \]

<p>e substituindo nas equações de Maxwell, sobra uma equação de Helmholtz na
seção transversal,</p>

\[ \left[\frac{\partial^2}{\partial x^2}+\frac{\partial^2}{\partial y^2}
   + \left(\frac{\omega^2}{c^2}-\beta^2\right)\right]\vet{E}_0 = 0, \]

<p>que é um problema de autovalores: só certas combinações transversais
sobrevivem, e cada uma é um <strong>modo</strong>.</p>

<div class="bloco fisica">
<span class="rotulo">Por que não existe modo TEM num tubo oco</span>
<p>No espaço livre, a onda é transversal nos dois campos ao mesmo tempo: é o
modo TEM. Dentro de um tubo oco isso é impossível. Se \(\vet{E}\) e \(\vet{B}\)
fossem ambos transversais, as linhas de \(\vet{E}\) na seção teriam de se fechar
ou terminar em carga, e com \(\rot{\vet{E}}\) nulo na seção e a parede sendo
equipotencial, a única solução é \(\vet{E} = 0\).</p>
<p>Por isso os modos se dividem em <strong>TE</strong> (\(E_z = 0\), \(B_z \ne
0\)) e <strong>TM</strong> (\(B_z = 0\), \(E_z \ne 0\)). O cabo coaxial, que tem
dois condutores, escapa dessa proibição e por isso transmite TEM desde a
frequência zero.</p>
</div>

<h3>Os modos do guia retangular</h3>

<p>Para o modo TE, resolvendo a equação de Helmholtz para \(B_z\) com as
condições de contorno,</p>

\[ B_z = B_0\cos\frac{m\pi x}{a}\cos\frac{n\pi y}{b},
   \qquad m,n = 0,1,2,\dots\ \text{(não ambos nulos)}, \]

<p>e a relação de dispersão fica</p>

\[ \boxed{\;\beta = \frac{1}{c}\sqrt{\omega^2-\omega_{mn}^2},
   \qquad \omega_{mn} = c\pi\sqrt{\frac{m^2}{a^2}+\frac{n^2}{b^2}}.\;} \]

<p>Aqui está o ponto central do assunto: <strong>abaixo de \(\omega_{mn}\) o
número de onda é imaginário</strong>, e a onda não se propaga, apenas decai
exponencialmente. Cada modo tem uma frequência de corte, e o guia é um filtro
passa-altas.</p>

<h3>Velocidades, e a que não viola a relatividade</h3>

\[ v_{\text{fase}} = \frac{\omega}{\beta}
   = \frac{c}{\sqrt{1-(\omega_{mn}/\omega)^2}} \gt c,
   \qquad
   v_{\text{grupo}} = \der{\omega}{\beta}
   = c\sqrt{1-(\omega_{mn}/\omega)^2} \lt c, \]

<p>e repare que \(v_{\text{fase}}\,v_{\text{grupo}} = c^2\). A velocidade de
fase passa de \(c\) e isso não é problema: ela é a velocidade com que um padrão
de interferência caminha, e padrão não carrega informação. Quem carrega energia
e sinal é a velocidade de grupo, sempre menor que \(c\).</p>

<div class="destaque">
<p><strong>Exemplo trabalhado: o guia WR-90, da bancada de micro-ondas.</strong>
O guia padrão da banda X tem \(a = 22{,}86\ \mathrm{mm}\) e
\(b = 10{,}16\ \mathrm{mm}\). Calcule as frequências de corte dos três
primeiros modos e as velocidades a 10 GHz.</p>

<p>O modo fundamental é o TE\(_{10}\), com \(m=1, n=0\):</p>

\[ f_{10} = \frac{c}{2a} = \frac{3{,}00\times10^{8}}{2\times0{,}02286}
   = 6{,}56\ \mathrm{GHz}. \]

<p>Os dois seguintes são TE\(_{20}\), com \(f = c/a = 13{,}1\ \mathrm{GHz}\), e
TE\(_{01}\), com \(f = c/2b = 14{,}8\ \mathrm{GHz}\).</p>

<p><strong>Por que a banda X vai de 8,2 a 12,4 GHz.</strong> Acima de 6,56 GHz o
fundamental propaga; acima de 13,1 GHz o segundo modo também, e aí o guia deixa
de ser monomodo, o que estraga qualquer medida de fase. A faixa útil é a de
monomodo, com folga nas duas pontas, e é exatamente a banda X.</p>

<p><strong>As velocidades a 10 GHz.</strong> Com \(f_{10}/f = 0{,}656\),</p>

\[ v_{\text{grupo}} = c\sqrt{1-0{,}656^2} = 0{,}755\,c
   = 2{,}26\times10^{8}\ \mathrm{m/s}, \]

\[ v_{\text{fase}} = \frac{c}{0{,}755} = 1{,}32\,c
   = 3{,}97\times10^{8}\ \mathrm{m/s}. \]

<p>O produto dá \(c^2\), como tinha de dar. E note a consequência prática: um
pulso de micro-ondas atravessa um guia de dez metros em 44 ns, e não em 33 ns
como faria no vácuo. Em radar, essa diferença é distância.</p>
</div>

<h3>A fibra óptica: o guia sem metal</h3>

<p>Um tubo metálico não serve para luz visível: nessas frequências o metal
absorve demais, e além disso o diâmetro teria de ser micrométrico. A fibra
resolve isso trocando a parede condutora por uma parede <em>dielétrica</em>, em
que a luz fica presa por reflexão interna total, como a seção 5 descreveu.</p>

<p>A diferença técnica é grande. No guia metálico, o campo é rigorosamente nulo
fora; na fibra, ele vaza para a casca como onda evanescente, e o modo é uma
solução que casa duas regiões. Escrevendo a componente longitudinal em cada
uma, com \(\beta\) o número de onda ao longo da fibra,</p>

\[ \text{núcleo}\;(s \lt a):\quad
   \left(\nabla_t^2 + \kappa^2\right)E_z = 0,
   \qquad \kappa^2 = n_1^2k_0^2 - \beta^2 \gt 0, \]

\[ \text{casca}\;(s \gt a):\quad
   \left(\nabla_t^2 - \gamma^2\right)E_z = 0,
   \qquad \gamma^2 = \beta^2 - n_2^2k_0^2 \gt 0, \]

<p>com \(k_0 = \omega/c\). A primeira dá oscilação (funções de Bessel \(J_m\)),
a segunda dá decaimento (funções de Bessel modificadas \(K_m\)), e casar as
duas na interface produz uma <strong>equação transcendental</strong> para
\(\beta\). Ela não tem solução fechada, e é resolvida numericamente: cada raiz
é um modo.</p>

<div class="bloco def">
<span class="rotulo">O parâmetro que decide tudo: o número V</span>
<p>As duas condições acima só podem valer ao mesmo tempo se
\(n_2k_0 \lt \beta \lt n_1k_0\), e toda a física de quantos modos existem cabe
num único número adimensional,</p>
<p>\[ V = k_0\,a\sqrt{n_1^2-n_2^2} = \frac{2\pi a}{\lambda}\,\mathrm{NA}. \]</p>
<p>O número de modos guiados é aproximadamente \(V^2/2\), e a fibra é
<strong>monomodo</strong> quando \(V \lt 2{,}405\), que é o primeiro zero de
\(J_0\). Abaixo desse valor sobra um único modo, o LP\(_{01}\), que não tem
corte: ele existe em qualquer frequência, por menor que seja.</p>
</div>

<div class="destaque">
<p><strong>Exemplo trabalhado: a fibra de telecomunicações.</strong> A fibra
padrão de enlace tem núcleo de raio \(a = 4{,}1\ \mu\mathrm{m}\),
\(n_1 = 1{,}4504\) e \(n_2 = 1{,}4447\). Ela é monomodo em quais comprimentos
de onda?</p>

<p>A abertura numérica é</p>

\[ \mathrm{NA} = \sqrt{n_1^2-n_2^2} = \sqrt{1{,}4504^2-1{,}4447^2} = 0{,}1285, \]

<p>e o número V vale</p>

\[ V(\lambda) = \frac{2\pi\times4{,}1\times10^{-6}}{\lambda}\times0{,}1285. \]

<div class="tabela-rolavel">
<table>
<thead><tr><th>\(\lambda\)</th><th>\(V\)</th><th>regime</th></tr></thead>
<tbody>
<tr><td>850 nm</td><td>3,89</td><td>multimodo (cerca de 7 modos)</td></tr>
<tr><td>1310 nm</td><td>2,53</td><td>logo acima do corte</td></tr>
<tr><td>1550 nm</td><td>2,14</td><td>monomodo</td></tr>
</tbody>
</table>
</div>

<p>O comprimento de onda de corte, onde \(V = 2{,}405\), é</p>

\[ \lambda_c = \frac{2\pi a\,\mathrm{NA}}{2{,}405} = 1376\ \mathrm{nm}, \]

<p>de modo que a fibra é monomodo acima disso. Não é coincidência que as duas
janelas de telecomunicações sejam 1310 nm e 1550 nm: a primeira é onde a
dispersão do sílica passa por zero, e a segunda é onde a atenuação é mínima,
0,2 dB por quilômetro. Em 1550 nm a luz percorre 100 km e ainda chega com 1 %
da potência, o que é o motivo de os cabos submarinos existirem.</p>

<p><strong>Uma comparação que vale guardar.</strong> O guia metálico da seção
anterior tem corte <em>inferior</em>: abaixo de \(f_{10}\) nada passa. A fibra
monomodo tem corte <em>superior</em> para os modos de ordem alta: acima de
\(\lambda_c\) só o fundamental sobrevive. São problemas de autovalor com
condições de contorno diferentes, e os comportamentos se invertem.</p>
</div>
'''

S7B = r'''
<p>Feche as duas pontas de um guia com paredes metálicas e a onda deixa de
viajar: ela vai e volta, e só sobrevivem as frequências em que a ida e a volta
se somam em fase. O tubo vira uma <strong>cavidade ressonante</strong>, que é o
análogo eletromagnético de um tubo de órgão.</p>

<p>Para a cavidade retangular de lados \(a\), \(b\), \(d\), a condição de onda
estacionária nas três direções dá</p>

\[ \boxed{\;f_{mnp} = \frac{c}{2}\sqrt{\frac{m^2}{a^2}+\frac{n^2}{b^2}
   +\frac{p^2}{d^2}}.\;} \]

<p>Note a diferença em relação ao guia: lá havia um contínuo de frequências
acima do corte, aqui há um conjunto <em>discreto</em>. Prender a onda nos três
eixos quantiza tudo.</p>

<p>A qualidade de uma cavidade se mede pelo fator \(Q\),</p>

\[ Q = 2\pi\frac{\text{energia guardada}}{\text{energia perdida por ciclo}}
   = \frac{f_0}{\Delta f}, \]

<p>que é também a razão entre a frequência de ressonância e a largura do pico.
Uma cavidade de cobre na banda X tem \(Q\) de alguns milhares; uma cavidade
supercondutora de nióbio, usada em aceleradores, chega a \(10^{10}\), e nela um
fóton de micro-ondas dá bilhões de voltas antes de ser absorvido.</p>

<h3>O Fabry-Perot</h3>

<p>Na óptica, a cavidade mais usada não tem paredes metálicas: são dois
espelhos parcialmente transparentes, paralelos, separados por \(L\). A luz
entra, faz muitas idas e voltas, e o que sai é a soma de infinitas
contribuições, cada uma com um atraso de fase</p>

\[ \delta = \frac{4\pi n L\cos\theta}{\lambda}. \]

<p>Somando a série geométrica, a transmissão é a função de Airy:</p>

\[ \boxed{\;T(\delta) = \frac{1}{1 + F\sen^2(\delta/2)},
   \qquad F = \frac{4R}{(1-R)^2},\;} \]

<p>com \(R\) a refletância de cada espelho. É um <strong>filtro</strong>:
transmite 100 % nas ressonâncias, onde \(\delta\) é múltiplo de \(2\pi\), e
quase nada entre elas.</p>

<p>Duas grandezas descrevem o filtro:</p>

<div class="cartoes">
  <article class="cartao">
    <h3>Intervalo espectral livre</h3>
    \[ \mathrm{FSR} = \frac{c}{2nL} \]
    <p>A distância em frequência entre dois picos vizinhos. Depende só do
    comprimento da cavidade.</p>
  </article>
  <article class="cartao">
    <h3>Finesse</h3>
    \[ \mathcal{F} = \frac{\pi\sqrt{R}}{1-R}
       = \frac{\mathrm{FSR}}{\Delta f} \]
    <p>Quantas vezes o pico é mais estreito que o espaçamento. Depende só da
    refletância dos espelhos.</p>
  </article>
</div>

<div class="destaque">
<p><strong>Exemplo trabalhado: um Fabry-Perot de bancada.</strong> Dois espelhos
de \(R = 0{,}99\) separados por \(L = 1{,}0\ \mathrm{cm}\) de ar, usados em
1550 nm. Calcule o intervalo espectral livre, a finesse, a largura de cada pico
e o fator \(Q\).</p>

\[ \mathrm{FSR} = \frac{c}{2L} = \frac{3{,}00\times10^{8}}{0{,}02}
   = 15{,}0\ \mathrm{GHz}, \]

\[ \mathcal{F} = \frac{\pi\sqrt{0{,}99}}{1-0{,}99} = 313, \]

\[ \Delta f = \frac{\mathrm{FSR}}{\mathcal{F}}
   = \frac{15{,}0\ \mathrm{GHz}}{313} = 48\ \mathrm{MHz}. \]

<p>Com a frequência da luz em 1550 nm valendo \(193{,}4\ \mathrm{THz}\),</p>

\[ Q = \frac{f_0}{\Delta f} = \frac{1{,}934\times10^{14}}{4{,}8\times10^{7}}
   = 4{,}0\times10^{6}. \]

<p><strong>O que esses números significam.</strong> O filtro separa frequências
que diferem de 48 MHz numa portadora de 193 THz, isto é, uma parte em quatro
milhões. É com isso que se mede a largura de linha de um laser, que se estabiliza
a frequência de um relógio óptico, e que se escolhe um único canal num cabo
que carrega oitenta deles.</p>

<p><strong>O preço.</strong> O FSR de 15 GHz significa que o filtro transmite em
<em>muitas</em> frequências, espaçadas de 15 GHz. Para escolher uma só é preciso
combinar o Fabry-Perot com um filtro mais grosseiro, ou usar dois em série com
comprimentos ligeiramente diferentes, no arranjo chamado de Vernier. Nenhum
filtro é bom em resolução e em alcance ao mesmo tempo, e isso é geral.</p>

<p><strong>E o laser?</strong> Um laser é exatamente isto com meio de ganho no
meio: a cavidade escolhe as frequências, o ganho repõe a energia perdida, e o
que sai é uma onda com a largura de linha da cavidade dividida por um fator que
depende da potência. O LIGO, no extremo, usa cavidades Fabry-Perot de 4 km com
finesse perto de 450, e é assim que ele mede deslocamentos de
\(10^{-18}\ \mathrm{m}\).</p>
</div>
'''

S8 = r'''
<div class="cartoes">
  <article class="cartao">
    <h3><a href="codigo/onda_plana.py">onda_plana.py</a></h3>
    <p>Monta uma onda plana numa grade e verifica, por diferenças finitas, que
    ela satisfaz as quatro equações de Maxwell; depois calcula Poynting,
    intensidade e pressão de radiação.</p>
    <p><strong>Confira assim:</strong> os divergentes têm de dar zero, os dois
    rotacionais têm de casar com as derivadas temporais, a média de \(S\) tem de
    dar \(\frac12 c\varepsilon_0E_0^2\), e as densidades elétrica e magnética de
    energia têm de ser iguais.</p>
  </article>
  <article class="cartao">
    <h3><a href="codigo/fresnel.py">fresnel.py</a></h3>
    <p>Calcula \(R\) e \(T\) para as duas polarizações em função do ângulo,
    acha Brewster e o ângulo crítico, e trata o caso de reflexão total.</p>
    <p><strong>Confira assim:</strong> \(R+T=1\) em todo ângulo e nas duas
    polarizações; \(R\) paralelo tem de zerar exatamente em
    \(\arctan(n_2/n_1)\); e acima do ângulo crítico \(R\) tem de valer 1.</p>
  </article>
  <article class="cartao">
    <h3><a href="codigo/fibra_fabry.py">fibra_fabry.py</a></h3>
    <p>Resolve a equação transcendental dos modos de um guia dielétrico e conta
    quantos sobrevivem em cada comprimento de onda; depois monta a função de
    Airy e mede FSR, finesse e largura direto da curva.</p>
    <p><strong>Confira assim:</strong> o número de modos tem de crescer como
    \(V\) e a fibra tem de ficar monomodo acima do corte; e o FSR e a finesse
    medidos na curva têm de reproduzir \(c/2nL\) e
    \(\pi\sqrt{R}/(1-R)\).</p>
  </article>
  <article class="cartao">
    <h3><a href="codigo/guia_onda.py">guia_onda.py</a></h3>
    <p>Acha os modos de um guia por autovalores do laplaciano discreto, para a
    seção retangular e para seções que não têm solução fechada.</p>
    <p><strong>Confira assim:</strong> no retângulo, os cortes numéricos têm de
    reproduzir \(c\pi\sqrt{m^2/a^2+n^2/b^2}\); e a seção em L, que nenhuma
    fórmula resolve, tem de dar corte menor que o do retângulo que a
    contém.</p>
  </article>
</div>
'''

SECOES = [
    ('De Maxwell à equação de onda', S1),
    ('Ondas planas monocromáticas', S2),
    ('Energia, momento e pressão de radiação', S3),
    ('Ondas na matéria e incidência normal', S4),
    ('Incidência oblíqua: Snell, Fresnel, Brewster', S5),
    ('Dispersão e condutores', S6),
    ('Guias de onda e fibras', S7),
    ('Cavidades e o Fabry-Perot', S7B),
    ('No Spyder', S8),
]

SECOES.append(('Exercícios propostos', exercicios.bloco(LISTA)))


def main():
    titulos = [t for t, _ in SECOES]
    escreve('cap09.html', secoes_html(SECOES), secoes=titulos)


if __name__ == '__main__':
    main()
