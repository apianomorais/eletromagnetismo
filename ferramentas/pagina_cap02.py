# -*- coding: utf-8 -*-
"""Capítulo 2: eletrostática.

O texto é escrito do zero. O Griffiths entra como referência de ordem e de
numeração de capítulo, nunca como fonte de frases, enunciados ou figuras:
os exemplos aqui são de nossa autoria, com contextos e números próprios.
"""
from molde import escreve, secoes_html
import exercicios
from lista_cap02 import LISTA

S1 = r'''
<p>A pergunta fundadora do curso é simples de enunciar: dado um conjunto de
cargas paradas, qual é a força sobre uma carga de prova? Tudo o que vem depois,
até as ondas eletromagnéticas do capítulo 9, é consequência da resposta e das
suas generalizações.</p>

<p>A resposta experimental é a lei de Coulomb. Para duas cargas pontuais
paradas,</p>

\[ \boxed{\;\vet{F} = \frac{1}{4\pi\varepsilon_0}\,\frac{q_1q_2}{\imath^2}\,
   \vers{\imath},\;} \]

<p>onde \(\imath\) é a distância entre elas e \(\vers{\imath}\) aponta da carga
que produz para a carga que sente. A constante vale</p>

\[ \frac{1}{4\pi\varepsilon_0} = 8{,}99\times10^{9}\
   \mathrm{N\,m^2/C^2},\qquad
   \varepsilon_0 = 8{,}85\times10^{-12}\ \mathrm{C^2/N\,m^2}. \]

<p>Três coisas na fórmula merecem atenção, porque nenhuma delas é óbvia.</p>

<p><strong>O inverso do quadrado.</strong> O expoente é 2, e é 2 com precisão
extraordinária. Experimentos no estilo do de Cavendish, medindo a ausência de
campo dentro de uma casca condutora fechada, limitam o desvio a menos de
\(10^{-16}\). Se o expoente fosse \(2+\epsilon\) com \(\epsilon\) não nulo, não
haveria lei de Gauss, não haveria potencial com \(1/r\), e metade das
ferramentas deste curso desapareceria.</p>

<p><strong>A instantaneidade.</strong> A fórmula não contém o tempo. Ela vale
para cargas paradas, e paradas há tempo suficiente; a correção para cargas que
se movem é assunto do capítulo 10, e aí a informação viaja a \(c\).</p>

<p><strong>A superposição.</strong> A força de várias cargas sobre uma é a soma
vetorial das forças individuais, sem nenhum termo cruzado. Isso é um fato
experimental, não uma necessidade lógica, e é o que torna o eletromagnetismo
linear e, portanto, tratável.</p>

<h3>O campo elétrico</h3>

<p>Em vez de calcular a força sobre cada carga de prova possível, convém
calcular uma vez só a grandeza que depende apenas das fontes:</p>

\[ \vet{E}(\vet{r}) = \frac{1}{4\pi\varepsilon_0}\sum_i
   \frac{q_i}{\imath_i^2}\,\vers{\imath}_i,
   \qquad \vet{F} = q\vet{E}. \]

<p>A pergunta "o campo existe mesmo, ou é só um artifício de cálculo" tem
resposta, e ela é não trivial: o campo existe, e o capítulo 8 vai mostrar que
ele carrega energia e momento próprios. Por enquanto, basta tratá-lo como uma
propriedade do espaço criada pelas fontes.</p>

<h3>Distribuições contínuas</h3>

<p>Carga de verdade vem em pedaços de \(1{,}6\times10^{-19}\ \mathrm{C}\), mas
em qualquer problema macroscópico há tantos pedaços que convém tratá-la como
contínua. Conforme a geometria,</p>

\[ \vet{E} = \frac{1}{4\pi\varepsilon_0}\int\frac{\vers{\imath}}{\imath^2}
   \left\{\begin{array}{l}
   \lambda\,d\ell'\\ \sigma\,da'\\ \rho\,d\tau'
   \end{array}\right. \]

<p>O integrando é vetorial, e esse é o trabalho: resolver três integrais em vez
de uma. Quando há simetria, as componentes transversais se cancelam aos pares e
sobra uma integral escalar.</p>

<div class="destaque">
<p><strong>Exemplo trabalhado: o fio finito.</strong> Um bastão de comprimento
\(2L\) tem carga \(Q\) uniformemente distribuída, \(\lambda = Q/2L\). Qual é o
campo num ponto a uma distância \(z\) do centro, sobre a perpendicular
mediana?</p>

<p>Ponha o bastão no eixo \(x\), de \(-L\) a \(L\), e o ponto em \((0,0,z)\).
Um pedaço \(dx'\) em \(x'\) está a uma distância \(\imath =
\sqrt{x'^2+z^2}\), e contribui com</p>

\[ dE = \frac{1}{4\pi\varepsilon_0}\frac{\lambda\,dx'}{x'^2+z^2}. \]

<p>A componente horizontal de cada pedaço é cancelada pelo pedaço simétrico em
\(-x'\), de modo que só sobra a componente vertical, que traz um fator
\(\cos\alpha = z/\sqrt{x'^2+z^2}\):</p>

\[ E_z = \frac{\lambda}{4\pi\varepsilon_0}\int_{-L}^{L}
   \frac{z\,dx'}{\left(x'^2+z^2\right)^{3/2}}
   = \frac{\lambda}{4\pi\varepsilon_0}\,\frac{2L}{z\sqrt{L^2+z^2}}, \]

<p>usando a primitiva \(\int dx/(x^2+z^2)^{3/2} = x/z^2\sqrt{x^2+z^2}\).
Escrevendo em termos da carga total,</p>

\[ \boxed{\;E_z = \frac{1}{4\pi\varepsilon_0}\,
   \frac{Q}{z\sqrt{L^2+z^2}}.\;} \]

<p><strong>Os dois limites, que é onde se confere.</strong> Para \(z \gg L\), a
raiz vira \(z\) e sobra \(E = Q/4\pi\varepsilon_0z^2\): de longe, o bastão é uma
carga pontual, como tinha de ser. Para \(z \ll L\), a raiz vira \(L\) e sobra
\(E = \lambda/2\pi\varepsilon_0 z\): de perto, o bastão é um fio infinito, e
aparece o \(1/z\) característico. Um resultado que não passa nesses dois testes
está errado, e vale sempre fazê-los antes de entregar a prova.</p>
</div>
'''

