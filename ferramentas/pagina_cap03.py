# -*- coding: utf-8 -*-
"""Capítulo 3: potenciais e técnicas especiais.

O texto é escrito do zero. O Griffiths entra como referência de ordem e de
numeração de capítulo, nunca como fonte de frases, enunciados ou figuras:
os exemplos aqui são de nossa autoria, com contextos e números próprios.
"""
from molde import escreve, secoes_html
import exercicios
from lista_cap03 import LISTA

S1 = r'''
<p>O capítulo 2 resolveu o problema direto: dada a carga, ache o campo. Em
quase todo problema de verdade, porém, a carga <em>não</em> é dada. Numa placa
condutora aterrada perto de uma carga, a distribuição de carga induzida depende
do campo, que depende da carga induzida: é um problema de autoconsistência, e a
integral de Coulomb não sabe por onde começar.</p>

<p>A saída é atacar a equação diferencial em vez da integral. Nas regiões onde
não há carga,</p>

\[ \boxed{\;\nabla^2 V = 0,\;} \]

<p>e o problema vira: achar a função que satisfaz Laplace dentro da região e
assume valores dados na fronteira. A carga induzida deixa de ser incógnita e
passa a ser consequência, lida no fim a partir de \(\sigma =
-\varepsilon_0\,\partial V/\partial n\).</p>

<h3>Três propriedades que decidem tudo</h3>

<p><strong>A propriedade da média.</strong> A solução de Laplace num ponto é
igual à média dela sobre qualquer esfera centrada nesse ponto:</p>

\[ V(\vet{r}) = \frac{1}{4\pi R^2}\oint_{\text{esfera}} V\,da. \]

<p>Em duas dimensões vale o mesmo com círculos, e em uma dimensão a
consequência é imediata: a solução é uma reta, porque o valor num ponto é a
média dos dois vizinhos.</p>

<p><strong>Sem máximos nem mínimos locais.</strong> Se o valor num ponto é a
média dos vizinhos, não pode haver pico nem vale no interior: todo extremo está
na fronteira. Daí sai o teorema de Earnshaw, que proíbe equilíbrio estável
puramente eletrostático: uma carga de prova não tem onde se acomodar, porque não
existe mínimo de potencial no vácuo.</p>

<p><strong>Rigidez.</strong> A solução é suave e "esticada": Laplace é a
equação da membrana de sabão presa num arame torto. Essa imagem é boa o
bastante para prever qualitativamente quase qualquer solução antes de calcular,
e vale usá-la.</p>

<div class="bloco fisica">
<span class="rotulo">A média não é um detalhe</span>
<p>A propriedade da média é a base do método numérico que este capítulo usa: se
o valor é a média dos vizinhos, basta varrer a grade substituindo cada ponto
pela média dos quatro vizinhos e repetir até parar de mudar. É a
<strong>relaxação</strong>, e ela resolve, com quinze linhas de código, geometrias
que não têm solução fechada nenhuma.</p>
</div>
'''

S2 = r'''
<p>Antes de inventar soluções é preciso saber se elas são únicas. Dois teoremas
resolvem isso, e a demonstração dos dois é a mesma ideia: supor duas soluções e
mostrar que a diferença é nula.</p>

<p><strong>Primeiro teorema.</strong> A solução de Laplace numa região é
determinada de forma única pelo valor de \(V\) na fronteira.</p>

<p><em>Prova.</em> Sejam \(V_1\) e \(V_2\) duas soluções. A diferença
\(W = V_1 - V_2\) também satisfaz Laplace, e vale zero em toda a fronteira. Como
não pode haver máximo nem mínimo no interior, o maior e o menor valor de \(W\)
estão na fronteira, e ambos são zero. Logo \(W \equiv 0\).</p>

<p><strong>Segundo teorema.</strong> Numa região cercada de condutores, com uma
densidade de carga \(\rho\) dada no espaço entre eles, o campo é determinado de
forma única pela <em>carga total</em> de cada condutor.</p>

<p>Esse segundo é mais sutil e mais útil: ele não exige saber como a carga se
distribui em cada condutor, apenas quanto há em cada um. É o que torna
solucionáveis os problemas de capacitores.</p>

<div class="bloco def">
<span class="rotulo">A consequência prática que todo o capítulo usa</span>
<p>Se você <em>achar</em>, por qualquer meio, inclusive por adivinhação, uma
função que satisfaça Laplace na região e dê os valores certos na fronteira,
então ela <strong>é</strong> a solução. Não existe "outra" solução esperando
para ser encontrada.</p>
<p>É essa licença que legitima o método das imagens: a solução obtida com uma
carga fictícia é a solução verdadeira, desde que a carga fictícia esteja
<em>fora</em> da região de interesse e as condições de contorno sejam
reproduzidas.</p>
</div>
'''

