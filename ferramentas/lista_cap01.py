# -*- coding: utf-8 -*-
"""Exercícios propostos do capítulo 1, análise vetorial."""

LISTA = [
    ('1.1  O ângulo entre as diagonais do cubo',
     r'''Um cubo tem um vértice na origem e lados de comprimento \(a\) ao longo
     dos eixos. Calcule o ângulo entre duas diagonais do cubo que partem de
     vértices diferentes da mesma face, usando o produto escalar. Mostre que o
     resultado não depende de \(a\).''',
     r'''<p>Tome a diagonal que vai de \((0,0,0)\) a \((a,a,a)\) e a que vai de
     \((a,0,0)\) a \((0,a,a)\). Os vetores são</p>
     <p>\[ \vet{A} = a(1,1,1),\qquad \vet{B} = a(-1,1,1). \]</p>
     <p>O produto escalar vale \(\vet{A}\cdot\vet{B} = a^2(-1+1+1) = a^2\), e os
     módulos são ambos \(a\sqrt{3}\). Logo</p>
     <p>\[ \cos\theta = \frac{a^2}{3a^2} = \frac{1}{3}
        \;\Longrightarrow\; \theta = 70{,}53^\circ. \]</p>
     <p>O \(a^2\) cancela, e tinha de cancelar: ângulo é propriedade de forma, e
     cubos de qualquer tamanho são semelhantes. O suplemento, \(109{,}47^\circ\),
     é o ângulo de ligação do carbono tetraédrico, e é exatamente a mesma
     geometria.</p>''' ),

    ('1.2  Um campo que gira sem rotacional',
     r'''Considere \(\vet{v} = \dfrac{\vers{\phi}}{s}\) em coordenadas
     cilíndricas, isto é, um campo cujas linhas são circunferências em torno do
     eixo \(z\). Calcule o rotacional para \(s \ne 0\) e a circulação ao longo
     de um círculo de raio \(s\) centrado no eixo. Explique a aparente
     contradição com o teorema de Stokes.''',
     r'''<p>Em cilíndricas, para um campo puramente azimutal com
     \(v_\phi = v_\phi(s)\),</p>
     <p>\[ \rot{\vet{v}} = \frac{1}{s}\der{\left(s v_\phi\right)}{s}\vers{z}
        = \frac{1}{s}\der{(1)}{s}\vers{z} = 0 \qquad (s \ne 0). \]</p>
     <p>A circulação, porém, não é nula:</p>
     <p>\[ \oint \vet{v}\cdot d\vet{\ell}
        = \int_0^{2\pi}\frac{1}{s}\,(s\,d\phi) = 2\pi. \]</p>
     <p><b>A contradição é só aparente.</b> O teorema de Stokes exige que o
     rotacional seja bem definido em <em>toda</em> a superfície apoiada na
     curva, e qualquer superfície que se apoie nesse círculo atravessa o eixo
     \(s = 0\), onde o campo explode. A circulação de \(2\pi\) está toda
     concentrada ali, exatamente como a divergência de \(\vers{r}/r^2\) está
     concentrada na origem.</p>
     <p>Este é o campo magnético de um fio, a menos de constantes, e a
     "singularidade" é a corrente. Troque o fio por um condutor de raio finito e
     tudo volta a ser suave: dentro dele o rotacional é \(\mu_0\vet{J}\), e a
     conta fecha sem nenhum mistério.</p>''' ),

    ('1.3  Gradiente de uma função só da distância',
     r'''Mostre que, para qualquer função \(f(r)\) que dependa apenas da
     distância à origem, vale \(\nabla f = \der{f}{r}\,\vers{r}\). Use o
     resultado para calcular \(\nabla(1/r)\) e \(\nabla(r^n)\), e diga o que o
     primeiro tem a ver com a eletrostática.''',
     r'''<p>Em esféricas, o gradiente é</p>
     <p>\[ \nabla f = \pder{f}{r}\vers{r} + \frac{1}{r}\pder{f}{\theta}
        \vers{\theta} + \frac{1}{r\sen\theta}\pder{f}{\phi}\vers{\phi}, \]</p>
     <p>e se \(f\) só depende de \(r\) as duas últimas derivadas se anulam,
     sobrando \(\nabla f = f'(r)\vers{r}\).</p>
     <p>Aplicando,</p>
     <p>\[ \nabla\!\left(\frac{1}{r}\right) = -\frac{1}{r^2}\vers{r},
        \qquad \nabla(r^n) = n r^{n-1}\vers{r}. \]</p>
     <p><b>A ligação com a eletrostática.</b> O campo de uma carga pontual é
     \(\vet{E} = \frac{q}{4\pi\varepsilon_0}\frac{\vers{r}}{r^2}\), e o primeiro
     resultado diz que ele é exatamente \(-\nabla V\) com
     \(V = \frac{q}{4\pi\varepsilon_0 r}\). Ou seja: o potencial de Coulomb não é
     adivinhado, ele é a primitiva radial do campo. O sinal negativo da
     definição \(\vet{E} = -\nabla V\) é escolhido justamente para que \(V\)
     decresça no sentido do campo.</p>''' ),

    ('1.4  Conferindo Stokes num hemisfério',
     r'''Tome \(\vet{v} = \left(2xz + 3y^2\right)\vers{y} + \left(4yz^2\right)
     \vers{z}\) e a superfície do quadrado unitário no plano \(x = 0\), com
     \(0 \le y \le 1\) e \(0 \le z \le 1\). Verifique o teorema de Stokes
     calculando os dois lados.''',
     r'''<p><b>Lado do rotacional.</b> Com \(v_x = 0\),
     \(v_y = 2xz+3y^2\) e \(v_z = 4yz^2\),</p>
     <p>\[ \left(\rot{\vet{v}}\right)_x
        = \pder{v_z}{y} - \pder{v_y}{z} = 4z^2 - 2x, \]</p>
     <p>e sobre o plano \(x=0\) isso vale \(4z^2\). Com
     \(d\vet{a} = dy\,dz\,\vers{x}\),</p>
     <p>\[ \int_S \left(\rot{\vet{v}}\right)\cdot d\vet{a}
        = \int_0^1\!\!\int_0^1 4z^2\,dy\,dz = \frac{4}{3}. \]</p>
     <p><b>Lado da circulação.</b> Percorrendo a borda no sentido
     anti-horário visto de \(+x\), são quatro trechos. Nos dois com \(z\)
     constante e \(y\) variando, o integrando é \(v_y\,dy = 3y^2dy\) (porque
     \(x=0\)), que dá \(+1\) na ida e \(-1\) na volta: cancelam. Nos dois com
     \(y\) constante e \(z\) variando, o integrando é \(v_z\,dz = 4yz^2dz\),
     que dá \(0\) em \(y=0\) e \(4/3\) em \(y=1\), este último percorrido no
     sentido positivo.</p>
     <p>Somando, \(\oint \vet{v}\cdot d\vet{\ell} = 4/3\), igual ao outro lado.</p>
     <p><b>O que conferir depois.</b> Pelo teorema, qualquer outra superfície
     apoiada no mesmo quadrado tem de dar \(4/3\) também. Experimente com uma
     calota que se projete na direção \(+x\): o programa
     <code>teoremas_integrais.py</code> faz isso numericamente.</p>''' ),

    ('1.5  A delta em ação',
     r'''Calcule, usando as propriedades da função delta:
     (a) \(\int_{-2}^{3}\left(x^3 - 2x\right)\delta(x-1)\,dx\);
     (b) \(\int_{0}^{5}\cos x\,\delta(x-\pi)\,dx\);
     (c) \(\int_{V}\left(r^2 + 3\right)\delta^3(\vet{r}-\vet{a})\,d\tau\), com
     \(\vet{a} = (1,2,2)\) dentro de \(V\);
     (d) \(\int_{2}^{6}x\,\delta(x-8)\,dx\).''',
     r'''<p>(a) O ponto \(x=1\) está dentro do intervalo, de modo que a integral
     é o integrando avaliado ali: \(1 - 2 = -1\).</p>
     <p>(b) O ponto \(x=\pi \approx 3{,}14\) está dentro de \([0,5]\), e
     \(\cos\pi = -1\).</p>
     <p>(c) A delta tridimensional avalia a função no ponto \(\vet{a}\), onde
     \(r^2 = 1+4+4 = 9\). Logo a integral vale \(9+3 = 12\).</p>
     <p>(d) O ponto \(x=8\) está <em>fora</em> do intervalo \([2,6]\), e
     portanto a integral é <b>zero</b>. Não há nada a avaliar.</p>
     <p><b>A armadilha.</b> O item (d) é o único que costuma errar em prova. A
     delta não "puxa" o valor da função de qualquer jeito: ela só age se o seu
     pico estiver dentro do domínio de integração. Fora dele, o integrando é
     identicamente nulo.</p>''' ),

    ('1.6  Por que são quatro equações',
     r'''Use o teorema de Helmholtz para explicar, em poucas linhas, por que as
     equações de Maxwell são quatro e não duas, e por que \(\divg{\vet{B}} = 0\)
     é uma equação com conteúdo físico, e não uma trivialidade matemática.''',
     r'''<p><b>Por que quatro.</b> O teorema de Helmholtz diz que um campo
     vetorial que caia rápido o bastante no infinito fica completamente
     determinado quando se conhecem o seu divergente e o seu rotacional. São
     dois campos, \(\vet{E}\) e \(\vet{B}\), e duas informações por campo: por
     isso quatro equações, nem mais nem menos. Dar só o divergente de
     \(\vet{E}\), por exemplo, deixaria o campo indeterminado a menos de
     qualquer campo com divergente nulo.</p>
     <p><b>Por que \(\divg{\vet{B}} = 0\) diz algo.</b> Matematicamente, nada
     obriga um campo vetorial a ter divergente nulo; o divergente de
     \(\vet{E}\), afinal, não é. A equação afirma um fato experimental: não
     existe carga magnética isolada. Se um dia se achar um monopolo, essa
     equação muda para \(\divg{\vet{B}} = \mu_0\rho_m\), e nada na matemática se
     oporá.</p>
     <p>A identidade \(\divg{\left(\rot{\vet{A}}\right)} = 0\), essa sim, é
     trivialidade matemática, e é ela que permite escrever
     \(\vet{B} = \rot{\vet{A}}\) <em>porque</em> o divergente é nulo. Vale a
     pena não confundir as duas coisas: uma é observação sobre o mundo, a outra
     é consequência de derivadas parciais comutarem.</p>''' ),
]