S2 = r'''
<p>Calcular integrais vetoriais para toda distribuição é insustentável. A lei de
Gauss é o atalho, e ela vale sempre, mas só é <em>útil</em> quando há simetria.</p>

<p>Comece pelo fluxo. Para uma carga pontual na origem, o fluxo através de uma
esfera de raio \(r\) centrada nela é</p>

\[ \oint \vet{E}\cdot d\vet{a}
   = \frac{q}{4\pi\varepsilon_0 r^2}\left(4\pi r^2\right)
   = \frac{q}{\varepsilon_0}, \]

<p>e o raio sumiu. Não é coincidência: o campo cai com \(1/r^2\) e a área cresce
com \(r^2\). É o inverso do quadrado, e só ele, que faz isso funcionar.</p>

<p>Como o fluxo não depende do raio, ele também não depende da <em>forma</em> da
superfície, desde que ela envolva a carga; e pela superposição, somando sobre
todas as cargas,</p>

\[ \boxed{\;\oint_S \vet{E}\cdot d\vet{a}
   = \frac{Q_{\text{int}}}{\varepsilon_0}.\;} \]

<p>Cargas de fora contribuem com fluxo nulo: o que entra por um lado sai pelo
outro.</p>

<h3>A forma diferencial</h3>

<p>Aplicando o teorema da divergência ao lado esquerdo e escrevendo
\(Q_{\text{int}} = \int\rho\,d\tau\),</p>

\[ \int_V \left(\divg{\vet{E}}\right)d\tau
   = \int_V \frac{\rho}{\varepsilon_0}\,d\tau, \]

<p>e como o volume é arbitrário, os integrandos têm de ser iguais ponto a
ponto:</p>

\[ \boxed{\;\divg{\vet{E}} = \frac{\rho}{\varepsilon_0}.\;} \]

<p>Esta é a primeira equação de Maxwell. Repare no que ela diz: a carga é a
fonte do campo elétrico, no sentido técnico da palavra fonte, que o capítulo 1
definiu. Onde há carga positiva, as linhas de campo nascem; onde há negativa,
morrem.</p>

<div class="bloco fisica">
<span class="rotulo">A carga pontual, de novo</span>
<p>Para uma carga pontual, \(\vet{E} = \frac{q}{4\pi\varepsilon_0}
\frac{\vers{r}}{r^2}\) e o divergente é nulo em toda parte menos na origem.
A identidade da seção 5 do capítulo 1 resolve:</p>
<p>\[ \divg{\vet{E}} = \frac{q}{4\pi\varepsilon_0}\,4\pi\delta^3(\vet{r})
   = \frac{q\,\delta^3(\vet{r})}{\varepsilon_0} = \frac{\rho}{\varepsilon_0}, \]</p>
<p>com \(\rho = q\delta^3(\vet{r})\), que é a maneira correta de escrever a
densidade de uma carga pontual. Sem a delta, a forma diferencial da lei de Gauss
não valeria no único caso em que sabemos a resposta exata.</p>
</div>

<h3>Como usar: três passos e três simetrias</h3>

<p>O procedimento é sempre o mesmo. Primeiro, descobrir a direção de
\(\vet{E}\) por simetria; segundo, escolher uma superfície em que o módulo seja
constante e a direção, conhecida; terceiro, contar a carga interna. Só três
simetrias permitem isso:</p>

<div class="cartoes">
  <article class="cartao">
    <h3>Esférica</h3>
    <p>Superfície: esfera concêntrica.</p>
    \[ E\left(4\pi r^2\right) = \frac{Q_{\text{int}}}{\varepsilon_0} \]
    <p>Serve para cargas pontuais, esferas, cascas.</p>
  </article>
  <article class="cartao">
    <h3>Cilíndrica</h3>
    <p>Superfície: cilindro coaxial de comprimento \(\ell\).</p>
    \[ E\left(2\pi s\ell\right) = \frac{Q_{\text{int}}}{\varepsilon_0} \]
    <p>Serve para fios, cilindros, cabos.</p>
  </article>
  <article class="cartao">
    <h3>Plana</h3>
    <p>Superfície: caixa atravessando o plano, de área \(A\).</p>
    \[ E\left(2A\right) = \frac{Q_{\text{int}}}{\varepsilon_0} \]
    <p>Serve para planos, placas, camadas.</p>
  </article>
</div>

<div class="destaque">
<p><strong>Exemplo trabalhado: a esfera que não é uniforme.</strong> Uma esfera
de raio \(R\) tem densidade de carga que cresce com o raio,
\(\rho(r) = \rho_0\,r/R\). Ache o campo dentro e fora, e a carga total.</p>

<p><strong>A carga total</strong>, integrando com o jacobiano correto:</p>

\[ Q = \int_0^{R}\rho_0\frac{r}{R}\left(4\pi r^2\,dr\right)
     = \frac{4\pi\rho_0}{R}\cdot\frac{R^4}{4} = \pi\rho_0R^3. \]

<p><strong>Dentro</strong> (\(r \lt R\)), a carga interna à esfera gaussiana de
raio \(r\) é \(\pi\rho_0r^4/R\), e</p>

\[ E\left(4\pi r^2\right) = \frac{\pi\rho_0 r^4}{\varepsilon_0 R}
   \;\Longrightarrow\;
   E = \frac{\rho_0 r^2}{4\varepsilon_0 R}. \]

<p><strong>Fora</strong> (\(r \gt R\)), a carga interna é toda a carga, e</p>

\[ E = \frac{Q}{4\pi\varepsilon_0 r^2}
     = \frac{\rho_0R^3}{4\varepsilon_0 r^2}. \]

<p>Os dois resultados coincidem em \(r = R\), valendo \(\rho_0R/4\varepsilon_0\):
o campo é contínuo ali, como tem de ser, porque não há carga <em>superficial</em>
na fronteira.</p>

<p>Compare com a esfera uniforme, em que o campo interno cresce com \(r\). Aqui
ele cresce com \(r^2\), porque há menos carga perto do centro. E repare que o
campo externo é o mesmo de uma carga pontual \(Q\) na origem, seja qual for a
distribuição radial: de fora, não se enxerga nada além do total.</p>
</div>
'''

