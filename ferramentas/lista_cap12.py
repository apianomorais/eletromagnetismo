# -*- coding: utf-8 -*-
"""Exercícios propostos do capítulo 12, a eletrodinâmica de Weber."""

LISTA = [
    ('12.1  Quando a correção de Weber importaria',
     r'''A força de Weber difere de Coulomb por termos da ordem de
     \(\dot r^2/2c^2\). Estime esse fator para dois elétrons de condução num
     fio de cobre (velocidade de deriva \(10^{-4}\ \mathrm{m/s}\)) e para dois
     elétrons num feixe acelerado por \(20\ \mathrm{kV}\). Comente o que isso
     diz sobre a possibilidade de distinguir as duas teorias no século XIX.''',
     r'''<p><b>No fio.</b> Com \(v = 10^{-4}\ \mathrm{m/s}\),</p>
     <p>\[ \frac{v^2}{2c^2} = \frac{10^{-8}}{2\times9{,}0\times10^{16}}
        = 5{,}6\times10^{-26}. \]</p>
     <p>É um número sem sentido experimental: nenhuma medida de qualquer época
     chega perto disso.</p>
     <p><b>No feixe.</b> De \(eV = \frac12mv^2\),</p>
     <p>\[ v = \sqrt{\frac{2eV}{m}} = 8{,}39\times10^{7}\ \mathrm{m/s},
        \qquad \frac{v^2}{2c^2} = 0{,}039, \]</p>
     <p>isto é, quase 4 %, perfeitamente mensurável.</p>
     <p><b>A moral.</b> A diferença entre Weber e Maxwell só aparece com cargas
     livres rápidas, e cargas livres rápidas exigem vácuo, alta tensão e
     detectores, coisas que só chegaram ao laboratório com Crookes e Thomson,
     nos anos 1890. Até lá, toda a eletrodinâmica experimental era feita com
     correntes em fios, em que a velocidade de deriva é ridícula e os dois
     formalismos dão exatamente o mesmo resultado. A disputa não durou cinquenta
     anos por teimosia: durou porque o experimento decisivo não existia.</p>''' ),

    ('12.2  A energia que Weber conserva',
     r'''Mostre que \(E = \frac12\mu\dot r^2 + \frac{k}{r}
     \left(1-\frac{\dot r^2}{2c^2}\right)\), com \(k = q_1q_2/4\pi
     \varepsilon_0\), é constante ao longo do movimento governado pela força de
     Weber.''',
     r'''<p><b>Derive no tempo</b>, com cuidado no termo cruzado:</p>
     <p>\[ \der{E}{t} = \mu\dot r\ddot r - \frac{k\dot r}{r^2}
        - \frac{k}{2c^2}\der{}{t}\!\left(\frac{\dot r^2}{r}\right). \]</p>
     <p>A última derivada vale</p>
     <p>\[ \der{}{t}\!\left(\frac{\dot r^2}{r}\right)
        = \frac{2\dot r\ddot r}{r} - \frac{\dot r^3}{r^2}. \]</p>
     <p><b>Substituindo e pondo \(\dot r\) em evidência:</b></p>
     <p>\[ \der{E}{t} = \dot r\left[\mu\ddot r - \frac{k}{r^2}
        + \frac{k\dot r^2}{2r^2c^2} - \frac{k\ddot r}{rc^2}\right]
        = \dot r\left[\mu\ddot r
        - \frac{k}{r^2}\left(1 - \frac{\dot r^2}{2c^2}
        + \frac{r\ddot r}{c^2}\right)\right]. \]</p>
     <p>O colchete é exatamente \(\mu\ddot r - F_{\text{Weber}}\), que é nulo
     pela segunda lei de Newton. Logo \(dE/dt = 0\).</p>
     <p><b>O que isso significa.</b> Weber tinha conservação de energia sem
     campo nenhum, e esse era um dos argumentos mais fortes a favor da teoria:
     toda a energia do sistema está nas partículas, como na mecânica, e não
     num ente invisível espalhado pelo espaço. O preço aparece no exercício
     12.5: energia que não pode sair do sistema é energia que não pode
     irradiar.</p>''' ),

    ('12.3  A massa efetiva, e onde ela muda de sinal',
     r'''Da equação de movimento implícita da seção 2, identifique a massa
     efetiva e calcule o raio crítico para dois elétrons e para dois prótons.
     Depois repita para um par elétron-próton e explique por que o problema
     desaparece nesse caso.''',
     r'''<p><b>A massa efetiva</b> é o coeficiente de \(\ddot r\):</p>
     <p>\[ \mu_{\text{ef}} = \mu - \frac{k}{rc^2},
        \qquad r_{\text{crit}} = \frac{k}{\mu c^2}. \]</p>
     <p><b>Dois elétrons.</b> Com \(\mu = m_e/2\),</p>
     <p>\[ r_{\text{crit}} = \frac{2e^2}{4\pi\varepsilon_0m_ec^2} = 2r_e
        = 5{,}64\times10^{-15}\ \mathrm{m}. \]</p>
     <p><b>Dois prótons.</b> A mesma conta com \(m_p = 1836\,m_e\) dá</p>
     <p>\[ r_{\text{crit}} = 3{,}07\times10^{-18}\ \mathrm{m}, \]</p>
     <p>mil vezes menor, e bem dentro do próton.</p>
     <p><b>Elétron e próton.</b> Agora \(q_1q_2 \lt 0\), de modo que \(k\) é
     negativo e</p>
     <p>\[ \mu_{\text{ef}} = \mu + \frac{|k|}{rc^2} \]</p>
     <p>é sempre <em>maior</em> que \(\mu\), e nunca se anula. Cargas opostas
     ficam mais "pesadas" ao se aproximarem, o que é inofensivo; o problema é
     só das cargas de mesmo sinal.</p>
     <p><b>A leitura.</b> A patologia mora na escala em que a energia
     eletrostática do par iguala a energia de repouso, \(k/r \sim \mu c^2\).
     Essa é a mesma condição que define o raio clássico do elétron e a mesma
     que faz a reação de radiação do capítulo 11 produzir soluções fugitivas.
     Duas teorias clássicas diferentes, e o mesmo muro.</p>''' ),

    ('12.4  Ampère contra Grassmann, na mão',
     r'''Calcule a força entre dois elementos de corrente paralelos, lado a
     lado, pelas duas expressões da seção 3, e depois para dois elementos
     perpendiculares alinhados um atrás do outro. Comente o que o resultado
     tem a ver com a terceira lei de Newton.''',
     r'''<p><b>Paralelos, lado a lado.</b> Tome
     \(d\vet{\ell}_1 = d\vet{\ell}_2 = d\ell\,\vers{x}\) e
     \(\vers{r} = \vers{y}\), de modo que
     \(d\vet{\ell}_1\cdot\vers{r} = d\vet{\ell}_2\cdot\vers{r} = 0\).</p>
     <p>Por Grassmann, \(d\vet{\ell}_1\cruz\vers{y} = d\ell\,\vers{z}\), e</p>
     <p>\[ d\vet{\ell}_2\cruz\left(d\ell\,\vers{z}\right)
        = -d\ell^2\,\vers{y}
        \;\Longrightarrow\;
        d^2\vet{F} = -\frac{\mu_0I_1I_2}{4\pi}\frac{d\ell^2}{r^2}\vers{y}. \]</p>
     <p>Por Ampère, só sobra o termo com o produto escalar:</p>
     <p>\[ d^2\vet{F} = -\frac{\mu_0I_1I_2}{4\pi}\frac{\vers{y}}{r^2}
        \left(2d\ell^2\right), \]</p>
     <p>o <b>dobro</b>. As duas concordam no sinal (atração, como se espera de
     correntes paralelas) e discordam no valor.</p>
     <p><b>Perpendiculares, em linha.</b> Tome
     \(d\vet{\ell}_1 = d\ell\,\vers{x}\),
     \(d\vet{\ell}_2 = d\ell\,\vers{y}\) e \(\vers{r} = \vers{y}\). Agora
     \(d\vet{\ell}_1\cdot d\vet{\ell}_2 = 0\) e
     \(d\vet{\ell}_1\cdot\vers{r} = 0\), de modo que a força de Ampère é
     <b>exatamente zero</b>. A de Grassmann dá</p>
     <p>\[ d^2\vet{F} = +\frac{\mu_0I_1I_2}{4\pi}\frac{d\ell^2}{r^2}\vers{x}, \]</p>
     <p>uma força <em>perpendicular</em> à linha que une os dois elementos.</p>
     <p><b>A terceira lei.</b> A força de Grassmann não é central e não é
     antissimétrica: trocando os papéis dos dois elementos, não se obtém o
     negativo da anterior. Isolada, ela viola a terceira lei de Newton na forma
     forte, e o capítulo 8 mostrou qual é a saída: o momento que falta está no
     campo. A de Ampère nunca precisa dessa saída, porque é central por
     construção, e é exatamente esse conforto que fazia a escola continental
     preferi-la. O desconforto da de Grassmann é o preço de ter campo, e o
     campo é o que permite ter radiação.</p>''' ),

    ('12.5  O experimento que decide',
     r'''Uma antena de \(30\ \mathrm{cm}\) a \(100\ \mathrm{MHz}\), com
     \(1\ \mathrm{A}\) de amplitude, irradia cerca de \(4\ \mathrm{W}\) segundo
     o capítulo 11. Quanto a teoria de Weber prevê? Projete, em palavras, o
     experimento mais simples que distingue as duas previsões, e explique por
     que ele não podia ser feito antes de 1880.''',
     r'''<p><b>A previsão de Weber: zero.</b> Não "pequeno", e sim
     identicamente nulo. A energia do sistema de cargas é função de \(r\) e
     \(\dot r\), e num movimento periódico ela retorna ao valor inicial a cada
     ciclo. Sem atraso não há para onde a energia ir, e sem campo não há onde
     guardá-la em trânsito.</p>
     <p><b>O experimento.</b> Ponha um oscilador num canto da sala e um
     detector ressonante no outro, sem nenhuma ligação entre eles. Meça três
     coisas: que o detector responde; que a resposta some quando se interpõe
     uma placa metálica; e que a fonte consome mais potência quando o detector
     está presente e sintonizado do que quando não está. A terceira é a
     decisiva, porque é a que mostra energia <em>saindo</em> da fonte.</p>
     <p>Melhor ainda: meça o comprimento de onda. Com um refletor metálico
     formam-se ondas estacionárias, e os nós ficam separados de meio
     comprimento de onda. Medindo essa distância e conhecendo a frequência,
     obtém-se uma velocidade de propagação finita, que é a refutação direta da
     ação a distância.</p>
     <p><b>Por que só depois de 1880.</b> O experimento exige gerar oscilações
     de dezenas de megahertz, o que pede centelhadores e circuitos ressonantes
     com indutância e capacitância pequenas, e exige detectar potências
     minúsculas sem amplificação. Hertz conseguiu entre 1886 e 1888 com um
     centelhador e um anel com uma fenda micrométrica, observando a faísca
     secundária no escuro. É um experimento de bancada, e ainda assim precisou
     de quarenta anos de desenvolvimento instrumental depois de Weber.</p>
     <p><b>Um detalhe histórico que vale a pena.</b> Hertz fez o experimento
     para <em>testar</em> as equações de Maxwell, em que ele mesmo não
     acreditava inteiramente, e a pedido do seu orientador Helmholtz, que havia
     formulado a objeção da massa negativa quinze anos antes. Perguntado sobre
     a utilidade prática das ondas que descobrira, respondeu que não via
     nenhuma. Marconi encontrou uma, sete anos depois.</p>''' ),

    ('12.6  A razão entre as unidades, sem olhar a resposta',
     r'''Mostre, por análise dimensional a partir da lei de Coulomb e da força
     entre dois fios paralelos, que a razão entre a unidade eletrostática e a
     unidade eletromagnética de carga tem dimensão de velocidade e vale
     \(1/\sqrt{\varepsilon_0\mu_0}\). Depois calcule o valor que Weber e
     Kohlrausch teriam obtido se os seus aparelhos fossem perfeitos, e compare
     com o que eles obtiveram de fato.''',
     r'''<p><b>A unidade eletrostática</b> é definida pela força de Coulomb:
     duas cargas unitárias a uma distância unitária se repelem com força
     unitária, de modo que \(q_{es}^2 \sim 4\pi\varepsilon_0 Fd^2\).</p>
     <p><b>A unidade eletromagnética</b> é definida pela força entre correntes:
     \(F/\ell \sim \mu_0I^2/2\pi d\), e como \(I = q_{em}/t\),</p>
     <p>\[ q_{em}^2 \sim \frac{2\pi F\ell d\,t^2}{\mu_0}. \]</p>
     <p><b>A razão.</b> Dividindo uma pela outra e cortando as grandezas
     mecânicas,</p>
     <p>\[ \left(\frac{q_{es}}{q_{em}}\right)^2
        \sim \frac{1}{\varepsilon_0\mu_0}\frac{t^2}{d^2}
        \;\Longrightarrow\;
        \frac{q_{es}}{q_{em}} \sim \frac{1}{\sqrt{\varepsilon_0\mu_0}}. \]</p>
     <p>Nenhuma óptica entrou na conta: a velocidade apareceu porque as duas
     definições de carga usam leis de força diferentes, e só isso.</p>
     <p><b>O valor ideal.</b></p>
     <p>\[ \frac{1}{\sqrt{\varepsilon_0\mu_0}}
        = 2{,}998\times10^{8}\ \mathrm{m/s}. \]</p>
     <p><b>O que eles obtiveram.</b> \(c_W = 4{,}39\times10^{8}\)
     m/s, que dividido por \(\sqrt2\) dá \(3{,}104\times10^{8}\) m/s: um erro
     de 3,5 % numa medida feita em 1855, comparando duas forças de naturezas
     completamente diferentes. A de Fizeau para a luz, seis anos antes, errava
     4,5 %, e no mesmo sentido.</p>
     <p><b>A pergunta que fica.</b> Com dois números concordando em 1 % e
     medidos por caminhos sem nenhuma relação aparente, por que ninguém
     concluiu imediatamente que luz é eletromagnetismo? Porque concluir isso
     exige uma teoria em que exista algo capaz de ondular. Na eletrodinâmica de
     Weber esse algo não existe, e a coincidência numérica fica sendo apenas
     uma coincidência numérica. O arcabouço decide o que um dado pode
     significar.</p>''' ),
]