S3 = r'''
<p>Uma carga pontual \(q\) a uma altura \(d\) de um plano condutor infinito e
aterrado. A carga induzida no plano é desconhecida, e a integral de Coulomb não
ajuda. Mas repare: o que o plano <em>faz</em>, do ponto de vista da região de
cima, é manter \(V = 0\) em \(z = 0\).</p>

<p>Ora, existe outra configuração que faz exatamente isso: duas cargas opostas,
\(+q\) em \(z=d\) e \(-q\) em \(z=-d\). O plano médio entre elas é uma
equipotencial de valor zero, por simetria.</p>

<p>Pelo teorema da unicidade, o potencial na região \(z \gt 0\) é o mesmo nos
dois casos:</p>

\[ V(x,y,z) = \frac{q}{4\pi\varepsilon_0}\left[
   \frac{1}{\sqrt{x^2+y^2+(z-d)^2}}
   - \frac{1}{\sqrt{x^2+y^2+(z+d)^2}}\right]. \]

<p>A carga imagem está em \(z = -d\), isto é, <em>fora</em> da região onde a
solução vale. Isso é obrigatório: dentro da região ela acrescentaria uma fonte
que não existe, e a solução deixaria de satisfazer Laplace.</p>

<h3>O que se lê da solução</h3>

<p><strong>A carga induzida.</strong> Derivando na superfície,</p>

\[ \sigma = -\varepsilon_0\pder{V}{z}\bigg|_{z=0}
   = \frac{-qd}{2\pi\left(x^2+y^2+d^2\right)^{3/2}}. \]

<p>Integrando sobre o plano inteiro, com \(da = 2\pi s\,ds\),</p>

\[ Q_{\text{ind}} = \int_0^\infty
   \frac{-qd}{2\pi\left(s^2+d^2\right)^{3/2}}\,2\pi s\,ds = -q. \]

<p>A carga induzida total é exatamente \(-q\), nem mais nem menos, e ela se
espalha com um raio característico da ordem de \(d\): metade dela está dentro de
um círculo de raio \(\sqrt{3}\,d\).</p>

<p><strong>A força.</strong> A carga é atraída pelo plano com a força que a
imagem faria:</p>

\[ F = -\frac{1}{4\pi\varepsilon_0}\frac{q^2}{(2d)^2}. \]

<p><strong>A energia, com uma armadilha.</strong> A energia do sistema
<em>não</em> é a do par de cargas. Para o par, \(W = -q^2/4\pi\varepsilon_0(2d)\);
para a carga e o plano, é a metade disso:</p>

\[ W = -\frac{1}{4\pi\varepsilon_0}\frac{q^2}{4d}. \]

<p>A razão é que no problema real não há campo na região \(z \lt 0\), de modo que
só metade da energia de campo existe. Integrar \(\varepsilon_0E^2/2\) apenas na
região de cima dá exatamente esse valor, e é o jeito seguro de não errar o
fator.</p>

<div class="destaque">
<p><strong>Exemplo trabalhado: a esfera aterrada.</strong> Uma carga \(q\) está
a uma distância \(a\) do centro de uma esfera condutora aterrada de raio
\(R\), com \(a \gt R\). Onde pôr a imagem, e com que carga?</p>

<p>Ponha a imagem \(q'\) sobre a reta que liga o centro à carga, a uma distância
\(b\) do centro, e imponha \(V = 0\) em toda a superfície da esfera. Num ponto
da superfície a um ângulo \(\theta\) da reta, as distâncias são</p>

\[ \imath_q = \sqrt{R^2+a^2-2Ra\cos\theta},\qquad
   \imath_{q'} = \sqrt{R^2+b^2-2Rb\cos\theta}, \]

<p>e a condição \(q/\imath_q + q'/\imath_{q'} = 0\) tem de valer para
<em>todo</em> \(\theta\). Elevando ao quadrado e igualando os coeficientes de
\(\cos\theta\) e os termos constantes, sai um sistema de duas equações cuja
solução é</p>

\[ \boxed{\;b = \frac{R^2}{a},\qquad q' = -\frac{R}{a}\,q.\;} \]

<p>A imagem é menor que a carga e fica mais perto do centro quanto mais longe
estiver a carga. Dois limites conferem o resultado: quando \(a \to R\), a imagem
tende a \(-q\) encostada na superfície, que é o caso do plano; e quando
\(a \to \infty\), a imagem some, porque uma esfera aterrada vista de muito longe
não tem como se polarizar.</p>

<p><strong>Os números.</strong> Com \(R = 5{,}0\ \mathrm{cm}\),
\(a = 15\ \mathrm{cm}\) e \(q = 2{,}0\ \mathrm{nC}\): a imagem vale
\(q' = -0{,}67\ \mathrm{nC}\) e fica a \(b = 1{,}67\ \mathrm{cm}\) do centro. A
força sobre a carga é atrativa e vale</p>

\[ F = \frac{1}{4\pi\varepsilon_0}\frac{qq'}{(a-b)^2}
   = 8{,}99\times10^{9}\,\frac{2{,}0\times10^{-9}\times0{,}67\times10^{-9}}
   {(0{,}1333)^2} = 6{,}8\times10^{-7}\ \mathrm{N}, \]

<p>isto é, menos de um micronewton. A carga total induzida na esfera é
\(-0{,}67\) nC, que é a imagem: o resto escoou para a terra.</p>
</div>
'''

