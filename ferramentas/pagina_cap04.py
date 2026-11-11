# -*- coding: utf-8 -*-
"""Capítulo 4: campos elétricos na matéria.

O texto é escrito do zero. O Griffiths entra como referência de ordem e de
numeração de capítulo, nunca como fonte de frases, enunciados ou figuras:
os exemplos aqui são de nossa autoria, com contextos e números próprios.
"""
from molde import escreve, secoes_html
import exercicios
from lista_cap04 import LISTA

S1 = r'''
<p>Até aqui, a matéria apareceu em duas formas extremas: o vácuo, que não faz
nada, e o condutor, que faz tudo, cancelando o campo no interior. Falta o caso
intermediário, que é o da maioria das substâncias: o isolante, onde as cargas
não podem viajar mas podem se deslocar um pouco.</p>

<p>Esse "um pouco" é o assunto do capítulo, e ele acontece por dois mecanismos
diferentes.</p>

<h3>Átomos que se deformam</h3>

<p>Num átomo neutro, a nuvem eletrônica está centrada no núcleo. Com campo
externo, o núcleo é empurrado para um lado e a nuvem para o outro, até que a
atração entre elas equilibre o campo aplicado. O átomo fica com um momento de
dipolo</p>

\[ \vet{p} = \alpha\vet{E}, \]

<p>com \(\alpha\) a polarizabilidade atômica, tabelada para cada elemento. Ela
tem dimensão de \(\varepsilon_0\) vezes volume, e o volume em questão é, com boa
aproximação, o do próprio átomo.</p>

<div class="destaque">
<p><strong>Exemplo trabalhado: estimando \(\alpha\) com um modelo de
criança.</strong> Trate o átomo como um núcleo pontual \(+q\) no centro de uma
nuvem esférica uniforme de carga \(-q\) e raio \(a\). Aplique um campo
\(\vet{E}\) e veja o quanto o núcleo se desloca.</p>

<p>Dentro de uma esfera uniformemente carregada, o campo a uma distância \(d\)
do centro vale, pela lei de Gauss,</p>

\[ E_{\text{nuvem}} = \frac{1}{4\pi\varepsilon_0}\frac{qd}{a^3}. \]

<p>O equilíbrio é onde esse campo restaurador iguala o aplicado:</p>

\[ E = \frac{qd}{4\pi\varepsilon_0a^3}
   \;\Longrightarrow\;
   p = qd = \left(4\pi\varepsilon_0a^3\right)E, \]

<p>de modo que \(\alpha = 4\pi\varepsilon_0a^3 = 3\varepsilon_0 V_{\text{átomo}}\).</p>

<p><strong>Confira com a tabela.</strong> Para o hidrogênio,
\(a \approx 0{,}53\ \text{Å}\), e o modelo dá</p>

\[ \frac{\alpha}{4\pi\varepsilon_0} = a^3
   = \left(0{,}53\times10^{-10}\right)^3
   = 1{,}5\times10^{-31}\ \mathrm{m^3}. \]

<p>O valor experimental é \(0{,}667\times10^{-30}\ \mathrm{m^3}\), ou seja, o
modelo erra por um fator 4,5. Para um modelo que trata a nuvem eletrônica como
uma bola de bilhar uniforme, errar por um fator 4 e acertar a <em>ordem de
grandeza e a dependência com o volume</em> é um resultado respeitável. A conta
quântica certa dá \(4{,}5\,a_0^3\), e o fator que falta é exatamente esse.</p>
</div>

<h3>Moléculas que giram</h3>

<p>Algumas moléculas já têm momento de dipolo permanente, sem campo nenhum: a
água, com \(p = 6{,}1\times10^{-30}\ \mathrm{C\,m}\), é o exemplo canônico. Para
elas, o campo não precisa induzir nada, basta alinhar, e o mecanismo é o torque
que o capítulo 6 vai reencontrar no magnetismo:</p>

\[ \vet{\tau} = \vet{p}\cruz\vet{E},\qquad U = -\vet{p}\cdot\vet{E}. \]

<p>A competição aqui é com a agitação térmica, e o resultado é uma
susceptibilidade que cai com \(1/T\). Num campo forte de laboratório,
\(10^{6}\ \mathrm{V/m}\), a energia de alinhamento da água vale
\(6{,}1\times10^{-24}\ \mathrm{J}\) contra \(4{,}1\times10^{-21}\ \mathrm{J}\) de
energia térmica a 300 K: uma parte em setecentas. O alinhamento é sempre
parcial, e é por isso que até a água, com o maior dipolo da química cotidiana,
tem polarização muito menor do que o alinhamento total daria.</p>

<p>Num campo não uniforme há ainda uma força resultante, \(\vet{F} =
\left(\vet{p}\cdot\nabla\right)\vet{E}\), e é ela que explica o jato de água
desviado por um canudo atritado: o canudo polariza as moléculas e depois atrai
os dipolos que ele mesmo criou, sempre para a região de campo mais
intenso.</p>
'''

