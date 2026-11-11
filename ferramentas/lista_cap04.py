# -*- coding: utf-8 -*-
"""Exercícios propostos do capítulo 4, campos elétricos na matéria."""

LISTA = [
    ('4.1  Quanto o átomo se estica, de verdade',
     r'''Use o modelo da nuvem uniforme para estimar o deslocamento \(d\) entre
     o núcleo e o centro da nuvem de um átomo de hidrogênio
     (\(a = 0{,}53\ \text{Å}\)) num campo de \(1{,}0\times10^{6}\
     \mathrm{V/m}\), que é um campo forte de laboratório. Compare \(d\) com o
     tamanho do átomo e com o tamanho de um núcleo.''',
     r'''<p>Do equilíbrio entre o campo aplicado e o restaurador da nuvem,</p>
     <p>\[ d = \frac{4\pi\varepsilon_0 a^3 E}{q}
        = \frac{a^3 E}{\left(1/4\pi\varepsilon_0\right)q}. \]</p>
     <p>Com \(a^3 = 1{,}49\times10^{-31}\ \mathrm{m^3}\),
     \(E = 10^{6}\ \mathrm{V/m}\), \(q = 1{,}60\times10^{-19}\ \mathrm{C}\) e
     \(1/4\pi\varepsilon_0 = 8{,}99\times10^{9}\):</p>
     <p>\[ d = \frac{1{,}49\times10^{-31}\times10^{6}}
        {8{,}99\times10^{9}\times1{,}60\times10^{-19}}
        = 1{,}0\times10^{-16}\ \mathrm{m}. \]</p>
     <p><b>As comparações.</b> O átomo tem \(5{,}3\times10^{-11}\) m, de modo
     que o deslocamento é duas partes em um milhão do raio atômico. E o núcleo
     do hidrogênio tem cerca de \(1{,}7\times10^{-15}\) m, ou seja, o
     deslocamento é <em>dezesseis vezes menor que o próprio núcleo</em>.</p>
     <p>Isso explica duas coisas. Primeiro, por que a resposta é linear: um
     deslocamento tão pequeno está no começo de qualquer curva, onde tudo é
     reta. Segundo, por que polarização eletrônica é rápida: a nuvem não precisa
     ir longe, e acompanha campos até frequências ópticas, o que é a origem do
     índice de refração.</p>''' ),

    ('4.2  Carga ligada de uma polarização que varia',
     r'''Uma esfera de raio \(R\) tem polarização radial que cresce com a
     distância ao centro, \(\vet{P} = k\,r\,\vers{r}\). Calcule \(\rho_b\) e
     \(\sigma_b\), mostre que a carga ligada total é nula e ache o campo dentro
     e fora.''',
     r'''<p>Em esféricas, para um vetor radial,</p>
     <p>\[ \rho_b = -\divg{\vet{P}}
        = -\frac{1}{r^2}\pder{\left(r^2\cdot kr\right)}{r}
        = -\frac{1}{r^2}\left(3kr^2\right) = -3k, \]</p>
     <p>uniforme e negativa. Na superfície,
     \(\sigma_b = \vet{P}\cdot\vers{n} = kR\).</p>
     <p><b>A carga total:</b></p>
     <p>\[ Q_b = (-3k)\frac{4}{3}\pi R^3 + (kR)\left(4\pi R^2\right)
        = -4\pi kR^3 + 4\pi kR^3 = 0, \]</p>
     <p>como tinha de ser: polarizar não cria carga, só a desloca.</p>
     <p><b>O campo.</b> Fora, a carga total é nula e, por simetria esférica,
     \(\vet{E} = 0\). Dentro, a carga enlaçada por uma gaussiana de raio \(r\)
     é \(-3k\cdot\frac43\pi r^3 = -4\pi kr^3\), e</p>
     <p>\[ E\left(4\pi r^2\right) = \frac{-4\pi kr^3}{\varepsilon_0}
        \;\Longrightarrow\;
        \vet{E} = -\frac{k r}{\varepsilon_0}\vers{r} = -\frac{\vet{P}}
        {\varepsilon_0}. \]</p>
     <p>Confira pelo outro caminho: com \(\rho_f = 0\) e simetria esférica,
     \(\vet{D} = 0\) em toda parte, e de \(\vet{D} = \varepsilon_0\vet{E} +
     \vet{P}\) sai imediatamente \(\vet{E} = -\vet{P}/\varepsilon_0\). Os dois
     caminhos concordam, e o segundo é bem mais rápido.</p>''' ),

    ('4.3  O capacitor com dois dielétricos',
     r'''Um capacitor de placas paralelas de área \(A\) e separação \(d\) é
     preenchido com duas camadas de dielétrico, de constantes
     \(\varepsilon_{r1}\) e \(\varepsilon_{r2}\) e espessuras \(d_1\) e
     \(d_2 = d - d_1\), empilhadas paralelamente às placas. Ache a capacitância
     e explique por que o resultado é o de capacitores em série.''',
     r'''<p>Com carga livre \(Q\) nas placas, uma gaussiana achatada dentro de
     cada camada enlaça a mesma carga livre, de modo que</p>
     <p>\[ D = \frac{Q}{A} \quad\text{nas duas camadas}. \]</p>
     <p>O campo, porém, é diferente em cada uma:</p>
     <p>\[ E_1 = \frac{Q}{\varepsilon_{r1}\varepsilon_0 A},\qquad
        E_2 = \frac{Q}{\varepsilon_{r2}\varepsilon_0 A}. \]</p>
     <p>A tensão é a soma das duas quedas:</p>
     <p>\[ V = E_1d_1 + E_2d_2
        = \frac{Q}{\varepsilon_0A}
          \left(\frac{d_1}{\varepsilon_{r1}}+\frac{d_2}{\varepsilon_{r2}}\right), \]</p>
     <p>de onde</p>
     <p>\[ C = \frac{Q}{V} = \frac{\varepsilon_0 A}
        {\dfrac{d_1}{\varepsilon_{r1}}+\dfrac{d_2}{\varepsilon_{r2}}}
        \qquad\Longleftrightarrow\qquad
        \frac{1}{C} = \frac{1}{C_1}+\frac{1}{C_2}. \]</p>
     <p><b>Por que em série.</b> As duas camadas carregam a mesma carga livre e
     as tensões se somam, que é exatamente a definição de associação em série.
     Compare com o exemplo do dielétrico parcialmente inserido, em que as partes
     dividem a tensão e somam a carga: aquilo é paralelo.</p>
     <p><b>Consequência prática.</b> A camada de menor \(\varepsilon_r\) fica
     com o maior campo, e é nela que o capacitor rompe. Uma bolha de ar de 10 µm
     dentro de um isolante de \(\varepsilon_r = 4\) sustenta quatro vezes o campo
     do material em volta, e é por isso que bolhas são o pesadelo da fabricação
     de capacitores de alta tensão.</p>''' ),

    ('4.4  A gota de água no campo',
     r'''Uma gota esférica de água (\(\varepsilon_r = 80\)) de raio
     \(1{,}0\ \mathrm{mm}\) está num campo uniforme de \(5{,}0\times10^{4}\
     \mathrm{V/m}\). Calcule o campo dentro da gota, a polarização, o momento de
     dipolo induzido e a carga ligada máxima na superfície.''',
     r'''<p><b>O campo dentro</b>, pelo resultado do exemplo:</p>
     <p>\[ E_{\text{in}} = \frac{3E_0}{\varepsilon_r+2}
        = \frac{3\times5{,}0\times10^{4}}{82}
        = 1{,}83\times10^{3}\ \mathrm{V/m}. \]</p>
     <p><b>A polarização:</b></p>
     <p>\[ P = \varepsilon_0\chi_e E_{\text{in}}
        = 8{,}85\times10^{-12}\times79\times1{,}83\times10^{3}
        = 1{,}28\times10^{-6}\ \mathrm{C/m^2}. \]</p>
     <p><b>O momento de dipolo</b> é \(P\) vezes o volume:</p>
     <p>\[ p = P\,\frac{4}{3}\pi R^3
        = 1{,}28\times10^{-6}\times4{,}19\times10^{-9}
        = 5{,}4\times10^{-15}\ \mathrm{C\,m}. \]</p>
     <p><b>A carga ligada máxima</b>, nos polos, é
     \(\sigma_b = P\cos\theta\) com \(\cos\theta = 1\), isto é
     \(1{,}28\ \mu\mathrm{C/m^2}\).</p>
     <p><b>Leitura.</b> A gota blinda 96 % do campo aplicado, e o dipolo
     induzido é \(9\times10^{14}\) vezes maior que o de uma molécula de água
     isolada (\(6{,}1\times10^{-30}\) C m). Não há contradição: a gota tem
     cerca de \(1{,}4\times10^{20}\) moléculas, de modo que o alinhamento
     corresponde a umas seis moléculas em cada milhão.</p>''' ),

    ('4.5  Por que o D não tem potencial',
     r'''Dê um exemplo concreto em que \(\rot{\vet{D}} \ne 0\), e explique por
     que, mesmo assim, \(\divg{\vet{D}} = \rho_f\) continua valendo. Em seguida
     diga o que daria errado se alguém escrevesse \(\vet{D} = -\nabla U\) e
     tentasse resolver um problema com isso.''',
     r'''<p><b>O exemplo.</b> Tome um bastão de eletreto, isto é, um material
     com polarização permanente \(\vet{P}\) congelada, sem carga livre nenhuma.
     Fora dele, \(\vet{P} = 0\) e \(\vet{D} = \varepsilon_0\vet{E}\); dentro,
     \(\vet{D} = \varepsilon_0\vet{E} + \vet{P}\).</p>
     <p>Como \(\rot{\vet{E}} = 0\) sempre em eletrostática,</p>
     <p>\[ \rot{\vet{D}} = \rot{\vet{P}}, \]</p>
     <p>que não é nulo se \(\vet{P}\) variar de direção, como acontece num
     eletreto curvo ou numa amostra com polarização não uniforme.</p>
     <p><b>Por que o divergente continua valendo.</b> A lei
     \(\divg{\vet{D}} = \rho_f\) saiu da lei de Gauss e da definição de carga
     ligada, sem nenhuma hipótese sobre o rotacional. As duas informações são
     independentes: uma diz onde \(\vet{D}\) nasce, a outra diz se ele
     circula.</p>
     <p><b>O que daria errado.</b> Escrever \(\vet{D} = -\nabla U\) impõe
     rotacional nulo, o que é falso no caso acima, e a solução obtida não
     satisfaria as condições de contorno corretas. Pelo teorema de Helmholtz do
     capítulo 1, conhecer só o divergente nunca determina um campo: é preciso
     o rotacional também. \(\vet{D}\) é uma conveniência de contabilidade da
     carga livre, e não um campo fundamental.</p>''' ),

    ('4.6  O fator de despolarização muda com a forma',
     r'''O exemplo do texto achou \(\vet{E} = -\vet{P}/3\varepsilon_0\) dentro de
     uma esfera uniformemente polarizada. Mostre, por um argumento de lei de
     Gauss, que uma placa fina polarizada perpendicularmente às faces tem
     \(\vet{E} = -\vet{P}/\varepsilon_0\), e que um bastão longo polarizado ao
     longo do eixo tem \(\vet{E} \approx 0\) no meio. Comente o que isso
     significa para o projeto de ímãs permanentes.''',
     r'''<p><b>A placa.</b> Com \(\vet{P}\) uniforme e perpendicular às faces,
     \(\rho_b = 0\) e as faces têm \(\sigma_b = \pm P\). Isso é exatamente um
     capacitor de placas paralelas com essas densidades, e o campo entre elas
     vale</p>
     <p>\[ E = \frac{\sigma_b}{\varepsilon_0} = \frac{P}{\varepsilon_0}, \]</p>
     <p>apontando da face positiva para a negativa, isto é, <em>contra</em>
     \(\vet{P}\). Logo \(\vet{E} = -\vet{P}/\varepsilon_0\), e o fator de
     despolarização é 1.</p>
     <p><b>O bastão.</b> Agora as cargas ligadas estão nas duas pontas,
     separadas por um comprimento grande. No meio do bastão, cada ponta está
     longe, e o campo de uma carga distante cai com o quadrado da distância: o
     resultado tende a zero quando o comprimento cresce. O fator de
     despolarização tende a 0.</p>
     <p><b>Para ímãs, que é o caso análogo do capítulo 6.</b> O campo
     despolarizante trabalha contra a própria magnetização e pode desmagnetizar
     o material. Quanto mais achatada a peça na direção da magnetização, maior
     esse campo contrário; quanto mais alongada, menor. Daí a forma clássica dos
     ímãs permanentes antigos, que são barras compridas ou ferraduras, e daí o
     fato de ímãs de geladeira, que são finos, precisarem de materiais de
     coercividade altíssima para sobreviver ao próprio campo
     desmagnetizante.</p>''' ),
]
