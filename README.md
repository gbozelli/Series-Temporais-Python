# Prevendo uma Série Temporal com Machine Learning
## Introdução
É natural que os dados sejam de extrema importância para uma análise científica. Ao longo do desenvolvimento da ciência, observar relações de causa e efeito era a base de qualquer experimento, e, para isso, era preciso coletar alguns pedaços de informações durante o processo. Esses 'pedaços' nada mais são que dados, e eles são a ponte entre a observação e a análise do método científico, principalmente no uso de predições. Um conjunto de dados pode, sozinho, indicar uma relação que é conduzida pelo tempo, ou seja, o tempo aqui é a nossa variável independente de uma função desconhecida. Chamamos essa função de série temporal.
## Conjunto de dados
A temperatura é uma variável que, não só depende do tempo, como é facilmente previsível por ele no senso comum. Costumamos fazer correlações básicas como "Está frio porque o inverno começou semana passada!" como "Vamos viajar em dezembro pois as praias estarão mais quentes". Há uma ligação entre épocas do ano e a temperatura registrada.
Nosso conjunto de dados se trata da temperatura mínima registrada na cidade de Melbourne, na Austrália, ao longo de 10 anos. Antes de começar a análise propriamente dita, vamos observar a cara dos nossos dados:
![Melbourne](https://user-images.githubusercontent.com/101020869/231739321-0ce4f724-8f5c-425a-8396-d0ed13994aa2.png)
De cara, você já deve pensar "Isso é uma função periódica!", e, de fato, ela se assemelha muito. Mas só olhando de longe. Vamos aproximar essa imagem:
![melbourne2](https://user-images.githubusercontent.com/101020869/236843597-ced440ac-7fda-40af-92a9-48f41bdcc402.png)
Deu pra ver que as coisas não são tão simples assim. Numa visão macroscópica, a função é periódica, mas observando suas características microscópicas, ela é bem bagunçada. Vamos partir pra análise do modelo e ver o que dá pra fazer com esse conjunto.
## Análise
Quando uma série dessas é proposta, a solução mais simples possível é pensar em utilizar dias anteriores para prever dias posteriores, principalmente pra lidar com esse 'caos' microscópico. A questão é: como? Podemos usar a semana passada, os dias de 1 mês atrás, ou até de anos anterioes. No geral, utilizar alguns dias anteriores ao que queremos prever pode funcionar, mas em análises mais complexas isso pode ser pouco suficiente. Só que análises mais complexas também exigem maior quantidade de dados, então vamos nos conter em trabalhar no seguinte modelo:
```math
G(t) = W^T X(t) + w_0
```
$G(t)$ é a temperatura do dia que queremos prever, e ela é uma função de 't' (o tempo), e X(t) é um vetor que contém as temperaturas de dias anteriores. $W$ um vetor de coeficientes, que multiplica o nosso X(t) para descobrir a resposta, enquanto w_0 é o nosso "viés". Nosso trabalho é encontrar quais os valores de coeficientes seriam bons pra prever temperaturas futuras e quantps dias passados nós precisamos utilizar. Vamos começar com os coeficientes:
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



