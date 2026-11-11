# -*- coding: utf-8 -*-
"""Capítulo 12: a eletrodinâmica de Weber.

Capítulo fora do Griffiths, pedido pelo professor. Texto escrito do zero, com
as contas conferidas em codigo/weber.py.
"""
from molde import escreve, secoes_html
import exercicios
from lista_cap12 import LISTA

S1 = r'''
<p>O curso inteiro foi construído sobre uma ideia: existe campo. A carga cria
alguma coisa no espaço em volta, essa coisa se propaga com velocidade finita, e
é ela que age sobre a outra carga. Parece inevitável depois de onze capítulos,
mas não era nada óbvio em 1850, e a maior parte dos físicos do continente
europeu achava essa ideia uma invenção desnecessária.</p>

<p>A alternativa tinha prestígio. A gravitação de Newton funcionava assim: uma
força entre dois corpos, dependendo só da distância, sem nada no meio e sem
atraso. Por que a eletricidade seria diferente? Entre 1820 e 1870, a escola
continental, com
<a href="https://pt.wikipedia.org/wiki/Andr%C3%A9-Marie_Amp%C3%A8re">Ampère</a>,
Neumann e
<a href="https://pt.wikipedia.org/wiki/Wilhelm_Eduard_Weber">Wilhelm Weber</a>,
construiu uma eletrodinâmica completa sem campo nenhum, e ela funcionava.</p>

<p>Este capítulo é sobre essa teoria. Não por curiosidade de museu: ela é o
melhor instrumento que conheço para mostrar <em>por que</em> o campo venceu. A
diferença entre as duas não é de gosto nem de elegância, é de um fato
mensurável, e o fato tem nome.</p>

<div class="bloco def">
<span class="rotulo">Aviso de enquadramento</span>
<p>A eletrodinâmica de Weber é uma teoria superada, e este capítulo a trata
como tal. Há hoje um grupo pequeno de pesquisadores que a defende como
alternativa viva à eletrodinâmica de Maxwell; a literatura deles é
historicamente valiosa e as objeções físicas da seção 4 continuam de pé. O
interesse aqui é pedagógico e histórico, e a conclusão do capítulo não está em
disputa.</p>
</div>
'''

S2 = r'''
<p>Weber publicou a sua lei de força em 1846, e ela é uma única expressão,
válida para duas cargas pontuais quaisquer:</p>

\[ \boxed{\;F = \frac{1}{4\pi\varepsilon_0}\frac{q_1q_2}{r^2}
   \left[1 - \frac{\dot r^2}{2c^2} + \frac{r\ddot r}{c^2}\right],\;} \]

<p>dirigida ao longo da linha que une as duas cargas. Aqui \(r\) é a distância
entre elas, \(\dot r\) é a taxa com que essa distância muda, e \(\ddot r\) a
derivada seguinte. Repare no que <em>não</em> aparece: a velocidade de cada
carga separadamente, a direção do movimento, o tempo retardado, e qualquer
referência a um meio ou a um referencial privilegiado. Só a distância entre as
duas e as suas duas primeiras derivadas.</p>

<p>Três leituras organizam a expressão.</p>

<p><strong>O limite estático.</strong> Com as cargas paradas, \(\dot r =
\ddot r = 0\) e sobra a lei de Coulomb exata. As correções entram com
\(\left(v/c\right)^2\), e para velocidades de laboratório elas são
invisíveis.</p>

<p><strong>A simetria.</strong> A força é central, depende apenas de grandezas
relativas e é rigorosamente igual e oposta nas duas cargas. Ela obedece à
terceira lei de Newton na forma forte, o que o capítulo 10 mostrou que a força
entre cargas em movimento, na teoria de Maxwell, <em>não</em> faz. Em Weber,
momento e momento angular se conservam sem que seja preciso inventar momento
guardado em campo nenhum.</p>

<p><strong>A energia.</strong> Existe uma função de \(r\) e \(\dot r\) que se
conserva,</p>

\[ E = \frac{1}{2}\mu\dot r^2
   + \frac{1}{4\pi\varepsilon_0}\frac{q_1q_2}{r}
     \left(1 - \frac{\dot r^2}{2c^2}\right), \]

<p>com \(\mu\) a massa reduzida. A verificação é direta: derivando no tempo e
agrupando, sobra \(\dot r\left[\mu\ddot r - F\right]\), que é nulo pela
equação de movimento. Weber tinha, portanto, uma teoria com conservação de
energia, momento e momento angular, todas exatas, e nenhum conceito novo além
da força.</p>

<div class="bloco fisica">
<span class="rotulo">De onde vem o fator 2</span>
<p>Weber escreveu a sua lei com uma constante própria, \(c_W\), determinada
experimentalmente, e na notação dele a força é
\(\left[1 - \dot r^2/c_W^2 + 2r\ddot r/c_W^2\right]\). A relação com a
velocidade da luz é \(c_W = \sqrt{2}\,c\), e é por isso que a medida de
Weber e Kohlrausch, que aparece na próxima seção, deu
\(4{,}4\times10^{8}\ \mathrm{m/s}\) e não \(3{,}0\times10^{8}\). O fator
\(\sqrt{2}\) é convenção, não física, e atrapalhou o entendimento do
resultado por alguns anos.</p>
</div>

<p>Uma consequência técnica merece atenção, porque a seção 4 vai voltar a ela.
A força depende de \(\ddot r\), e \(\ddot r\) é justamente o que a segunda lei
de Newton deveria fornecer. A equação de movimento é implícita, e resolvê-la
para a aceleração dá</p>

\[ \ddot r = \frac{\dfrac{k}{r^2}\left(1-\dfrac{\dot r^2}{2c^2}\right)}
   {\mu - \dfrac{k}{rc^2}},
   \qquad k = \frac{q_1q_2}{4\pi\varepsilon_0}. \]

<p>O denominador é uma <strong>massa efetiva</strong>, e ela depende da
distância.</p>
'''