S4 = r'''
<p>Quando não há imagem que sirva, resta resolver Laplace de frente. A técnica
padrão é supor que a solução se escreve como produto de funções de uma variável
cada, e ver se a equação permite.</p>

<h3>Em cartesianas</h3>

<p>Com \(V(x,y) = X(x)Y(y)\) em duas dimensões, a equação de Laplace vira</p>

\[ \frac{1}{X}\dder{X}{x} + \frac{1}{Y}\dder{Y}{y} = 0. \]

<p>O primeiro termo só depende de \(x\) e o segundo só de \(y\), e a soma é zero
para todo par \((x,y)\). A única maneira é cada um ser uma constante, uma
positiva e a outra negativa:</p>

\[ \dder{X}{x} = -k^2X,\qquad \dder{Y}{y} = +k^2Y, \]

<p>de modo que \(X\) é seno e cosseno e \(Y\) é exponencial, ou vice-versa. Qual
é qual, decide a condição de contorno: a direção em que a solução precisa
oscilar fica com os senos.</p>

<div class="destaque">
<p><strong>Exemplo trabalhado: o duto com uma tampa.</strong> Um duto de seção
quadrada, infinito na direção \(z\), tem três paredes aterradas e a quarta,
em \(y = a\), mantida a um potencial constante \(V_0\). A seção vai de
\(x = 0\) a \(x = a\) e de \(y = 0\) a \(y = a\). Ache \(V(x,y)\).</p>

<p>A solução precisa se anular em \(x=0\) e \(x=a\), de modo que a oscilação é
em \(x\):</p>

\[ X_n(x) = \sen\frac{n\pi x}{a},\qquad n = 1,2,3,\dots \]

<p>Em \(y\), a solução é combinação de exponenciais, e como ela precisa se
anular em \(y=0\), fica com o seno hiperbólico:</p>

\[ V(x,y) = \sum_n c_n \sen\!\left(\frac{n\pi x}{a}\right)
   \senh\!\left(\frac{n\pi y}{a}\right). \]

<p>Falta impor a quarta parede. Em \(y=a\),</p>

\[ V_0 = \sum_n c_n \senh(n\pi)\,\sen\frac{n\pi x}{a}, \]

<p>e os coeficientes saem pela ortogonalidade dos senos, multiplicando os dois
lados por \(\sen(m\pi x/a)\) e integrando de \(0\) a \(a\):</p>

\[ c_n\senh(n\pi) = \frac{2V_0}{a}\int_0^a \sen\frac{n\pi x}{a}\,dx
   = \frac{2V_0}{n\pi}\left[1-(-1)^n\right], \]

<p>que é nulo para \(n\) par e vale \(4V_0/n\pi\) para \(n\) ímpar. Logo</p>

\[ \boxed{\;V(x,y) = \frac{4V_0}{\pi}\sum_{n\ \text{ímpar}}
   \frac{1}{n}\,\frac{\senh(n\pi y/a)}{\senh(n\pi)}\,
   \sen\frac{n\pi x}{a}.\;} \]

<p><strong>Por que a série converge depressa.</strong> O fator
\(\senh(n\pi y/a)/\senh(n\pi) \approx e^{-n\pi(1-y/a)}\) cai exponencialmente
com \(n\), e tanto mais rápido quanto mais longe da tampa. No centro do duto,
\(y = a/2\), o termo \(n=3\) já é \(e^{-\pi} \approx 4\%\) do primeiro, e o
\(n=5\) é 0,2 %. Três termos bastam para qualquer uso prático, e o programa
desta página mostra isso num gráfico.</p>
</div>

<h3>Em esféricas</h3>

<p>Com simetria azimutal, a separação \(V = R(r)\Theta(\theta)\) leva à equação
de Legendre, cujas soluções bem-comportadas são os polinômios
\(P_l(\cos\theta)\). A solução geral é</p>

\[ \boxed{\;V(r,\theta) = \sum_{l=0}^{\infty}
   \left(A_l r^l + \frac{B_l}{r^{l+1}}\right)P_l(\cos\theta).\;} \]

<p>Dentro de uma região que inclui a origem, os \(B_l\) têm de ser nulos, senão
o potencial explode; fora, numa região que inclui o infinito, os \(A_l\) têm de
ser nulos, senão o potencial não vai a zero. É sempre assim, e metade do
trabalho é só decidir qual dos dois conjuntos sobrevive.</p>

<div class="destaque">
<p><strong>Exemplo trabalhado: a esfera condutora num campo uniforme.</strong>
Uma esfera condutora neutra de raio \(R\) é posta num campo uniforme
\(\vet{E}_0 = E_0\vers{z}\). Qual o potencial fora, e qual a carga induzida?</p>

<p>Longe da esfera o campo volta a ser o uniforme, cujo potencial é
\(V = -E_0z = -E_0 r\cos\theta = -E_0 r P_1\). Isso fixa o comportamento
assintótico: só o termo \(l=1\) aparece com \(A_l\), e vale \(-E_0\).</p>

<p>Na superfície, a esfera é uma equipotencial, e com a esfera neutra e o
problema simétrico, esse valor é zero. Então</p>

\[ V(r,\theta) = \left(-E_0r + \frac{B_1}{r^2}\right)\cos\theta
   + \sum_{l\ne1}\frac{B_l}{r^{l+1}}P_l, \]

<p>e impor \(V(R,\theta) = 0\) para todo \(\theta\) obriga, pela ortogonalidade,
que todo \(B_l\) com \(l\ne1\) seja nulo e que \(-E_0R + B_1/R^2 = 0\), ou seja
\(B_1 = E_0R^3\). Portanto</p>

\[ \boxed{\;V = -E_0\left(r - \frac{R^3}{r^2}\right)\cos\theta.\;} \]

<p>O segundo termo é exatamente o potencial de um dipolo de momento
\(p = 4\pi\varepsilon_0R^3E_0\): a esfera responde ao campo externo polarizando-se
como um dipolo, e nada mais. A polarizabilidade de uma esfera condutora é
\(4\pi\varepsilon_0R^3\), isto é, três vezes o seu volume vezes
\(\varepsilon_0\).</p>

<p>A carga induzida sai da derivada normal:</p>

\[ \sigma = -\varepsilon_0\pder{V}{r}\bigg|_{r=R} = 3\varepsilon_0E_0\cos\theta, \]

<p>máxima nos polos, nula no equador, positiva de um lado e negativa do outro,
com soma zero como manda a neutralidade. E note o campo logo fora do polo:
\(\sigma/\varepsilon_0 = 3E_0\), <em>três vezes</em> o campo aplicado. É por isso
que descargas começam em pontas e saliências, e é o princípio do para-raios.</p>
</div>
'''

