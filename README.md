# Prevendo uma Série Temporal com Machine Learning
## Definições
Uma série temporal é uma coleção de observações feitas sequencialmente ao longo do tempo.
## Modelo
Inicialmente, o modelo proposto foi linear:
```math
y(n) = w^T x(n) + w_0
```
Onde $\y(n)$ seria a saída esperada, $w$ um vetor de coeficientes, $x(n)$ uma coleção de amostras passadas e $w_0$ a constante.
## Análise
## Parte Computacional
A linguagem utilizada para a realização do modelo foi Python, devido a sua extensa biblioteca gráfica MatPlotLib, utilizada para plotar a série temporal e suas predições, bem como a biblioteca Pandas, utilizada para ler arquivos .csv através da linguagem Python, e a biblioteca NumPy, para cálculos de matrizes. Não foi permitida a utilização de bibliotecas de aprendizado de máquina, como SciKit-Learn e ToolBox, pois o objetivo era justamente aplicar os conceitos desde sua implementação ayé seu funcionamento.

