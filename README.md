#Projeto
O objetivo do trabalho é a utilização da Álgebra Linear para a solução de um problema prático.
Para isso, contruimos uma aplicação que é capaz de realizar uma consulta numa base de dados de documentos e assim retornar aqueles que melhor são representados 
pelos termos consultados.

#Desenvolvimento
O projeto foi desenvolvido na linguagem [Python 2.7](http://www.python.org/download/releases/2.7.5/) e faz uso também da biblioteca 
[PyGTK](http://www.pygtk.org/) para a construção da interface. A base de dados dos documentos aqui apresentada foi construída com auxílio de um script 
em PHP e apresenta abstracts de artigos disponíveis em [IEEE](http://ieeexplore.ieee.org/Xplore/home.jsp).

#Introdução
O projeto se dividiu em quatro etapas principais:

1. Busca de documentos
2. Tratamento dos documentos
3. Montagem da matriz de dados para consulta
4. Consulta sobre a matriz de dados

#Busca dos documentos
Para se criar uma base de dados, utilizamos um script PHP. Com ele foi possível capturar informações de artigos (em [IEEE](http://ieeexplore.ieee.org/Xplore/home.jsp)),
como título e abstract.
Esta base então é construída num arquivo com a seguinte estrutura:

IDENTIFICADOR_DO_ARTIGO
TITULO_DO_ARTIGO
ABSTRACT_DO_ARTGO

Exemplo:
6185384
Wireless Network System with Autonomous Antenna Actuator Control for Disaster Information
In Japan, there have been a number of serious natural disasters such as earthquakes, tsunami, as represented by the East Japan Great...
1185384
A novel technique for optimising the harmonics and reactive power under nonsinusoidal voltage conditions
The conventional power factor correction techniques assume the voltage source to be purely sinusoidal. But this is rarely true because...
6325384
Picosecond laser machining in the bulk of transparent dielectrics: Critical comparison with fs-laser direct writing
Picosecond lasers for bulk machining of transparent dielectrics are assessed as an alternative to fs-lasers. Nanogratings and...
6315384
Verification of automotive control applications using S-TaLiRo
S-TALIRO is a software toolbox that performs stochastic search for system trajectories that falsify realtime temporal logic specifications...
6315383
A high gain observer for enclosed mass estimation in a spark ignited engine
A high gain non linear observer is implemented to estimate the enclosed mass in the combustion chamber of a spark ignited engine. The observer...
5718383
A Software Size Estimation Method Based on Improved FPA
Software size estimation is the key of entire software program project, and the accurate estimation immediately affect the success of project...
5718384
Classification of Software Defect Detected by Black-Box Testing: An Empirical Study
Software defects which are detected by black box testing (called black-box defect) are very large due to the wide use of black-box testing, but...

#Tratamento dos documentos
Para o desenvolvimento da aplicação, é necessário também realizar um tratamento nos dados coletados. Isso inclui:

1. Separação do texto em palavras (termos)
2. Redução das palavras ao seu radical (técnica como [stemming](http://en.wikipedia.org/wiki/Stemming))
3. Remoção de palavras que não agregam informação ao texto, como artigos, preposições e advérbios.

Quanto à redução, foi utilizada a biblioteca [stemming](https://bitbucket.org/mchaput/stemming) do Python. Já a identificação das chamadas stop words foi 
baseada na [lista de Armand Brahaj](http://norm.al/2009/04/14/list-of-english-stop-words/).

#Montagem da matriz de dados para consulta

#Latent semantic analysis (LSA)
Técnica utilizada para analisar relacionamento entre conjuntos de documentos e seus termos. Para isso, uma matriz contendo a contagem de palavras por
documento é construída e a técnica, conhecida como Decomposição em Valores Singulares (SVD - Singular Value Decomposition) é utilizada a fim de reduzir
o número de colunas enquanto a similaridade entre linhas é preservada.

Desta forma, é possível relacionar palavras, palavras e documentos e também documentos entre si.

#Latent semantic indexing (LSI)
Técnica utilizada para se encontrar padrões entre termos e conceitos contidos em um conjunto de textos. É possível assim realizar consultas sobre um 
conjunto de documentos, que retornam resultados que são semanticamente similares ao critério de busca. Isso é possível mesmo que os resultados não 
compartilhem uma palavra ou mais palavras específicas com o critério de busca.

#Matriz de termos e documentos
O método é iniciado construindo uma matriz de termos por documentos, A(m x n), que identifica a ocorrencia de m termos distintos numa coleção de n documentos.
Desta forma, cada termo é representado por uma linha (num total de m linhas) e cada documento, por uma coluna (num total de n colunas). Assim, cada 
célula da matriz A, aij, é representado pelo produto do peso local do termo (lij) e do peso global do termo (gi).

O peso local, lij, nada mais é que a frequência relativa de um termo i num documento j, enquanto o global descreve a freqência relativa de um termo na 
coleção de documentos.

Algumas funções locais:

Lij = 1 se o termo i está presente no documento j, 0 caso contrário
Lij = numero de ocorrências do termo i no documento j

Algumas funções globais:

Gi = 1
Gi = razão entre o número total de ocorrencias do termo i na coleção de documentos e o número de documentos que apresentam o termo i
Gi = logaritmo da razão entre o número total de termos e o número de documentos que apresentam o termo i + 1

#Redução das dimensões da matriz - SVD
Construída a matriz, o segundo passo é determinar os relacionamentos entre termos e documentos. Para isso, utilizamos o SVD para encontrar uma matriz de 
posto reduzido. Com isso, as informações semânticas mais relevantes são preservadas, além de reduzir o ruído e outros artefatos indesejáveis no espaço original 
de A.

## SVD
A Decomposição em valores singulares de uma matriz A é uma fatoração na forma

A = U S V*

onde U é uma matriz quadrada m x m; S, uma matriz diagonal com elementos não negativos, cujos elementos são denominados valores 
singulares e V* (transposta de V) é uma matriz n x n.
As m colunas de U são chamadas de vetores singulares esquerdos e as n colunas de V, vetores singulares direitos.

Os vetores singulares esquerdos de M são os auto vetores de MM*
Os vetores singulares direitos de M são os auto vetores de M*M
Os valores singulares não nulos de M são as raizes quadradas dos auto valores de ambas as matrizes MM* e M*M.

## Aproximação da matriz original para uma de menor posto
Algumas aplicações requerem a aproximação da matriz M por uma M' de posto r. Nesse caso, é possível demosntrar que a matriz M' é dada por

M' = U S' V*

onde S' é a mesma matriz S, porém com apenas or r maiores valores singulares. Esse é conhecido como teorema de Eckart-Young.

#Consulta
A similaridade entre os termos e documentos é um fator de quão próximos cada um destes espaços está, o que é tipicamente calculado como a função do ângulo
entre cada um destes vetores.

Os mesmos passos são aplicados à consulta.

### Montar a base de dados
Usando o PHP, foi feita uma aplicação que acessa o servidor do IEEE e coleta ot títulos e abstracts de N papers cadastrados.
É gerado um arquivo contendo todas essas informações.

### Remover stopwords e aplicar stemming
Em python, foi criada uma aplicação que lê o arquivo gerado pelo PHP e, para cada documento, separa as palavras, remove os stopwords e faz stemming.

### Construir tabela de frequencias e relevancias
Para cada documento, é calculada a freqencia de cada termo
Em sequida, para cada termo, é calculado o deu IDF. Ou seja, log(|numDocs| / |numdocs com termo i|).
Com esses valores calculados, a frequencia do termo é dada pelo TF * IDF. Esse valor é colocado na matriz.

### Calcular SVD
