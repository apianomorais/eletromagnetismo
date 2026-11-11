# -*- coding: utf-8 -*-
"""Capítulo 8: leis de conservação.

O texto é escrito do zero. O Griffiths entra como referência de ordem e de
numeração de capítulo, nunca como fonte de frases, enunciados ou figuras:
os exemplos aqui são de nossa autoria, com contextos e números próprios.
"""
from molde import escreve, secoes_html
import exercicios
from lista_cap08 import LISTA

S1 = r'''
<p>Três grandezas se conservam na mecânica: energia, momento e momento angular.
Em eletrodinâmica as três continuam se conservando, com uma condição: é preciso
incluir na contabilidade o que está guardado <em>no campo</em>. Este capítulo
faz essa contabilidade, e o resultado muda a maneira de pensar sobre o que o
campo é.</p>

<p>O molde de toda lei de conservação local já apareceu no capítulo 5, com a
carga:</p>

\[ \pder{\rho}{t} = -\divg{\vet{J}}. \]

<p>Lida devagar, a equação diz: a quantidade dentro de uma região só muda se
houver fluxo atravessando a fronteira. A carga não desaparece aqui para
reaparecer ali; ela <em>viaja</em>. Essa exigência é mais forte do que a
conservação global, e é ela que se exige das outras três grandezas.</p>

<p>Em forma integral,</p>

\[ \der{Q_{\text{int}}}{t} = -\oint \vet{J}\cdot d\vet{a}. \]

<p>Todas as leis deste capítulo terão essa cara: uma derivada temporal de uma
densidade de um lado, um divergente de uma corrente do outro. O trabalho é
descobrir <em>quem</em> faz o papel da densidade e quem faz o papel da
corrente.</p>
'''

S2 = r'''
<p>Comece pelo trabalho que o campo faz sobre as cargas. Numa região de volume
\(V\), a força de Lorentz dá, em potência,</p>

\[ \der{W_{\text{mec}}}{t} = \int \vet{E}\cdot\vet{J}\,d\tau, \]

<p>e repare que o campo magnético não aparece, como o capítulo 5 já havia
garantido: ele não realiza trabalho.</p>

<p>Agora troque \(\vet{J}\) pela lei de Ampère-Maxwell,
\(\vet{J} = \frac{1}{\mu_0}\rot{\vet{B}} - \varepsilon_0\partial\vet{E}
/\partial t\), e use a identidade do capítulo 1,
\(\divg{\left(\vet{E}\cruz\vet{B}\right)} =
\vet{B}\cdot\left(\rot{\vet{E}}\right) -
\vet{E}\cdot\left(\rot{\vet{B}}\right)\), junto com a lei de Faraday. Depois de
algumas linhas que vale a pena fazer uma vez na vida,</p>

\[ \boxed{\;\der{W_{\text{mec}}}{t}
   = -\der{}{t}\int_V u\,d\tau - \oint_S \vet{S}\cdot d\vet{a},\;} \]

<p>com</p>

\[ u = \frac{\varepsilon_0}{2}E^2 + \frac{1}{2\mu_0}B^2,
   \qquad
   \vet{S} = \frac{1}{\mu_0}\left(\vet{E}\cruz\vet{B}\right). \]

<p>É o <strong>teorema de Poynting</strong>, e ele é a lei de conservação da
energia na forma exigida acima: a energia que as cargas ganham sai de duas
fontes, do estoque guardado no campo dentro da região e do fluxo que entra pela
fronteira. Nada aparece do nada.</p>

<div class="destaque">
<p><strong>Exemplo trabalhado: por onde entra a energia que aquece um
fio.</strong> Um fio de cobre de raio \(a = 1{,}0\ \mathrm{mm}\) e comprimento
\(L = 1{,}0\ \mathrm{m}\) conduz \(I = 10\ \mathrm{A}\). Ele dissipa
\(I^2R\). A pergunta é: por onde essa energia chega?</p>

<p>A resistência é \(R = \rho L/A = 1{,}68\times10^{-8}\times1{,}0/
(3{,}14\times10^{-6}) = 5{,}35\ \mathrm{m}\Omega\), e a potência dissipada é
\(I^2R = 0{,}535\ \mathrm{W}\).</p>

<p><strong>Os campos na superfície do fio.</strong> O campo elétrico é
longitudinal, e vale a queda de tensão dividida pelo comprimento:</p>

\[ E_z = \frac{IR}{L} = \frac{10\times5{,}35\times10^{-3}}{1{,}0}
   = 5{,}35\times10^{-2}\ \mathrm{V/m}. \]

<p>O campo magnético é azimutal, e na superfície vale</p>

\[ B_\phi = \frac{\mu_0 I}{2\pi a}
   = \frac{4\pi\times10^{-7}\times10}{2\pi\times10^{-3}}
   = 2{,}0\times10^{-3}\ \mathrm{T}. \]

<p><strong>O vetor de Poynting.</strong> Com \(\vet{E}\) ao longo do fio e
\(\vet{B}\) em volta dele, o produto \(\vet{E}\cruz\vet{B}\) aponta
<em>radialmente para dentro</em>:</p>

\[ S = \frac{E_zB_\phi}{\mu_0}
   = \frac{5{,}35\times10^{-2}\times2{,}0\times10^{-3}}{4\pi\times10^{-7}}
   = 85{,}1\ \mathrm{W/m^2}. \]

<p>Multiplicando pela área lateral, \(2\pi aL = 6{,}28\times10^{-3}\
\mathrm{m^2}\),</p>

\[ P = 85{,}1\times6{,}28\times10^{-3} = 0{,}535\ \mathrm{W}, \]

<p>exatamente o \(I^2R\).</p>

<p><strong>O que isso quer dizer.</strong> A energia <em>não</em> viaja dentro
do fio, empurrada pelos elétrons: ela viaja no campo, no espaço em volta, e
entra pela superfície lateral em toda a extensão. O fio não é um cano por onde
a energia passa; é um sorvedouro em que ela cai, vinda de fora.</p>

<p>Pareceria filosofia, não fosse por uma consequência prática: em alta
frequência, a energia continua viajando por fora, e o condutor serve apenas para
<em>guiar</em> o campo. É por isso que um guia de onda oco funciona sem nenhum
condutor central, e é por isso que a qualidade do dielétrico, no cabo coaxial,
importa mais que a do cobre.</p>
</div>
'''