S3 = r'''
<p>A teoria de Weber não era uma curiosidade marginal: durante trinta anos ela
foi a eletrodinâmica padrão na Alemanha, e por bons motivos.</p>

<h3>Ela reproduz a magnetostática</h3>

<p>Somando a força de Weber sobre todos os pares de cargas de dois elementos
de corrente neutros, obtém-se a força de Ampère entre elementos de corrente,</p>

\[ d^2\vet{F} = -\frac{\mu_0I_1I_2}{4\pi}\frac{\vers{r}}{r^2}
   \left[2\,d\vet{\ell}_1\cdot d\vet{\ell}_2
   - 3\left(d\vet{\ell}_1\cdot\vers{r}\right)
     \left(d\vet{\ell}_2\cdot\vers{r}\right)\right], \]

<p>que é central, como tudo em Weber. A expressão que este curso usou, vinda
de Biot-Savart, é a de Grassmann,</p>

\[ d^2\vet{F} = \frac{\mu_0I_1I_2}{4\pi}
   \frac{d\vet{\ell}_2\cruz\left(d\vet{\ell}_1\cruz\vers{r}\right)}{r^2}, \]

<p>que não é central e não obedece à terceira lei elemento a elemento. As duas
discordam abertamente: para dois elementos paralelos lado a lado, a de Ampère
dá o dobro da de Grassmann; para dois elementos perpendiculares em linha, a de
Grassmann dá uma força transversal e a de Ampère dá exatamente zero.</p>

<div class="bloco alerta">
<span class="rotulo">E mesmo assim nenhum experimento as distingue</span>
<p>A diferença entre as duas expressões é um diferencial exato ao longo do
circuito fonte. Somando sobre um circuito <em>fechado</em>, ela se cancela, e
as duas dão rigorosamente a mesma força. O script
<code>weber.py</code> verifica isso: as duas somas coincidem em
\(10^{-15}\), e não apenas no limite de malha fina, mas em qualquer número de
pedaços.</p>
<p>Como corrente estacionária exige circuito fechado, nenhum experimento de
magnetostática podia escolher entre elas. A disputa durou meio século por
falta de um experimento decisivo, e não por falta de rigor.</p>
</div>

<h3>Ela reproduz a indução</h3>

<p>Weber derivou a lei de Faraday da sua força, sem campo e sem linhas. O termo
em \(\ddot r\) é o responsável: quando a corrente de um circuito varia, as
cargas do outro sentem uma força proporcional a essa variação, e o resultado é
uma força eletromotriz induzida com o sinal e o valor corretos.</p>

<h3>Ela produziu o número</h3>

<div class="destaque">
<p><strong>Exemplo trabalhado: a medida que mudou a física.</strong> Em 1855,
Weber e <a href="https://en.wikipedia.org/wiki/Rudolf_Kohlrausch">Rudolf
Kohlrausch</a> mediram a mesma carga de duas maneiras independentes: pela força
eletrostática entre cargas paradas e pela força magnética entre correntes. Cada
método define a sua unidade de carga, e a razão entre as duas unidades tem
dimensão de velocidade.</p>

<p><strong>Por que tem dimensão de velocidade.</strong> Pela lei de Coulomb,
\(F \sim q_{es}^2/4\pi\varepsilon_0r^2\); pela lei de Ampère,
\(F \sim \mu_0I^2/2\pi r \sim \mu_0q_{em}^2/2\pi rt^2\). Igualando as duas
forças,</p>

\[ \frac{q_{es}^2}{q_{em}^2} \sim \frac{1}{\varepsilon_0\mu_0}
   \times\frac{\text{distância}^{2}}{\text{tempo}^{2}}
   \;\Longrightarrow\;
   \frac{q_{es}}{q_{em}} \sim \frac{1}{\sqrt{\varepsilon_0\mu_0}} = c. \]

<p>A constante \(c\) aparece porque \(\varepsilon_0\) e \(\mu_0\) aparecem, e
nada nessa conta menciona óptica.</p>

<p><strong>O resultado.</strong> Eles obtiveram
\(c_W = 4{,}39\times10^{8}\ \mathrm{m/s}\), que na constante da teoria de
Weber corresponde a</p>

\[ c = \frac{c_W}{\sqrt2} = 3{,}104\times10^{8}\ \mathrm{m/s}. \]

<p>A medida de Fizeau para a velocidade da luz, de 1849, dava
\(3{,}133\times10^{8}\ \mathrm{m/s}\). A diferença entre as duas é de
<strong>0,9 %</strong>, dentro das incertezas da época. Vale notar que as duas
erravam no mesmo sentido: a de Fizeau está 4,5 % acima do valor moderno, e a de
Weber e Kohlrausch, 3,5 %.</p>

<p><strong>O que fizeram com isso.</strong> Weber e Kohlrausch publicaram o
número e, surpreendentemente, não concluíram nada sobre luz: para eles, \(c\)
era a velocidade relativa em que a força entre duas cargas se anula, um
parâmetro da teoria. Foi Kirchhoff, em 1857, quem notou que sinais elétricos
num fio deveriam viajar com essa velocidade, e foi Maxwell, em 1861, quem disse
a frase inteira: a luz <em>é</em> uma onda eletromagnética. A diferença não é
de competência, é de arcabouço. Quem não tem campo não tem onde pôr uma
onda.</p>
</div>

<p>Vale fixar esse ponto, porque ele é a moral do capítulo. O mesmo número,
medido pelas mesmas pessoas com os mesmos aparelhos, significa uma coisa numa
teoria e outra coisa na outra. Dados não falam sozinhos.</p>
'''

