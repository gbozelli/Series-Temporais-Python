# Prevendo uma Série Temporal com Machine Learning
## Definições
Uma série temporal é uma coleção de observações feitas sequencialmente ao longo do tempo. Numa série temporal, há a análise desse conjunto (advindo da variável de interesse). 
## Modelo
O conjunto de dados oferecido foi a temperatura mínima registrada em Melbourne, na Austrália, todos os dias, durante 10 anos (1981 a 1990). A temperatura foi considerada como uma variável aleatória discreta no tempo, e é representada por $x$, sendo $x(n) = [x(n-1),....,x(n-K)]^T$ um vetor de entradas.
Inicialmente, o modelo proposto foi linear:
```math
g(n) = w^T x(n) + w_0
```
Onde $g(n)$ seria a saída, $w$ um vetor de coeficientes, $x(n)$ uma coleção de amostras passadas e $w_0$ o "viés". O Hiperperâmetro K será selecionado de acordo com um algoritmo de validação (será posteriormente discutido na seção 'Parte Computacional'). Inicialmente, era preciso construir um sistema tal qual:
```math
[G_1,...G_K] = [W_1,...,W_K] [X_{11},...,X_{KK}]+ w_0
```
Que representa um sistema linear $KxK$. Era necessário encontrar os valores de W através de uma solução desse sistema, e $w_0$ era calculado de acordo com a seguinte equação:
```math
viés = sqrt{(g-y)^2}
```
Onde $y$ é a saída esperada. 
## Análise
![Melbourne](https://user-images.githubusercontent.com/101020869/231739321-0ce4f724-8f5c-425a-8396-d0ed13994aa2.png)
O gráfico, se analisado em termos anuais, se assemelha a uma função periódica. Caso a função seja vista de perto, há uma relativa "desordem" no nosso sistema:
![melbourne2](https://user-images.githubusercontent.com/101020869/236843597-ced440ac-7fda-40af-92a9-48f41bdcc402.png)

Traçar uma reta sobre os pontos seria inviável, visto que a confiabilidade obtida seria muita baixa para ser válida
## Parte Computacional
A linguagem utilizada para a realização do modelo foi Python, devido a sua extensa biblioteca gráfica MatPlotLib, utilizada para plotar a série temporal e suas predições, bem como a biblioteca Pandas, utilizada para ler arquivos .csv através da linguagem Python, e a biblioteca NumPy, para cálculos de matrizes. Não foi permitida a utilização de bibliotecas de aprendizado de máquina, como SciKit-Learn e ToolBox, pois o objetivo era justamente aplicar os conceitos de Machine Learning desde sua implementação até seu funcionamento.
O modelo básico de algorimo foi construído da seguinte forma:
```python
Conjunto de dados
para i em 3650*0,7/30 iterações:
  Cálculo de W
  Cálculo do viés
  Teste de W
  Teste do Viés
 retornar W e o Viés
```
![0483](https://user-images.githubusercontent.com/101020869/236843677-83126113-d468-405f-8830-cf08b63faf31.png)
Erro Percentual = 30%