S3 = r'''
<p>Para o momento, a conta tem a mesma estrutura e um resultado mais
surpreendente. Partindo da força total sobre as cargas de uma região,</p>

\[ \vet{F} = \int \left(\rho\vet{E} + \vet{J}\cruz\vet{B}\right)d\tau, \]

<p>e repetindo o jogo de trocar \(\rho\) e \(\vet{J}\) pelas equações de
Maxwell, chega-se a</p>

\[ \boxed{\;\vet{F} = \oint_S \vet{T}\cdot d\vet{a}
   - \varepsilon_0\mu_0\der{}{t}\int_V \vet{S}\,d\tau,\;} \]

<p>com o <strong>tensor de tensões de Maxwell</strong></p>

\[ T_{ij} = \varepsilon_0\left(E_iE_j - \tfrac12\delta_{ij}E^2\right)
   + \frac{1}{\mu_0}\left(B_iB_j - \tfrac12\delta_{ij}B^2\right). \]

<p>Duas leituras valem o esforço de entender.</p>

<p><strong>Primeira: a força vira um fluxo pela superfície.</strong> Para
situações estáticas, o segundo termo some e a força sobre tudo o que está
dentro é a integral de \(\vet{T}\) sobre qualquer superfície que envolva a
região. Não é preciso saber nada sobre o que há lá dentro: basta medir o campo
na fronteira. É o equivalente eletromagnético de calcular a força num fluido
pela pressão nas paredes.</p>

<p><strong>Segunda: o campo tem momento.</strong> O termo com a derivada
temporal diz que, além da força, existe</p>

\[ \vet{p}_{\text{campo}} = \varepsilon_0\mu_0\int\vet{S}\,d\tau
   = \varepsilon_0\int\left(\vet{E}\cruz\vet{B}\right)d\tau, \]

<p>isto é, uma densidade de momento \(\vet{g} = \varepsilon_0
\left(\vet{E}\cruz\vet{B}\right) = \vet{S}/c^2\), que é a mesma relação usada
no capítulo 9 para a pressão de radiação.</p>

<div class="bloco fisica">
<span class="rotulo">A terceira lei, finalmente resolvida</span>
<p>O capítulo 10 observa que a força entre duas cargas em movimento não obedece
à terceira lei de Newton: elas não são iguais e opostas. Se só as partículas
existissem, o momento total não se conservaria.</p>
<p>Com o momento do campo na conta, tudo fecha. O que falta de um lado está
guardado no campo, e será devolvido depois. A terceira lei, na forma forte, é
uma aproximação válida quando a propagação pode ser tratada como instantânea; o
que vale sempre é a conservação do momento total, campo incluído.</p>
</div>

<div class="destaque">
<p><strong>Exemplo trabalhado: a força entre as placas, pelo tensor.</strong>
Um capacitor de placas paralelas tem densidade superficial \(\sigma\) e campo
\(E = \sigma/\varepsilon_0\) entre elas, nulo fora. Calcule a força por unidade
de área sobre a placa positiva usando o tensor de tensões.</p>

<p>Escolha uma superfície que envolva apenas a placa positiva: uma caixa
achatada com uma face entre as placas e a outra fora. Tome \(z\)
perpendicular às placas, com \(\vet{E} = -E\vers{z}\) na região interna.</p>

<p>Na face de fora o campo é nulo e nada contribui. Na face de dentro, a normal
aponta para \(-\vers{z}\), e a componente relevante do tensor é</p>

\[ T_{zz} = \varepsilon_0\left(E_z^2 - \tfrac12E^2\right)
   = \frac{\varepsilon_0E^2}{2}. \]

<p>Logo a força por unidade de área é</p>

\[ \frac{F}{A} = \frac{\varepsilon_0E^2}{2}
   = \frac{\sigma^2}{2\varepsilon_0}, \]

<p>atrativa, e é exatamente a pressão eletrostática que o capítulo 2 obteve por
outro caminho, somando a força da carga com o campo médio.</p>

<p><strong>Os números.</strong> Para \(E = 10^{6}\ \mathrm{V/m}\), que é um
terço da ruptura do ar, a pressão vale</p>

\[ \frac{\varepsilon_0E^2}{2}
   = \frac{8{,}85\times10^{-12}\times10^{12}}{2} = 4{,}4\ \mathrm{Pa}, \]

<p>ou seja, 0,45 gramas-força por centímetro quadrado. É pouco, e é essa
pequenez que explica por que motores eletrostáticos nunca competiram com os
magnéticos: a pressão magnética \(B^2/2\mu_0\), com um tesla, vale
\(4\times10^{5}\) Pa, cem mil vezes mais.</p>
</div>
'''

