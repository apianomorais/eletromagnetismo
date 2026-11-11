# -*- coding: utf-8 -*-
"""Exercícios propostos do capítulo 5, magnetostática."""

LISTA = [
    ('5.1  O cíclotron de bancada',
     r'''Um próton (\(q = 1{,}60\times10^{-19}\ \mathrm{C}\),
     \(m = 1{,}67\times10^{-27}\ \mathrm{kg}\)) entra perpendicularmente num
     campo uniforme de \(0{,}60\ \mathrm{T}\) com energia cinética de
     \(1{,}0\ \mathrm{MeV}\). Calcule o raio da órbita e o período, e diga por
     que o período não depende da energia enquanto a velocidade for pequena
     comparada à da luz.''',
     r'''<p>Da energia, \(v = \sqrt{2K/m}\), com
     \(K = 1{,}0\ \mathrm{MeV} = 1{,}60\times10^{-13}\ \mathrm{J}\):</p>
     <p>\[ v = \sqrt{\frac{2\times1{,}60\times10^{-13}}{1{,}67\times10^{-27}}}
        = 1{,}38\times10^{7}\ \mathrm{m/s}. \]</p>
     <p>O raio sai de \(qvB = mv^2/r\):</p>
     <p>\[ r = \frac{mv}{qB}
        = \frac{1{,}67\times10^{-27}\times1{,}38\times10^{7}}
               {1{,}60\times10^{-19}\times0{,}60}
        = 0{,}24\ \mathrm{m}. \]</p>
     <p>O período é \(T = 2\pi m/qB = 1{,}09\times10^{-7}\ \mathrm{s}\), isto é
     \(0{,}11\ \mu\mathrm{s}\), e a frequência de cíclotron é
     \(9{,}2\ \mathrm{MHz}\).</p>
     <p><b>Por que o período não depende da energia.</b> Dobrar a velocidade
     dobra o raio, e portanto dobra também o comprimento da volta; os dois
     efeitos se cancelam exatamente. É essa coincidência que torna o cíclotron
     possível, porque a tensão aceleradora pode oscilar com frequência fixa. Ela
     se perde quando \(v\) se aproxima de \(c\), porque aí a massa efetiva
     cresce com \(\gamma\) e o período aumenta: daí o síncrotron.</p>''' ),

    ('5.2  O seletor de velocidades',
     r'''Numa região há um campo elétrico de \(1{,}2\times10^{4}\ \mathrm{V/m}\)
     e um campo magnético de \(0{,}25\ \mathrm{T}\), perpendiculares entre si e
     ambos perpendiculares a um feixe de íons. Qual velocidade atravessa a
     região sem desviar? Mostre que a resposta não depende da carga nem da
     massa do íon, e explique o que acontece com os íons mais rápidos e mais
     lentos.''',
     r'''<p>A força total é \(\vet{F} = q(\vet{E} + \vet{v}\cruz\vet{B})\), e
     ela se anula quando \(E = vB\), ou seja</p>
     <p>\[ v = \frac{E}{B} = \frac{1{,}2\times10^{4}}{0{,}25}
        = 4{,}8\times10^{4}\ \mathrm{m/s}. \]</p>
     <p>A carga \(q\) aparece como fator comum nas duas forças e se cancela; a
     massa nem chega a entrar, porque a condição é de força nula e não de
     aceleração dada. Por isso o aparelho seleciona velocidade, e não energia
     nem momento.</p>
     <p>Um íon mais rápido tem a força magnética maior que a elétrica e é
     desviado no sentido de \(\vet{v}\cruz\vet{B}\); um mais lento é desviado no
     sentido oposto, pela força elétrica. Colocando uma fenda na saída, só a
     velocidade certa passa. É o primeiro estágio de um espectrômetro de massa:
     o segundo estágio, com só campo magnético, aí sim separa por \(m/q\).</p>''' ),

    ('5.3  A força sobre meio círculo',
     r'''Um fio conduz corrente \(I\) e tem a forma de um semicírculo de raio
     \(a\) fechado pelo diâmetro, todo num plano perpendicular a um campo
     uniforme \(\vet{B}\). Calcule a força sobre o arco e sobre o diâmetro, e
     mostre que a força total sobre o circuito fechado é nula.''',
     r'''<p>Para um fio num campo uniforme, a força é</p>
     <p>\[ \vet{F} = I\int d\vet{\ell}\cruz\vet{B}
        = I\left(\int d\vet{\ell}\right)\cruz\vet{B}, \]</p>
     <p>porque \(\vet{B}\) é constante e sai da integral. Ou seja, <b>só importa
     o vetor que liga as duas pontas</b>, e não o caminho.</p>
     <p>Para o arco, esse vetor é o diâmetro, de módulo \(2a\), de modo que
     \(F_{\text{arco}} = 2aIB\), perpendicular ao diâmetro e ao campo. Para o
     segmento reto, o vetor é o mesmo diâmetro, porém percorrido no sentido
     contrário, de modo que \(F_{\text{reta}} = 2aIB\) na direção oposta.</p>
     <p>A soma é nula, e tinha de ser: num circuito fechado,
     \(\oint d\vet{\ell} = 0\), e portanto a força resultante num campo uniforme
     é sempre zero. Sobra o torque, que é o assunto do capítulo 6.</p>''' ),

    ('5.4  O fio grosso com corrente mal distribuída',
     r'''Um fio cilíndrico de raio \(a\) conduz corrente total \(I\), mas com
     densidade que cresce com a distância ao eixo, \(J(s) = k s\). Ache \(k\) em
     função de \(I\) e \(a\), e calcule \(B(s)\) dentro e fora do fio. Compare o
     resultado interno com o do fio de densidade uniforme.''',
     r'''<p>A corrente total fixa \(k\):</p>
     <p>\[ I = \int_0^a k s\,(2\pi s\,ds) = \frac{2\pi k a^3}{3}
        \;\Longrightarrow\; k = \frac{3I}{2\pi a^3}. \]</p>
     <p>Para \(s \lt a\), a corrente enlaçada é</p>
     <p>\[ I_{\text{enl}} = \frac{2\pi k s^3}{3} = I\frac{s^3}{a^3}, \]</p>
     <p>e a lei de Ampère dá</p>
     <p>\[ B\,(2\pi s) = \mu_0 I\frac{s^3}{a^3}
        \;\Longrightarrow\; B = \frac{\mu_0 I s^2}{2\pi a^3}. \]</p>
     <p>Fora, a corrente enlaçada é \(I\) e vale o resultado de sempre,
     \(B = \mu_0 I/2\pi s\), que é contínuo com o de dentro em \(s=a\).</p>
     <p><b>Comparação.</b> Com densidade uniforme o campo interno cresce
     linearmente, \(B \propto s\); aqui ele cresce com \(s^2\), porque há menos
     corrente perto do eixo. Em ambos os casos o campo externo é idêntico: de
     fora não se enxerga como a corrente está distribuída, só o total. É o
     análogo magnético do teorema das cascas da eletrostática.</p>''' ),

    ('5.5  O campo na boca do solenoide',
     r'''Mostre, por Biot-Savart, que o campo no centro da extremidade de um
     solenoide semi-infinito vale metade do campo no interior profundo,
     \(B = \mu_0 n I/2\). Em seguida estime o erro de usar \(\mu_0 n I\) no
     centro de um solenoide real de comprimento \(L = 20\ \mathrm{cm}\) e raio
     \(R = 2{,}0\ \mathrm{cm}\).''',
     r'''<p>O campo no eixo, a uma distância \(z\) de uma espira de raio \(R\),
     vale \(\mu_0 I R^2/2(R^2+z^2)^{3/2}\). Somando as espiras de um solenoide
     com \(n\) por unidade de comprimento, a contribuição das que estão entre
     \(z\) e \(z+dz\) é \(n\,dz\) vezes isso. Para o solenoide que vai de
     \(z = 0\) a \(\infty\), com o ponto na boca,</p>
     <p>\[ B = \frac{\mu_0 n I R^2}{2}\int_0^{\infty}
        \frac{dz}{(R^2+z^2)^{3/2}}
        = \frac{\mu_0 n I R^2}{2}\cdot\frac{1}{R^2}
        = \frac{\mu_0 n I}{2}. \]</p>
     <p>Para o solenoide infinito nos dois sentidos a integral vai de
     \(-\infty\) a \(\infty\) e dá o dobro, \(\mu_0 n I\), como manda a lei de
     Ampère.</p>
     <p><b>O solenoide real.</b> Integrando de \(-L/2\) a \(L/2\) com o ponto no
     centro, sai</p>
     <p>\[ B = \mu_0 n I\,\frac{L/2}{\sqrt{R^2+(L/2)^2}}
        = \mu_0 n I\,\frac{0{,}10}{\sqrt{0{,}02^2+0{,}10^2}}
        = 0{,}981\,\mu_0 n I. \]</p>
     <p>O erro é de 1,9 %, e cai com \((R/L)^2\). É por isso que a aproximação
     de solenoide infinito funciona tão bem em laboratório: basta o comprimento
     ser umas cinco vezes o diâmetro.</p>''' ),

    ('5.6  Uma casca com outra corrente: qual multipolo sobrevive',
     r'''Repita o raciocínio do exemplo da casca girante, mas com uma corrente
     superficial que varia como \(\vet{K} = K_0\sen\theta'\cos\theta'\,
     \vers{\phi}'\) em vez de \(\sen\theta'\). Mostre, sem calcular nenhuma
     integral difícil, qual termo da série de Legendre sobrevive, e conclua se o
     campo externo ainda é um dipolo puro.''',
     r'''<p>No exemplo da casca girante, a integral angular que decide tudo é
     \(\int_{-1}^{1} u\,P_l(u)\,du\), que é o produto escalar de \(P_1\) com
     \(P_l\). A dependência angular da fonte entra ali, e a ortogonalidade faz o
     resto.</p>
     <p>Com \(\vet{K} \propto \sen\theta'\cos\theta'\), o papel de \(u\) passa a
     ser ocupado por \(u\sqrt{1-u^2}\)... convém reescrever de outro jeito: a
     fonte agora é proporcional a \(\sen\theta'\cos\theta'\), e a família
     angular natural para correntes azimutais é a dos polinômios associados
     \(P_l^1(\cos\theta')\). Os dois primeiros são</p>
     <p>\[ P_1^1 = -\sen\theta',\qquad P_2^1 = -3\sen\theta'\cos\theta'. \]</p>
     <p>Ou seja: a corrente do exemplo era puro \(P_1^1\), e esta é puro
     \(P_2^1\). Pela ortogonalidade, o único termo que sobrevive agora é o de
     \(l = 2\).</p>
     <p><b>Conclusão.</b> O campo externo não é mais dipolo nenhum: o momento de
     dipolo é <em>zero</em>, e o termo de menor ordem é o quadrupolo, que cai
     com \(1/r^4\) em vez de \(1/r^3\). Fisicamente faz sentido: a corrente
     muda de sentido no equador (\(\cos\theta'\) troca de sinal), de modo que os
     dois hemisférios produzem momentos opostos que se cancelam.</p>
     <p>Confira com o programa <code>casca_legendre.py</code>: troque a
     dependência angular da corrente e veja os coeficientes mudarem de linha na
     tabela.</p>''' ),
]