S3 = r'''
<p>O campo eletrostático tem uma segunda propriedade, tão importante quanto a
primeira, e que não decorre dela: a sua circulação é nula.</p>

\[ \oint \vet{E}\cdot d\vet{\ell} = 0
   \qquad\Longleftrightarrow\qquad
   \boxed{\;\rot{\vet{E}} = 0.\;} \]

<p>Para ver isso no caso de uma carga pontual, calcule a integral de linha entre
dois pontos. Com \(\vet{E}\) radial e \(d\vet{\ell}\) tendo componente radial
\(dr\),</p>

\[ \int_a^b \vet{E}\cdot d\vet{\ell}
   = \frac{q}{4\pi\varepsilon_0}\int_{r_a}^{r_b}\frac{dr}{r^2}
   = \frac{q}{4\pi\varepsilon_0}\left(\frac{1}{r_a}-\frac{1}{r_b}\right), \]

<p>que só depende das pontas. Pela superposição, o mesmo vale para qualquer
conjunto de cargas paradas. Fechando o caminho, \(r_a = r_b\) e a integral
zera.</p>

<h3>O potencial</h3>

<p>Campo com rotacional nulo é gradiente de alguma coisa, como o capítulo 1
estabeleceu. Define-se</p>

\[ V(\vet{r}) = -\int_{\mathcal{O}}^{\vet{r}} \vet{E}\cdot d\vet{\ell},
   \qquad \vet{E} = -\nabla V, \]

<p>com \(\mathcal{O}\) um ponto de referência, em geral o infinito. O sinal
negativo é convenção, escolhida para que o potencial decresça no sentido do
campo e para que uma carga positiva "caia" para potenciais menores.</p>

<p>Três observações que evitam confusão:</p>

<figure class="figura-exemplo" style="max-width:44rem">
  <img src="assets/img/cap02_equipotenciais.svg" alt="Linhas de campo e equipotenciais de duas cargas">
  <figcaption>As duas famílias de curvas se cruzam sempre em ângulo reto, e a
  razão é a definição: \(\vet{E} = -\nabla V\), e gradiente é perpendicular à
  superfície de nível. Repare no plano médio do par de cargas iguais, onde o
  campo é horizontal e a equipotencial, vertical.</figcaption>
</figure>

<ul>
<li>O potencial é um <strong>escalar</strong>. Somar potenciais de várias cargas
é somar números, não vetores, e é por isso que calcular \(V\) e depois derivar é
quase sempre mais fácil do que calcular \(\vet{E}\) diretamente.</li>
<li>Só diferenças de potencial têm significado. Escolher a referência é escolher
onde pôr o zero, e nenhuma grandeza física depende dessa escolha.</li>
<li>Potencial não é energia potencial. A energia de uma carga \(q\) num
potencial \(V\) é \(U = qV\); o potencial é energia <em>por unidade de
carga</em>, e se mede em volts.</li>
</ul>

<p>Para distribuições,</p>

\[ V(\vet{r}) = \frac{1}{4\pi\varepsilon_0}\int\frac{\rho(\vet{r}')}{\imath}
   \,d\tau', \]

<p>com \(\imath = |\vet{r}-\vet{r}'|\), e a referência no infinito.</p>

<h3>Poisson e Laplace</h3>

<p>Juntando \(\vet{E} = -\nabla V\) com \(\divg{\vet{E}} = \rho/\varepsilon_0\),</p>

\[ \boxed{\;\nabla^2 V = -\frac{\rho}{\varepsilon_0}\;}
   \qquad\text{(Poisson)}, \]

<p>que nas regiões vazias de carga vira</p>

\[ \nabla^2 V = 0 \qquad\text{(Laplace)}. \]

<p>Toda a eletrostática está contida nessas duas linhas mais as condições de
contorno. O capítulo 3 é inteiramente dedicado a resolvê-las quando a carga não
é dada de antemão.</p>

<div class="destaque">
<p><strong>Exemplo trabalhado: o anel, pelo potencial.</strong> Um anel de raio
\(a\) tem carga \(Q\) uniformemente distribuída. Ache o potencial e o campo no
eixo, a uma altura \(z\).</p>

<p>Todo ponto do anel está à mesma distância \(\imath = \sqrt{a^2+z^2}\) do
ponto do eixo, de modo que a integral é trivial:</p>

\[ V(z) = \frac{1}{4\pi\varepsilon_0}\frac{1}{\sqrt{a^2+z^2}}
   \int dq = \frac{Q}{4\pi\varepsilon_0\sqrt{a^2+z^2}}. \]

<p>O campo no eixo sai derivando, e aqui é preciso cuidado: a derivada só dá a
componente \(z\), porque só temos \(V\) sobre o eixo. Felizmente, por simetria,
é a única componente que existe ali:</p>

\[ E_z = -\der{V}{z}
   = \frac{Q}{4\pi\varepsilon_0}\,\frac{z}{\left(a^2+z^2\right)^{3/2}}. \]

<p><strong>Confira.</strong> Em \(z = 0\), no centro do anel, o campo é nulo por
simetria, e a fórmula concorda. Para \(z \gg a\), sobra
\(Q/4\pi\varepsilon_0z^2\), a carga pontual. E o campo tem um máximo em
\(z = a/\sqrt{2}\), que se acha derivando outra vez: é a altura em que a
contribuição vertical de cada pedaço é mais eficiente.</p>

<p>Compare o trabalho: pelo potencial, uma integral de uma função escalar
constante; diretamente pelo campo, uma integral vetorial com cancelamento de
componentes. Sempre que o ponto de observação tiver simetria, vá pelo
potencial.</p>
</div>
'''

