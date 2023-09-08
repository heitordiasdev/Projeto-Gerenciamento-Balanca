# Projeto-Gerenciamento-Balanca

Software de Gerenciamento de Balanças - Ponto de Venda (PDV)

    1) Introdução
    O objetivo principal deste documento é descrever a estrutura que deve ser utilizada para obter dados dos produtos gerados pelas balanças e passados pelo PDV.

    2) Etiqueta de Produtos

    Etiquetas são informações referentes aos produtos manipulados nas balanças.

    CONFIGURAÇÃO DO LAYOUT DA ETIQUETA

    A seqüência dos campos deve ser a seguinte:

    ·Código verificador um (1) caracter numérico (Obs: Código vai de 1 a 6)

    ·Tamanho do código do produto um (1) caracter. (Obs: Código vai de 4 a 6).

    ·Venda por Peso ou Preço.


3) Implementação
O armazenamento dos produtos deve ser feito em uma matriz com duas linhas, a primeira linha são códigos de etiqueta válidos e a segunda são códigos inválidos.



O subprograma deve perguntar para o usuário qual a configuração de etiqueta que deseja seguir (Essa pergunta é feita somente uma vez no início do subprograma). 

Perguntas:

Qual o tamanho do código do produto?
Qual o código do produto pesável?
Venda por Peso (1) ou Preço (2)? 

Um código é válido quando: o tamanho do código da ETIQUETA é 13 e o início do código começa com o valor inserido na pergunta “Qual o código do produto pesável?”

Se o usuário inserir 2 na pergunta “Qual o código do produto pesável?” então um código de etiqueta que começa com o número 2 e tem o tamanho 13 é um código válido. Por exemplo: 

 

2001234009966 é um código válido pois começa com 2 e o seu tamanho total é 13.


Após fazer as perguntas iniciais o subprograma deve ficar perguntando para o usuário qual código de etiqueta ele quer inserir. Ex:

Informe o produto no PDV: 2001234009966 

Caso o código seja válido (Siga e estrutura definida no início do subprograma) então 
o subprograma deve imprimir as informações do produtos da etiqueta baseada nas seguintes regras:

Digamos que o usuário colocou as seguintes informações iniciais:

Qual o tamanho do código do produto? 4
Qual o código do produto pesável? 2
Venda por Peso (1) ou Preço (2)? 1

A saída deve ser:

código do produto: 1234
código do produto pesável: 2
peso do produto: 9,966

Digamos que o usuário colocou as seguintes informações iniciais:

Qual o tamanho do código do produto? 5
Qual o código do produto pesável? 2
Venda por Peso (1) ou Preço (2)? 2

A saída deve ser:

código do produto: 01234
código do produto pesável: 2
preço do produto: 9,97 (arredonda)

Depois de imprimir o subprograma deve armazenar o código válido na primeira linha da matriz. Se o código inserido não seguir esses padrões ele deve ser armazenado na segunda linha da matriz (que são os códigos inválidos) E perguntar pro usuário se ele deseja continuar inserindo códigos.

Caso o usuário diga que não quer continuar inserindo o programa imprime a matriz e é encerrado.



