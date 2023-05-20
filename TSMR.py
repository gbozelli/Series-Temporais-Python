import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from LinearRegression import DescentGradient as dg
import LinearRegression as aux

def TestModel(Theta1,Theta0,X,T,Error):
    N = len(X)
    for i in range(N):
        XPred = Theta1*X[i] + Theta0
        Error = 1/N*(sum((X-XPred)**2))
    plotTest = plt.subplot()
    plotData(T,X)
    plotGraph(Theta1, Theta0, T, Error)
    return None

def plotGraph(Theta1, Theta0, T, Error):
    print(Error)
    plt.plot(T, Theta1*T+Theta0, 'black')
    return None

def plotData(T, X):
    plt.plot(T,X,'bo')
    plt.plot(T,X,'blue')
    plt.title("Temperatura mínima diária em Melbourne")
    plt.ylabel("Temperatura")
    plt.xlabel("Data")
    plt.grid(True)
    plt.ylim(0,30)
    return None

def createSet(Set,Inf,Sup):
    T = np.arange(0,Sup-Inf,1, dtype=int)
    X = Set[Inf:Sup]
    return X, T

def generateSet(Set,N,K):
    N = N - K
    X, Y, S = [], [], []
    for i in range(1,N+1):
        S.append(Set[K+i])
        Y.append(S)
        S = []
    for i in range(1,N+1):
        for j in range(K):
            S.append(Set[j+i])
        X.append(S)
        S = []
    return X,Y

def TrainModel(T,X):
    Theta1, Theta0, Error = dg(T,X)
    plotData(T,X)
    plotGraph(Theta1, Theta0, T, Error)
    return Theta1, Theta0, Error


def MultiVariableTest(Set,Theta, Theta0):
    Ys,Y1 = [], []
    yp = 0
    Ytest = []
    X = Set[0:K]
    K1 = 60
    Ys = Set[0:K]
    for i in range (K+1,K1+K+1):
        y = np.dot(X,Theta) + Theta0
        yp = np.dot(Ys,Theta) + Theta0
        plt.plot(data.index[i],y,'or')
        if y>X[-1]:
            plt.vlines(data.index[i], y, X[-1], color='black')
        else:
            plt.vlines(data.index[i], X[-1],y, color='black')
        X = Set[i:K+i]
        Y1.append(y)
        Ys.append(y)
        Ys = Ys[1:K+1]
        print(yp)
        Ytest.append(yp)
    T = np.arange(K+1,K1+K+1)
    X1 = Set[K+1:K1+K+1]
    plt.plot(T,X1,'bo')
    plt.plot(T,X1,'blue')
    plt.plot(T,Y1,'red')
    plt.scatter(T,Ytest,c='#e377c2')
    plt.title("Temperatura mínima diária em Melbourne")
    plt.ylabel("Temperatura")
    plt.xlabel("Data")
    plt.grid(True)
    plt.show()
    

filename = 'daily-minimum-temperatures.csv'
names = ['Date','Temp']
data = pd.read_csv(filename)
Time = pd.to_datetime(data.Date, format="%Y-%m-%d")
Set = data['Temp'].values.tolist()
Train = Set[0:2550]
Test = Set[2550:3650]

K = 2
N = len(Train)-K
X, Y = generateSet(Train,N,K)

Theta, Theta0 = aux.GenericLinearModel(X,Y,K)
A,T = aux.generateSet(N,K)
Y = T
N = N-K

MultiVariableTest(Test,Theta,Theta0)