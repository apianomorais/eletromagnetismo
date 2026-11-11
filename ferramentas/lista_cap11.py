# -*- coding: utf-8 -*-
"""Exercícios propostos do capítulo 11, radiação."""

LISTA = [
    ('11.1  Um elétron ao sol',
     r'''Um elétron livre está exposto à luz solar, de intensidade
     \(1361\ \mathrm{W/m^2}\). Calcule a amplitude do campo elétrico, a
     amplitude da aceleração do elétron e a potência que ele irradia. Depois
     obtenha a seção de choque dividindo uma pela outra e compare com
     \(\sigma_T = 8\pi r_e^2/3\).''',
     r'''<p><b>O campo.</b> De \(I = \frac12c\varepsilon_0E_0^2\),</p>
     <p>\[ E_0 = \sqrt{\frac{2I}{c\varepsilon_0}}
        = 1{,}013\times10^{3}\ \mathrm{V/m}. \]</p>
     <p><b>A aceleração.</b></p>
     <p>\[ a_0 = \frac{eE_0}{m} = 1{,}78\times10^{14}\ \mathrm{m/s^2}, \]</p>
     <p>um número que impressiona até lembrarmos que a massa do elétron é
     \(9\times10^{-31}\) kg.</p>
     <p><b>A potência.</b> Com \(\langle a^2\rangle = a_0^2/2\),</p>
     <p>\[ \langle P\rangle = \frac{\mu_0e^2\langle a^2\rangle}{6\pi c}
        = 9{,}05\times10^{-26}\ \mathrm{W}. \]</p>
     <p><b>A seção de choque.</b></p>
     <p>\[ \sigma = \frac{\langle P\rangle}{I}
        = \frac{9{,}05\times10^{-26}}{1361}
        = 6{,}65\times10^{-29}\ \mathrm{m^2}, \]</p>
     <p>exatamente \(\sigma_T\), como tem de ser: a seção de choque de Thomson
     <em>é</em> essa razão.</p>
     <p><b>Leitura.</b> O elétron intercepta uma área de
     \(6{,}65\times10^{-29}\ \mathrm{m^2}\), isto é, cerca de
     \(10^{-9}\) vezes a seção de um átomo. Um gás de elétrons livres é
     quase transparente, e só fica opaco quando a coluna é astronômica: é por
     isso que \(\sigma_T\) governa a opacidade do interior das estrelas e o
     momento em que o universo, ao esfriar e recombinar, ficou
     transparente.</p>''' ),

    ('11.2  Quanto tempo dura o átomo clássico',
     r'''Um elétron em órbita circular de raio \(r\) em torno de um próton
     irradia pela fórmula de Larmor e, portanto, espirala para dentro. Monte a
     equação para \(r(t)\), integre-a e calcule o tempo até o colapso partindo
     do raio de Bohr. Quantas voltas ele dá nesse tempo?''',
     r'''<p><b>A energia e a aceleração.</b> Para a órbita circular,</p>
     <p>\[ E(r) = -\frac{e^2}{8\pi\varepsilon_0 r},
        \qquad a = \frac{e^2}{4\pi\varepsilon_0 mr^2}. \]</p>
     <p><b>A equação.</b> Impondo \(dE/dt = -P\) com Larmor,</p>
     <p>\[ \frac{e^2}{8\pi\varepsilon_0 r^2}\der{r}{t}
        = -\frac{\mu_0e^2}{6\pi c}
          \left(\frac{e^2}{4\pi\varepsilon_0 mr^2}\right)^2, \]</p>
     <p>que, em termos do raio clássico do elétron
     \(r_e = e^2/4\pi\varepsilon_0mc^2\), se reduz a</p>
     <p>\[ \der{r}{t} = -\frac{4}{3}\,\frac{cr_e^2}{r^2}. \]</p>
     <p><b>A integral.</b> Separando e integrando de \(a_0\) até zero,</p>
     <p>\[ t = \frac{a_0^3}{4cr_e^2}
        = \frac{\left(5{,}29\times10^{-11}\right)^3}
               {4\times3{,}00\times10^{8}\times
                \left(2{,}82\times10^{-15}\right)^2}
        = 1{,}56\times10^{-11}\ \mathrm{s}. \]</p>
     <p><b>As voltas.</b> O período inicial é
     \(T = 2\pi a_0/v = 1{,}52\times10^{-16}\) s, de modo que o elétron dá
     cerca de \(1{,}0\times10^{5}\) voltas antes de cair. Parece muito, e são
     16 picossegundos.</p>
     <p><b>A moral.</b> Se o eletromagnetismo clássico valesse dentro do átomo,
     toda a matéria teria colapsado em dezenas de picossegundos, emitindo um
     clarão de espectro contínuo. A matéria existir, e os espectros atômicos
     serem discretos, são os dois fatos que forçaram a quantização. Repare que
     o argumento não é vago: ele dá um número, e o número está errado por
     todas as ordens de grandeza possíveis.</p>''' ),

    ('11.3  Por que a antena curta é um mau negócio',
     r'''Uma antena de \(60\ \mathrm{cm}\) opera em \(10\ \mathrm{MHz}\), feita
     de um bastão de cobre de \(2\ \mathrm{mm}\) de raio
     (\(\sigma = 5{,}96\times10^{7}\ \mathrm{S/m}\)). Calcule a resistência de
     radiação (com perfil de corrente triangular) e a resistência ôhmica em
     alta frequência, e obtenha a eficiência. Comente.''',
     r'''<p><b>A resistência de radiação.</b> Com
     \(\lambda = c/f = 30\ \mathrm{m}\), \(d/\lambda = 0{,}020\), e corrente
     triangular,</p>
     <p>\[ R_{\text{rad}} = 20\pi^2\left(\frac{d}{\lambda}\right)^2
        = 20\pi^2\times4{,}0\times10^{-4}
        = 0{,}079\ \Omega. \]</p>
     <p><b>A resistência ôhmica.</b> Em 10 MHz a corrente só ocupa uma casca
     de espessura \(\delta\) (capítulo 9):</p>
     <p>\[ \delta = \sqrt{\frac{2}{\omega\mu_0\sigma}}
        = 2{,}06\times10^{-5}\ \mathrm{m}, \]</p>
     <p>de modo que a seção útil é \(2\pi a\delta\) e</p>
     <p>\[ R_\Omega = \frac{d}{\sigma\,2\pi a\delta}
        = 0{,}0388\ \Omega. \]</p>
     <p><b>A eficiência.</b></p>
     <p>\[ \eta = \frac{R_{\text{rad}}}{R_{\text{rad}}+R_\Omega}
        = \frac{0{,}079}{0{,}118} = 67\ \%. \]</p>
     <p><b>Comentário.</b> Dois terços da potência vira onda e um terço vira
     calor, e isso com um bastão de cobre grosso. Encurte a antena pela metade
     e \(R_{\text{rad}}\) cai por quatro, para 0,020 Ω, enquanto
     \(R_\Omega\) cai só por dois: a eficiência despenca para 51 %. Encurte
     mais e a antena vira um aquecedor. É o dilema de toda antena de rádio de
     onda média num carro, e a razão pela qual elas vêm com bobinas de carga,
     que aumentam a corrente efetiva sem encurtar mais a estrutura.</p>''' ),

    ('11.4  O próximo colisor circular',
     r'''O projeto FCC-ee prevê um anel com raio de curvatura
     \(\rho = 10\,760\ \mathrm{m}\) operando com elétrons a
     \(182{,}5\ \mathrm{GeV}\). Calcule a energia perdida por volta. Depois
     estime quanto seria perdido se a mesma máquina acelerasse múons
     (\(m_\mu = 207\,m_e\)) na mesma energia, e comente a proposta de um
     colisor de múons.''',
     r'''<p><b>Elétrons.</b> Pela regra prática do texto,</p>
     <p>\[ \Delta E\,[\mathrm{keV}] = 88{,}46\,\frac{E^4}{\rho}
        = 88{,}46\times\frac{182{,}5^4}{10\,760}
        = 9{,}12\times10^{6}\ \mathrm{keV}, \]</p>
     <p>isto é, <b>9,1 GeV por volta</b>, ou 5 % da energia do feixe a cada
     27 km percorridos. Repondo isso a cada volta, a máquina precisa de uma
     potência de radiofrequência da ordem de 50 MW por feixe.</p>
     <p><b>Múons.</b> A perda vai com \(1/m^4\):</p>
     <p>\[ \frac{\Delta E_\mu}{\Delta E_e} = \frac{1}{207^4}
        = 5{,}5\times10^{-10}, \]</p>
     <p>de modo que a perda cairia para cerca de \(5\ \mathrm{eV}\) por volta.
     Radiação deixaria completamente de ser um problema.</p>
     <p><b>A proposta, e o problema dela.</b> O múon é pesado o bastante para
     não irradiar e leve o bastante para ser acelerado, e é uma partícula
     elementar, de modo que toda a sua energia entra na colisão (diferente do
     próton, em que só uma fração vai para o quark que colide). O obstáculo é
     outro: o múon decai em \(2{,}2\ \mu\mathrm{s}\) de tempo próprio. A
     dilatação temporal ajuda, mas obriga a acelerar, armazenar e colidir tudo
     em milissegundos, com um feixe que se desintegra o tempo todo e inunda os
     detectores de elétrons. É um problema de engenharia, não de física, e por
     isso continua em aberto.</p>''' ),

    ('11.5  Por que as transições proibidas demoram',
     r'''Estime a razão entre as taxas de emissão de dipolo magnético e de
     dipolo elétrico numa transição atômica típica, usando
     \(a_0 = 0{,}053\ \mathrm{nm}\) e \(\lambda = 122\ \mathrm{nm}\) (a linha
     Lyman-alfa do hidrogênio). Se a transição de dipolo elétrico dura
     \(1{,}6\ \mathrm{ns}\), quanto duraria a magnética?''',
     r'''<p><b>A estimativa.</b> Do texto, a razão das potências é da ordem de
     \(\left(a_0/\lambda\right)^2\) a menos de fatores de ordem um:</p>
     <p>\[ \left(\frac{a_0}{\lambda}\right)^2
        = \left(\frac{0{,}053}{122}\right)^2
        = 1{,}9\times10^{-7}. \]</p>
     <p><b>A duração.</b> O tempo de vida é o inverso da taxa, de modo que</p>
     <p>\[ \tau_{\text{mag}} \sim \frac{1{,}6\ \mathrm{ns}}{1{,}9\times10^{-7}}
        = 8{,}5\ \mathrm{ms}, \]</p>
     <p>cinco milhões de vezes mais.</p>
     <p><b>O que isso explica.</b> Um estado que só pode decair por dipolo
     magnético fica preso por um tempo enorme em escala atômica: é um estado
     <em>metaestável</em>. Em pressão normal ele colide com outra molécula
     muito antes disso e perde a energia sem emitir luz. Em gás rarefeito, não:
     é por isso que as auroras polares brilham em verde (uma transição
     proibida do oxigênio atômico, com \(0{,}7\ \mathrm{s}\) de vida) e por que
     essa linha nunca aparece numa lâmpada de laboratório. O verde da aurora só
     existe porque, a 100 km de altitude, o átomo tem tempo.</p>
     <p><b>Cuidado com a estimativa.</b> A conta acima é uma estimativa de
     ordem de grandeza, e não um cálculo: as regras de seleção e os elementos
     de matriz exatos vêm da mecânica quântica. O que o eletromagnetismo
     clássico fornece, e fornece corretamente, é a <em>hierarquia</em>: cada
     ordem de multipolo custa mais um fator \(a_0/\lambda\).</p>''' ),

    ('11.6  O tempo da reação de radiação',
     r'''Calcule \(\tau = \mu_0q^2/6\pi mc\) para o elétron e interprete o
     resultado geometricamente. Depois compare \(\tau\) com o período de uma
     órbita atômica e com o período de uma antena de \(100\ \mathrm{MHz}\), e
     diga quando a força de Abraham-Lorentz pode ser ignorada.''',
     r'''<p><b>O número.</b></p>
     <p>\[ \tau = \frac{\mu_0e^2}{6\pi m c}
        = 6{,}27\times10^{-24}\ \mathrm{s}. \]</p>
     <p><b>A interpretação.</b> Multiplicando por \(c\),
     \(c\tau = 1{,}9\times10^{-15}\ \mathrm{m}\), que é da ordem do raio
     clássico do elétron (\(2{,}8\times10^{-15}\) m). Ou seja: \(\tau\) é o
     tempo que a luz leva para atravessar o próprio elétron, visto como uma
     bolinha clássica. Toda a patologia da reação de radiação mora nessa
     escala.</p>
     <p><b>As comparações.</b></p>
     <div class="tabela-rolavel">
     <table>
     <thead><tr><th>situação</th><th>tempo característico</th>
     <th>razão com τ</th></tr></thead>
     <tbody>
     <tr><td>órbita no átomo de hidrogênio</td><td>1,5×10⁻¹⁶ s</td>
         <td>4×10⁻⁸</td></tr>
     <tr><td>antena de 100 MHz</td><td>1,0×10⁻⁸ s</td>
         <td>6×10⁻¹⁶</td></tr>
     </tbody>
     </table>
     </div>
     <p><b>A conclusão.</b> A força de reação é desprezível sempre que o tempo
     em que a aceleração muda for muito maior que \(\tau\), o que cobre
     essencialmente tudo, inclusive o interior do átomo. Ela só deixa de ser
     desprezível em campos extremos, como os de um laser de petawatt focalizado
     ou os da magnetosfera de um pulsar, e aí o tratamento correto já não é
     Abraham-Lorentz, e sim a versão relativística
     (Landau-Lifshitz) ou a eletrodinâmica quântica em campo forte.</p>
     <p><b>Repare na ironia.</b> A reação de radiação é desprezível em toda
     parte, e mesmo assim é ela que mostra onde a eletrodinâmica clássica
     termina. Uma teoria não precisa errar muito para avisar que acabou.</p>''' ),
]
