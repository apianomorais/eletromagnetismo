# -*- coding: utf-8 -*-
"""Capítulo 10: potenciais e campos.

O texto é escrito do zero. O Griffiths entra como referência de ordem e de
numeração de capítulo, nunca como fonte de frases, enunciados ou figuras:
os exemplos aqui são de nossa autoria, com contextos e números próprios.
"""
from molde import escreve, secoes_html
import exercicios
from lista_cap10 import LISTA

S1 = r'''
<p>As quatro equações de Maxwell são seis funções incógnitas, as componentes de
\(\vet{E}\) e \(\vet{B}\), amarradas por oito equações escalares. É mais do que
o necessário, e há um jeito melhor de organizar: trocar os campos por
potenciais.</p>

<p>Duas das quatro equações são homogêneas, isto é, não têm fonte, e são elas
que permitem a troca. De \(\divg{\vet{B}} = 0\) e da identidade do capítulo 1,</p>

\[ \vet{B} = \rot{\vet{A}}, \]

<p>sempre, inclusive com tudo variando no tempo. Levando isso à lei de
Faraday,</p>

\[ \rot{\vet{E}} = -\pder{}{t}\left(\rot{\vet{A}}\right)
   \;\Longrightarrow\;
   \rot{\left(\vet{E} + \pder{\vet{A}}{t}\right)} = 0, \]

<p>e o que tem rotacional nulo é gradiente de alguma coisa:</p>

\[ \boxed{\;\vet{E} = -\nabla V - \pder{\vet{A}}{t}.\;} \]

<p>Repare na novidade em relação à eletrostática: agora o campo elétrico tem
<em>duas</em> origens. Uma é a carga, pelo gradiente do potencial escalar; a
outra é a variação do potencial vetor, isto é, do campo magnético. É a lei de
Faraday escrita em potenciais.</p>

<p>Levando as duas definições às equações com fonte, sobram duas equações
acopladas:</p>

\[ \nabla^2 V + \pder{}{t}\left(\divg{\vet{A}}\right)
   = -\frac{\rho}{\varepsilon_0}, \]

\[ \nabla^2\vet{A} - \mu_0\varepsilon_0\frac{\partial^2\vet{A}}{\partial t^2}
   - \nabla\left(\divg{\vet{A}}
   + \mu_0\varepsilon_0\pder{V}{t}\right) = -\mu_0\vet{J}. \]

<p>São feias, e estão acopladas: \(V\) aparece na equação de \(\vet{A}\) e
vice-versa. A próxima seção mostra que essa feiura é removível, e de graça.</p>
'''

S2 = r'''
<p>Os potenciais não são únicos. Troque</p>

\[ \vet{A}' = \vet{A} + \nabla\lambda,
   \qquad V' = V - \pder{\lambda}{t}, \]

<p>com \(\lambda(\vet{r},t)\) uma função qualquer. Os campos não mudam:</p>

\[ \rot{\vet{A}'} = \rot{\vet{A}} + \rot{\left(\nabla\lambda\right)}
   = \vet{B}, \]

\[ -\nabla V' - \pder{\vet{A}'}{t}
   = -\nabla V + \nabla\pder{\lambda}{t}
     - \pder{\vet{A}}{t} - \pder{}{t}\nabla\lambda = \vet{E}. \]

<p>Essa liberdade chama-se <strong>transformação de calibre</strong>, e ela é
usada como ferramenta: escolhe-se o \(\lambda\) que simplifica o problema.</p>

<div class="cartoes">
  <article class="cartao">
    <h3>Calibre de Coulomb</h3>
    \[ \divg{\vet{A}} = 0 \]
    <p>A equação de \(V\) vira a de Poisson, e \(V\) é o potencial
    instantâneo da carga, como na eletrostática.</p>
    <p>Bom para problemas quase estáticos; ruim para radiação.</p>
  </article>
  <article class="cartao">
    <h3>Calibre de Lorenz</h3>
    \[ \divg{\vet{A}} = -\mu_0\varepsilon_0\pder{V}{t} \]
    <p>As duas equações desacoplam e viram equações de onda idênticas, uma
    para \(V\) e outra para \(\vet{A}\).</p>
    <p>É o calibre deste capítulo e de toda a eletrodinâmica relativística.</p>
  </article>
</div>

<div class="bloco alerta">
<span class="rotulo">Lorenz, e não Lorentz</span>
<p>A condição de calibre é de <strong>Ludvig Lorenz</strong>, dinamarquês, de
1867. A força \(q(\vet{E}+\vet{v}\cruz\vet{B})\) e as transformações da
relatividade são de <strong>Hendrik Lorentz</strong>, holandês, trinta anos
depois. A troca dos dois nomes é tão comum que boa parte da literatura escreve
"calibre de Lorentz" por engano.</p>
</div>

<p>No calibre de Lorenz, as duas equações acopladas da seção anterior viram</p>

\[ \boxed{\;\Box^2 V = -\frac{\rho}{\varepsilon_0},
   \qquad \Box^2\vet{A} = -\mu_0\vet{J},\;} \]

<p>com o operador d'alembertiano
\(\Box^2 \equiv \nabla^2 - \mu_0\varepsilon_0\,\partial^2/\partial t^2\).</p>

<p>São quatro equações de onda independentes, com a mesma estrutura, cada uma
com a sua fonte. Toda a eletrodinâmica está aí, e a simetria entre \(V\) com
\(\rho\) e \(\vet{A}\) com \(\vet{J}\) é a primeira pista de que, na
relatividade, os quatro formam um único objeto.</p>

<p><strong>Um ponto que convém saber:</strong> sempre existe um \(\lambda\) que
leva ao calibre de Lorenz. Partindo de potenciais quaisquer, basta resolver
\(\Box^2\lambda = -\left(\divg{\vet{A}}+\mu_0\varepsilon_0\partial V/\partial
t\right)\), que é de novo uma equação de onda com fonte, e sempre tem
solução.</p>
'''

