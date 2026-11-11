# -*- coding: utf-8 -*-
"""A página dos programas: tudo o que há em codigo/, organizado por técnica.

A organização é por técnica, e não por capítulo, de propósito: a mesma
integração de Biot-Savart serve ao capítulo 5 e ao 6, e a mesma relaxação que
resolver o capacitor resolverá depois o guia de onda. O aluno que procura "como
se integra um campo" acha tudo junto.
"""
from molde import escreve, secoes_html

GRUPOS = [
    ('Operadores, teoremas e a delta', [
        ('operadores_vetoriais.py', 'Capítulo 1',
         'Gradiente, divergente, rotacional e laplaciano por diferenças finitas '
         'numa grade tridimensional.',
         'As identidades rot(grad) = 0 e div(rot) = 0 valem exatamente na '
         'grade, e o resíduo que sobra é arredondamento: ele cresce, e não '
         'cai, quando a grade é refinada.'),
        ('teoremas_integrais.py', 'Capítulo 1',
         'Os dois lados do teorema da divergência e do teorema de Stokes, '
         'calculados por quadratura.',
         'No cubo, os dois lados dão 48 exatos; na calota, o fluxo do '
         'rotacional, o fluxo pelo disco de mesma borda e a circulação '
         'convergem para o mesmo número, com razão 4 por refinamento.'),
        ('delta_dirac.py', 'Capítulo 1',
         'A delta como limite de gaussianas, a propriedade de filtragem e o '
         'fluxo de r/r² por esferas de qualquer raio.',
         'O erro da filtragem cai como ε² e o fluxo dá 4π de 0,1 a 100 de '
         'raio, apesar de o divergente ser nulo fora da origem.'),
    ]),

    ('Integração de campos: Biot-Savart e companhia', [
        ('biot_savart.py', 'Capítulo 5',
         'O módulo de base: discretiza um fio em segmentos e soma a '
         'contribuição de cada um. É importado pelos outros programas desta '
         'seção.',
         'O campo no centro de uma espira tem de dar μ₀I/2R, e o erro cai por '
         'um fator 4 a cada duplicação do número de segmentos.'),
        ('helmholtz.py', 'Capítulo 5',
         'Campo no eixo de duas bobinas coaxiais, e a demonstração de que a '
         'uniformidade é máxima quando a separação iguala o raio.',
         'A curvatura no centro troca de sinal exatamente em d = R, e o campo '
         'ali vale (4/5)^(3/2) μ₀NI/R.'),
        ('casca_legendre.py', 'Capítulo 5',
         'A casca girante pelos dois caminhos: a série de Legendre, que '
         'colapsa no termo de dipolo, e a integral de superfície por força '
         'bruta.',
         'Os coeficientes de l ≠ 1 se anulam, a integral bruta reproduz a '
         'fórmula fechada com erro de 2×10⁻¹², e o campo externo é dipolo puro '
         'até oito raios.'),
        ('esfera_magnetizada.py', 'Capítulo 6',
         'A esfera uniformemente magnetizada resolvida pela corrente ligada de '
         'superfície, somando anéis de latitude.',
         'O interior dá (2/3)μ₀M uniforme, o exterior é o dipolo de momento '
         '(4/3)πR³M, e H dentro dá −M/3.'),
        ('esfera_legendre.py', 'Capítulo 6',
         'A mesma esfera por separação de variáveis, com o potencial escalar '
         'magnético e a série de Legendre.',
         'Só o coeficiente l = 1 sobrevive, A₁ dá M/3, e o campo bate com o da '
         'corrente ligada em quatro casas.'),
        ('indutancia_mutua.py', 'Capítulo 7',
         'Indutância mútua pela fórmula de Neumann, por integração dupla sobre '
         'os dois contornos.',
         'A reciprocidade é confirmada por dois caminhos independentes, o '
         'resultado bate com a fórmula de integrais elípticas e converge em '
         'segunda ordem.'),
    ]),

    ('Trajetórias e circuitos no tempo', [
        ('trajetoria_lorentz.py', 'Capítulo 5',
         'Movimento de uma carga em campos E e B pelo método de Boris, o '
         'integrador padrão de física de plasmas.',
         'Sem campo elétrico a energia tem de ser conservada exatamente, '
         'porque a parte magnética é implementada como rotação; e a deriva '
         'tem de valer E/B, qualquer que seja a carga.'),
        ('barra_deslizante.py', 'Capítulo 7',
         'A barra nos trilhos, com a equação de movimento acoplada à corrente '
         'e os acumuladores de energia.',
         'A velocidade tende ao valor terminal FR/(Bh)², o decaimento sem '
         'força externa é exponencial, e o balanço W = ΔEc + Q fecha com '
         'desvio de 10⁻⁹.'),
        ('capacitor_deslocamento.py', 'Capítulo 7',
         'O capacitor carregando num circuito RC, com a corrente de condução e '
         'a de deslocamento lado a lado.',
         'As duas superfícies apoiadas na mesma curva dão a mesma corrente, e o '
         'resíduo cai como dt²; o campo magnético é contínuo na borda da placa.'),
    ]),

    ('Matéria e transições', [
        ('weiss_histerese.py', 'Capítulo 6',
         'A equação de campo médio de Weiss resolvida por ponto fixo '
         'amortecido, varrendo o campo nos dois sentidos.',
         'Abaixo de Tc o laço abre sozinho e acima fecha (área 8×10⁻¹²), e a '
         'susceptibilidade ajusta o expoente −1 de Curie-Weiss.'),
    ]),
]

