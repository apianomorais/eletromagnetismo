# -*- coding: utf-8 -*-
"""Exercícios propostos do capítulo 7, eletrodinâmica."""

LISTA = [
    ('7.1  Drude no alumínio',
     r'''O alumínio tem resistividade \(2{,}65\times10^{-8}\ \Omega\cdot
     \mathrm{m}\) e cerca de \(1{,}8\times10^{29}\) elétrons de condução por
     metro cúbico. Calcule o tempo médio entre colisões e o livre caminho
     médio, usando a velocidade de Fermi \(v_F = 2{,}0\times10^{6}\
     \mathrm{m/s}\). Comente por que usar a velocidade térmica clássica daria
     um número errado.''',
     r'''<p>Da condutividade \(\sigma = ne^2\tau/m\), com
     \(\sigma = 1/\rho = 3{,}77\times10^{7}\ \mathrm{S/m}\),</p>
     <p>\[ \tau = \frac{m\sigma}{ne^2}
        = \frac{9{,}11\times10^{-31}\times3{,}77\times10^{7}}
               {1{,}8\times10^{29}\times(1{,}60\times10^{-19})^2}
        = 7{,}5\times10^{-15}\ \mathrm{s}. \]</p>
     <p>O livre caminho médio é \(\ell = v_F\tau = 2{,}0\times10^{6}\times
     7{,}5\times10^{-15} = 1{,}5\times10^{-8}\ \mathrm{m}\), isto é 15 nm, ou
     umas cinquenta distâncias interatômicas.</p>
     <p><b>Por que não a velocidade térmica.</b> A velocidade térmica clássica,
     \(\sqrt{3\kB T/m} \approx 1{,}2\times10^{5}\ \mathrm{m/s}\), é dezesseis
     vezes menor, e daria um livre caminho de menos de um nanômetro, isto é,
     menos que a distância entre dois átomos. O conflito foi um dos primeiros
     sinais de que o gás de elétrons não é clássico: quem conduz são os
     elétrons da superfície de Fermi, que andam a \(v_F\), e essa velocidade
     quase não depende da temperatura.</p>''' ),

    ('7.2  A barra que escorrega sozinha',
     r'''A barra dos trilhos tem massa \(m\), comprimento \(h\), resistência
     total \(R\), e os trilhos são verticais, de modo que a gravidade a puxa.
     Ache a velocidade terminal e o tempo característico, e calcule os dois
     para \(m = 15\ \mathrm{g}\), \(h = 10\ \mathrm{cm}\),
     \(B = 0{,}45\ \mathrm{T}\) e \(R = 0{,}20\ \Omega\).''',
     r'''<p>A equação de movimento é</p>
     <p>\[ m\der{v}{t} = mg - \frac{(Bh)^2}{R}v, \]</p>
     <p>que é a mesma do texto com \(F = mg\). A velocidade terminal é onde a
     aceleração zera:</p>
     <p>\[ v_t = \frac{mgR}{(Bh)^2}
        = \frac{0{,}015\times9{,}8\times0{,}20}{(0{,}45\times0{,}10)^2}
        = \frac{0{,}0294}{2{,}025\times10^{-3}}
        = 14{,}5\ \mathrm{m/s}. \]</p>
     <p>O tempo característico é</p>
     <p>\[ \tau = \frac{mR}{(Bh)^2}
        = \frac{0{,}015\times0{,}20}{2{,}025\times10^{-3}}
        = 1{,}48\ \mathrm{s}. \]</p>
     <p><b>Leitura física.</b> Quatorze metros por segundo é rápido, e 1,5 s é
     muito: nesse arranjo o freio magnético quase não se nota. Para travar de
     verdade seria preciso \(B\) maior ou \(R\) menor; com \(R\) dez vezes
     menor, \(v_t\) cai para 1,5 m/s e \(\tau\) para 0,15 s. É exatamente isso
     que o ímã em queda dentro de um tubo de cobre faz: o "resistor" é a própria
     parede do tubo, de resistência baixíssima.</p>''' ),

    ('7.3  O gerador de bancada',
     r'''Uma bobina quadrada de lado \(12\ \mathrm{cm}\) com \(N = 200\) espiras
     gira a \(1800\ \mathrm{rpm}\) num campo uniforme de \(0{,}30\
     \mathrm{T}\), com o eixo perpendicular ao campo. Escreva a fem em função do
     tempo e calcule a amplitude e a frequência.''',
     r'''<p>O fluxo por espira é \(\Phi = BA\cos(\omega t)\), com
     \(A = 0{,}12^2 = 1{,}44\times10^{-2}\ \mathrm{m^2}\). Com \(N\) espiras,</p>
     <p>\[ \mathcal{E} = -N\der{\Phi}{t} = NBA\omega\sen(\omega t). \]</p>
     <p>A velocidade angular é</p>
     <p>\[ \omega = 1800\ \frac{\text{voltas}}{\text{min}}
        \times\frac{2\pi}{60} = 188{,}5\ \mathrm{rad/s}, \]</p>
     <p>isto é \(f = 30\ \mathrm{Hz}\). A amplitude é</p>
     <p>\[ \mathcal{E}_0 = NBA\omega
        = 200\times0{,}30\times1{,}44\times10^{-2}\times188{,}5
        = 163\ \mathrm{V}. \]</p>
     <p><b>Observações.</b> A fem é senoidal sem que ninguém tenha imposto
     senoide alguma: ela vem da geometria da rotação. E ela cresce linearmente
     com a rotação, o que explica por que geradores grandes giram devagar mas
     têm muitas espiras e campos altos: aumentar \(\omega\) custa caro em
     esforço mecânico.</p>''' ),

    ('7.4  A autoindutância do cabo coaxial',
     r'''Calcule a autoindutância por unidade de comprimento de um cabo coaxial
     de raio interno \(a\) e externo \(b\), supondo a corrente concentrada nas
     superfícies. Em seguida avalie para \(a = 0{,}5\ \mathrm{mm}\) e
     \(b = 3{,}5\ \mathrm{mm}\), que são valores típicos de um cabo de antena.''',
     r'''<p>Entre os condutores o campo é o de um fio, \(B = \mu_0 I/2\pi s\), e
     é nulo fora. O fluxo por unidade de comprimento, através da faixa retangular
     que vai de \(a\) até \(b\), é</p>
     <p>\[ \frac{\Phi}{\ell} = \int_a^b \frac{\mu_0 I}{2\pi s}\,ds
        = \frac{\mu_0 I}{2\pi}\ln\frac{b}{a}, \]</p>
     <p>e portanto</p>
     <p>\[ \frac{L}{\ell} = \frac{\mu_0}{2\pi}\ln\frac{b}{a}. \]</p>
     <p>Com os números, \(\ln(3{,}5/0{,}5) = \ln 7 = 1{,}95\), de modo que</p>
     <p>\[ \frac{L}{\ell} = 2\times10^{-7}\times1{,}95
        = 3{,}9\times10^{-7}\ \mathrm{H/m}
        = 0{,}39\ \mu\mathrm{H/m}. \]</p>
     <p><b>Por que isso importa.</b> Junto com a capacitância por unidade de
     comprimento, \(C/\ell = 2\pi\varepsilon_0/\ln(b/a)\), ela dá a impedância
     característica \(Z = \sqrt{L/C}\), que para este cabo vale
     \(117\ \Omega\) com dielétrico de ar. Com o polietileno que se usa de
     verdade, \(\varepsilon_r \approx 2{,}25\), cai para \(78\ \Omega\), que
     é a faixa dos \(75\ \Omega\) do cabo de antena. O capítulo 9 mostra que esse mesmo \(LC\) fixa também a
     velocidade do sinal no cabo.</p>''' ),

    ('7.5  Onde cabe mais energia',
     r'''Compare a densidade de energia de um campo magnético de \(1{,}0\
     \mathrm{T}\), que é o de um ímã supercondutor pequeno, com a de um campo
     elétrico de \(3{,}0\times10^{6}\ \mathrm{V/m}\), que é a rigidez
     dielétrica do ar. Comente o resultado.''',
     r'''<p>Para o campo magnético,</p>
     <p>\[ u_B = \frac{B^2}{2\mu_0} = \frac{1{,}0}{2\times4\pi\times10^{-7}}
        = 4{,}0\times10^{5}\ \mathrm{J/m^3}. \]</p>
     <p>Para o elétrico,</p>
     <p>\[ u_E = \tfrac12\varepsilon_0E^2
        = 0{,}5\times8{,}85\times10^{-12}\times(3{,}0\times10^{6})^2
        = 40\ \mathrm{J/m^3}. \]</p>
     <p>Uma razão de dez mil para um.</p>
     <p><b>Interpretação.</b> É muito mais fácil guardar energia em campo
     magnético do que em campo elétrico no ar, porque o ar rompe muito antes de
     o campo elétrico chegar perto. Ainda assim, \(4\times10^{5}\ \mathrm{J/m^3}\)
     é pouco: uma bateria de lítio guarda cerca de \(10^{9}\ \mathrm{J/m^3}\),
     quatro ordens de grandeza acima. Campo serve para transmitir energia, não
     para armazená-la.</p>''' ),

    ('7.6  O campo magnético dentro do capacitor',
     r'''Um capacitor de placas circulares de raio \(4{,}0\ \mathrm{cm}\) é
     carregado por uma corrente constante de \(0{,}50\ \mathrm{A}\). Calcule o
     campo magnético a \(2{,}0\ \mathrm{cm}\) do eixo, entre as placas, e na
     borda da placa. Depois verifique que a corrente de deslocamento total vale
     exatamente a corrente do fio.''',
     r'''<p>Entre as placas, com a corrente de deslocamento distribuída
     uniformemente na área,</p>
     <p>\[ B = \frac{\mu_0 I s}{2\pi R^2}. \]</p>
     <p>Em \(s = 2{,}0\ \mathrm{cm}\),</p>
     <p>\[ B = \frac{4\pi\times10^{-7}\times0{,}50\times0{,}020}
                  {2\pi\times(0{,}040)^2}
        = 1{,}25\times10^{-6}\ \mathrm{T}, \]</p>
     <p>e na borda, \(s = R\), dá o dobro, \(2{,}5\ \mu\mathrm{T}\), que é
     exatamente \(\mu_0I/2\pi R\), o campo do fio ali: as duas expressões se
     encontram, como tinham de se encontrar.</p>
     <p><b>A verificação.</b> Entre as placas \(E = \sigma/\varepsilon_0 =
     Q/\varepsilon_0\pi R^2\), de modo que</p>
     <p>\[ I_d = \varepsilon_0\der{}{t}\left(E\,\pi R^2\right)
        = \varepsilon_0\,\frac{\pi R^2}{\varepsilon_0\pi R^2}\der{Q}{t}
        = \der{Q}{t} = I. \]</p>
     <p>A corrente de deslocamento não é uma aproximação nem um truque: ela vale
     exatamente a corrente de condução, e é isso que torna a lei de Ampère
     consistente. Confira os números com
     <code>capacitor_deslocamento.py</code>.</p>''' ),
]