S2 = r'''
<p>Chame de <strong>polarização</strong> o momento de dipolo por unidade de
volume,</p>

\[ \vet{P} = \frac{d\vet{p}}{d\tau}. \]

<p>A pergunta é: qual é o campo produzido por um objeto polarizado? A resposta
é mais simples do que parece, e tem a mesma estrutura do capítulo 6.</p>

<p>O potencial de um dipolo é \(\frac{1}{4\pi\varepsilon_0}
\frac{\vet{p}\cdot\vers{\imath}}{\imath^2}\). Somando sobre o volume,</p>

\[ V = \frac{1}{4\pi\varepsilon_0}\int
   \frac{\vet{P}\cdot\vers{\imath}}{\imath^2}\,d\tau'. \]

<p>Usando \(\nabla'(1/\imath) = \vers{\imath}/\imath^2\) e integrando por
partes, como o capítulo 1 ensinou, o integrando se separa em dois termos: um de
superfície e um de volume. O resultado é que</p>

\[ \boxed{\;\sigma_b = \vet{P}\cdot\vers{n},\qquad
   \rho_b = -\divg{\vet{P}},\;} \]

<p>e o potencial do objeto polarizado é <em>exatamente</em> o de duas
distribuições de carga comuns, uma na superfície e outra no volume.</p>

<div class="bloco fisica">
<span class="rotulo">Carga ligada é carga de verdade</span>
<p>Não há nada de fictício nessas cargas. Pense numa fileira de dipolos
alinhados dentro do material: a ponta positiva de cada um encosta na ponta
negativa do vizinho, e as duas se cancelam. Isso vale em todo ponto onde
\(\vet{P}\) é uniforme, e é por isso que \(\rho_b\) só não é nulo onde a
polarização varia. Nas faces, porém, não há vizinho para cancelar, e sobra
carga de verdade, que se pode medir e que produz campo.</p>
<p>É o mesmo argumento, palavra por palavra, que o capítulo 6 usa para a
corrente ligada \(\vet{K}_b = \vet{M}\cruz\vers{n}\). As duas figuras são
irmãs.</p>
</div>

<figure class="figura-exemplo" style="max-width:40rem">
  <img src="assets/img/cap04_ligadas.svg" alt="Cargas ligadas num dielétrico polarizado">
  <figcaption>Dentro, cada ponta positiva encosta numa negativa e as duas se
  anulam; nas faces não há vizinho, e sobra carga de verdade.</figcaption>
</figure>

<div class="destaque">
<p><strong>Exemplo trabalhado: a esfera uniformemente polarizada.</strong> Uma
esfera de raio \(R\) tem polarização uniforme \(\vet{P} = P\vers{z}\). Ache o
campo dentro e fora.</p>

<p>Com \(\vet{P}\) uniforme, \(\rho_b = -\divg{\vet{P}} = 0\): não há carga
ligada no volume. Na superfície,</p>

\[ \sigma_b = \vet{P}\cdot\vers{n} = P\cos\theta, \]

<p>que é puro \(P_1\) na base de Legendre. O problema virou, então, o de achar o
potencial de uma casca esférica com densidade \(\sigma = P\cos\theta\), e isso o
capítulo 3 resolve de olhos fechados: a série de Legendre só pode ter o termo
\(l = 1\), pela ortogonalidade.</p>

<p>Escrevendo \(V_{\text{in}} = A r\cos\theta\) e \(V_{\text{out}} =
B\cos\theta/r^2\), a continuidade em \(r=R\) dá \(AR = B/R^2\), e o salto da
derivada normal dá</p>

\[ -\pder{V_{\text{out}}}{r} + \pder{V_{\text{in}}}{r}\bigg|_{r=R}
   = \frac{\sigma_b}{\varepsilon_0} = \frac{P\cos\theta}{\varepsilon_0}, \]

<p>de onde \(2B/R^3 + A = P/\varepsilon_0\). Resolvendo,
\(A = P/3\varepsilon_0\) e \(B = PR^3/3\varepsilon_0\). Portanto</p>

\[ \boxed{\;\vet{E}_{\text{dentro}} = -\frac{\vet{P}}{3\varepsilon_0},\;} \]

<p>uniforme e <em>contra</em> a polarização, e fora o campo é o de um dipolo
puro de momento \(p = \frac{4}{3}\pi R^3P\), isto é, \(\vet{P}\) vezes o
volume.</p>

<p><strong>Guarde o fator 1/3.</strong> Ele é o fator de despolarização da
esfera, o mesmo que aparece no capítulo 6 como \(\vet{H} = -\vet{M}/3\). Para
outras formas ele muda: vale 1 para uma placa fina polarizada
perpendicularmente, e 0 para um bastão longo polarizado ao longo do eixo. Quanto
mais alongado na direção da polarização, menor o campo despolarizante, e é por
isso que ímãs e eletretos são compridos.</p>
</div>
'''