S1 = r'''
<p>Todos os programas usam apenas <code>numpy</code>, <code>scipy</code> e
<code>matplotlib</code>, que já vêm na instalação padrão do Anaconda. Nenhum
deles precisa de configuração, argumento de linha de comando ou arquivo de
dados: baixe, abra no Spyder e aperte o botão de executar.</p>

<div class="cartoes">
  <article class="cartao">
    <h3>1. Baixar</h3>
    <p>Clique no nome do programa, nesta página ou na do capítulo, e salve o
    arquivo <code>.py</code> numa pasta sua.</p>
  </article>
  <article class="cartao">
    <h3>2. Abrir</h3>
    <p>No Spyder, use <em>Arquivo → Abrir</em> e escolha o arquivo. O cabeçalho
    explica o que ele resolve e como conferir a resposta.</p>
  </article>
  <article class="cartao">
    <h3>3. Executar</h3>
    <p>F5, ou o botão verde. Os números saem no console e as figuras no painel
    de gráficos.</p>
  </article>
  <article class="cartao">
    <h3>4. Mexer</h3>
    <p>Os parâmetros ficam em maiúsculas logo depois dos <code>import</code>.
    Troque um, rode de novo, veja o que muda.</p>
  </article>
</div>

<div class="bloco alerta">
<span class="rotulo">Uma dependência, só uma</span>
<p>O arquivo <code>biot_savart.py</code> é importado por
<code>helmholtz.py</code>, <code>esfera_magnetizada.py</code>,
<code>esfera_legendre.py</code> e <code>indutancia_mutua.py</code>. Se for usar
qualquer um desses, guarde os dois na <em>mesma pasta</em>. Todos os outros
programas são independentes.</p>
</div>

<p>Cada programa traz, no alto, quatro blocos: o que resolve, a física por trás,
como conferir se a resposta está certa, e a autoria. O terceiro é o mais
importante. Programa numérico que roda sem erro e entrega número errado é a
regra, não a exceção, e a única defesa é ter sempre um limite conhecido, uma
simetria ou uma lei de conservação para comparar.</p>
'''


def tabela():
    partes = []
    for titulo, itens in GRUPOS:
        partes.append('<h3>%s</h3>' % titulo)
        partes.append('<div class="cartoes">')
        for arquivo, cap, oque, confere in itens:
            partes.append(
                '  <article class="cartao">\n'
                '    <h3><a href="codigo/%s">%s</a></h3>\n'
                '    <p class="ficha">%s</p>\n'
                '    <p>%s</p>\n'
                '    <p><strong>Confira assim:</strong> %s</p>\n'
                '  </article>' % (arquivo, arquivo, cap, oque, confere))
        partes.append('</div>')
    return '\n'.join(partes) + '\n'


S2 = tabela()

S3 = r'''
<p>O que ainda falta escrever, e que entra junto com os capítulos
correspondentes:</p>

<ul>
<li><strong>Relaxação para a equação de Laplace</strong>, no capítulo 3: o
método que resolve o potencial numa região de forma qualquer, iterando a média
dos vizinhos até parar de mudar. É a mesma técnica que depois resolve o guia de
onda.</li>
<li><strong>Método das imagens conferido numericamente</strong>, também no
capítulo 3: comparar a solução de imagem com a relaxação é o jeito mais
convincente de mostrar que a imagem não é um truque, é a solução.</li>
<li><strong>Propagação de pulso</strong>, no capítulo 9: integrar a equação de
onda no tempo e ver a reflexão numa interface, com a fração refletida batendo
com os coeficientes de Fresnel.</li>
<li><strong>Dipolo radiante</strong>, no capítulo 11: os campos retardados de
uma carga oscilante, e o padrão de radiação em sen²θ.</li>
</ul>

<p>Quem quiser se adiantar pode começar pelo primeiro: a relaxação cabe em
quinze linhas e resolve, com uma mudança de condição de contorno, metade dos
problemas de eletrostática que não têm simetria.</p>
'''

SECOES = [
    ('Como rodar', S1),
    ('Os programas, por técnica', S2),
    ('O que ainda falta', S3),
]


def main():
    titulos = [t for t, _ in SECOES]
    escreve('codigo.html', secoes_html(SECOES), secoes=titulos)


if __name__ == '__main__':
    main()
