# -*- coding: utf-8 -*-
"""Exercícios propostos do capítulo 10, potenciais e campos."""

LISTA = [
    ('10.1  Um calibre esquisito, e os campos que não mudam',
     r'''Considere os potenciais \(V = 0\) e \(\vet{A} = -\dfrac{1}{4\pi
     \varepsilon_0}\dfrac{qt}{r^2}\vers{r}\). Calcule \(\vet{E}\) e \(\vet{B}\)
     e diga que situação física eles descrevem. Depois ache a função
     \(\lambda\) que leva esses potenciais aos mais familiares da
     eletrostática.''',
     r'''<p><b>Os campos.</b> Como \(\vet{A}\) é radial e só depende de \(r\),
     \(\rot{\vet{A}} = 0\) e portanto \(\vet{B} = 0\). E</p>
     <p>\[ \vet{E} = -\nabla V - \pder{\vet{A}}{t}
        = 0 + \frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}\vers{r}. \]</p>
     <p>É o campo de uma carga pontual parada na origem, sem campo magnético
     nenhum: a eletrostática de sempre, escrita de um jeito irreconhecível.</p>
     <p><b>A transformação.</b> Queremos chegar a \(V' = q/4\pi\varepsilon_0 r\)
     e \(\vet{A}' = 0\). De \(V' = V - \partial\lambda/\partial t\),</p>
     <p>\[ \pder{\lambda}{t} = -\frac{q}{4\pi\varepsilon_0 r}
        \;\Longrightarrow\;
        \lambda = -\frac{qt}{4\pi\varepsilon_0 r}, \]</p>
     <p>e conferindo na outra equação,
     \(\vet{A}' = \vet{A} + \nabla\lambda = \vet{A}
     + \frac{qt}{4\pi\varepsilon_0 r^2}\vers{r} = 0\). Fecha.</p>
     <p><b>A moral.</b> Os potenciais não são observáveis: a mesma física admite
     descrições completamente diferentes. O que é observável é o campo, e, na
     mecânica quântica, também a <em>integral</em> de \(\vet{A}\) ao longo de um
     caminho fechado, que é o efeito Aharonov-Bohm. Mas nunca \(\vet{A}\)
     ponto a ponto.</p>''' ),

    ('10.2  Por que não se pode simplesmente retardar Coulomb',
     r'''Mostre, com um exemplo concreto, que escrever
     \(\vet{E}(\vet{r},t) = \frac{1}{4\pi\varepsilon_0}\int
     \frac{\rho(\vet{r}',t_r)}{\imath^2}\vers{\imath}\,d\tau'\) está errado.
     Use uma carga pontual em movimento uniforme e compare com o resultado
     correto do texto.''',
     r'''<p>Para uma carga pontual em \(\vet{w}(t_r)\), a fórmula ingênua daria
     um campo que aponta da posição <b>retardada</b> para o observador, com
     módulo \(q/4\pi\varepsilon_0\imath^2\), isto é, Coulomb avaliado no passado.</p>
     <p>O resultado correto, do exemplo do texto, aponta para a posição
     <b>presente</b> e tem o fator de achatamento:</p>
     <p>\[ \vet{E} = \frac{q}{4\pi\varepsilon_0}
        \frac{1-v^2/c^2}{\left(1-\frac{v^2}{c^2}\sen^2\theta\right)^{3/2}}
        \frac{\vers{R}}{R^2}. \]</p>
     <p>São diferentes em <em>direção</em> (posição retardada contra presente) e
     em <em>módulo</em> (o fator angular). A \(v = 0{,}5c\) e \(\theta =
     90^\circ\), por exemplo, o fator vale \(1/\sqrt{1-0{,}25}\cdot ... \) — a
     conta dá \(1{,}155\), ou seja, 15 % de diferença só no módulo.</p>
     <p><b>De onde vem o erro.</b> O campo é \(-\nabla V - \partial\vet{A}
     /\partial t\), e o gradiente age também sobre o \(t_r\), que depende de
     \(\vet{r}\). Essa dependência produz termos com \(\dot\rho\) e
     \(\dot{\vet{J}}\) que a fórmula ingênua não tem, e são exatamente esses
     termos que carregam a radiação. Sem eles, cargas aceleradas não irradiariam
     nada, o que contraria qualquer antena.</p>''' ),

    ('10.3  Uma carga só aparece uma vez no cone de luz',
     r'''Prove que a equação do tempo retardado,
     \(\left|\vet{r}-\vet{w}(t_r)\right| = c(t-t_r)\), tem exatamente uma
     solução para qualquer carga com \(v \lt c\). Em seguida explique o que
     aconteceria se a carga pudesse exceder \(c\).''',
     r'''<p><b>A prova.</b> Suponha duas soluções, \(t_1 \lt t_2\), ambas
     anteriores a \(t\). Então</p>
     <p>\[ \left|\vet{r}-\vet{w}(t_1)\right| = c(t-t_1),\qquad
        \left|\vet{r}-\vet{w}(t_2)\right| = c(t-t_2). \]</p>
     <p>Subtraindo, o lado direito dá \(c(t_2-t_1)\), que é a distância que a
     luz percorre entre os dois instantes. O lado esquerdo é a diferença entre
     duas distâncias ao mesmo ponto, que pela desigualdade triangular não passa
     de \(\left|\vet{w}(t_2)-\vet{w}(t_1)\right|\), a distância que a
     <em>carga</em> percorreu.</p>
     <p>Logo seria preciso que a carga tivesse percorrido pelo menos tanto
     quanto a luz no mesmo intervalo, isto é, \(v \ge c\). Com \(v \lt c\) isso
     é impossível, e a solução é única.</p>
     <p><b>Se a carga excedesse c.</b> Haveria mais de uma contribuição
     simultânea da mesma carga, e o observador a "veria" em vários lugares ao
     mesmo tempo. Isso não é só ficção: num meio material a velocidade da luz é
     \(c/n\), e uma partícula pode ultrapassá-la. O resultado é a radiação
     Cherenkov, com o seu cone característico e o brilho azul dos reatores
     nucleares.</p>''' ),

    ('10.4  O campo achatado de uma carga rápida',
     r'''Para uma carga em movimento uniforme, calcule a razão entre o campo
     perpendicular ao movimento e o campo paralelo, a mesma distância, para
     \(v/c = 0{,}1\), \(0{,}5\), \(0{,}9\) e \(0{,}99\). Comente a consequência
     para a colisão de dois feixes num acelerador.''',
     r'''<p>Da fórmula do texto, com \(\beta = v/c\):</p>
     <p>\[ E_\perp = \frac{q}{4\pi\varepsilon_0R^2}\frac{1}{\sqrt{1-\beta^2}},
        \qquad
        E_\parallel = \frac{q}{4\pi\varepsilon_0R^2}\left(1-\beta^2\right), \]</p>
     <p>de modo que a razão é</p>
     <p>\[ \frac{E_\perp}{E_\parallel} = \frac{1}{\left(1-\beta^2\right)^{3/2}}
        = \gamma^3. \]</p>
     <div class="tabela-rolavel">
     <table>
     <thead><tr><th>\(\beta\)</th><th>\(\gamma\)</th>
     <th>\(E_\perp/E_\parallel\)</th></tr></thead>
     <tbody>
     <tr><td>0,10</td><td>1,005</td><td>1,02</td></tr>
     <tr><td>0,50</td><td>1,155</td><td>1,54</td></tr>
     <tr><td>0,90</td><td>2,294</td><td>12,1</td></tr>
     <tr><td>0,99</td><td>7,089</td><td>356</td></tr>
     </tbody>
     </table>
     </div>
     <p><b>No acelerador.</b> O campo de um feixe ultrarrelativístico é um
     "panqueca" transversal, quase um pulso plano. Quando dois feixes se
     cruzam, cada partícula de um vê o campo do outro como um tapa curto e
     intenso, perpendicular ao movimento. É esse achatamento que torna
     possível tratar colisões como interação de fótons quase reais, a chamada
     aproximação de Weizsäcker-Williams.</p>''' ),

    ('10.5  A potência de uma antena de dipolo, por análise dimensional',
     r'''Sem fazer a conta completa do capítulo 11, mostre por análise
     dimensional que a potência irradiada por uma carga acelerada tem de ter a
     forma \(P \propto \mu_0q^2a^2/c\), e estime a constante comparando com o
     campo de aceleração do texto.''',
     r'''<p><b>A dimensional.</b> A potência tem de depender de \(q\), de
     \(a\), e das constantes do eletromagnetismo. O campo de aceleração do
     texto vai com \(qa/\imath\) vezes constantes, e o fluxo de energia vai com
     \(E^2/\mu_0c\). Multiplicando pela área, \(\imath^2\):</p>
     <p>\[ P \sim \frac{1}{\mu_0 c}\left(\frac{\mu_0qa}{4\pi \imath}\right)^2
        \imath^2 = \frac{\mu_0q^2a^2}{16\pi^2c}, \]</p>
     <p>e o \(\imath\) sumiu, que é o conteúdo físico: a potência atravessa
     qualquer esfera igualmente.</p>
     <p><b>A constante.</b> Falta a integral angular do padrão
     \(\sen^2\theta\), que vale</p>
     <p>\[ \int\sen^2\theta\,d\Omega
        = 2\pi\int_0^\pi\sen^3\theta\,d\theta = \frac{8\pi}{3}, \]</p>
     <p>e isso leva de \(16\pi^2\) para</p>
     <p>\[ P = \frac{\mu_0q^2a^2}{6\pi c}, \]</p>
     <p>que é a fórmula de Larmor, deduzida por inteiro no capítulo 11.</p>
     <p><b>Quanto vale.</b> Para um elétron com a aceleração de um átomo de
     hidrogênio no estado fundamental, \(a \sim 9\times10^{22}\
     \mathrm{m/s^2}\), isso dá \(P = 4{,}7\times10^{-8}\ \mathrm{W}\). Com a
     energia de ligação de 13,6 eV, o átomo clássico gastaria toda a energia em
     \(4{,}7\times10^{-11}\) s, isto é, dezenas de picossegundos (a conta
     feita com cuidado, acompanhando o raio encolher, dá algo ainda menor). O
     átomo existir é, portanto, uma prova de que a eletrodinâmica clássica não
     vale lá dentro.</p>''' ),

    ('10.6  O calibre de Coulomb e a propagação instantânea',
     r'''No calibre de Coulomb, \(V(\vet{r},t)\) é o potencial instantâneo da
     distribuição de carga, isto é, ele muda em todo o espaço no mesmo instante
     em que a carga muda. Isso viola a relatividade? Justifique.''',
     r'''<p><b>Não viola.</b> O potencial escalar não é observável; o campo é. No
     calibre de Coulomb, o termo instantâneo de \(-\nabla V\) é exatamente
     cancelado por uma parte de \(-\partial\vet{A}/\partial t\), e o campo
     resultante propaga a \(c\), como tem de ser.</p>
     <p>Dito de outro jeito: a divisão da informação entre \(V\) e \(\vet{A}\)
     depende do calibre, e nada impede que uma das partes seja instantânea
     desde que a soma não seja. O calibre de Lorenz distribui a informação de
     modo que cada potencial, separadamente, já propaga a \(c\), o que é mais
     elegante e muito mais conveniente.</p>
     <p><b>Por que alguém usaria Coulomb, então.</b> Porque nele
     \(\nabla^2 V = -\rho/\varepsilon_0\) é a equação de Poisson de sempre, com
     solução conhecida, e sobra apenas uma equação de onda para \(\vet{A}\).
     Em problemas quase estáticos, e em boa parte da física da matéria
     condensada, isso simplifica muito. O preço é que a parte instantânea
     assusta quem vê pela primeira vez.</p>''' ),
]