S4 = r'''
<p>Montar uma distribuição de cargas custa trabalho, porque é preciso vencer a
repulsão entre as que já estão lá. Esse trabalho fica guardado, e a pergunta é
onde.</p>

<p>Para trazer uma carga \(q\) do infinito até um ponto onde o potencial das
outras vale \(V\), o trabalho é</p>

\[ W = qV. \]

<p>Montando uma coleção de cargas pontuais uma a uma e somando, cada par aparece
duas vezes, de onde</p>

\[ W = \frac{1}{2}\sum_i q_iV(\vet{r}_i)
   \;\longrightarrow\;
   W = \frac{1}{2}\int \rho V\,d\tau. \]

<p>O fator \(1/2\) é o preço de contar cada par duas vezes, e esquecê-lo é o
erro mais comum da seção.</p>

<h3>A energia mora no campo</h3>

<p>Troque \(\rho\) por \(\varepsilon_0\divg{\vet{E}}\) e integre por partes, como
o capítulo 1 ensinou:</p>

\[ W = \frac{\varepsilon_0}{2}\int V\left(\divg{\vet{E}}\right)d\tau
   = \frac{\varepsilon_0}{2}\left[-\int \vet{E}\cdot\left(\nabla V\right)d\tau
   + \oint V\vet{E}\cdot d\vet{a}\right]. \]

<p>Com \(\nabla V = -\vet{E}\) e levando a superfície ao infinito, onde
\(V\vet{E}\) cai como \(1/r^3\) enquanto a área cresce como \(r^2\), o termo de
fronteira morre e sobra</p>

\[ \boxed{\;W = \frac{\varepsilon_0}{2}\int E^2\,d\tau,
   \qquad u_E = \frac{\varepsilon_0E^2}{2}.\;} \]

<p>As duas expressões dão o mesmo número, mas contam histórias diferentes: a
primeira diz que a energia está nas cargas, a segunda, que está no campo. A
segunda é a certa, e o capítulo 8 vai mostrar por quê, quando a energia precisar
viajar.</p>

<div class="destaque">
<p><strong>Exemplo trabalhado: a energia de uma esfera carregada.</strong> Uma
esfera isolante de raio \(R\) tem carga \(Q\) uniformemente distribuída no
volume. Quanta energia custa montá-la?</p>

<p>Pela lei de Gauss, o campo é</p>

\[ E = \frac{Q r}{4\pi\varepsilon_0R^3}\;(r \lt R),
   \qquad E = \frac{Q}{4\pi\varepsilon_0r^2}\;(r \gt R). \]

<p>Integrando a densidade de energia nas duas regiões, com
\(d\tau = 4\pi r^2dr\):</p>

\[ W_{\text{dentro}} = \frac{\varepsilon_0}{2}
   \int_0^{R}\left(\frac{Qr}{4\pi\varepsilon_0R^3}\right)^2 4\pi r^2dr
   = \frac{Q^2}{8\pi\varepsilon_0R^6}\cdot\frac{R^5}{5}
   = \frac{Q^2}{40\pi\varepsilon_0R}, \]

\[ W_{\text{fora}} = \frac{\varepsilon_0}{2}
   \int_R^{\infty}\left(\frac{Q}{4\pi\varepsilon_0r^2}\right)^2 4\pi r^2dr
   = \frac{Q^2}{8\pi\varepsilon_0R}. \]

<p>Somando, com \(1/40 + 5/40 = 6/40 = 3/20\),</p>

\[ \boxed{\;W = \frac{3}{5}\,\frac{Q^2}{4\pi\varepsilon_0 R}.\;} \]

<p><strong>Números.</strong> Para \(Q = 1{,}0\ \mu\mathrm{C}\) e
\(R = 5{,}0\ \mathrm{cm}\), isso dá \(W = 0{,}6\times8{,}99\times10^{9}\times
10^{-12}/0{,}05 = 0{,}108\ \mathrm{J}\). Pouco mais de um décimo de joule, o que
já é bastante: é o que custa separar um microcoulomb, e é por isso que
eletrostática de bancada trabalha com nanocoulombs.</p>

<p><strong>E a carga pontual?</strong> Fazendo \(R \to 0\) a energia diverge.
Uma carga pontual tem energia de campo infinita, e isso não é um defeito da
conta: é um problema de verdade, que a eletrodinâmica clássica não resolve e a
quântica só contorna, com renormalização. Vale saber que ele está lá.</p>
</div>
'''