S3 = r'''
<p>A solução da equação de onda com fonte, na eletrostática, era a integral de
Coulomb. Com o tempo entrando, o que muda é <em>quando</em> a fonte é
avaliada:</p>

\[ \boxed{\;V(\vet{r},t) = \frac{1}{4\pi\varepsilon_0}
   \int\frac{\rho(\vet{r}',t_r)}{\imath}\,d\tau',
   \qquad
   \vet{A}(\vet{r},t) = \frac{\mu_0}{4\pi}
   \int\frac{\vet{J}(\vet{r}',t_r)}{\imath}\,d\tau',\;} \]

<p>com o <strong>tempo retardado</strong></p>

\[ t_r = t - \frac{\imath}{c}. \]

<p>A leitura é física e bonita: o potencial aqui e agora depende do que a fonte
estava fazendo há \(\imath/c\) segundos, que é o tempo que a notícia leva para
chegar. Nada se propaga instantaneamente.</p>

<div class="bloco alerta">
<span class="rotulo">A tentação que não funciona</span>
<p>Se os potenciais retardados são as fórmulas da eletrostática com \(t_r\) no
lugar de \(t\), seria natural supor que vale o mesmo para os campos, isto é,
que \(\vet{E}\) é a integral de Coulomb avaliada no tempo retardado.</p>
<p><strong>É falso.</strong> A razão é que \(\vet{E} = -\nabla V - \partial
\vet{A}/\partial t\), e o gradiente age também sobre o \(t_r\), que depende da
posição. Derivar \(\rho(\vet{r}',t_r)/\imath\) em relação a \(\vet{r}\) produz
termos extras, com \(\dot\rho\) e \(\dot{\vet{J}}\), que não existem na
eletrostática e que são justamente os termos de radiação.</p>
<p>As fórmulas corretas, chamadas de equações de Jefimenko, têm esses termos a
mais. Guarde a moral: <em>potenciais</em> se retardam de graça, <em>campos</em>
não.</p>
</div>

<h3>Por que a solução é essa</h3>

<p>Não vamos deduzir linha a linha, mas vale o argumento. A equação de onda com
fonte pontual e instantânea tem como solução uma casca esférica que se afasta à
velocidade \(c\), e isso é a função de Green retardada. Qualquer fonte é uma
superposição de pontos e instantes, e a integral acima é a soma dessas
contribuições, cada uma com o seu atraso.</p>

<p>Matematicamente existe também a solução <strong>avançada</strong>, com
\(t_a = t + \imath/c\), que descreve ondas convergindo do futuro. Ela satisfaz
as equações igualmente bem e é descartada por causalidade, não por
matemática. Essa assimetria entre passado e futuro, que não está nas equações,
é um dos problemas mais antigos e menos resolvidos da física.</p>
'''

