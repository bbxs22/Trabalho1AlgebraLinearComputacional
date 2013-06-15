#Projeto
O objetivo do trabalho � a utiliza��o da �lgebra Linear para a solu��o de um problema pr�tico.
Para isso, contruimos uma aplica��o que � capaz de realizar uma consulta numa base de dados de documentos e assim retornar aqueles que melhor s�o representados 
pelos termos consultados.

#Desenvolvimento
O projeto foi desenvolvido na linguagem [Python 2.7](http://www.python.org/download/releases/2.7.5/) e faz uso tamb�m da biblioteca 
[PyGTK](http://www.pygtk.org/) para a constru��o da interface. A base de dados dos documentos aqui apresentada foi constru�da com aux�lio de um script 
em PHP e apresenta abstracts de artigos dispon�veis em [IEEE](http://ieeexplore.ieee.org/Xplore/home.jsp).

#Latent semantic analysis (LSA)
T�cnica utilizada para analisar relacionamento entre conjuntos de documentos e seus termos. Para isso, uma matriz contendo a contagem de palavras por
documento � constru�da e a t�cnica, conhecida como Decomposi��o em Valores Singulares (SVD - Singular Value Decomposition) � utilizada a fim de reduzir
o n�mero de colunas enquanto a similaridade entre linhas � preservada.

Desta forma, � poss�vel relacionar palavras, palavras e documentos e tamb�m documentos entre si.

#Latent semantic indexing (LSI)
T�cnica utilizada para se encontrar padr�es entre termos e conceitos contidos em um conjunto de textos. � poss�vel assim realizar consultas sobre um 
conjunto de documentos, que retornam resultados que s�o semanticamente similares ao crit�rio de busca. Isso � poss�vel mesmo que os resultados n�o 
compartilhem uma palavra ou mais palavras espec�ficas com o crit�rio de busca.

#Matriz de termos e documentos
O m�todo � iniciado construindo uma matriz de termos por documentos, A(m x n), que identifica a ocorrencia de m termos distintos numa cole��o de n documentos.
Desta forma, cada termo � representado por uma linha (num total de m linhas) e cada documento, por uma coluna (num total de n colunas). Assim, cada 
c�lula da matriz A, aij, � representado pelo produto do peso local do termo (lij) e do peso global do termo (gi).

O peso local, lij, nada mais � que a frequ�ncia relativa de um termo i num documento j, enquanto o global descreve a freq�ncia relativa de um termo na 
cole��o de documentos.

Algumas fun��es locais:

Lij = 1 se o termo i est� presente no documento j, 0 caso contr�rio
Lij = numero de ocorr�ncias do termo i no documento j

Algumas fun��es globais:

Gi = 1
Gi = raz�o entre o n�mero total de ocorrencias do termo i na cole��o de documentos e o n�mero de documentos que apresentam o termo i
Gi = logaritmo da raz�o entre o n�mero total de termos e o n�mero de documentos que apresentam o termo i + 1

#Redu��o das dimens�es da matriz - SVD
Constru�da a matriz, o segundo passo � determinar os relacionamentos entre termos e documentos. Para isso, utilizamos o SVD para encontrar uma matriz de 
posto reduzido. Com isso, as informa��es sem�nticas mais relevantes s�o preservadas, al�m de reduzir o ru�do e outros artefatos indesej�veis no espa�o original 
de A.

## SVD
A Decomposi��o em valores singulares de uma matriz A � uma fatora��o na forma

A = U S V*

onde U � uma matriz quadrada m x m; S, uma matriz diagonal com elementos n�o negativos, cujos elementos s�o denominados valores 
singulares e V* (transposta de V) � uma matriz n x n.
As m colunas de U s�o chamadas de vetores singulares esquerdos e as n colunas de V, vetores singulares direitos.

Os vetores singulares esquerdos de M s�o os auto vetores de MM*
Os vetores singulares direitos de M s�o os auto vetores de M*M
Os valores singulares n�o nulos de M s�o as raizes quadradas dos auto valores de ambas as matrizes MM* e M*M.

## Aproxima��o da matriz original para uma de menor posto
Algumas aplica��es requerem a aproxima��o da matriz M por uma M' de posto r. Nesse caso, � poss�vel demosntrar que a matriz M' � dada por

M' = U S' V*

onde S' � a mesma matriz S, por�m com apenas or r maiores valores singulares. Esse � conhecido como teorema de Eckart-Young.

#Consulta
A similaridade entre os termos e documentos � um fator de qu�o pr�ximos cada um destes espa�os est�, o que � tipicamente calculado como a fun��o do �ngulo
entre cada um destes vetores.

Os mesmos passos s�o aplicados � consulta.

### Montar a base de dados
Usando o PHP, foi feita uma aplica��o que acessa o servidor do IEEE e coleta ot t�tulos e abstracts de N papers cadastrados.
� gerado um arquivo contendo todas essas informa��es.

### Remover stopwords e aplicar stemming
Em python, foi criada uma aplica��o que l� o arquivo gerado pelo PHP e, para cada documento, separa as palavras, remove os stopwords e faz stemming.

### Construir tabela de frequencias e relevancias
Para cada documento, � calculada a freqencia de cada termo
Em sequida, para cada termo, � calculado o deu IDF. Ou seja, log(|numDocs| / |numdocs com termo i|).
Com esses valores calculados, a frequencia do termo � dada pelo TF * IDF. Esse valor � colocado na matriz.

### Calcular SVD