S4 = r'''
<p>Se o campo guarda momento, guarda também momento angular, com densidade</p>

\[ \vet{\ell} = \vet{r}\cruz\vet{g}
   = \varepsilon_0\,\vet{r}\cruz\left(\vet{E}\cruz\vet{B}\right). \]

<p>Isso não é uma formalidade: existe momento angular guardado em
configurações <em>completamente estáticas</em>, em que nada se move e nada
gira.</p>

<div class="destaque">
<p><strong>Exemplo trabalhado: o momento angular escondido.</strong> Monte o
seguinte arranjo, todo ele parado. Duas cascas cilíndricas coaxiais de
comprimento \(L\), uma de raio \(a\) com carga \(+Q\) e outra de raio \(b \gt
a\) com carga \(-Q\), de modo que haja campo elétrico radial na região entre
elas. Dentro dessa região, um solenoide longo de raio \(R\) (com \(a \lt R \lt
b\)), com \(n\) espiras por metro e corrente \(I\), produzindo
\(\vet{B} = \mu_0nI\vers{z}\) no seu interior.</p>

<p>Na casca de raio entre \(a\) e \(R\) os dois campos coexistem:</p>

\[ \vet{E} = \frac{\lambda}{2\pi\varepsilon_0 s}\vers{s},
   \qquad \lambda = \frac{Q}{L},
   \qquad \vet{B} = \mu_0nI\,\vers{z}. \]

<p>A densidade de momento é então</p>

\[ \vet{g} = \varepsilon_0\left(\vet{E}\cruz\vet{B}\right)
   = \varepsilon_0EB\left(\vers{s}\cruz\vers{z}\right)
   = -\varepsilon_0EB\,\vers{\phi}, \]

<p>que é <em>azimutal</em>: o momento do campo circula em torno do eixo. A
componente \(z\) do momento angular é \(s\,g_\phi\), e integrando sobre a casca,
com \(d\tau = 2\pi sL\,ds\),</p>

\[ L_z = -\varepsilon_0 B\int_a^R
   \frac{\lambda}{2\pi\varepsilon_0 s}\,s\,\left(2\pi sL\right)ds
   = -\frac{1}{2}\mu_0 nIQ\left(R^2-a^2\right). \]

<p>Com \(n = 1000\) espiras por metro, \(I = 2{,}0\ \mathrm{A}\),
\(Q = 10\ \mathrm{nC}\), \(a = 1{,}0\ \mathrm{cm}\) e \(R = 2{,}0\
\mathrm{cm}\), isso dá \(3{,}8\times10^{-15}\ \mathrm{kg\,m^2/s}\), ridiculamente
pequeno e, ainda assim, diferente de zero.</p>

<p><strong>Agora desligue a corrente.</strong> O campo magnético cai, e pela lei
de Faraday aparece um campo elétrico induzido azimutal, que empurra as cargas
das cascas e põe o conjunto a <em>girar</em>. O exercício 8.4 refaz a conta por
esse caminho, integrando o torque sobre as duas cascas durante o desligamento,
e o resultado é o mesmo \(L_z\): o momento angular que estava guardado no campo
passa para a matéria, e o total se conserva.</p>

<p><strong>Por que isso é desconcertante.</strong> Antes de desligar, nada se
movia. Nenhuma peça girava, nenhuma corrente variava. E mesmo assim havia
momento angular, pronto para ser entregue. O campo não é um acessório de
cálculo: é um depósito de energia, momento e momento angular, tão real quanto o
cilindro de metal.</p>

<p>Este arranjo é conhecido como paradoxo do disco de Feynman, e a resposta é
que não há paradoxo nenhum: há apenas uma contabilidade incompleta quando se
esquece o campo.</p>
</div>

<h3>O quadro completo</h3>

<p>Vale fechar o capítulo com a tabela que organiza tudo, porque as três leis
têm exatamente a mesma estrutura:</p>

<div class="tabela-rolavel">
<table>
<thead><tr>
  <th>grandeza</th><th>densidade no campo</th><th>corrente</th>
</tr></thead>
<tbody>
<tr><td>carga</td>
    <td>\(\rho\) (nas partículas)</td>
    <td>\(\vet{J}\)</td></tr>
<tr><td>energia</td>
    <td>\(u = \frac{\varepsilon_0}{2}E^2+\frac{1}{2\mu_0}B^2\)</td>
    <td>\(\vet{S} = \frac{1}{\mu_0}\vet{E}\cruz\vet{B}\)</td></tr>
<tr><td>momento</td>
    <td>\(\vet{g} = \varepsilon_0\,\vet{E}\cruz\vet{B} = \vet{S}/c^2\)</td>
    <td>\(-\vet{T}\) (tensor de tensões)</td></tr>
<tr><td>momento angular</td>
    <td>\(\vet{\ell} = \vet{r}\cruz\vet{g}\)</td>
    <td>\(-\vet{r}\cruz\vet{T}\)</td></tr>
</tbody>
</table>
</div>

<p>Repare na economia: \(\vet{S}\) aparece duas vezes, como corrente de energia
e, dividido por \(c^2\), como densidade de momento. Essa coincidência não é
coincidência, e a relatividade a explica: energia e momento são componentes do
mesmo objeto, e \(u\), \(\vet{S}\) e \(\vet{T}\) são as peças de um único tensor
de energia-momento.</p>
'''

