#Projeto
O objetivo do trabalho � a utiliza��o da �lgebra Linear para a solu��o de um problema pr�tico.
Para isso, contruimos uma aplica��o que � capaz de realizar uma consulta numa base de dados de documentos e assim retornar aqueles que melhor s�o representados 
pelos termos consultados.

#Desenvolvimento
O projeto foi desenvolvido na linguagem [Python 2.7](http://www.python.org/download/releases/2.7.5/) e faz uso tamb�m da biblioteca 
[PyGTK](http://www.pygtk.org/) para a constru��o da interface. A base de dados dos documentos aqui apresentada foi constru�da com aux�lio de um script 
em PHP e apresenta abstracts de artigos dispon�veis em [IEEE](http://ieeexplore.ieee.org/Xplore/home.jsp).

#Introdu��o
O projeto se dividiu em quatro etapas principais:

1. Busca de documentos
2. Tratamento dos documentos
3. Montagem da matriz de dados para consulta
4. Consulta sobre a matriz de dados

#Busca dos documentos
Para se criar uma base de dados, utilizamos um script PHP. Com ele foi poss�vel capturar informa��es de artigos (em [IEEE](http://ieeexplore.ieee.org/Xplore/home.jsp)),
como t�tulo e abstract.
Esta base ent�o � constru�da num arquivo com a seguinte estrutura:

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
Para o desenvolvimento da aplica��o, � necess�rio tamb�m realizar um tratamento nos dados coletados. Isso inclui:

1. Separa��o do texto em palavras (termos)
2. Redu��o das palavras ao seu radical (t�cnica como [stemming](http://en.wikipedia.org/wiki/Stemming))
3. Remo��o de palavras que n�o agregam informa��o ao texto, como artigos, preposi��es e adv�rbios.

Quanto � redu��o, foi utilizada a biblioteca [stemming](https://bitbucket.org/mchaput/stemming) do Python. J� a identifica��o das chamadas stop words foi 
baseada na [lista de Armand Brahaj](http://norm.al/2009/04/14/list-of-english-stop-words/).

#Montagem da matriz de dados para consulta
At� este ponto, foram obtidos os documentos e tamb�m seus termos relevantes. A pr�xima etapa � relacionar como esses documentos e termos ser�o processados de 
maneira que um usu�rio consiga, atrav�s de uma consulta, recuperar os documentos relacionados.

##Latent semantic analysis (LSA) / Latent semantic indexing (LSI)
T�cnica utilizada para analisar relacionamento entre conjuntos de documentos e seus termos. A partir destes relacionamentos, � poss�vel realizar consultas de 
maneira a resgatar apenas os documentos similares ao crit�rio de busca. A primeira etapa consiste na montagem de uma matriz de termos por documentos e, 
em seguida, na redu��o dessa matriz de maneira a facilitar a an�lise.

###Matriz de termos e documentos
O m�todo � iniciado construindo uma matriz de termos por documentos, *A*<sub>m x n</sub>, que identifica a ocorrencia de *m* termos distintos numa cole��o 
de *n* documentos.

Cada termo � representado por uma linha (num total de *m* linhas) e cada documento, por uma coluna (num total de *n* colunas), sendo cada c�lula da matriz *A*, 
*a<sub>i,j</sub>*, dada pelo produto do peso local do termo *l<sub>i,j</sub>* com o peso global do termo *g<sub>i</sub>*.

O peso local, *l<sub>i,j</sub>*, nada mais � que a frequ�ncia relativa de um termo *i* num documento *j*, enquanto o global descreve a freq�ncia relativa 
de um termo *i* na cole��o de documentos. Esses pesos podem ser calculados de diferentes maneiras, como por exemplo:

- *l<sub>i,j</sub>* = 1 se o termo *i* est� presente no documento *j*, 0 caso contr�rio
- *l<sub>i,j</sub>* = *freq_term<sub>i,j</sub>* que � o total de ocorr�ncias do termo *i* no documento *j*
- *l<sub>i,j</sub>* = *log<sub>2</sub> (freq_term<sub>i,j</sub> + 1)* que � o total de ocorr�ncias do termo *i* no documento *j*
- *g<sub>i</sub>* = 1
- *g<sub>i</sub>* = *global_freq_term<sub>i</sub> / doc_freq<sub>i</sub>* onde *global_freq_term<sub>i</sub>* � o total de ocorr�ncias do termo *i* 
na cole��o de documentos e *doc_freq<sub>i</sub>*, o total de documentos que apresentam o termo *i*.
- *g<sub>i</sub>* = *log<sub>2</sub> (n / (1 + doc_freq<sub>i</sub>))*

### Aplica��o do m�todo SVD para redu��o da matriz
Constru�da a matriz, o passo seguinte � determinar como os termos e documentos est�o relacionados. Para isso, utilizamos a Decomposi��o em Valores Singulares 
para encontrar uma matriz de menor dimens�o que ressalte as rela��es e permita uma melhor an�lise dos dados. A partir desta fatora��o, as informa��es 
sem�nticas mais relevantes s�o preservadas e o ru�do e outros artefatos indesej�veis no espa�o original s�o reduzidos.

#### Decomposi��o em Valores Singulares (SVD - Singular Value Decomposition)
A Decomposi��o em valores singulares de uma matriz *A* � uma fatora��o na forma *A = U . S . V<sup>T</sup>*, onde *U* � uma matriz quadrada *m x m*; 
*S*, uma matriz diagonal com elementos n�o negativos, cujos elementos s�o denominados __valores singulares__ e *V<sup>T</sup>* (transposta de *V*) 
� uma matriz *n x n*. As *m* colunas de *U* s�o chamadas de __vetores singulares esquerdos__ e as *n* colunas de V, __vetores singulares direitos__.

A rela��o entre essas matrizes obtidas com a decomposi��o e a matriz original �:

- Os vetores singulares esquerdos de *A* s�o os auto vetores de *AA<sup>T</sup>*
- Os vetores singulares direitos de *A* s�o os auto vetores de *A<sup>T</sup>A*
- Os valores singulares n�o nulos de *A* s�o as ra�zes quadradas dos auto valores de ambas as matrizes *AA<sup>T</sup>* e *A<sup>T</sup>A*.

### Aproxima��o da matriz original para uma de menor posto
Algumas aplica��es requerem a aproxima��o da matriz *A* (de posto *r*) por uma *A'* (de posto *k*, com *k < r*). Nesse caso, � poss�vel demonstrar 
que a matriz *A'* � dada por *A' = U . S' . V<sup>T</sup>* onde *S'* � a mesma matriz *S*, por�m com apenas os *r* maiores valores singulares 
(__Teorema de Eckart-Young__).

#Consulta sobre a matriz de dados
A similaridade entre os termos e documentos � um fator de qu�o pr�ximos cada um destes espa�os est�, o que � tipicamente calculado como a fun��o do �ngulo
entre cada um destes vetores.
