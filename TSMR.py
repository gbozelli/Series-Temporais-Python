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

def TrainModel(T,X):
    Theta1, Theta0, Error = dg(T,X)
    plotData(T,X)
    plotGraph(Theta1, Theta0, T, Error)
    return Theta1, Theta0, Error


def MultiVariableTest(Set,Theta, Theta0):
    n = np.random.randint(0,900)
    X = Set[n:100+n]
    Y = []
    for i in range (1,2*40):
        y = np.dot(Theta,X) + Theta0
        plt.plot(data.index[3+40-2+i],y,'or')
        if y>X[-1]:
            plt.vlines(data.index[3+40-2+i], y, X[-1], color='black')
        else:
            plt.vlines(data.index[3+40-2+i], X[-1],y, color='black')
        X = Set[n+i:40+n+i]
        Y.append(y)
    T = data.index[n+3+40-1:n+3+3*40-2]
    X1 = Set[n+3+40-1,n+3+3*40-2]
    plt.plot(T,X1,'bo')
    plt.plot(T,X1,'blue')
    plt.plot(T,Y,'red')
    plt.title("Temperatura mínima diária em Melbourne")
    plt.ylabel("Temperatura")
    plt.xlabel("Data")
    plt.grid(True)
    

filename = 'daily-minimum-temperatures.csv'
names = ['Date','Temp']
data = pd.read_csv(filename)
Time = pd.to_datetime(data.Date, format="%Y-%m-%d")
Set = data['Temp'].values.tolist()
Train = Set[0:2550]
Test = Set[2550:3650]
X = Train
N = len(X)
K = 10
X, Y = aux.generateSet(N,K)
A,T = aux.generateSet(N,K)
Theta, Theta0 = aux.GenericLinearModel(X,Y,K)
Y = T
N = N-K
MultiVariableTest(X,Theta,Theta0)