S5 = r'''
<p>Condutor é um material com cargas livres para se mover. Essa única hipótese,
levada às últimas consequências em equilíbrio, produz cinco resultados que
valem para qualquer condutor, de qualquer forma.</p>

<div class="cartoes">
  <article class="cartao">
    <h3>1. \(\vet{E} = 0\) dentro</h3>
    <p>Se houvesse campo, as cargas livres se moveriam, e não haveria
    equilíbrio. O campo externo é cancelado pelo rearranjo da carga.</p>
  </article>
  <article class="cartao">
    <h3>2. \(\rho = 0\) dentro</h3>
    <p>Consequência de \(\divg{\vet{E}} = \rho/\varepsilon_0\) com
    \(\vet{E}=0\): a carga toda vai para a superfície.</p>
  </article>
  <article class="cartao">
    <h3>3. \(V\) constante</h3>
    <p>Com \(\vet{E} = -\nabla V = 0\), o potencial não varia: o condutor
    inteiro é uma equipotencial.</p>
  </article>
  <article class="cartao">
    <h3>4. \(\vet{E}\) normal fora</h3>
    <p>Componente tangencial moveria carga ao longo da superfície. Logo o campo
    sai perpendicular.</p>
  </article>
  <article class="cartao">
    <h3>5. \(E = \sigma/\varepsilon_0\)</h3>
    <p>Da condição de contorno, com campo nulo de um lado: o campo logo fora
    vale a densidade superficial dividida por \(\varepsilon_0\).</p>
  </article>
</div>

<p>O quinto resultado merece uma observação, porque colide com o do plano
infinito, que dá \(\sigma/2\varepsilon_0\). Não há contradição: no plano
isolado, metade do campo vai para cada lado; na superfície do condutor, todo o
campo vai para fora, porque dentro ele é nulo. A mesma carga superficial, duas
situações diferentes.</p>

<h3>Pressão eletrostática</h3>

<p>A superfície de um condutor carregado é puxada para fora. Cada pedaço de
carga \(\sigma\,da\) sente o campo das <em>outras</em> cargas, que é a média
entre o campo de dentro (zero) e o de fora (\(\sigma/\varepsilon_0\)), ou seja
\(\sigma/2\varepsilon_0\). Logo</p>

\[ P = \frac{\sigma^2}{2\varepsilon_0} = \frac{\varepsilon_0E^2}{2} = u_E. \]

<p>A pressão é numericamente igual à densidade de energia do campo logo fora, e
isso não é coincidência: é o começo do tensor de tensões de Maxwell, do capítulo
8.</p>

<div class="destaque">
<p><strong>Exemplo trabalhado: a carga induzida numa cavidade.</strong> Um bloco
condutor neutro tem uma cavidade esférica no interior, e dentro da cavidade,
sem tocar as paredes, está uma carga pontual \(q = +3{,}0\ \mathrm{nC}\). O que
há na parede da cavidade, na superfície externa do bloco, e qual o campo fora?</p>

<p><strong>Na parede da cavidade.</strong> Tome uma superfície gaussiana
inteiramente dentro do metal, envolvendo a cavidade. Como \(\vet{E} = 0\) em
todo ponto dela, o fluxo é nulo, e portanto a carga interna é nula. Já que
\(q = +3{,}0\) nC está lá dentro, a parede tem de ter
\(-3{,}0\ \mathrm{nC}\).</p>

<p><strong>Na superfície externa.</strong> O bloco é neutro no total; se
\(-3{,}0\) nC foram para a parede da cavidade, sobram \(+3{,}0\) nC, que vão
para a superfície externa, porque dentro do metal não pode haver carga.</p>

<p><strong>O campo fora.</strong> Aqui está o ponto bonito: a carga externa se
distribui como se a cavidade e a carga de dentro não existissem. Se o bloco for
esférico de raio \(b\), o campo fora é</p>

\[ E = \frac{q}{4\pi\varepsilon_0 r^2}, \]

<p>exatamente como o de uma carga pontual no centro, <em>mesmo que \(q\) esteja
descentrada dentro da cavidade</em>. O metal apaga toda a informação sobre onde
a carga está. Essa é a blindagem eletrostática, e é por isso que o interior de
um carro é um lugar razoável para estar durante uma tempestade.</p>

<p><strong>E o contrário?</strong> Uma carga <em>fora</em> do bloco não produz
campo nenhum dentro da cavidade, pelo mesmo mecanismo. A gaiola de Faraday
funciona nos dois sentidos, mas por razões ligeiramente diferentes: a de fora
para dentro é um resultado de unicidade do capítulo 3.</p>
</div>
'''