S4 = r'''
<p>Três problemas derrubaram a teoria, e vale a pena conhecer os três, porque
eles são de naturezas diferentes.</p>

<h3>A massa negativa de Helmholtz</h3>

<p>Em 1872, Helmholtz apontou a massa efetiva da seção 2. Ela se anula
quando</p>

\[ \mu = \frac{k}{rc^2}
   \;\Longrightarrow\;
   r_{\text{crit}} = \frac{q_1q_2}{4\pi\varepsilon_0\mu c^2}, \]

<p>e para dois elétrons isso dá, como o script confere,</p>

\[ r_{\text{crit}} = 2r_e = 5{,}64\times10^{-15}\ \mathrm{m}, \]

<p>exatamente duas vezes o raio clássico do elétron. Abaixo desse raio a massa
efetiva é negativa, e o sistema responde à força ao contrário: duas cargas de
mesmo sinal se atrairiam e ganhariam energia cinética indefinidamente. Weber e
os seus defensores responderam que essa escala era inatingível, e tinham razão
na prática. Mas uma teoria que produz energia do nada a alguma distância é uma
teoria com um problema, não com um detalhe.</p>

<div class="bloco fisica">
<span class="rotulo">Repare onde isso acontece</span>
<p>A patologia aparece em \(2r_e\), e o capítulo 11 mostrou que a reação de
radiação de Abraham-Lorentz enlouquece exatamente na mesma escala, \(r_e\).
Não é coincidência: as duas teorias tentam descrever uma carga pontual usando
a energia eletrostática dela própria, e as duas quebram quando essa energia se
torna comparável a \(mc^2\). A escala em que a eletrodinâmica clássica termina
não depende de qual versão dela se escolhe.</p>
</div>

<h3>Não há radiação</h3>

<p>Este é o problema fatal, e é simples de enunciar. Na teoria de Weber, a
energia de um par de cargas é função de \(r\) e \(\dot r\). Num movimento
periódico, \(r\) e \(\dot r\) voltam ao valor inicial a cada ciclo, de modo que
a energia volta também: <strong>nada é perdido, nunca</strong>. Não há atraso,
então não há para onde a energia ir; não há campo, então não há onde guardá-la
em trânsito.</p>

<p>O script compara as duas previsões para um elétron oscilando com 0,1 nm de
amplitude a \(10^{15}\ \mathrm{Hz}\):</p>

<div class="tabela-rolavel">
<table>
<thead><tr><th>grandeza</th><th>Maxwell</th><th>Weber</th></tr></thead>
<tbody>
<tr><td>potência irradiada</td><td>4,45×10⁻¹¹ W</td><td>0</td></tr>
<tr><td>taxa de perda</td><td>2,47×10⁸ s⁻¹</td><td>0</td></tr>
<tr><td>vida da oscilação</td><td>4,0 ns, ou 4×10⁶ ciclos</td><td>infinita</td></tr>
</tbody>
</table>
</div>

<p>Os 4 nanossegundos não são um número qualquer: é a ordem de grandeza certa
da vida de um estado atômico excitado, medida em laboratório. O oscilador
clássico acerta, e Weber não tem o que dizer.</p>

<p>A prova definitiva veio de Hertz, entre 1886 e 1888. Ele gerou ondas
eletromagnéticas com um centelhador, detectou-as a metros de distância, mediu o
comprimento de onda com um espelho e ondas estacionárias, e mostrou que elas
refletiam, refratavam e polarizavam como luz. Uma teoria de ação a distância
não pode explicar um sinal que sai de um lugar, leva tempo para chegar e chega
carregando energia que a fonte perdeu.</p>

<h3>Não é compatível com a relatividade</h3>

<p>A terceira objeção é posterior e é mais estrutural. A força de Weber depende
de \(\dot r\), a taxa de variação da distância, que não é uma grandeza
invariante: dois observadores em movimento relativo discordam sobre ela de
maneira que não se encaixa nas transformações de Lorentz. A teoria de Maxwell,
que ninguém projetou para ser relativística, acabou sendo exatamente isso, e
foi dela que Einstein partiu em 1905. A de Weber, projetada para ser simples e
newtoniana, não sobrevive à mudança de referencial.</p>

<div class="bloco ex">
<span class="rotulo">O que fica</span>
<p>A lição que vale levar não é "Weber errou". É que uma teoria pode reproduzir
todos os experimentos disponíveis, conservar tudo o que precisa conservar, ser
matematicamente consistente e ainda assim estar errada, porque o experimento
que a distingue ainda não foi feito. O campo não venceu por ser mais bonito:
venceu porque alguém, em 1888, mediu uma onda atravessando uma sala.</p>
</div>
'''

