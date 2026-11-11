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

    ('Eletrostática: distribuições, Gauss e Laplace', [
        ('campo_distribuicao.py', 'Capítulo 2',
         'Integra E e V de fio, anel e disco discretizados em pedaços, e '
         'compara com as fórmulas fechadas.',
         'O erro cai como 1/n², os limites de carga pontual e de fio infinito '
         'aparecem sozinhos, e E_z bate com −dV/dz em 1e-7.'),
        ('gauss_numerico.py', 'Capítulo 2',
         'Fluxo de uma carga pontual por esfera centrada, deslocada, amassada '
         'e cubo, com a carga dentro e fora.',
         'Dentro, dá q/ε₀ em todas as superfícies; fora, dá zero. A esfera '
         'amassada dá o mesmo que a centrada, porque o integrando se reduz ao '
         'ângulo sólido.'),
        ('laplace_relaxacao.py', 'Capítulo 3',
         'Resolve Laplace por relaxação, substituindo cada ponto pela média '
         'dos vizinhos até convergir. É o programa mais reaproveitável do '
         'site.',
         'No duto, o centro dá V0/4 exato (a grade tem a mesma simetria), e o '
         'erro num ponto sem simetria cai como h². Com um bloco aterrado no '
         'meio, que nenhuma série resolve, ele não se incomoda.'),
        ('metodo_imagens.py', 'Capítulo 3',
         'A carga acima do plano aterrado pela imagem, com a carga induzida '
         'integrada, e o mesmo problema refeito por relaxação sem usar imagem '
         'nenhuma.',
         'A carga induzida total dá −q, metade dela está dentro de √3 d, e a '
         'relaxação reproduz o perfil de σ com erro de 1 a 2 % longe da '
         'carga.'),
        ('multipolos.py', 'Capítulo 3',
         'Momentos de uma distribuição discreta e comparação da série '
         'truncada com o potencial exato, ordem por ordem.',
         'O erro da ordem n cai com o expoente certo (medido: 2,00 para o '
         'dipolo), e o momento de dipolo muda com a origem assim que a carga '
         'total deixa de ser nula.'),
    ]),

    ('Leis de conservação', [
        ('poynting_fio.py', 'Capítulo 8',
         'Integra o vetor de Poynting sobre cilindros de vários raios em volta '
         'de um fio com corrente e compara com a potência dissipada.',
         'O fluxo entra radialmente, dá exatamente I²R e não depende do raio '
         'escolhido; dentro do condutor, acompanha a dissipação do miolo, que '
         'cresce com s².'),
        ('tensor_maxwell.py', 'Capítulo 8',
         'Calcula a força entre duas cargas integrando o tensor de tensões '
         'sobre superfícies de formas diferentes, sem usar a lei de Coulomb.',
         'Esferas (inclusive deslocadas) reproduzem Coulomb em 1e-13; o cubo '
         'converge em h², limitado pelas quinas, com 2e-6 em malha fina.'),
    ]),

    ('Potenciais, radiação e calibre', [
        ('lienard_wiechert.py', 'Capítulo 10',
         'Resolve o tempo retardado por bisseção e monta os campos de uma carga '
         'em movimento qualquer, com as parcelas de velocidade e de aceleração.',
         'Em movimento uniforme o campo bate com a fórmula fechada em 1e-16 e '
         'aponta exatamente para a posição presente; a potência média que '
         'atravessa qualquer esfera é a de Larmor.'),
        ('calibre.py', 'Capítulo 10',
         'Aplica uma transformação de calibre arbitrária e mede o que muda e o '
         'que não muda.',
         'E e B ficam iguais; os potenciais ficam irreconhecíveis; e a condição '
         'de Lorenz deixa de valer, porque o lambda escolhido não satisfaz a '
         'equação de onda.'),
        ('radiacao_dipolo.py', 'Capítulo 11',
         'Monta os potenciais retardados exatos de uma antena curta, tira E e B '
         'por diferenças finitas e integra o fluxo de energia sobre esferas.',
         'A potência média bate com Larmor e não depende do raio; o padrão é '
         'sen²θ com erro de 1e-4; e o expoente do campo passa de −3 a −1 ao '
         'cruzar um comprimento de onda.'),
        ('sincrotron.py', 'Capítulo 11',
         'A fórmula de Liénard aplicada ao movimento circular, com a energia '
         'perdida por volta no LEP, no LHC e no Sirius.',
         'Reproduz a regra prática 88,46 E⁴/ρ em 1,0000; o expoente com a '
         'energia dá 4,0000; e a razão próton/elétron dá (mₑ/m_p)⁴.'),
        ('espalhamento.py', 'Capítulo 11',
         'A seção de choque de Thomson obtida de Larmor, e a de Rayleigh obtida '
         'do índice de refração do ar, aplicada à atmosfera cor por cor.',
         'σ_T dá 6,652e-29 m² para qualquer intensidade e frequência, e a '
         'profundidade óptica calculada bate com a medida: 0,21 no azul contra '
         '0,05 no vermelho.'),
    ]),

    ('Matéria polarizada e magnetizada', [
        ('esfera_dieletrica.py', 'Capítulo 4',
         'A esfera dielétrica num campo uniforme, pela série de Legendre e por '
         'relaxação com a permissividade variável.',
         'O campo interno sai uniforme (desvio de 4e-4) e vale '
         '3E₀/(εr+2); refinando, o erro cai só em primeira ordem, porque a '
         'interface curva numa grade quadrada é o fator limitante.'),
        ('cargas_ligadas.py', 'Capítulo 4',
         'Calcula ρ_b e σ_b de polarizações uniformes, radiais e azimutais, e '
         'monta o campo que elas produzem.',
         'A carga ligada total dá zero em todos os casos, o campo dentro da '
         'esfera uniformemente polarizada dá −P/3ε₀ com erro de 1e-5, e fora '
         'é dipolar.'),
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

    ('Ondas', [
        ('onda_plana.py', 'Capítulo 9',
         'Verifica, por diferenças finitas, que a onda plana satisfaz as quatro '
         'equações de Maxwell, e calcula Poynting, intensidade e pressão de '
         'radiação.',
         'Os divergentes dão zero, os dois rotacionais casam com as derivadas '
         'temporais em 1e-4, as densidades elétrica e magnética de energia são '
         'iguais, e a intensidade bate com (1/2)cε₀E₀².'),
        ('fresnel.py', 'Capítulo 9',
         'R e T das duas polarizações em função do ângulo, com Brewster, '
         'ângulo crítico e a onda evanescente tratada com cosseno complexo.',
         'R + T = 1 em todo ângulo e nas duas polarizações; R paralelo zera '
         'exatamente em arctan(n₂/n₁); acima do crítico R = 1.'),
        ('fibra_fabry.py', 'Capítulo 9',
         'Os modos de um guia dielétrico pela equação transcendental, e o '
         'filtro Fabry-Perot pela função de Airy.',
         'A fibra fica monomodo acima do comprimento de onda de corte, e o FSR '
         'e a finesse medidos na curva reproduzem c/2nL e π√R/(1−R) em 4e-5.'),
        ('guia_onda.py', 'Capítulo 9',
         'Modos de um guia por autovalores do laplaciano discreto, com '
         'Dirichlet para TM e Neumann para TE, em qualquer seção.',
         'No WR-90 o TE10 sai 6,5566 GHz contra 6,5571 analíticos; e a seção '
         'em L, sem fórmula fechada, tem corte maior que o retângulo que a '
         'contém.'),
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