S6 = r'''
<p>Dois programas, no padrão dos outros capítulos. Eles atacam justamente os dois
pontos em que a conta no papel é mais trabalhosa: a integral vetorial de uma
distribuição qualquer e a verificação da lei de Gauss em superfícies que não têm
simetria.</p>

<div class="cartoes">
  <article class="cartao">
    <h3><a href="codigo/campo_distribuicao.py">campo_distribuicao.py</a></h3>
    <p>Integra numericamente \(\vet{E}\) e \(V\) de uma distribuição discretizada
    em pedaços, para fio, anel e disco, e compara com as fórmulas fechadas.</p>
    <p><strong>Confira assim:</strong> o erro tem de cair como o quadrado do
    número de pedaços; os limites de longe (carga pontual) e de perto (fio
    infinito, plano infinito) têm de aparecer sozinhos; e \(-dV/dz\) numérico
    tem de reproduzir \(E_z\).</p>
  </article>
  <article class="cartao">
    <h3><a href="codigo/gauss_numerico.py">gauss_numerico.py</a></h3>
    <p>Calcula o fluxo de uma carga pontual por superfícies fechadas de formas
    diferentes, com a carga dentro e fora, inclusive superfícies deformadas sem
    simetria nenhuma.</p>
    <p><strong>Confira assim:</strong> o fluxo tem de dar \(q/\varepsilon_0\)
    sempre que a carga estiver dentro, seja qual for a forma, e exatamente zero
    quando estiver fora.</p>
  </article>
</div>
'''

SECOES = [
    ('Coulomb, campo e superposição', S1),
    ('A lei de Gauss', S2),
    ('Potencial, Poisson e Laplace', S3),
    ('Trabalho e energia', S4),
    ('Condutores', S5),
    ('No Spyder', S6),
]

SECOES.append(('Exercícios propostos', exercicios.bloco(LISTA)))


def main():
    titulos = [t for t, _ in SECOES]
    escreve('cap02.html', secoes_html(SECOES), secoes=titulos)


if __name__ == '__main__':
    main()
