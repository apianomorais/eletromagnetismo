# -*- coding: utf-8 -*-
"""Exercícios propostos do capítulo 6, campos magnéticos na matéria."""

LISTA = [
    ('6.1  Quanto vale o alinhamento, de verdade',
     r'''Uma amostra paramagnética tem \(n = 5{,}0\times10^{27}\) átomos por
     metro cúbico, cada um com momento \(\mu = 1{,}0\,\mu_B\). Compare a energia
     de alinhamento \(\mu B\) num campo de \(1{,}0\ \mathrm{T}\) com a energia
     térmica a \(300\ \mathrm{K}\), e estime a fração de momentos efetivamente
     alinhados e a magnetização resultante.''',
     r'''<p>A energia de alinhamento é</p>
     <p>\[ \mu B = 9{,}27\times10^{-24}\times1{,}0
        = 9{,}27\times10^{-24}\ \mathrm{J}, \]</p>
     <p>e a térmica é \(\kB T = 1{,}38\times10^{-23}\times300 =
     4{,}14\times10^{-21}\ \mathrm{J}\). A razão é</p>
     <p>\[ \frac{\mu B}{\kB T} = 2{,}2\times10^{-3}. \]</p>
     <p>Dois milésimos. No regime de campo fraco a magnetização vale
     \(M \approx n\mu\,(\mu B/\kB T)\), de modo que a fração alinhada é da ordem
     de \(0{,}2\,\%\) e</p>
     <p>\[ M \approx 5{,}0\times10^{27}\times9{,}27\times10^{-24}
        \times2{,}2\times10^{-3} \approx 1{,}0\times10^{2}\ \mathrm{A/m}, \]</p>
     <p>que corresponde a \(\mu_0 M \approx 1{,}3\times10^{-4}\ \mathrm{T}\),
     isto é \(\chi_m \sim 10^{-4}\).</p>
     <p><b>A moral.</b> Mesmo num campo de um tesla, que já é um ímã
     supercondutor pequeno, o alinhamento é quase nada. A agitação térmica ganha
     por três ordens de grandeza, e é por isso que o paramagnetismo é fraco e
     depende de \(1/T\). O ferromagnetismo só é forte porque não depende do
     campo externo para alinhar: quem alinha é o vizinho.</p>''' ),

    ('6.2  Corrente ligada num cilindro mal magnetizado',
     r'''Um cilindro longo de raio \(a\) tem magnetização que cresce com a
     distância ao eixo, \(\vet{M} = k s\,\vers{\phi}\). Calcule as correntes
     ligadas de volume e de superfície, verifique que a corrente total é nula e
     ache \(\vet{B}\) dentro e fora.''',
     r'''<p>Em cilíndricas, com \(\vet{M} = M_\phi(s)\vers{\phi}\),</p>
     <p>\[ \vet{J}_b = \rot{\vet{M}}
        = \frac{1}{s}\der{(sM_\phi)}{s}\vers{z}
        = \frac{1}{s}\der{(ks^2)}{s}\vers{z} = 2k\,\vers{z}, \]</p>
     <p>uniforme. Na superfície,</p>
     <p>\[ \vet{K}_b = \vet{M}\cruz\vers{n}
        = ka\,\vers{\phi}\cruz\vers{s} = -ka\,\vers{z}. \]</p>
     <p><b>A corrente total.</b> No volume, \(2k \times \pi a^2 = 2\pi k a^2\);
     na superfície, \(-ka \times 2\pi a = -2\pi k a^2\). Somam zero, como tem de
     ser: corrente ligada não transporta carga para lugar nenhum.</p>
     <p><b>O campo.</b> Fora, a corrente enlaçada é nula e portanto
     \(\vet{B} = 0\). Dentro, pela lei de Ampère com a corrente ligada de
     volume,</p>
     <p>\[ B\,(2\pi s) = \mu_0\,2k\,\pi s^2
        \;\Longrightarrow\; \vet{B} = \mu_0 k s\,\vers{\phi} = \mu_0\vet{M}, \]</p>
     <p>o que também sai de imediato de \(\vet{H} = 0\), já que não há corrente
     livre e a simetria obriga \(\vet{H}\) a ser azimutal e com circulação
     nula.</p>''' ),

    ('6.3  O torque que a bússola sente',
     r'''A agulha de uma bússola tem momento magnético
     \(m = 0{,}80\ \mathrm{A\,m^2}\) e está num campo horizontal de
     \(2{,}5\times10^{-5}\ \mathrm{T}\), que é a ordem do campo terrestre.
     Calcule o torque máximo e a energia necessária para virar a agulha de
     ponta-cabeça. Compare com a energia de uma formiga de 5 mg subindo
     1 cm.''',
     r'''<p>O torque é \(\tau = mB\sen\theta\), máximo em \(\theta = 90^\circ\):</p>
     <p>\[ \tau_{\max} = 0{,}80\times2{,}5\times10^{-5}
        = 2{,}0\times10^{-5}\ \mathrm{N\,m}. \]</p>
     <p>A energia é \(U = -\vet{m}\cdot\vet{B}\), de modo que virar de
     \(\theta = 0\) para \(\theta = 180^\circ\) custa</p>
     <p>\[ \Delta U = 2mB = 4{,}0\times10^{-5}\ \mathrm{J}. \]</p>
     <p>A formiga: \(mgh = 5\times10^{-6}\times9{,}8\times0{,}01 =
     4{,}9\times10^{-7}\ \mathrm{J}\), isto é, oitenta vezes menos.</p>
     <p><b>Interpretação.</b> O campo terrestre é fraco, mas a agulha é leve e o
     atrito do pivô é minúsculo, de modo que esse torque basta. É também por isso
     que a bússola é tão sensível a qualquer ferro por perto: um prego a dez
     centímetros produz facilmente mais do que \(2{,}5\times10^{-5}\
     \mathrm{T}\).</p>''' ),

    ('6.4  O entreferro domina o circuito magnético',
     r'''Um toroide de ferro de permeabilidade relativa \(\mu_r = 2000\),
     comprimento médio \(\ell = 30\ \mathrm{cm}\), tem um entreferro de ar de
     \(g = 1{,}0\ \mathrm{mm}\). Com \(N = 500\) espiras e \(I = 1{,}5\
     \mathrm{A}\), calcule \(B\) no entreferro, supondo que o fluxo não se
     espalhe nas bordas.''',
     r'''<p>A lei de Ampère para \(\vet{H}\) dá, ao longo do caminho médio,</p>
     <p>\[ H_{\text{fe}}(\ell - g) + H_{\text{ar}}\,g = NI. \]</p>
     <p>A componente normal de \(\vet{B}\) é contínua na interface, de modo que
     \(B\) é o mesmo nos dois meios, e</p>
     <p>\[ H_{\text{fe}} = \frac{B}{\mu_r\mu_0},\qquad
        H_{\text{ar}} = \frac{B}{\mu_0}. \]</p>
     <p>Substituindo,</p>
     <p>\[ B = \frac{\mu_0 NI}{\dfrac{\ell-g}{\mu_r} + g}
        = \frac{4\pi\times10^{-7}\times500\times1{,}5}
               {\dfrac{0{,}299}{2000} + 0{,}0010}
        = \frac{9{,}42\times10^{-4}}{1{,}15\times10^{-3}}
        = 0{,}82\ \mathrm{T}. \]</p>
     <p><b>O que o resultado ensina.</b> O entreferro tem um milímetro contra
     trinta centímetros de ferro, e mesmo assim responde por 87 % da
     "resistência magnética" do circuito, porque o ferro é dois mil vezes mais
     permeável. Fechando o entreferro, a mesma conta daria \(6{,}3\
     \mathrm{T}\), quase oito vezes mais, resultado que o ferro não entrega:
     ele satura em torno de \(2\ \mathrm{T}\) e a permeabilidade despenca
     muito antes disso. Em compensação, é no entreferro que o campo fica
     acessível, e é por isso que todo eletroímã útil tem um.</p>''' ),

    ('6.5  A energia que o transformador joga fora',
     r'''O laço de histerese de um material tem área equivalente a
     \(240\ \mathrm{J/m^3}\) por ciclo. Um núcleo de transformador desse
     material tem volume de \(1{,}2\times10^{-3}\ \mathrm{m^3}\) e opera a
     \(60\ \mathrm{Hz}\). Calcule a potência perdida só por histerese e compare
     com um transformador de 500 W.''',
     r'''<p>A área do laço é a energia dissipada por unidade de volume e por
     ciclo. Logo</p>
     <p>\[ \wp = (240\ \mathrm{J/m^3})\times(1{,}2\times10^{-3}\ \mathrm{m^3})
        \times(60\ \mathrm{s^{-1}}) = 17{,}3\ \mathrm{W}. \]</p>
     <p>Contra 500 W de potência útil, isso é 3,5 % só de histerese, sem contar
     as perdas por corrente de Foucault e as ôhmicas do enrolamento.</p>
     <p><b>Por isso o material importa.</b> Um aço-silício de grão orientado tem
     laço bem mais estreito que o do exemplo, e os ferrites, usados em alta
     frequência, mais estreito ainda. Repare que a perda cresce linearmente com
     a frequência: a 60 Hz ela é tolerável, a 100 kHz, numa fonte chaveada, o
     mesmo material derreteria o núcleo.</p>''' ),

    ('6.6  Uma esfera com magnetização não uniforme',
     r'''Uma esfera de raio \(R\) tem magnetização \(\vet{M} = M_0
     \left(\frac{3}{2}\cos^2\theta - \frac{1}{2}\right)\vers{r}\), isto é,
     radial e proporcional a \(P_2(\cos\theta)\). Usando o potencial escalar
     magnético, diga qual termo da série de Legendre sobrevive e escreva
     \(\vet{H}\) dentro e fora, sem fazer nenhuma integral difícil.''',
     r'''<p>A magnetização é radial, de modo que a carga magnética efetiva de
     superfície é</p>
     <p>\[ \sigma_m = \vet{M}\cdot\vers{n} = M_0 P_2(\cos\theta), \]</p>
     <p>e, como \(\vet{M}\) não depende de \(r\), não há carga de volume:
     \(\divg{\vet{M}} = \frac{1}{r^2}\partial_r(r^2 M_r) = \frac{2M_r}{r}\),
     que não é nula, atenção: aparece sim uma densidade de volume
     \(\rho_m = -\divg{\vet{M}} = -2M_0P_2/r\). Trate-a como fonte distribuída,
     ou resolva por superposição; o essencial para esta questão é a estrutura
     angular.</p>
     <p><b>A estrutura angular.</b> Tanto a fonte de superfície quanto a de
     volume são proporcionais a \(P_2(\cos\theta)\). Pela ortogonalidade dos
     polinômios de Legendre, só o termo \(l = 2\) da série pode ser excitado:</p>
     <p>\[ W_{\text{dentro}} = A_2\,r^2 P_2(\cos\theta),\qquad
        W_{\text{fora}} = \frac{B_2}{r^3}P_2(\cos\theta), \]</p>
     <p>e \(\vet{H} = -\nabla W\) em cada região. Os coeficientes saem das duas
     condições de contorno em \(r = R\), como no exemplo da esfera
     uniformemente magnetizada, trocando \(l = 1\) por \(l = 2\).</p>
     <p><b>O que isso diz.</b> Não há dipolo: o momento de dipolo desta esfera é
     rigorosamente nulo, e o campo externo cai como \(1/r^4\), não como
     \(1/r^3\). A estrutura angular da fonte decide, sozinha, qual multipolo
     existe, e é essa a utilidade prática da base de Legendre.</p>''' ),
]
