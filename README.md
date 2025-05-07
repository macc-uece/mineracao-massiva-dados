# Material da Disciplina Mineracao Massiva de Dados PPGCC/UECE

Código dos exemplos usados no curso Mineração Massiva de Dados PPGCC/UECE usando o Apache Spark e Tensorflow.

## Objetivo

Este repositório tem como objetivo disponibilizar os códigos utilizados na disciplina Mineração Massiva de Dados ofertado para o Programa de Pós-graduação em Ciência da Computação da UECE ([MACC/UECE](https://www.uece.br/macc)). O repositório possui um diretório *data* contendo os arquivos de *dataset* necessário para os scripts, alguns compactados em format gzip para reduzir o tamanho. O dataset para contagem de palavra distribuída e o dataset de imagens para o script de classificação de imagens, estão hospedados no Cluster LASID devido, respectivamente, a necessidade do arquivo texto estar disponivel para todos os workers e ao tamanho do dataset de imagens.

Todos os scripts foram testados em Python versão 3.11 e disponibilizados em formato Jupyter Lab Notebook para ser usado no Cluster do Laboratório de Sistemas Digitais ([LASID/UECE](https://lasid.uece.br)) 

Para acessar a plataforma Jupyter Lab use o endereço ([LASIDHUB/UECE](https://lasidhub.uece.br)) .

## Instalação

Se voce é aluno da disciplina, deve criar a conta  em ([LASIDHUB/UECE](https://lasidhub.uece.br)) conforme indicações do professor. Todo o ambiente está preparado para executar os scripts sem necessidade de nenhuma instalação adicional, no entanto voce pode instalar seus pacotes prediletos usando *pip* ou *conda*.

Na tela do Jupyter Lab, voce deve abrir uma janela do terminal para clonar os arquivos para sua conta usando git:

```
git clone https://github.com/macc-uece/mineracao-massiva-dados.git
```

Os scripts e as bases de dados estarão no diretório *mineracao-massiva-dados*

## Autores

Prof. Marcial P. Fernandez (marcial@larces.uece.br)

# Descrição dos Scripts

## Exemplo 01: Estatística e Gráficos

Análise de dados da Organização Mundial de Saude (WHO) sobre espectativa de vida e dados sociais de todos os paises do mundo. esse exemplo mostra algumas análises estatísticas simples e mostra a correlação entra vários parametros. Mostra também a criação de gráficos com *matplotlib*.

## Exemplo 02: Similaridade de Textos usando Locality-Sensitive Hashing (LSH)

Locality-Sensitive Hashing (LSH) é um algoritmo que separa grupos de palavras em baldes para identificar a probabilidade de semelhança. Com o LSH é possível fazer a comparação entre dois textos para medir a similaridade entre eles através do cálculo de uma função *Hash*. Essa técnica é muito usada para identificar plágio entre textos. Esse exemplo comparar dois livros da série Harry Potter. 

## Exemplo 03: Análise de Enlace

Muitos problemas em Ciência de Dados podem ser modelados com um grafo. Um exemplo é a análise da rede aérea em uma região, onde os vertices são os aeroportos e as arestas são as linhas aéreas. No entanto, apenas a contagem dos voos não indica o aeroporto com melhor conectividade, pois pode ser uma grande metrópole com muitos passageiros. Usando o algoritmo Pagerank podemos extrair infomações mais reais sobre os aeroportos com mais conectividade.

## Exemplo 04: Clustering

O clustering ou agrupamento de dados é um conjunto de técnicas de análise de dados que visa fazer agrupamentos automáticos (não supervisionados) de dados segundo o seu grau de semelhança. O critério de semelhança faz parte da definição do problema, podendo ser distância geográfica, custo, eficiência etc. A cada conjunto de dados resultante do processo dá-se o nome de grupo, aglomerado ou agrupamento (cluster). Esse exemplo procura definir a quantidade e localização de bases de distribução para veículos do Uber.

## Exemplo 05: Regras de Associação

Regras de associação são usadas para descobrir elementos que ocorrem em comum dentro de um determinado conjunto de dados e suas possiveis associações. As regras de Associação têm como premissa básica encontrar elementos que implicam na ocorrencia de outros elementos em uma mesma transação, ou seja, encontrar relacionamentos ou padrões frequentes entre conjuntos de dados. Esse exemplo clássico é estabelecer associação de compra de produtos por um consumidor, isto é, se o cliente compra um determinado produto, quais outros produtos ele tende a comprar também.

## Exemplo 06: Processamento Paralelo - Cálculo de Pi

Esse script mostra um exemplo de processamento paralelo no cluster LASID. Esse exemplo faz o cálculo do valor do número Pi usando método Monte Carlo. Neste exemplo é avaliado o desempenho para realização de operações matemáticas de forma distribuída. O tempo de processamento paralelo é comparado com a execução serial do mesmo número de instâncias.

## Exemplo 07: Processamento Paralelo - Contagem de Palavras 

Esse script mostra um exemplo de processamento paralelo com leitura de arquivo no cluster LASID. Esse exemplo faz a contagem de palavras de um texto usando o paradigma MapReduce, isto é, cada *worker* lê um pedaço do texto, conta a quantidade de ocorrências de cada palavra e faz a função Reduce consolidando o valor da contagem. Neste exemplo é avaliado o desempenho para realização de leitura de arquivo e operações matemáticas simples de forma distribuída. O tempo de processamento paralelo com diferentes particionamentos é comparado com a execução serial da contagem do mesmo texto.

## Exemplo 08: Análise de Comunidades

Análise de comunidades em grafos usando algoritmos Girvan-Newman e Spectral Clustering. Os algoritmos de comunidades é utilizado para analisar redes sociais através da modelagem das relações entre os entes através de um grafo agregando os mais próximos. O Zachary Karate Club é um exemplo clássico que modela a relação entre os membros de um clube de Karate para identificar a qual grupo eles pertencem.

## Exemplo 09: Sistemas de Recomendação

Sistema de Recomendação tem como objetivo selecionar itens personalizados para um usuário (cliente) com base nos interesses dele e dos interesses de usuários semelhantes conforme o contexto no qual estão inseridos. Essa técnica pode recomendar itens variados como, por exemplo, livros, filmes, notícias, música, vídeos, páginas de internet e produtos de uma loja virtual. Este exemplo faz a recomendação de filmes para um determinado usuário baseado nos seus gostos e de gostos de usuários semelhantes. O dataset utilizado é do site de recomendação de filmes MovieLens.

## Exemplo 10: Redução de Dimensionalidade usando Principal Component Analysis (PCA) 

Redução de dimensionalidade é uma técnica usada em mineração de dados e aprendizado de máquina que tem como objetivo reduzir o número de variáveis de entrada através da seleção do conjunto de variáveis principais. Apesar do risco de perda de acurácia na análise, a redução do tempo de processamento torna esta técnca importante para a análise de dados multivariáveis. Principal Component Analysis (PCA) é principal técnica para redução de dimensionalidade e análise de componentes principais. Este exemplo apresenta a redução de dimensionalidade usando PCA sobre dados nutricionais de alimentos da USDA National Nutrient Database de 45 campos para os 5 campos mais relevantes.  

## Exemplo 11: Aprendizado de Máquina (Machine Learning)

Aprendizado de Máquina (do inglês: *Machine learning*) é um campo da ciência da computação que estuda algoritmos para reconhecimento de padrões e do aprendizado computacional através de Inteligência Artificial (IA). Também podemos dizer que essas técnicas propiciam aos computadores a habilidade de aprender sem serem explicitamente programados, através de algoritmos que podem aprender com seus erros e fazer previsões sobre dados novos sem a necessidade de reprogramar o código. Este exemplo faz uma comparação de vários algoritmos de *Aprendizagem de Máquina* para predizer a espécie de flores Iris (Iris dataset) baseado no tamanho das pétalas e sépalas. Sã comparados os algoritmos K-Nearest Neighbors (KNN), Multilayer Perceptron (Rede Neural), Naive Bayes, Suport Vector Machines (SVM) e Decision Tree, mostrando acurácia e tempo de treinamento.

## Exemplo 12: Análise de Dados Contínuos (Streaming) 

Streaming é o processamento de dados contínuos gerados em tempo real por alguma fonte, como, dados de monitoramente, logs de erros ou transação de cartão de crédito. Os dados são ingeridos e pode ser realizado processamentos complexos como grafos e aprendizado de máquina nessa fonte de dados contínuos. Este exemplo realiza a identificação e contagem de palavras em um período de tempo a partir de um gerador de dados contínuo em formato texto. 

## Exemplo 13: Reconhecimento de Imagens

Uma das mais interessantes aplicações em visão computacional é o reconhecimento de imagens. Na Classificação de Imagens gostaríamos de classificar uma determinada imagem (foto) em algumas categorias pré-definidas, por exemplo, identificar se uma imagem é um gato ou um cão. A técnica mais eficaz para essa tarefa são as Redes Neurais Convolucionais (CNNs) e o procedimento é treinar um classificador a partir de uma base de dados conhecida e avaliar a acurácia do modelo. Uma outra técnica mostrada neste exemplo é o aumento de imagens (Image Augmentation) onde uma imagem pré-classificada sofre deslocamento, inversão, distorção para melhorar a capacidade de reconhecimento do modelo. Este exemplo mostra o treinamento e avaliação do reconhecimento de cinco espécies de flores usando Tensorflow e Keras.
