# Prevendo uma Série Temporal com Machine Learning
## Introdução
Uma série temporal é uma coleção de observações feitas sequencialmente ao longo do tempo. Numa previsão de séries temporais, há a análise desse conjunto de observações com o uso de algum método de regressão, e esse método realizará previsões sobre o sistema. 
## Modelo
O conjunto de dados oferecido foi a temperatura mínima registrada em Melbourne, na Austrália, todos os dias, durante 10 anos (1981 a 1990). A temperatura foi considerada como uma variável aleatória discreta no tempo, e é representada por $x$, sendo $x(n) = [x(n-1),....,x(n-K)]^T$ um vetor de entradas.
Inicialmente, o modelo proposto foi linear:
```math
G(n) = W^T X(n) + w_0
```
Onde $g(n)$ seria a saída, $w$ um vetor de coeficientes, $x(n)$ uma coleção de amostras passadas e $w_0$ o "viés". O Hiperperâmetro K será selecionado de acordo com uma validação baseada em tentativa e erro (que será posteriormente discutida na seção 'Parte Computacional'). Inicialmente, era preciso construir um sistema tal qual:
```math
[G_1,...G_K] = [w_1,...,w_K] [x_{11},...,x_{KK}]+ w_0
```
Que representa um sistema linear $KxK$. Era necessário encontrar os valores de $W$ e $w_0$ através de uma solução desse sistema. Utilizando um algoritmo de aprendizado via gradiente descendente, é possível aferir que os coeficientes serão dados por:
```math
[G_1,...G_K] = [W_1,...,W_K] [X_{11},...,X_{KK}]+ w_0
W_k = lam*(2/N)*np.sum((X[k-1]*(Y-Ypred)))
```
O conjunto será separado em 2 partes: 70% será destinada ao treino e 30% ao teste, sendo que o treino se baseará no método de implementação do gradiente descendente para mais de uma variável e o teste corresponderá à confiabilidade do modelo treinado.
## Análise
![Melbourne](https://user-images.githubusercontent.com/101020869/231739321-0ce4f724-8f5c-425a-8396-d0ed13994aa2.png)
O gráfico, se analisado em termos anuais, se assemelha a uma função periódica. Caso a função seja vista de perto, há uma relativa "desordem" no nosso sistema:
![melbourne2](https://user-images.githubusercontent.com/101020869/236843597-ced440ac-7fda-40af-92a9-48f41bdcc402.png)

O modelo linear deve ser capaz de utilizar $n-1$ dias anterioes para prever o $n-ésimo$ dia.
## Parte Computacional
A linguagem utilizada para a realização do modelo foi Python, devido a sua extensa biblioteca gráfica MatPlotLib, utilizada para plotar a série temporal e suas predições, bem como a biblioteca Pandas, utilizada para ler arquivos .csv através da linguagem Python, e a biblioteca NumPy, para cálculos de matrizes. Não foi permitida a utilização de bibliotecas de aprendizado de máquina, como SciKit-Learn e ToolBox, pois o objetivo era justamente aplicar os conceitos de Machine Learning, desde sua implementação até seu funcionamento.
O modelo básico de algorimo foi construído da seguinte forma:
```python
def GenericLinearModel(X,Y,K):
    N = len(Y)
    Theta = np.zeros((K,1))
    Theta0 = 0
    iterations = 250
    lam = 0.001
    for i in range(iterations):
        Ypred = np.dot(X,Theta) + Theta0
        for k in range(1,K+1):
            D = lam*(2/N)*np.sum((X[k-1]*(Y-Ypred)))
            if(D>1e-30):
                Theta[k-1] += D
        Theta0 += lam*(2/N)*np.sum(Y-Ypred)
    return Theta, Theta0
```

Observe que na 12º linha há uma validação do valor de D é avaliado por um erro do Python



