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

```
IDENTIFICADOR_DO_ARTIGO_NO_SITE
TITULO_DO_ARTIGO
ABSTRACT_DO_ARTGO
```

Exemplo:
```
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
```

#Tratamento dos documentos
Para o desenvolvimento da aplicação, é necessário também realizar um tratamento nos dados coletados. Isso inclui:

1. Separação do texto em palavras (termos)
2. Redução das palavras ao seu radical (técnica como [stemming](http://en.wikipedia.org/wiki/Stemming))
3. Remoção de palavras que não agregam informação ao texto, como artigos, preposições e advérbios.

Quanto à redução, foi utilizada a biblioteca [stemming](https://bitbucket.org/mchaput/stemming) do Python. Já a identificação das chamadas stop words foi 
baseada na [lista de Armand Brahaj](http://norm.al/2009/04/14/list-of-english-stop-words/).

#Montagem da matriz de dados para consulta
Até este ponto, foram obtidos os documentos e também seus termos relevantes. A próxima etapa é relacionar como esses documentos e termos serão processados de 
maneira que um usuário consiga, através de uma consulta, recuperar os documentos relacionados.

##Latent semantic analysis (LSA) / Latent semantic indexing (LSI)
Técnica utilizada para analisar relacionamento entre conjuntos de documentos e seus termos. A partir destes relacionamentos, é possível realizar consultas de 
maneira a resgatar apenas os documentos similares ao critério de busca. A primeira etapa consiste na montagem de uma matriz de termos por documentos e, 
em seguida, na redução dessa matriz de maneira a facilitar a análise.

###Matriz de termos e documentos
O método é iniciado construindo uma matriz de termos por documentos, *A*<sub>m x n</sub>, que identifica a ocorrencia de *m* termos distintos numa coleção 
de *n* documentos.

Cada termo é representado por uma linha (num total de *m* linhas) e cada documento, por uma coluna (num total de *n* colunas), sendo cada célula da matriz *A*, 
*a<sub>i,j</sub>*, dada pelo produto do peso local do termo *l<sub>i,j</sub>* com o peso global do termo *g<sub>i</sub>*.

O peso local, *l<sub>i,j</sub>*, nada mais é que a frequência relativa de um termo *i* num documento *j*, enquanto o global descreve a freqência relativa 
de um termo *i* na coleção de documentos. Esses pesos podem ser calculados de diferentes maneiras, como por exemplo:

- *l<sub>i,j</sub>* = 1 se o termo *i* está presente no documento *j*, 0 caso contrário
- *l<sub>i,j</sub>* = *freq_term<sub>i,j</sub>* que é o total de ocorrências do termo *i* no documento *j*
- *l<sub>i,j</sub>* = *log<sub>2</sub> (freq_term<sub>i,j</sub> + 1)* que é o total de ocorrências do termo *i* no documento *j*
- *g<sub>i</sub>* = 1
- *g<sub>i</sub>* = *global_freq_term<sub>i</sub> / doc_freq<sub>i</sub>* onde *global_freq_term<sub>i</sub>* é o total de ocorrências do termo *i* 
na coleção de documentos e *doc_freq<sub>i</sub>*, o total de documentos que apresentam o termo *i*.
- *g<sub>i</sub>* = *log<sub>2</sub> (n / (1 + doc_freq<sub>i</sub>))*

### Aplicação do método SVD para redução da matriz
Construída a matriz, o passo seguinte é determinar como os termos e documentos estão relacionados. Para isso, utilizamos a Decomposição em Valores Singulares 
para encontrar uma matriz de menor dimensão que ressalte as relações e permita uma melhor análise dos dados. A partir desta fatoração, as informações 
semânticas mais relevantes são preservadas e o ruído e outros artefatos indesejáveis no espaço original são reduzidos.

#### Decomposição em Valores Singulares (SVD - Singular Value Decomposition)
A Decomposição em valores singulares de uma matriz *A* é uma fatoração na forma *A = U . S . V<sup>T</sup>*, onde *U* é uma matriz quadrada *m x m*; 
*S*, uma matriz diagonal com elementos não negativos, cujos elementos são denominados __valores singulares__ e *V<sup>T</sup>* (transposta de *V*) 
é uma matriz *n x n*. As *m* colunas de *U* são chamadas de __vetores singulares esquerdos__ e as *n* colunas de V, __vetores singulares direitos__.

A relação entre essas matrizes obtidas com a decomposição e a matriz original é:

- Os vetores singulares esquerdos de *A* são os auto vetores de *AA<sup>T</sup>*
- Os vetores singulares direitos de *A* são os auto vetores de *A<sup>T</sup>A*
- Os valores singulares não nulos de *A* são as raízes quadradas dos auto valores de ambas as matrizes *AA<sup>T</sup>* e *A<sup>T</sup>A*.

### Aproximação da matriz original para uma de menor posto
Algumas aplicações requerem a aproximação da matriz *A* (de posto *r*) por uma *A'* (de posto *k*, com *k < r*). Nesse caso, é possível demonstrar 
que a matriz *A'* é dada por *A' = U . S' . V<sup>T</sup>* onde *S'* é a mesma matriz *S*, porém com apenas os *r* maiores valores singulares 
(__Teorema de Eckart-Young__).

#Consulta sobre a matriz de dados
A similaridade entre os termos e documentos é um fator de quão próximos cada um destes espaços está, o que é tipicamente calculado como a função do ângulo
entre cada um destes vetores.

#Referências
- (Latent Semantic Analysis)[http://en.wikipedia.org/wiki/Latent_semantic_analysis]
- (Latent Semantic Indexing)[http://en.wikipedia.org/wiki/Latent_semantic_indexing]
- (Singular Value Decomposition)[http://en.wikipedia.org/wiki/Singular_Value_Decomposition]
- (Singular Value Decomposition Tutorial)[http://www.ling.ohio-state.edu/~kbaker/pubs/Singular_Value_Decomposition_Tutorial.pdf]
- (LingPipe)[http://alias-i.com/lingpipe/demos/tutorial/svd/read-me.html]
- (QR)[http://people.maths.ox.ac.uk/wendland/teaching/mt201011/part3.pdf]
- (Golub)[http://www.alterlab.org/teaching/BIOEN6670-1_2012/papers/Golub_1964.pdf]
