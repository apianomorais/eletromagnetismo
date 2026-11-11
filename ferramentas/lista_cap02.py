# -*- coding: utf-8 -*-
"""Exercícios propostos do capítulo 2, eletrostática."""

LISTA = [
    ('2.1  O disco, e o plano que ele vira',
     r'''Um disco de raio \(a\) tem carga \(Q\) uniformemente distribuída na
     face, \(\sigma = Q/\pi a^2\). Calcule o campo num ponto do eixo a uma
     altura \(z\), integrando em anéis, e obtenha os dois limites: \(z \gg a\) e
     \(z \ll a\).''',
     r'''<p>Um anel de raio \(s\) e espessura \(ds\) tem carga
     \(dq = \sigma\,2\pi s\,ds\) e, pelo resultado do exemplo do anel,
     contribui no eixo com</p>
     <p>\[ dE_z = \frac{1}{4\pi\varepsilon_0}
        \frac{z\,dq}{\left(s^2+z^2\right)^{3/2}}. \]</p>
     <p>Integrando de \(0\) a \(a\), com \(u = s^2+z^2\),</p>
     <p>\[ E_z = \frac{\sigma z}{2\varepsilon_0}\int_0^a
        \frac{s\,ds}{\left(s^2+z^2\right)^{3/2}}
        = \frac{\sigma}{2\varepsilon_0}
          \left[1 - \frac{z}{\sqrt{a^2+z^2}}\right]. \]</p>
     <p><b>Longe</b> (\(z \gg a\)): expandindo a raiz,
     \(z/\sqrt{a^2+z^2} \approx 1 - a^2/2z^2\), e sobra</p>
     <p>\[ E_z \approx \frac{\sigma a^2}{4\varepsilon_0 z^2}
        = \frac{Q}{4\pi\varepsilon_0 z^2}, \]</p>
     <p>a carga pontual, como tinha de ser.</p>
     <p><b>Perto</b> (\(z \ll a\)): o segundo termo tende a zero e sobra
     \(E_z = \sigma/2\varepsilon_0\), o plano infinito, independente da
     distância. Note que o campo <em>não</em> tende a infinito ao encostar no
     disco: ele tende a um valor finito, e é esse valor que aparece na condição
     de contorno de uma superfície carregada.</p>''' ),

    ('2.2  A cavidade que esconde um campo uniforme',
     r'''Uma esfera de raio \(R\) tem carga uniforme de densidade \(\rho\), mas
     dentro dela há uma cavidade esférica vazia, de raio \(b\), cujo centro está
     deslocado de \(\vet{d}\) em relação ao centro da esfera grande. Mostre que o
     campo dentro da cavidade é uniforme e vale \(\rho\vet{d}/3\varepsilon_0\).''',
     r'''<p>O truque é a superposição: a peça furada é a soma de uma esfera
     cheia de densidade \(+\rho\) com uma esfera pequena de densidade
     \(-\rho\) ocupando exatamente a cavidade.</p>
     <p>Para uma esfera uniforme, a lei de Gauss dá, num ponto interno a uma
     distância \(\vet{r}\) do seu centro,</p>
     <p>\[ \vet{E} = \frac{\rho\,\vet{r}}{3\varepsilon_0}. \]</p>
     <p>Num ponto dentro da cavidade, chame de \(\vet{r}_+\) o vetor desde o
     centro da esfera grande e de \(\vet{r}_-\) o vetor desde o centro da
     cavidade. Então</p>
     <p>\[ \vet{E} = \frac{\rho\vet{r}_+}{3\varepsilon_0}
        - \frac{\rho\vet{r}_-}{3\varepsilon_0}
        = \frac{\rho}{3\varepsilon_0}\left(\vet{r}_+-\vet{r}_-\right)
        = \frac{\rho\,\vet{d}}{3\varepsilon_0}, \]</p>
     <p>porque \(\vet{r}_+ - \vet{r}_- = \vet{d}\) para <em>qualquer</em> ponto
     da cavidade.</p>
     <p><b>O que isso tem de notável.</b> O campo não depende do ponto: é
     rigorosamente uniforme dentro da cavidade, aponta sempre ao longo de
     \(\vet{d}\), e não depende nem do raio \(b\) da cavidade nem do raio
     \(R\) da esfera. Se a cavidade for concêntrica (\(\vet{d} = 0\)), o campo
     é nulo, que é o resultado conhecido da casca.</p>''' ),

    ('2.3  O cabo com densidade que cresce',
     r'''Um cilindro longo de raio \(a\) tem densidade de carga
     \(\rho(s) = \rho_0\,s/a\). Ache o campo dentro e fora, e a carga por
     unidade de comprimento.''',
     r'''<p>A carga por unidade de comprimento é</p>
     <p>\[ \lambda = \int_0^a \rho_0\frac{s}{a}\,(2\pi s\,ds)
        = \frac{2\pi\rho_0}{a}\cdot\frac{a^3}{3}
        = \frac{2\pi\rho_0a^2}{3}. \]</p>
     <p><b>Dentro</b> (\(s \lt a\)), a carga enlaçada por unidade de comprimento
     é \(2\pi\rho_0s^3/3a\), e a superfície gaussiana cilíndrica dá</p>
     <p>\[ E\,(2\pi s) = \frac{2\pi\rho_0 s^3}{3a\varepsilon_0}
        \;\Longrightarrow\;
        E = \frac{\rho_0 s^2}{3a\varepsilon_0}. \]</p>
     <p><b>Fora</b> (\(s \gt a\)),</p>
     <p>\[ E = \frac{\lambda}{2\pi\varepsilon_0 s}
        = \frac{\rho_0a^2}{3\varepsilon_0 s}. \]</p>
     <p>Em \(s = a\) as duas dão \(\rho_0a/3\varepsilon_0\): contínuo, porque não
     há carga superficial. Compare com o fio uniforme, em que o campo interno
     cresce linearmente: aqui ele cresce com \(s^2\).</p>''' ),

    ('2.4  Dois modos de errar o dipolo',
     r'''Duas cargas \(+q\) e \(-q\) estão separadas por uma distância \(d\) ao
     longo do eixo \(z\), com o centro na origem. Calcule o potencial exato num
     ponto \((r,\theta)\) e mostre que, para \(r \gg d\), ele tende a
     \(V = \dfrac{qd\cos\theta}{4\pi\varepsilon_0r^2}\). Em seguida explique por
     que seria errado dizer que o campo do dipolo cai com \(1/r^2\).''',
     r'''<p>As distâncias às duas cargas são</p>
     <p>\[ \imath_\pm = \sqrt{r^2 \mp r d\cos\theta + d^2/4}, \]</p>
     <p>e o potencial exato é a soma</p>
     <p>\[ V = \frac{q}{4\pi\varepsilon_0}
        \left(\frac{1}{\imath_+}-\frac{1}{\imath_-}\right). \]</p>
     <p>Para \(r \gg d\), escreva
     \(\imath_\pm \approx r\left(1 \mp \frac{d\cos\theta}{2r}\right)\) e use
     \((1+x)^{-1} \approx 1-x\):</p>
     <p>\[ \frac{1}{\imath_\pm} \approx \frac{1}{r}
        \left(1 \pm \frac{d\cos\theta}{2r}\right), \]</p>
     <p>de modo que a diferença deixa só o termo cruzado:</p>
     <p>\[ V \approx \frac{q}{4\pi\varepsilon_0}\,\frac{d\cos\theta}{r^2}
        = \frac{p\cos\theta}{4\pi\varepsilon_0 r^2},\qquad p = qd. \]</p>
     <p><b>O erro a evitar.</b> O <em>potencial</em> do dipolo cai com
     \(1/r^2\); o <em>campo</em> cai com \(1/r^3\), porque é o gradiente dele.
     Dizer que o campo do dipolo vai com \(1/r^2\) é confundir as duas
     grandezas, e é o erro mais comum do capítulo. Em geral, cada ordem de
     multipolo tem potencial \(\sim 1/r^{n+1}\) e campo \(\sim 1/r^{n+2}\).</p>''' ),

    ('2.5  Onde é mais caro guardar carga',
     r'''Compare a energia necessária para carregar com \(Q\) uma esfera
     condutora de raio \(R\) (carga toda na superfície) com a de uma esfera
     isolante do mesmo raio com a carga espalhada uniformemente no volume.
     Calcule a razão e diga qual custa mais.''',
     r'''<p><b>Condutora.</b> A carga está toda na superfície, de modo que o
     campo é nulo dentro e vale \(Q/4\pi\varepsilon_0r^2\) fora. Só a região
     externa contribui:</p>
     <p>\[ W_{\text{cond}} = \frac{\varepsilon_0}{2}\int_R^\infty
        \left(\frac{Q}{4\pi\varepsilon_0r^2}\right)^2 4\pi r^2dr
        = \frac{Q^2}{8\pi\varepsilon_0R}
        = \frac{1}{2}\,\frac{Q^2}{4\pi\varepsilon_0R}. \]</p>
     <p><b>Isolante uniforme.</b> É o exemplo resolvido do texto:</p>
     <p>\[ W_{\text{isol}} = \frac{3}{5}\,\frac{Q^2}{4\pi\varepsilon_0R}. \]</p>
     <p><b>A razão</b> é \( \frac{3/5}{1/2} = \frac{6}{5} = 1{,}2\): a esfera
     isolante custa 20 % a mais.</p>
     <p><b>Por quê.</b> Na condutora, a carga se arranja sozinha do jeito mais
     barato possível, que é o mais espalhado: toda na superfície, o mais longe
     que der uma da outra. Forçá-la a ficar no volume, como no isolante,
     significa empilhar carga perto do centro, onde o potencial das outras é
     maior. O condutor minimiza a energia por conta própria, e esse é um caso
     particular do princípio de Thomson.</p>''' ),

    ('2.6  Esfera dentro de casca',
     r'''Uma esfera condutora de raio \(a\) com carga \(+Q\) está no centro de
     uma casca condutora neutra de raios \(b\) e \(c\) (\(a \lt b \lt c\)).
     Ache a carga em cada uma das três superfícies, o campo nas quatro regiões e
     o potencial da esfera interna, com referência no infinito.''',
     r'''<p><b>As cargas.</b> Na esfera, \(+Q\) na superfície \(r=a\). Dentro do
     metal da casca o campo é nulo, logo uma gaussiana entre \(b\) e \(c\) não
     enlaça carga: a superfície \(r=b\) tem \(-Q\). Como a casca é neutra, a
     superfície \(r=c\) fica com \(+Q\).</p>
     <p><b>O campo.</b></p>
     <p>\[ E = 0 \ (r\lt a);\quad
        E = \frac{Q}{4\pi\varepsilon_0r^2}\ (a\lt r\lt b);\quad
        E = 0 \ (b\lt r\lt c);\quad
        E = \frac{Q}{4\pi\varepsilon_0r^2}\ (r\gt c). \]</p>
     <p><b>O potencial da esfera</b>, integrando \(-\int\vet{E}\cdot d\vet{\ell}\)
     desde o infinito e pulando as regiões de campo nulo:</p>
     <p>\[ V(a) = \frac{Q}{4\pi\varepsilon_0}
        \left[\frac{1}{c} + \frac{1}{a} - \frac{1}{b}\right]. \]</p>
     <p><b>Leitura.</b> O termo \(1/c\) vem de trazer a carga do infinito até a
     casca; a região entre \(b\) e \(c\) não contribui, porque lá o campo é
     nulo; e \(1/a - 1/b\) é o trecho entre a esfera e a casca. Se a casca for
     aterrada, a carga de \(r=c\) escoa, o termo \(1/c\) some e o potencial da
     esfera cai para \(\frac{Q}{4\pi\varepsilon_0}(1/a - 1/b)\).</p>''' ),
]
