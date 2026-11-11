# -*- coding: utf-8 -*-
"""Exercícios propostos do capítulo 8, leis de conservação."""

LISTA = [
    ('8.1  Onde viaja a energia num cabo coaxial',
     r'''Um cabo coaxial tem condutor interno de raio \(a = 1{,}0\ \mathrm{mm}\)
     e malha externa de raio \(b = 3{,}5\ \mathrm{mm}\). Ele alimenta uma carga
     com \(V = 50\ \mathrm{V}\) e \(I = 2{,}0\ \mathrm{A}\). Calcule o vetor de
     Poynting na região entre os condutores, integre sobre a seção reta e
     compare com \(VI\). Suponha os condutores perfeitos.''',
     r'''<p><b>Os campos.</b> Entre os condutores, pela lei de Gauss e pela lei
     de Ampère,</p>
     <p>\[ \vet{E} = \frac{\lambda}{2\pi\varepsilon_0 s}\vers{s},
        \qquad \vet{B} = \frac{\mu_0 I}{2\pi s}\vers{\phi}. \]</p>
     <p>A diferença de potencial entre os condutores liga \(\lambda\) a \(V\):</p>
     <p>\[ V = \frac{\lambda}{2\pi\varepsilon_0}\ln\frac{b}{a}
        \;\Longrightarrow\;
        \lambda = \frac{2\pi\varepsilon_0 V}{\ln(b/a)}
        = 2{,}22\ \mathrm{nC/m}. \]</p>
     <p><b>O Poynting.</b> Com \(\vet{E}\) radial e \(\vet{B}\) azimutal, o
     produto aponta ao longo do cabo:</p>
     <p>\[ \vet{S} = \frac{1}{\mu_0}\vet{E}\cruz\vet{B}
        = \frac{\lambda I}{4\pi^2\varepsilon_0 s^2}\vers{z}. \]</p>
     <p><b>O fluxo.</b> Integrando sobre a coroa, com \(da = 2\pi s\,ds\),</p>
     <p>\[ P = \int_a^b \frac{\lambda I}{4\pi^2\varepsilon_0 s^2}2\pi s\,ds
        = \frac{\lambda I}{2\pi\varepsilon_0}\ln\frac{b}{a} = VI
        = 100\ \mathrm{W}, \]</p>
     <p>exatamente a potência entregue.</p>
     <p><b>A leitura.</b> A energia viaja pelo <em>dielétrico</em>, no espaço
     vazio entre o condutor central e a malha; o cobre apenas segura os campos
     no lugar. Com condutores perfeitos não há campo elétrico dentro do metal e,
     portanto, não há nenhum fluxo de energia lá. É a mesma lição do exemplo do
     fio, agora com a energia sendo transportada em vez de dissipada: o cabo é
     um guia, e o que importa é o que acontece entre os condutores.</p>''' ),

    ('8.2  A vela solar',
     r'''A constante solar vale \(1361\ \mathrm{W/m^2}\) à distância da Terra.
     Calcule a pressão de radiação sobre uma superfície perfeitamente absorvente
     e sobre uma perfeitamente refletora. Depois estime o ganho de velocidade,
     em um ano, de uma vela refletora com densidade superficial de
     \(10\ \mathrm{g/m^2}\), ignorando a variação da distância ao Sol e a
     gravidade.''',
     r'''<p><b>A pressão.</b> A densidade de momento do campo é
     \(g = S/c^2\), e o fluxo de momento sobre a superfície é \(S/c\):</p>
     <p>\[ P_{\text{abs}} = \frac{S}{c} = \frac{1361}{3{,}00\times10^{8}}
        = 4{,}5\times10^{-6}\ \mathrm{Pa}. \]</p>
     <p>Na reflexão o momento não é apenas absorvido, é <em>invertido</em>, e a
     variação dobra:</p>
     <p>\[ P_{\text{ref}} = \frac{2S}{c} = 9{,}1\times10^{-6}\ \mathrm{Pa}. \]</p>
     <p>É dez bilhões de vezes menos que a pressão atmosférica. Numa vela de um
     quilômetro quadrado, dá 9 newtons.</p>
     <p><b>A aceleração.</b> Com \(\sigma = 0{,}010\ \mathrm{kg/m^2}\),</p>
     <p>\[ a = \frac{P_{\text{ref}}}{\sigma}
        = \frac{9{,}1\times10^{-6}}{0{,}010}
        = 9{,}1\times10^{-4}\ \mathrm{m/s^2}, \]</p>
     <p>e em um ano (\(3{,}16\times10^{7}\) s),</p>
     <p>\[ \Delta v = 2{,}9\times10^{4}\ \mathrm{m/s} = 29\ \mathrm{km/s}. \]</p>
     <p><b>Por que isso é interessante.</b> Nenhum foguete químico entrega
     29 km/s de incremento de velocidade, e a vela não carrega combustível
     nenhum. O preço é a paciência: a aceleração é mil vezes menor que a da
     gravidade terrestre, de modo que a vela só serve fora de um poço
     gravitacional profundo. A IKAROS japonesa, em 2010, foi a primeira a
     demonstrar propulsão por vela solar de fato, no caminho para Vênus.</p>''' ),

    ('8.3  A força de um eletroímã, pelo tensor',
     r'''Um eletroímã em forma de ferradura segura uma placa de ferro. Em cada
     um dos dois polos, de área \(10\ \mathrm{cm^2}\), o campo no entreferro vale
     \(1{,}0\ \mathrm{T}\). Use o tensor de tensões para obter a força de
     sustentação e converta para quilogramas-força.''',
     r'''<p><b>A tensão.</b> Tome uma superfície que corte o entreferro, com a
     normal paralela a \(\vet{B}\). A componente relevante é</p>
     <p>\[ T_{nn} = \frac{1}{\mu_0}\left(B_n^2-\tfrac12B^2\right)
        = \frac{B^2}{2\mu_0}, \]</p>
     <p>positiva, isto é, uma <em>tração</em> ao longo das linhas de campo: as
     linhas se comportam como elásticos esticados, puxando as faces uma contra a
     outra. (Na direção transversal o sinal se inverte, e as linhas se repelem
     lateralmente, como um feixe de elásticos que tende a se abrir.)</p>
     <p><b>Os números.</b> Por polo,</p>
     <p>\[ \frac{F}{A} = \frac{1{,}0^2}{2\times4\pi\times10^{-7}}
        = 4{,}0\times10^{5}\ \mathrm{Pa}, \]</p>
     <p>e com \(A = 10\ \mathrm{cm^2} = 10^{-3}\ \mathrm{m^2}\) em cada um dos
     dois polos,</p>
     <p>\[ F = 2\times4{,}0\times10^{5}\times10^{-3} = 8{,}0\times10^{2}\
        \mathrm{N}, \]</p>
     <p>cerca de <b>81 kgf</b>.</p>
     <p><b>Comentário.</b> Compare com a pressão eletrostática do exemplo do
     texto, 4,4 Pa a um megavolt por metro. A razão de cem mil é o que decide a
     engenharia: guindastes, alto-falantes, motores e travas elétricas são todos
     magnéticos. A exceção são os dispositivos microscópicos, em que as
     distâncias minúsculas permitem campos elétricos enormes sem ruptura, e por
     isso os atuadores de MEMS costumam ser eletrostáticos.</p>''' ),

    ('8.4  O momento angular escondido, pelo outro caminho',
     r'''No arranjo do exemplo do texto (cascas de raios \(a\) e \(b\) com cargas
     \(\pm Q\), solenoide de raio \(R\) com \(a \lt R \lt b\)), desligue a
     corrente lentamente. Calcule o torque que o campo elétrico induzido exerce
     sobre cada casca, integre no tempo e compare com o momento angular que
     estava guardado no campo.''',
     r'''<p><b>O campo induzido.</b> Pela lei de Faraday, para um círculo de raio
     \(s\),</p>
     <p>\[ E_\phi\,2\pi s = -\der{\Phi}{t}. \]</p>
     <p>Dentro do solenoide (\(s \lt R\)) o fluxo é \(\pi s^2 B\), e fora
     (\(s \gt R\)) é \(\pi R^2B\), de modo que</p>
     <p>\[ E_\phi = -\frac{s}{2}\der{B}{t}\ \ (s\lt R),
        \qquad
        E_\phi = -\frac{R^2}{2s}\der{B}{t}\ \ (s\gt R). \]</p>
     <p><b>Os torques.</b> Na casca interna, de raio \(a \lt R\) e carga \(+Q\),</p>
     <p>\[ \tau_z = a\,QE_\phi(a) = -\frac{Qa^2}{2}\der{B}{t}, \]</p>
     <p>e na externa, de raio \(b \gt R\) e carga \(-Q\),</p>
     <p>\[ \tau_z = b\left(-Q\right)E_\phi(b) = +\frac{QR^2}{2}\der{B}{t}. \]</p>
     <p>Somando,</p>
     <p>\[ \tau_z^{\text{tot}}
        = \frac{Q}{2}\left(R^2-a^2\right)\der{B}{t}. \]</p>
     <p><b>A integral no tempo.</b> Como \(B\) vai de \(\mu_0nI\) a zero,</p>
     <p>\[ \Delta L_z = \int\tau_z\,dt
        = \frac{Q}{2}\left(R^2-a^2\right)\int\der{B}{t}dt
        = -\frac{1}{2}\mu_0nIQ\left(R^2-a^2\right), \]</p>
     <p>que é <em>exatamente</em> o \(L_z\) calculado no texto como integral de
     \(\vet{r}\cruz\vet{g}\).</p>
     <p><b>Três observações.</b> O resultado não depende de quão depressa a
     corrente é desligada, apenas de quanto \(B\) variou no total. Ele também não
     depende de \(b\): o raio da casca externa some, porque fora do solenoide o
     campo induzido cai com \(1/s\) e o braço de alavanca cresce com \(s\). E o
     sentido é o esperado: o conjunto começa parado e termina girando, com o
     momento angular que o campo tinha desde o início.</p>''' ),

    ('8.5  Tudo junto numa onda plana',
     r'''Para uma onda plana monocromática,
     \(\vet{E} = E_0\cos(kz-\omega t)\vers{x}\) e
     \(\vet{B} = (E_0/c)\cos(kz-\omega t)\vers{y}\), calcule \(u\), \(\vet{S}\),
     \(\vet{g}\) e a componente \(T_{zz}\) do tensor. Mostre que
     \(S = uc\), que \(g = u/c\) e que a pressão sobre um absorvedor perfeito é
     a intensidade dividida por \(c\).''',
     r'''<p><b>A densidade de energia.</b> Com \(B = E/c\) e
     \(c^2 = 1/\varepsilon_0\mu_0\), as duas parcelas são iguais:</p>
     <p>\[ \frac{B^2}{2\mu_0} = \frac{E^2}{2\mu_0c^2}
        = \frac{\varepsilon_0E^2}{2}
        \;\Longrightarrow\;
        u = \varepsilon_0E_0^2\cos^2(kz-\omega t). \]</p>
     <p><b>O Poynting.</b></p>
     <p>\[ \vet{S} = \frac{EB}{\mu_0}\vers{z}
        = \frac{E^2}{\mu_0c}\vers{z}
        = \varepsilon_0cE^2\vers{z} = uc\,\vers{z}. \]</p>
     <p>A energia viaja na direção de propagação, com velocidade \(c\), como
     deveria.</p>
     <p><b>O momento.</b> \(\vet{g} = \vet{S}/c^2 = (u/c)\vers{z}\).</p>
     <p><b>O tensor.</b> Como \(E_z = B_z = 0\),</p>
     <p>\[ T_{zz} = \varepsilon_0\left(0-\tfrac12E^2\right)
        + \frac{1}{\mu_0}\left(0-\tfrac12B^2\right) = -u. \]</p>
     <p><b>A pressão.</b> O fluxo de momento na direção \(z\) através de um plano
     perpendicular a \(z\) é \(-T_{zz} = u\). Tomando a média temporal, com
     \(\langle\cos^2\rangle = 1/2\),</p>
     <p>\[ \langle u\rangle = \frac{\varepsilon_0E_0^2}{2}
        = \frac{I}{c}, \]</p>
     <p>já que a intensidade é \(I = \langle S\rangle = c\langle u\rangle\). Um
     absorvedor perfeito sente, portanto, uma pressão \(I/c\), que é o resultado
     usado no exercício da vela solar.</p>
     <p><b>A moral.</b> Numa onda plana, energia, momento e tensão não são três
     coisas: são a mesma coisa vista de três ângulos, ligadas por fatores de
     \(c\). A relatividade diz por quê, e a mecânica quântica traduz: um fóton
     de energia \(\mathcal{E}\) tem momento \(\mathcal{E}/c\).</p>''' ),

    ('8.6  A energia entra pela borda do capacitor',
     r'''Um capacitor de placas circulares de raio \(R\), separadas por \(d\),
     está sendo carregado, de modo que o campo entre elas cresce a uma taxa
     \(dE/dt\) constante. Calcule o campo magnético entre as placas, o vetor de
     Poynting na borda, e mostre que o fluxo para dentro é exatamente a taxa com
     que a energia armazenada cresce.''',
     r'''<p><b>O campo magnético.</b> Pela lei de Ampère-Maxwell, com corrente de
     deslocamento e sem corrente de condução, para um círculo de raio
     \(s \lt R\):</p>
     <p>\[ B_\phi\,2\pi s = \mu_0\varepsilon_0\pi s^2\der{E}{t}
        \;\Longrightarrow\;
        B_\phi = \frac{\mu_0\varepsilon_0 s}{2}\der{E}{t}. \]</p>
     <p><b>O Poynting na borda.</b> Com \(\vet{E}\) axial e \(\vet{B}\)
     azimutal, \(\vet{S}\) é radial, e em \(s = R\) aponta para <em>dentro</em>,
     com módulo</p>
     <p>\[ S = \frac{EB_\phi}{\mu_0}
        = \frac{\varepsilon_0 R}{2}E\der{E}{t}. \]</p>
     <p><b>O fluxo.</b> A área da borda é \(2\pi Rd\), de modo que a potência
     que entra é</p>
     <p>\[ P = \frac{\varepsilon_0R}{2}E\der{E}{t}\,2\pi Rd
        = \pi R^2d\,\varepsilon_0E\der{E}{t}. \]</p>
     <p><b>A energia armazenada.</b> O volume é \(\pi R^2d\) e a densidade é
     \(\varepsilon_0E^2/2\), de modo que</p>
     <p>\[ \der{U}{t} = \pi R^2d\,\der{}{t}\frac{\varepsilon_0E^2}{2}
        = \pi R^2d\,\varepsilon_0E\der{E}{t} = P. \]</p>
     <p>Fecha exatamente.</p>
     <p><b>O que aprender com isso.</b> Os fios chegam às placas pelo centro, mas
     a energia não entra por eles: ela entra <em>lateralmente</em>, pela borda
     aberta do capacitor, exatamente como no fio resistivo do texto. Repare
     ainda que nada disso funciona sem a corrente de deslocamento: sem ela não
     haveria campo magnético entre as placas, não haveria \(\vet{S}\), e a
     energia armazenada teria aparecido do nada. A conservação da energia é mais
     um argumento, ao lado da consistência com a continuidade da carga, para o
     termo que Maxwell acrescentou.</p>''' ),
]