S5 = r'''
<p>Falta uma técnica, e ela responde a uma pergunta diferente: não "qual é o
potencial exatamente", mas "com o que ele se parece de longe".</p>

<p>Para uma distribuição localizada, expanda \(1/\imath\) em polinômios de
Legendre, como no capítulo 1:</p>

\[ V(\vet{r}) = \frac{1}{4\pi\varepsilon_0}\sum_{n=0}^{\infty}
   \frac{1}{r^{n+1}}\int (r')^n P_n(\cos\alpha)\,\rho(\vet{r}')\,d\tau', \]

<p>com \(\alpha\) o ângulo entre \(\vet{r}\) e \(\vet{r}'\). Os primeiros termos
são:</p>

<div class="cartoes">
  <article class="cartao">
    <h3>Monopolo</h3>
    \[ V_0 = \frac{Q}{4\pi\varepsilon_0 r} \]
    <p>Domina sempre que a carga total não for nula. Cai com \(1/r\).</p>
  </article>
  <article class="cartao">
    <h3>Dipolo</h3>
    \[ V_1 = \frac{\vet{p}\cdot\vers{r}}{4\pi\varepsilon_0 r^2},
       \quad \vet{p} = \int\vet{r}'\rho\,d\tau' \]
    <p>Domina quando a carga total é nula. Cai com \(1/r^2\).</p>
  </article>
  <article class="cartao">
    <h3>Quadrupolo</h3>
    \[ V_2 \sim \frac{1}{r^3} \]
    <p>Domina quando carga e dipolo são nulos, por simetria.</p>
  </article>
</div>

<div class="bloco alerta">
<span class="rotulo">O momento de dipolo depende da origem</span>
<p>Mudando a origem para \(\vet{r}' \to \vet{r}' - \vet{a}\), o momento de
dipolo vira \(\vet{p}' = \vet{p} - Q\vet{a}\). Ou seja: ele só é
<strong>independente da origem quando a carga total é nula</strong>.</p>
<p>Isso não é um defeito. A regra geral é que o primeiro momento não nulo da
série é independente da origem, e todos os seguintes não são. Faz sentido:
quando há carga total, o termo de dipolo é apenas uma correção de como se
escolheu o centro, e não tem significado próprio.</p>
</div>

<p>Para o campo, derivando o termo de dipolo em esféricas,</p>

\[ \vet{E}_{\text{dip}} = \frac{p}{4\pi\varepsilon_0 r^3}
   \left(2\cos\theta\,\vers{r} + \sen\theta\,\vers{\theta}\right), \]

<p>que cai com \(1/r^3\), e não com \(1/r^2\). Vale repetir porque é o erro
clássico: o potencial do dipolo vai com \(1/r^2\), o campo vai com
\(1/r^3\).</p>
'''

