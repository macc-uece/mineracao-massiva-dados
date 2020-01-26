# Material da Disciplina Mineracao Massiva de Dados MACC/UECE

Código dos exemplos usados no curso Mineração Massiva de Dados MACC/UECE usando o Apache Spark.

## Objetivo

Este repositório tem como objetivo disponibilizar os códigos utilizados na disciplina Mineração Massiva de Dados ofertado para o Mestrado Acadêmico em Ciência da Computação da UECE ([MACC/UECE](https://www.uece.br/macc)). O repositório possui um diretório *data* contendo os arquivos de *dataset* necessário para os scripts em format gzip para reduzir o tamanho. 

Todos os scripts foram escritos em Python versão 3.6 e disponibilizados em formato Jupyter Lab Notebook para ser usado no Cluster do Laboratório de Sistemas Digitais ([LASID/UECE](https://lasid.uece.br)) 

ATENÇÃO: Desde julho/2019 o LASID está usando a plataforma Jupyter Lab no endereço ([LASIDHUB/UECE](https://lasidhub.uece.br)) .

## Instalação

Se voce é aluno da disciplina, deve solicitar ao professor a criação de sua conta no cluster LASID. Todo o ambiente está preparado para executar os scripts sem necessidade de instalação adicional.

Na tela do Jupyter Lab, abrir uma janela do terminal para copiar os arquivos para sua conta usando git:

```
git clone https://github.com/macc-uece/mineracao-massiva-dados.git
```

## Autores

Prof. Marcial P. Fernandez (marcial@larces.uece.br)


# Descrição dos Scripts

## Exemplo 01: Estatística e Gráficos

Análise de dados da Organização Mundial de Saude (WHO) sobre espectativa de vida e dados sociais de todos os paises do mundo. Mostra algumas análises estatísticas simples e a criação de gráficos com *matplotlib*.

## Exemplo 02: Similaridade de Textos usando Locality-Sensitive Hashing (LSH)

Comparação de dois textos de livros para verificar a similaridade entre eles. Os livros são dois romances de James Joyce do projeto Gutemberg: Ulysses e Dubliners.

## Exemplo 03: Análise de Enlace

## Exemplo 04: Análise de Dados Contínuos (Streaming)

## Exemplo 05: Regras de Associação e Clustering

## Exemplo 06: Processamento Paralelo - Cálculo de Pi

Esse script mostra um exemplo de processamento paralelo no cluster LASID. Esse exemplo faz o cálculo do valor do número Pi usando método Monte Carlo. O tempo de processamento é comparado com a execução serial do mesmo número de instâncias.

## Exemplo 07: Processamento Paralelo - Contagem de Palavras 

## Exemplo 08: Análise de Comunidades

Análise de comunidades em grafos usando algoritmos Girvan-Newman e Spectral Clustering. Dataset Zachary Karate Club. 

## Exemplo 09: Sistemas de Recomendação

Sistema de Recomendação tem como objetivo selecionar itens personalizados para um usuário (cliene) com base nos interesses dele e dos interesses de usuários semelhantes conforme o contexto no qual estão inseridos. Esta técnica pode recomendar itens variados como, por exemplo, livros, filmes, notícias, música, vídeos, páginas de internet e produtos de uma loja virtual. esse exemplo faz a recomendação de filmes para um determinado usuário baseado nos seus gostos e de gostos de outros usuários semelhantes.

## Exemplo 10: Redução de Dimensionalidade usando Principal Component Analysis (PCA) 

## Exemplo 11: Aprendizado de Máquina (Machine Learning)

Comparação de vários algoritmos de Aprendizagem de Máquina para predizer espécie de flores Iris (Iris dataset). Executa os algoritmos K-Nearest Neighbors (KNN), Multilayer Perceptron (Rede Neural), Naive Bayes, Suport Vector Machines (SVM) e Decision Tree, mostrando acurácia e tempo de treinamento.         
