# Prevendo uma Série Temporal com Machine Learning
## Definições
Uma série temporal é uma coleção de observações feitas sequencialmente ao longo do tempo. Numa série temporal, há a análise desse conjunto (advindo da variável de interesse). 
## Modelo
O conjunto de dados oferecido foi a temperatura mínima registrada em Melbourne, na Austrália, todos os dias, durante 10 anos (1981 a 1990). A temperatura foi considerada como uma variável aleatória discreta no tempo, e é representada por $x$, sendo $x(n) = [x(n-1),....,x(n-K)]^T$ um vetor de entradas.
Inicialmente, o modelo proposto foi linear:
```math
y(n) = w^T x(n) + w_0
```
Onde $y(n)$ seria a saída eperada, $w$ um vetor de coeficientes, $x(n)$ uma coleção de amostras passadas e $w_0$ a constante. O Hiperperâmetro K será selecionado de acordo com a validação cruzada (do inglês, k-fold). 
## Análise
![Melbourne](https://user-images.githubusercontent.com/101020869/231739321-0ce4f724-8f5c-425a-8396-d0ed13994aa2.png)

## Parte Computacional
A linguagem utilizada para a realização do modelo foi Python, devido a sua extensa biblioteca gráfica MatPlotLib, utilizada para plotar a série temporal e suas predições, bem como a biblioteca Pandas, utilizada para ler arquivos .csv através da linguagem Python, e a biblioteca NumPy, para cálculos de matrizes. Não foi permitida a utilização de bibliotecas de aprendizado de máquina, como SciKit-Learn e ToolBox, pois o objetivo era justamente aplicar os conceitos de Machine Learning desde sua implementação até seu funcionamento.