S6 = r'''
<p>Três programas, e o primeiro deles é o mais importante do curso inteiro:
ele resolve, por força bruta, problemas que nenhuma das técnicas analíticas
alcança.</p>

<div class="cartoes">
  <article class="cartao">
    <h3><a href="codigo/laplace_relaxacao.py">laplace_relaxacao.py</a></h3>
    <p>Resolve a equação de Laplace numa grade por relaxação, substituindo cada
    ponto pela média dos vizinhos até convergir, com qualquer condição de
    contorno.</p>
    <p><strong>Confira assim:</strong> no duto do exemplo resolvido, a solução
    numérica tem de bater com a série de Fourier; o erro tem de cair como
    \(h^2\); e o valor no centro tem de ser a média dos valores da fronteira,
    pela propriedade da média.</p>
  </article>
  <article class="cartao">
    <h3><a href="codigo/metodo_imagens.py">metodo_imagens.py</a></h3>
    <p>Compara a solução por imagem com a relaxação, para a carga acima do
    plano aterrado, e integra a carga induzida na superfície.</p>
    <p><strong>Confira assim:</strong> a carga induzida total tem de dar
    \(-q\); o perfil de \(\sigma\) tem de seguir
    \(-qd/2\pi(s^2+d^2)^{3/2}\); e a relaxação tem de reproduzir o potencial da
    imagem onde as duas valem.</p>
  </article>
  <article class="cartao">
    <h3><a href="codigo/multipolos.py">multipolos.py</a></h3>
    <p>Calcula os momentos de uma distribuição discreta e compara a série
    truncada com o potencial exato, ordem por ordem.</p>
    <p><strong>Confira assim:</strong> o erro da série truncada na ordem \(n\)
    tem de cair como \(1/r^{\,n+2}\); e o momento de dipolo tem de mudar quando
    a origem muda, a menos que a carga total seja nula.</p>
  </article>
</div>
'''

SECOES = [
    ('Laplace, e o que as suas soluções têm de especial', S1),
    ('Unicidade', S2),
    ('O método das imagens', S3),
    ('Separação de variáveis', S4),
    ('A expansão multipolar', S5),
    ('No Spyder', S6),
]

SECOES.append(('Exercícios propostos', exercicios.bloco(LISTA)))


def main():
    titulos = [t for t, _ in SECOES]
    escreve('cap03.html', secoes_html(SECOES), secoes=titulos)


if __name__ == '__main__':
    main()