S3 = r'''
<p>Dentro de um dielétrico há dois tipos de carga: a ligada, que veio da
polarização, e a livre, que alguém pôs lá. A lei de Gauss não distingue as
duas, porque campo é campo:</p>

\[ \varepsilon_0\divg{\vet{E}} = \rho = \rho_b + \rho_f
   = -\divg{\vet{P}} + \rho_f. \]

<p>Passando a polarização para o outro lado,</p>

\[ \divg{\left(\varepsilon_0\vet{E}+\vet{P}\right)} = \rho_f, \]

<p>e definindo o <strong>deslocamento elétrico</strong></p>

\[ \boxed{\;\vet{D} \equiv \varepsilon_0\vet{E} + \vet{P},
   \qquad \divg{\vet{D}} = \rho_f,\;} \]

<p>obtém-se uma lei de Gauss em que só a carga livre aparece. Na forma
integral,</p>

\[ \oint \vet{D}\cdot d\vet{a} = Q_{f,\text{int}}. \]

<p>Isso é muito conveniente, porque a carga livre é a que se conhece: é a que
foi posta nas placas do capacitor, a que veio pelo fio.</p>

<div class="bloco alerta">
<span class="rotulo">Três armadilhas do D</span>
<p><strong>D não é um campo como E.</strong> O rotacional de \(\vet{D}\) é
\(\rot{\vet{P}}\), que não é nulo em geral. Logo <em>não existe</em> potencial
para \(\vet{D}\), e não vale escrever \(\vet{D} = -\nabla U\).</p>
<p><strong>D não é determinado só pela carga livre.</strong> A lei de Gauss dá o
divergente; faltam o rotacional e as condições de contorno. Dois problemas com a
mesma carga livre podem ter \(\vet{D}\) diferente se a geometria do dielétrico
for diferente.</p>
<p><strong>A simetria tem de ser do conjunto.</strong> Usar
\(\oint\vet{D}\cdot d\vet{a} = Q_f\) para tirar \(\vet{D}\) da integral exige
que a simetria valha para a carga livre <em>e</em> para o dielétrico. Com um
pedaço de vidro de lado, a conta não vale, por mais simétrica que seja a
carga.</p>
</div>
'''