S4 = r'''
<p>Para uma carga pontual em movimento arbitrário, a integral dos potenciais
retardados tem uma sutileza que vale examinar, porque ela produz um fator
inesperado.</p>

<p>A carga está em \(\vet{w}(t)\), e no instante retardado estava em
\(\vet{w}(t_r)\), definido implicitamente por</p>

\[ \left|\vet{r}-\vet{w}(t_r)\right| = c\,(t-t_r). \]

<p>Essa equação tem <em>uma</em> solução só, para \(v \lt c\): a carga não pode
aparecer duas vezes no cone de luz do passado. A demonstração é simples e vale
pensar nela: se houvesse duas, a carga teria de ter viajado entre elas mais
rápido que a luz.</p>

<h3>O fator que ninguém espera</h3>

<p>Ao integrar sobre a distribuição de uma carga que se move, o volume
"efetivo" que contribui não é o volume próprio dela. Como a informação de cada
pedaço sai em instantes diferentes, uma carga que se aproxima entrega mais
contribuição por unidade de volume, e uma que se afasta entrega menos. O fator
de correção é</p>

\[ \frac{1}{1 - \vers{\imath}\cdot\vet{v}/c}, \]

<p>e ele <em>não</em> é um efeito relativístico de contração: aparece mesmo na
conta clássica, e vem apenas da geometria do atraso. Com ele,</p>

\[ \boxed{\;V(\vet{r},t) = \frac{1}{4\pi\varepsilon_0}
   \frac{qc}{\imath c - \vet{\imath}\cdot\vet{v}},
   \qquad
   \vet{A}(\vet{r},t) = \frac{\vet{v}}{c^2}V(\vet{r},t),\;} \]

<p>que são os <strong>potenciais de Liénard-Wiechert</strong>, com todas as
quantidades do lado direito avaliadas no tempo retardado.</p>

<div class="destaque">
<p><strong>Exemplo trabalhado: a carga que passa reto.</strong> Uma carga \(q\)
move-se com velocidade constante \(\vet{v} = v\vers{x}\), passando pela origem
em \(t=0\). Qual o campo elétrico num ponto qualquer?</p>

<p>Resolvendo a condição de retardo e levando aos potenciais, a álgebra (que é
longa, e cujo resultado vale guardar) dá</p>

\[ \vet{E}(\vet{r},t) = \frac{q}{4\pi\varepsilon_0}
   \frac{1-v^2/c^2}
        {\left(1-\frac{v^2}{c^2}\sen^2\theta\right)^{3/2}}
   \frac{\vers{R}}{R^2}, \]

<p>com \(\vet{R}\) o vetor que liga a posição <em>atual</em> da carga ao ponto
de observação, e \(\theta\) o ângulo entre \(\vet{R}\) e a velocidade.</p>

<p><strong>Três leituras.</strong></p>

<p>Primeira: o campo aponta para a posição <em>presente</em> da carga, e não
para onde ela estava quando a informação saiu. Isso parece violar causalidade e
não viola: a carga está em movimento uniforme, e o campo "extrapola" o que ela
vinha fazendo. Se ela for freada, a notícia da freada leva \(R/c\) para
chegar, e só a partir daí o campo deixa de apontar para a posição extrapolada.
É dessa discrepância que nasce a radiação do capítulo 11.</p>

<p>Segunda: o campo não é mais isotrópico. Para \(\theta = 0\), na direção do
movimento, ele é <em>reduzido</em> pelo fator \(1-v^2/c^2\); para
\(\theta = 90^\circ\), perpendicular, é <em>aumentado</em> por
\(1/\sqrt{1-v^2/c^2}\). O campo de uma carga rápida se achata num disco
perpendicular ao movimento.</p>

<p><strong>Números.</strong> A \(v = 0{,}9c\), o campo perpendicular é
\(1/\sqrt{1-0{,}81} = 2{,}29\) vezes o de Coulomb, e o longitudinal é
\(0{,}19\) vezes. Uma diferença de doze vezes entre as duas direções.</p>

<p>Terceira: com \(v \to 0\) tudo volta a Coulomb, como tinha de voltar.</p>
</div>
'''