S5 = r'''
<div class="cartoes">
  <article class="cartao">
    <h3><a href="codigo/poynting_fio.py">poynting_fio.py</a></h3>
    <p>Monta os campos na superfície de um fio com corrente, integra o vetor de
    Poynting sobre a superfície lateral e compara com \(I^2R\).</p>
    <p><strong>Confira assim:</strong> o fluxo tem de dar exatamente a potência
    dissipada, e tem de apontar para <em>dentro</em> em toda a superfície; e
    o resultado não pode depender do raio da superfície escolhida, desde que
    ela envolva o fio.</p>
  </article>
  <article class="cartao">
    <h3><a href="codigo/tensor_maxwell.py">tensor_maxwell.py</a></h3>
    <p>Calcula a força entre duas cargas pontuais integrando o tensor de
    tensões sobre uma superfície que envolve uma delas, sem usar a lei de
    Coulomb.</p>
    <p><strong>Confira assim:</strong> o resultado tem de reproduzir Coulomb; e
    tem de ser o mesmo para superfícies de formas e tamanhos diferentes, desde
    que envolvam a mesma carga.</p>
  </article>
</div>
'''

SECOES = [
    ('O molde: a conservação da carga', S1),
    ('Energia: o teorema de Poynting', S2),
    ('Momento e o tensor de tensões', S3),
    ('Momento angular, e o que fica escondido', S4),
    ('No Spyder', S5),
]

SECOES.append(('Exercícios propostos', exercicios.bloco(LISTA)))


def main():
    titulos = [t for t, _ in SECOES]
    escreve('cap08.html', secoes_html(SECOES), secoes=titulos)


if __name__ == '__main__':
    main()
