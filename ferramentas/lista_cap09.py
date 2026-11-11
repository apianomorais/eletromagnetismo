# -*- coding: utf-8 -*-
"""Exercícios propostos do capítulo 9, ondas eletromagnéticas."""

LISTA = [
    ('9.1  O campo elétrico de um laser de bolso',
     r'''Um apontador laser de \(5{,}0\ \mathrm{mW}\) tem feixe de
     \(1{,}0\ \mathrm{mm^2}\) de seção. Calcule a intensidade, a amplitude do
     campo elétrico e a do campo magnético, e compare com a rigidez dielétrica
     do ar (\(3\times10^{6}\ \mathrm{V/m}\)). Depois repita para o mesmo laser
     focalizado num ponto de \(10\ \mu\mathrm{m}\) de diâmetro.''',
     r'''<p><b>Feixe largo.</b> A intensidade é</p>
     <p>\[ I = \frac{5{,}0\times10^{-3}}{1{,}0\times10^{-6}}
        = 5{,}0\times10^{3}\ \mathrm{W/m^2}, \]</p>
     <p>quase quatro vezes a constante solar. De
     \(I = \frac12 c\varepsilon_0E_0^2\),</p>
     <p>\[ E_0 = \sqrt{\frac{2I}{c\varepsilon_0}} = 1{,}9\times10^{3}\
        \mathrm{V/m},\qquad B_0 = \frac{E_0}{c} = 6{,}5\ \mu\mathrm{T}. \]</p>
     <p>O campo é 1500 vezes menor que o de ruptura do ar: o feixe não ioniza
     nada.</p>
     <p><b>Focalizado.</b> Numa área de \(\pi(5\ \mu\mathrm{m})^2 =
     7{,}9\times10^{-11}\ \mathrm{m^2}\),</p>
     <p>\[ I = 6{,}4\times10^{7}\ \mathrm{W/m^2},
        \qquad E_0 = 2{,}2\times10^{5}\ \mathrm{V/m}, \]</p>
     <p>ainda catorze vezes abaixo da ruptura. <b>A moral:</b> focalizar
     aumenta a intensidade com o quadrado da redução do raio, mas o campo só
     com a primeira potência, porque \(E_0 \propto \sqrt{I}\). Para chegar a
     campos de ruptura é preciso pulsar, concentrando a mesma energia em
     nanossegundos.</p>''' ),

    ('9.2  A camada antirreflexo',
     r'''Mostre que uma camada fina de índice \(n\) sobre o vidro
     (\(n_v = 1{,}5\)) cancela a reflexão na incidência normal quando
     \(n = \sqrt{n_{ar}n_v}\) e a espessura é um quarto do comprimento de onda
     <em>dentro</em> da camada. Calcule os dois valores para
     \(\lambda = 550\ \mathrm{nm}\) e compare com o fluoreto de magnésio, que é
     o material usado na prática.''',
     r'''<p><b>A condição de espessura.</b> A onda refletida na face de cima e
     a refletida na face de baixo precisam sair em oposição de fase. A segunda
     percorre duas vezes a espessura \(d\) dentro da camada, de modo que a
     diferença de caminho óptico é \(2nd\); para oposição de fase, isso tem de
     valer meio comprimento de onda:</p>
     <p>\[ 2nd = \frac{\lambda}{2} \;\Longrightarrow\; d = \frac{\lambda}{4n}. \]</p>
     <p>(As duas reflexões são de meio menos denso para mais denso, e portanto
     ambas invertem a fase; as inversões se cancelam e não entram na conta.)</p>
     <p><b>A condição de índice.</b> Cancelar de verdade exige amplitudes
     iguais:</p>
     <p>\[ \frac{n-1}{n+1} = \frac{n_v-n}{n_v+n}
        \;\Longrightarrow\; n^2 = n_v \;\Longrightarrow\;
        n = \sqrt{n_v} = 1{,}225. \]</p>
     <p><b>Os números.</b> \(d = 550/(4\times1{,}225) = 112\ \mathrm{nm}\).</p>
     <p><b>Na prática.</b> Não existe material transparente, duro e aderente com
     \(n = 1{,}22\); o mais próximo é o MgF\(_2\), com \(n = 1{,}38\). Com ele a
     reflexão não zera, mas cai de 4 % para cerca de 1,3 %, o que já é uma
     melhora de três vezes. Revestimentos modernos usam várias camadas
     alternadas justamente para conseguir o cancelamento em toda a faixa
     visível, e não apenas em 550 nm.</p>''' ),

    ('9.3  O ângulo do óculos de pescador',
     r'''Calcule o ângulo de Brewster para a interface ar-água
     (\(n = 1{,}333\)) e explique, com a geometria, por que o óculos polarizado
     deve ter o eixo de transmissão <em>vertical</em>. O que acontece se a
     pessoa deitar a cabeça de lado?''',
     r'''<p><b>O ângulo.</b></p>
     <p>\[ \theta_B = \arctan(1{,}333) = 53{,}1^\circ, \]</p>
     <p>medido da normal, isto é, \(36{,}9^\circ\) acima da superfície. É mais
     ou menos a altura em que se olha a água a alguns metros de distância, e é
     por isso que o efeito é tão notável.</p>
     <p><b>A geometria.</b> O plano de incidência contém o raio e a normal à
     água, e é portanto <em>vertical</em>. No ângulo de Brewster a luz refletida
     é inteiramente polarizada perpendicularmente a esse plano, isto é,
     <em>horizontalmente</em>. Para cortá-la, o filtro precisa bloquear o
     horizontal, e portanto transmitir o vertical.</p>
     <p><b>Deitando a cabeça.</b> O eixo do filtro gira junto, e a 90° ele passa
     a transmitir justamente a componente horizontal: o brilho volta com força
     total. É um experimento de dois segundos, e convence mais que qualquer
     dedução.</p>''' ),

    ('9.4  A abertura numérica da fibra',
     r'''Uma fibra óptica tem núcleo de \(n_1 = 1{,}48\) e casca de
     \(n_2 = 1{,}46\). Ache o ângulo crítico na interface núcleo-casca e o maior
     ângulo, medido do eixo, com que um raio pode entrar pela ponta e ainda ser
     guiado. Comente a consequência para a dispersão modal.''',
     r'''<p><b>O ângulo crítico, dentro da fibra:</b></p>
     <p>\[ \theta_c = \arcsen\frac{n_2}{n_1}
        = \arcsen\frac{1{,}46}{1{,}48} = 80{,}6^\circ, \]</p>
     <p>medido da normal à interface, ou seja, apenas \(9{,}4^\circ\) do eixo da
     fibra. Os raios guiados são quase paralelos ao eixo.</p>
     <p><b>Na entrada.</b> Um raio que entra do ar com ângulo \(\theta_a\) do
     eixo refrata para \(\theta_1\) com \(\sen\theta_a = n_1\sen\theta_1\), e
     precisa bater na casca acima de \(\theta_c\). A conta dá a abertura
     numérica:</p>
     <p>\[ \mathrm{NA} = \sen\theta_{a,\max} = \sqrt{n_1^2-n_2^2}
        = \sqrt{1{,}48^2-1{,}46^2} = 0{,}243, \]</p>
     <p>isto é, \(\theta_{a,\max} = 14{,}0^\circ\).</p>
     <p><b>Dispersão modal.</b> O raio axial percorre \(L\); o raio no limite da
     aceitação percorre \(L/\sen\theta_c = L/0{,}986\), isto é, 1,4 % a mais. Em
     um quilômetro, isso são 14 metros de caminho extra, ou perto de 70 ns de
     atraso: pulsos vizinhos se misturam e a taxa de dados cai. É exatamente
     por isso que enlaces longos usam fibra monomodo, com núcleo de poucos
     micrômetros, em que só um caminho existe.</p>''' ),

    ('9.5  Quanta blindagem dá uma folha de alumínio',
     r'''Calcule a profundidade de pele do alumínio
     (\(\sigma = 3{,}77\times10^{7}\ \mathrm{S/m}\)) a \(1\ \mathrm{MHz}\) e a
     \(1\ \mathrm{GHz}\), e a atenuação, em decibéis, que uma folha de
     \(1{,}0\ \mathrm{mm}\) oferece em cada frequência. Depois explique por que
     a mesma folha não blinda o campo magnético de um ímã.''',
     r'''<p><b>As profundidades:</b></p>
     <p>\[ \delta = \sqrt{\frac{2}{\omega\mu_0\sigma}}
        = 82\ \mu\mathrm{m}\ (1\ \mathrm{MHz}),\qquad
        2{,}6\ \mu\mathrm{m}\ (1\ \mathrm{GHz}). \]</p>
     <p><b>A atenuação</b> de uma espessura \(d\) é \(e^{-d/\delta}\) em
     amplitude, isto é</p>
     <p>\[ \text{dB} = 20\log_{10}e^{d/\delta} = 8{,}686\,\frac{d}{\delta}. \]</p>
     <p>Com \(d = 1{,}0\) mm: <b>106 dB</b> a 1 MHz e <b>3350 dB</b> a 1 GHz. O
     segundo número é absurdo de tão grande e, na prática, a blindagem real é
     limitada pelas frestas, e não pelo metal.</p>
     <p><b>E o ímã?</b> A profundidade de pele vai a infinito quando
     \(\omega \to 0\): a fórmula já diz que campo estático atravessa. O
     mecanismo da blindagem é a corrente induzida, e campo que não varia não
     induz corrente nenhuma. Para blindar campo estático é preciso outra coisa:
     um material de \(\mu\) alto, como o mumetal, que desvia as linhas de campo
     por dentro de si, em vez de refleti-las.</p>''' ),

    ('9.6  Projetando um guia para 5 GHz',
     r'''Escolha as dimensões de um guia retangular para operar em
     \(5{,}0\ \mathrm{GHz}\) no modo fundamental, com margem para não propagar o
     segundo modo. Calcule as velocidades de fase e de grupo nessa frequência e
     verifique o produto. Compare com o guia padrão WR-187
     (\(a = 47{,}55\ \mathrm{mm}\), \(b = 22{,}15\ \mathrm{mm}\)).''',
     r'''<p><b>O critério.</b> Monomodo exige
     \(f_{10} \lt f \lt f_{20} = 2f_{10}\), e na prática se usa a faixa de
     1,25 a 1,9 vezes \(f_{10}\), para ficar longe das duas bordas.</p>
     <p>Tomando \(f_{10} = 3{,}2\ \mathrm{GHz}\),</p>
     <p>\[ a = \frac{c}{2f_{10}}
        = \frac{3{,}00\times10^{8}}{2\times3{,}2\times10^{9}}
        = 4{,}7\ \mathrm{cm}, \]</p>
     <p>e para \(b\) a regra usual é \(b \approx a/2\), que maximiza a potência
     antes da ruptura sem deixar TE\(_{01}\) entrar na faixa. Isso dá
     \(b \approx 2{,}3\ \mathrm{cm}\), e é <b>exatamente o WR-187</b>, cujas
     frequências de corte são 3,15 GHz (TE\(_{10}\)), 6,31 GHz (TE\(_{20}\)) e
     6,77 GHz (TE\(_{01}\)).</p>
     <p><b>As velocidades a 5 GHz.</b> Com \(f_{10}/f = 0{,}630\),</p>
     <p>\[ v_g = c\sqrt{1-0{,}630^2} = 0{,}776\,c,\qquad
        v_f = \frac{c}{0{,}776} = 1{,}288\,c, \]</p>
     <p>e \(v_fv_g = 0{,}999\,c^2\), como manda a relação exata
     \(v_fv_g = c^2\) (a diferença é arredondamento).</p>
     <p><b>Leitura.</b> O guia é dispersivo: a velocidade de grupo depende da
     frequência, e um pulso largo em banda se espalha ao viajar. Perto do corte
     a situação piora, e \(v_g \to 0\): a energia praticamente para. É por isso
     que ninguém opera um guia logo acima da frequência de corte, mesmo sendo
     tecnicamente possível.</p>''' ),
]