S5 = r'''
<p>Derivando os potenciais de Liénard-Wiechert, com o cuidado de tratar a
dependência implícita de \(t_r\) com a posição, chega-se ao campo de uma carga
pontual em movimento arbitrário. O resultado se organiza em duas partes:</p>

\[ \vet{E}(\vet{r},t) = \frac{q}{4\pi\varepsilon_0}
   \frac{\imath}{\left(\vet{\imath}\cdot\vet{u}\right)^3}
   \left[\underbrace{\left(c^2-v^2\right)\vet{u}}_{\text{campo de velocidade}}
   + \underbrace{\vet{\imath}\cruz\left(\vet{u}\cruz\vet{a}\right)}
     _{\text{campo de aceleração}}\right], \]

<p>com \(\vet{u} = c\,\vers{\imath}-\vet{v}\), e</p>

\[ \vet{B}(\vet{r},t) = \frac{1}{c}\,\vers{\imath}\cruz\vet{E}(\vet{r},t). \]

<p>Vale a pena olhar o que distingue as duas parcelas.</p>

<div class="cartoes">
  <article class="cartao">
    <h3>Campo de velocidade</h3>
    <p>Não depende da aceleração, cai com \(1/\imath^2\) e é o que sobra numa
    carga em movimento uniforme.</p>
    <p>Energia fica <em>presa</em> à carga: ela acompanha o movimento e não vai
    embora.</p>
  </article>
  <article class="cartao">
    <h3>Campo de aceleração</h3>
    <p>Proporcional a \(\vet{a}\), cai com \(1/\imath\) apenas.</p>
    <p>É este que sobrevive a grandes distâncias e que leva energia embora para
    sempre: é a <strong>radiação</strong>.</p>
  </article>
</div>

<p>A diferença entre \(1/\imath^2\) e \(1/\imath\) é o que decide tudo. O fluxo
de energia vai com \(E^2\), e a área de uma esfera cresce com \(\imath^2\); logo
a potência que atravessa uma esfera grande vai com \(E^2\imath^2\). Para o campo
de velocidade isso cai como \(1/\imath^2\) e tende a zero, mas para o campo de
aceleração ela é <strong>constante</strong>: a energia escapa de verdade, até o
infinito.</p>

<p>E o campo magnético é sempre perpendicular ao elétrico e à linha de visada
retardada, com \(B = E/c\), exatamente como na onda plana do capítulo 9.</p>

<div class="bloco fisica">
<span class="rotulo">A força de uma carga sobre outra não obedece à terceira lei</span>
<p>Com os campos acima, calcule a força que uma carga em movimento faz sobre
outra, e vice-versa: elas não são iguais e opostas. A terceira lei de Newton
falha na eletrodinâmica, e isso não é um defeito da teoria.</p>
<p>O que se conserva é o momento <em>total</em>, somando o das cargas com o
momento guardado no campo eletromagnético, que o capítulo 8 contabiliza. O
campo é um participante, e não um intermediário passivo.</p>
</div>
'''

S6 = r'''
<div class="cartoes">
  <article class="cartao">
    <h3><a href="codigo/lienard_wiechert.py">lienard_wiechert.py</a></h3>
    <p>Resolve a condição de tempo retardado por bisseção, monta os potenciais e
    os campos de uma carga em movimento qualquer, e compara com os resultados
    fechados conhecidos.</p>
    <p><strong>Confira assim:</strong> em movimento uniforme, o campo tem de
    reproduzir a fórmula do achatamento, e apontar para a posição
    <em>presente</em> da carga; com \(v \to 0\) tem de virar Coulomb; e
    \(\vet{B}\) tem de ser perpendicular a \(\vet{E}\) com \(B = E/c\).</p>
  </article>
  <article class="cartao">
    <h3><a href="codigo/calibre.py">calibre.py</a></h3>
    <p>Aplica uma transformação de calibre arbitrária a potenciais dados e
    verifica, numericamente, que os campos não mudam.</p>
    <p><strong>Confira assim:</strong> \(\vet{E}\) e \(\vet{B}\) calculados a
    partir de \((V,\vet{A})\) e de \((V',\vet{A}')\) têm de coincidir até o erro
    de truncamento; e a condição de Lorenz, que valia antes, não vale mais
    depois de uma transformação qualquer.</p>
  </article>
</div>
'''

SECOES = [
    ('Trocando os campos pelos potenciais', S1),
    ('Calibre: a liberdade que se usa como ferramenta', S2),
    ('Potenciais retardados', S3),
    ('Liénard-Wiechert', S4),
    ('Os campos de uma carga em movimento', S5),
    ('No Spyder', S6),
]

SECOES.append(('Exercícios propostos', exercicios.bloco(LISTA)))


def main():
    titulos = [t for t, _ in SECOES]
    escreve('cap10.html', secoes_html(SECOES), secoes=titulos)


if __name__ == '__main__':
    main()