S4 = r'''
<p>Para a maioria dos materiais, e para campos não muito fortes, a polarização é
proporcional ao campo:</p>

\[ \vet{P} = \varepsilon_0\chi_e\vet{E}, \]

<p>com \(\chi_e\) a susceptibilidade elétrica, adimensional e positiva.
Substituindo na definição de \(\vet{D}\),</p>

\[ \vet{D} = \varepsilon_0(1+\chi_e)\vet{E} \equiv \varepsilon\vet{E},
   \qquad \varepsilon_r = \frac{\varepsilon}{\varepsilon_0} = 1+\chi_e, \]

<p>com \(\varepsilon_r\) a constante dielétrica, que é o número tabelado. Alguns
valores a 20 °C: ar, 1,00059; papel, 3,7; vidro, 4 a 7; água, 80,1.</p>

<p>A água se destaca por duas ordens de grandeza, e a razão é o dipolo
permanente: nos outros materiais da lista o mecanismo é a deformação dos
átomos, e nela o deslocamento é minúsculo. É também por isso que a constante
dielétrica da água cai com a temperatura, enquanto a do vidro quase não
muda.</p>

<h3>Condições de contorno</h3>

<p>Na interface entre dois dielétricos, sem carga livre na superfície,</p>

\[ D^{\text{ac}}_\perp = D^{\text{ab}}_\perp,
   \qquad \vet{E}^{\text{ac}}_\parallel = \vet{E}^{\text{ab}}_\parallel. \]

<p>A componente normal de \(\vet{D}\) é contínua porque não há carga livre; a
tangencial de \(\vet{E}\), porque o rotacional dele é nulo. Repare que são
campos <em>diferentes</em> em cada condição, e trocá-los é o erro mais comum do
capítulo.</p>

<div class="destaque">
<p><strong>Exemplo trabalhado: a esfera dielétrica num campo uniforme.</strong>
Uma esfera de constante dielétrica \(\varepsilon_r\) e raio \(R\) é posta num
campo uniforme \(E_0\vers{z}\). Ache o campo dentro.</p>

<p>Não há carga livre em lugar nenhum, de modo que \(V\) satisfaz Laplace dentro
e fora, e a solução é a série de Legendre do capítulo 3. Longe, o potencial tem
de voltar a \(-E_0r\cos\theta\), o que fixa o termo \(l=1\); e como a fonte é
puro \(P_1\), nenhum outro \(l\) é excitado. Então</p>

\[ V_{\text{in}} = A\,r\cos\theta,\qquad
   V_{\text{out}} = \left(-E_0r + \frac{B}{r^2}\right)\cos\theta. \]

<p>As duas condições de contorno em \(r=R\) são a continuidade de \(V\) e a
continuidade de \(D_\perp = \varepsilon\,E_r\):</p>

\[ AR = -E_0R + \frac{B}{R^2},
   \qquad -\varepsilon_r A = E_0 + \frac{2B}{R^3}. \]

<p>Resolvendo o sistema,</p>

\[ A = -\frac{3E_0}{\varepsilon_r+2},
   \qquad B = \frac{\varepsilon_r-1}{\varepsilon_r+2}E_0R^3, \]

<p>e portanto</p>

\[ \boxed{\;\vet{E}_{\text{dentro}}
   = \frac{3}{\varepsilon_r+2}\,\vet{E}_0,\;} \]

<p>uniforme, na mesma direção do campo aplicado, e <em>menor</em> que ele.</p>

<p><strong>Os limites conferem.</strong> Com \(\varepsilon_r = 1\) não há
material e o campo interno é \(E_0\). Com \(\varepsilon_r \to \infty\), que é o
condutor, o campo interno vai a zero, como manda o capítulo 2. Para a água,
\(\varepsilon_r = 80\), o campo dentro de uma gota é
\(3E_0/82 \approx 0{,}037E_0\): a gota blinda 96 % do campo aplicado.</p>

<p>O termo \(B\) é o de um dipolo, e dele se lê a polarizabilidade da esfera
inteira: \(\alpha_{\text{esfera}} = 4\pi\varepsilon_0R^3
\frac{\varepsilon_r-1}{\varepsilon_r+2}\). Essa fração é a relação de
Clausius-Mossotti, e é ela que liga a constante dielétrica macroscópica à
polarizabilidade molecular.</p>
</div>
'''