S5 = r'''
<div class="cartoes">
  <article class="cartao">
    <h3><a href="codigo/weber.py">weber.py</a></h3>
    <p>Implementa a força de Weber e faz os quatro testes do capítulo: as três
    conservações, a massa efetiva de Helmholtz, Ampère contra Grassmann e a
    ausência de radiação.</p>
    <p><strong>Confira assim:</strong> o raio crítico tem de dar exatamente
    \(2r_e\); a energia tem de ficar constante na colisão frontal sem nenhum
    campo na conta; a soma de Ampère e a de Grassmann sobre a espira fechada
    têm de coincidir em \(10^{-15}\) para qualquer número de pedaços; e a vida
    do oscilador tem de ser 4 ns em Maxwell contra infinita em Weber.</p>
  </article>
  <article class="cartao">
    <h3><a href="codigo/lienard_wiechert.py">lienard_wiechert.py</a></h3>
    <p>Do capítulo 10, e útil aqui para a comparação: ele mostra o campo
    apontando para a posição <em>presente</em> da carga, embora a informação
    tenha saído da posição retardada.</p>
    <p><strong>Confira assim:</strong> esse acerto, que parece ação a distância,
    sai de uma teoria com atraso. A aparência de instantaneidade não é prova de
    instantaneidade.</p>
  </article>
</div>
'''

SECOES = [
    ('Duas escolas, uma pergunta', S1),
    ('A força de Weber', S2),
    ('O que ela acerta, e o número que ela produziu', S3),
    ('As três rachaduras', S4),
    ('No Spyder', S5),
]

SECOES.append(('Exercícios propostos', exercicios.bloco(LISTA)))


def main():
    titulos = [t for t, _ in SECOES]
    escreve('cap12.html', secoes_html(SECOES), secoes=titulos)


if __name__ == '__main__':
    main()
