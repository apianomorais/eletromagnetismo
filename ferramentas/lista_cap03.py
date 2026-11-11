# -*- coding: utf-8 -*-
"""Exercícios propostos do capítulo 3, potenciais e técnicas especiais."""

LISTA = [
    ('3.1  Por que não existe armadilha eletrostática',
     r'''Mostre, a partir da propriedade da média, que uma carga de prova não
     pode ficar em equilíbrio estável numa região vazia de carga, por mais
     engenhosa que seja a configuração das cargas fixas em volta. Em seguida
     explique por que a armadilha de Paul, usada para prender íons, não
     contradiz isso.''',
     r'''<p>Suponha que uma carga de prova positiva estivesse em equilíbrio
     estável num ponto \(P\) do vácuo. Estável significa que qualquer
     deslocamento produz força restauradora, isto é, que o campo externo aponta
     para dentro em toda a superfície de uma pequena esfera em torno de
     \(P\).</p>
     <p>Mas isso daria fluxo negativo nessa esfera, e pela lei de Gauss haveria
     carga negativa dentro dela, o que contraria a hipótese de a região estar
     vazia. Dito em termos do potencial: estabilidade exigiria um mínimo de
     \(V\) em \(P\), e a propriedade da média proíbe mínimos no interior. É o
     <b>teorema de Earnshaw</b>.</p>
     <p><b>Por que a armadilha de Paul escapa.</b> Ela não é eletrostática: o
     campo oscila, tipicamente em radiofrequência. Em cada instante há sempre
     uma direção instável, mas a oscilação troca qual é essa direção antes que
     o íon tenha tempo de escapar, e o efeito médio é um poço. Earnshaw proíbe
     equilíbrio estático, e não equilíbrio dinâmico. Pela mesma razão, a
     levitação magnética de um diamagneto ou de um supercondutor também não
     viola nada: ali a resposta do material depende do campo.</p>''' ),

    ('3.2  Uma carga entre dois planos',
     r'''Uma carga \(q\) está entre dois planos condutores aterrados e
     paralelos, separados por \(L\), a uma distância \(d\) de um deles.
     Descreva o conjunto de imagens necessário e explique por que ele é
     infinito. Qual a carga total induzida nos dois planos juntos?''',
     r'''<p>Uma imagem só não basta: a imagem que zera o potencial no primeiro
     plano estraga o do segundo. É preciso então uma imagem da imagem, e assim
     por diante.</p>
     <p>O resultado é uma fileira infinita de cargas alternadas, em
     \(z = 2nL \pm d\) para todo inteiro \(n\), com sinais alternados conforme
     o número de reflexões. Cada reflexão sucessiva fica mais longe, de modo que
     a série converge, e na prática três ou quatro termos já dão boa
     precisão.</p>
     <p><b>A carga induzida total.</b> Vale \(-q\), repartida entre os dois
     planos. A repartição não é meio a meio: o plano mais próximo recebe a
     parte maior, e a divisão é \(-q(1-d/L)\) no plano próximo e \(-qd/L\) no
     distante. O total tem de ser \(-q\) porque o campo é nulo dentro dos dois
     condutores e, portanto, qualquer gaussiana que envolva o conjunto todo
     enlaça carga nula.</p>
     <p>Este arranjo é o modelo mais simples de uma carga num capacitor, e a
     série de imagens é a mesma estrutura que aparece em óptica com dois
     espelhos paralelos.</p>''' ),

    ('3.3  A esfera isolada, e não aterrada',
     r'''Refaça o exemplo da esfera condutora com a carga \(q\) a uma distância
     \(a\), mas agora com a esfera <em>isolada e neutra</em>, em vez de
     aterrada. Onde ficam as imagens, e qual o potencial da esfera?''',
     r'''<p>Com a esfera aterrada, a imagem é \(q' = -qR/a\) em \(b = R^2/a\), e
     a carga total induzida é \(q'\), que veio da terra. Se a esfera está
     isolada e era neutra, essa carga não pode aparecer do nada.</p>
     <p>A correção é acrescentar uma segunda imagem, \(-q' = +qR/a\), no
     <b>centro</b> da esfera. Ela restaura a neutralidade (as duas imagens
     somam zero) e, por estar no centro, mantém a superfície equipotencial, já
     que uma carga central produz potencial constante sobre a esfera.</p>
     <p>O potencial da esfera deixa de ser zero e passa a valer o da carga
     central vista da superfície:</p>
     <p>\[ V_{\text{esfera}} = \frac{1}{4\pi\varepsilon_0}\frac{qR/a}{R}
        = \frac{q}{4\pi\varepsilon_0 a}, \]</p>
     <p>que é, curiosamente, o potencial que \(q\) produziria no centro da
     esfera se ela não estivesse lá. A força sobre \(q\) continua atrativa, mas
     é menor que no caso aterrado, porque a imagem central, de mesmo sinal que
     \(q\), repele.</p>''' ),

    ('3.4  Três termos bastam',
     r'''No duto do exemplo resolvido, calcule \(V\) no centro da seção
     (\(x = y = a/2\)) somando um, dois e três termos não nulos da série.
     Depois mostre, por um argumento de simetria que não usa série nenhuma, que
     o valor exato é \(V_0/4\).''',
     r'''<p>No centro, \(\sen(n\pi/2)\) vale \(+1, -1, +1, \dots\) para
     \(n = 1, 3, 5, \dots\), e a razão de senos hiperbólicos vale</p>
     <p>\[ \frac{\senh(n\pi/2)}{\senh(n\pi)} = 0{,}199268;\;
        0{,}008983;\; 0{,}000388 \quad (n = 1, 3, 5). \]</p>
     <p>Somando os termos \(\frac{4V_0}{\pi n}\) vezes isso, com os sinais
     alternados:</p>
     <p>\[ 0{,}253716\,V_0;\quad 0{,}249904\,V_0;\quad
        0{,}250003\,V_0. \]</p>
     <p>Com <b>um</b> termo o erro já é de 1,5 %; com <b>dois</b>, de 0,04 %;
     com <b>três</b>, de 0,001 %. A convergência é exponencial porque
     \(\senh(n\pi/2)/\senh(n\pi) \approx e^{-n\pi/2}\).</p>
     <p><b>O argumento de simetria.</b> Tome quatro cópias do problema, cada uma
     girada de 90°, de modo que em cada cópia uma parede diferente esteja em
     \(V_0\). Somando as quatro soluções, todas as quatro paredes ficam em
     \(V_0\), e a solução dessa soma é \(V = V_0\) em toda parte, por
     inspeção e por unicidade.</p>
     <p>No centro, as quatro cópias dão o mesmo valor, porque o centro é
     invariante pelas rotações. Logo \(4V_{\text{centro}} = V_0\), isto é</p>
     <p>\[ V_{\text{centro}} = \frac{V_0}{4}. \]</p>
     <p>É um resultado exato obtido sem resolver nada, e serve de teste para
     qualquer método numérico: <code>laplace_relaxacao.py</code> devolve
     0,25000 e é por aí que se confere o programa.</p>''' ),

    ('3.5  A esfera com potencial dado na casca',
     r'''A superfície de uma esfera de raio \(R\) é mantida ao potencial
     \(V(R,\theta) = V_0\cos^2\theta\). Ache o potencial dentro e fora, usando
     a série de Legendre.''',
     r'''<p>Primeiro escreva a condição de contorno na base de Legendre. Como
     \(P_2 = \frac12(3\cos^2\theta - 1)\),</p>
     <p>\[ \cos^2\theta = \frac{2P_2 + 1}{3} = \frac{2}{3}P_2 + \frac{1}{3}P_0, \]</p>
     <p>de modo que \(V(R,\theta) = V_0\left(\frac13 P_0 + \frac23 P_2\right)\):
     só \(l = 0\) e \(l = 2\) aparecem.</p>
     <p><b>Dentro</b>, com os termos \(r^l\) apenas:</p>
     <p>\[ V = V_0\left[\frac{1}{3} + \frac{2}{3}\frac{r^2}{R^2}P_2(\cos\theta)
        \right]. \]</p>
     <p><b>Fora</b>, com os termos \(1/r^{l+1}\) apenas:</p>
     <p>\[ V = V_0\left[\frac{1}{3}\frac{R}{r}
        + \frac{2}{3}\frac{R^3}{r^3}P_2(\cos\theta)\right]. \]</p>
     <p><b>Leitura.</b> O termo \(l=0\) de fora é o de uma carga pontual, e
     comparando com \(Q/4\pi\varepsilon_0 r\) lê-se a carga total da esfera:
     \(Q = \frac{4\pi\varepsilon_0 V_0R}{3}\). Não há dipolo, porque
     \(\cos^2\theta\) é par em \(\cos\theta\) e \(P_1\) é ímpar: a
     ortogonalidade mata o termo antes de qualquer conta.</p>''' ),

    ('3.6  Onde o dipolo deixa de valer',
     r'''Duas cargas \(+q\) e \(-q\) separadas por \(d\) formam um dipolo de
     momento \(p = qd\). A partir de que distância a fórmula do dipolo acerta o
     potencial com erro menor que 1 %, sobre o eixo do par? Faça a conta e
     compare com o que o programa <code>multipolos.py</code> devolve.''',
     r'''<p>Sobre o eixo, a uma distância \(r\) do centro, o potencial exato
     é</p>
     <p>\[ V_{\text{ex}} = \frac{q}{4\pi\varepsilon_0}
        \left[\frac{1}{r-d/2} - \frac{1}{r+d/2}\right]
        = \frac{q}{4\pi\varepsilon_0}\frac{d}{r^2 - d^2/4}, \]</p>
     <p>enquanto a aproximação de dipolo dá
     \(V_{\text{dip}} = qd/4\pi\varepsilon_0r^2\). A razão é</p>
     <p>\[ \frac{V_{\text{ex}}}{V_{\text{dip}}}
        = \frac{r^2}{r^2-d^2/4} = \frac{1}{1 - (d/2r)^2}
        \approx 1 + \left(\frac{d}{2r}\right)^2. \]</p>
     <p>O erro relativo é, então, \((d/2r)^2\), e ele fica abaixo de 1 % quando</p>
     <p>\[ \frac{d}{2r} \lt 0{,}1 \;\Longrightarrow\; r \gt 5d. \]</p>
     <p><b>Interpretação.</b> Cinco separações já bastam, e o erro cai
     rapidamente: a dez separações ele é 0,25 %, a vinte é 0,06 %. Fora do eixo
     a convergência é ainda mais rápida, porque o termo de quadrupolo tem um
     fator angular que o reduz. É por isso que tratar moléculas polares como
     dipolos pontuais funciona tão bem a distâncias de poucos angstroms.</p>''' ),
]