S5 = r'''
<p>Com dielétrico linear, a energia guardada no campo ganha uma forma
compacta:</p>

\[ W = \frac{1}{2}\int \vet{D}\cdot\vet{E}\,d\tau
     = \frac{\varepsilon}{2}\int E^2\,d\tau. \]

<p>Repare que ela <em>não</em> é \(\frac{\varepsilon_0}{2}\int E^2\): a diferença
é a energia gasta para polarizar o material, isto é, para esticar cada átomo.
Essa parcela é real e recuperável, e é por isso que ela entra na conta.</p>

<p>A consequência prática é a capacitância. Preenchendo um capacitor com
dielétrico de constante \(\varepsilon_r\), a mesma carga livre produz um campo
\(\varepsilon_r\) vezes menor, a tensão cai na mesma proporção, e</p>

\[ C = \varepsilon_r C_0. \]

<p>É o motivo de todo capacitor comercial ter um dielétrico dentro: ele aumenta
a capacitância e, de quebra, aumenta a tensão de ruptura, porque o material
suporta campos maiores que o ar.</p>

<div class="destaque">
<p><strong>Exemplo trabalhado: o capacitor que engole a placa.</strong> Um
capacitor de placas paralelas, de largura \(w\) e separação \(d\), tem uma placa
de dielétrico parcialmente inserida, cobrindo um comprimento \(x\) das placas.
Com a <em>carga</em> fixa, qual a força sobre o dielétrico?</p>

<p>A capacitância é a soma das duas partes, em paralelo:</p>

\[ C(x) = \frac{\varepsilon_0 w}{d}\left[(\ell-x) + \varepsilon_r x\right]
   = \frac{\varepsilon_0 w}{d}\left[\ell + (\varepsilon_r-1)x\right]. \]

<p>Com carga fixa, a energia é \(W = Q^2/2C\), e a força é menos o gradiente da
energia:</p>

\[ F = -\der{W}{x} = \frac{Q^2}{2C^2}\der{C}{x}
     = \frac{Q^2}{2C^2}\,\frac{\varepsilon_0w(\varepsilon_r-1)}{d}. \]

<p>Como \(dC/dx \gt 0\), a força é <strong>positiva</strong>: o dielétrico é
puxado para dentro. Isso vale também com tensão fixa, embora a conta pareça dar
o contrário se feita sem cuidado, porque aí a bateria fornece energia e o sinal
de \(dW/dx\) engana.</p>

<p><strong>De onde vem a força, fisicamente?</strong> Não é do campo uniforme
entre as placas, que é paralelo à placa dielétrica e não puxa nada. Vem do campo
de borda, aquele que escapa nas extremidades e que todo mundo desenha torto e
ignora. Ele é não uniforme, e sobre os dipolos induzidos age
\(\left(\vet{p}\cdot\nabla\right)\vet{E}\), que aponta para dentro. É um caso em
que o resultado é obtido com segurança pela energia, e a explicação local exige
justamente o efeito que todo mundo despreza.</p>

<p><strong>Números.</strong> Com \(w = 5{,}0\ \mathrm{cm}\),
\(d = 1{,}0\ \mathrm{mm}\), \(\varepsilon_r = 4\) (vidro),
\(\ell = 10\ \mathrm{cm}\), \(x = 5{,}0\ \mathrm{cm}\) e
\(Q = 20\ \mathrm{nC}\): a capacitância vale \(1{,}11\times10^{-10}\
\mathrm{F}\), e a força dá \(F = 2{,}2\times10^{-5}\ \mathrm{N}\), ou cerca de
2 miligramas-força. Pequena, mas perfeitamente mensurável numa balança de
torção, e ela cresce com o quadrado da carga.</p>
</div>
'''

S6 = r'''
<div class="cartoes">
  <article class="cartao">
    <h3><a href="codigo/esfera_dieletrica.py">esfera_dieletrica.py</a></h3>
    <p>Resolve a esfera dielétrica num campo uniforme pela série de Legendre e
    confere o resultado por relaxação numa grade, sem usar a série.</p>
    <p><strong>Confira assim:</strong> o campo interno tem de ser uniforme e
    valer \(3E_0/(\varepsilon_r+2)\); os limites \(\varepsilon_r \to 1\) e
    \(\varepsilon_r \to \infty\) têm de dar \(E_0\) e zero; e a relaxação tem de
    reproduzir os dois.</p>
  </article>
  <article class="cartao">
    <h3><a href="codigo/cargas_ligadas.py">cargas_ligadas.py</a></h3>
    <p>Calcula \(\rho_b\) e \(\sigma_b\) para polarizações dadas, incluindo as
    não uniformes, e integra tudo.</p>
    <p><strong>Confira assim:</strong> a carga ligada total tem de ser
    rigorosamente nula, volume mais superfície, para qualquer \(\vet{P}\); e o
    campo obtido somando as cargas ligadas tem de dar
    \(-\vet{P}/3\varepsilon_0\) dentro da esfera uniformemente polarizada.</p>
  </article>
</div>
'''

SECOES = [
    ('Como a matéria responde', S1),
    ('Carga ligada, e o campo do objeto polarizado', S2),
    ('O deslocamento elétrico', S3),
    ('Meios lineares', S4),
    ('Energia e forças', S5),
    ('No Spyder', S6),
]

SECOES.append(('Exercícios propostos', exercicios.bloco(LISTA)))


def main():
    titulos = [t for t, _ in SECOES]
    escreve('cap04.html', secoes_html(SECOES), secoes=titulos)


if __name__ == '__main__':
    main()
