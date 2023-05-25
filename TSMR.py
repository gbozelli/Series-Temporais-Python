import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

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

def GenericLinearModel(X,Y,K):
    N = len(Y)
    Theta = np.zeros((K,1))
    Theta0 = 0
    iterations = 250
    lam = 0.001
    for i in range(iterations):
        Ypredred = np.dot(X,Theta) + Theta0
        for k in range(1,K+1):
            D = lam*(2/N)*np.sum((X[k-1]*(Y-Ypredred)))
            if(D>1e-30):
                Theta[k-1] += D
        Theta0 += lam*(2/N)*np.sum(Y-Ypredred)
    return Theta, Theta0
  
def rSquared(Y,Ypredred):
    meanY = np.sum(Y)/len(Y)
    sTotal, sResidual = 0, 0
    for i in range(len(Y)):
      sTotal += (Y[i]-meanY)**2
      sResidual += (Y[i]-Ypredred[i])**2
    return 1-(sResidual/sTotal)

def plotPrevision(Set,Theta,Theta0):
    X = []
    Ypred = 0
    Prevision = []
    N = 1000
    X = Set[0:K]
    for i in range (K+1,N+K+1):
        Ypred = np.dot(X,Theta) + Theta0
        X.append(Ypred[0])
        X = X[1:K+1]
        Prevision.append(Ypred)
    T = np.arange(K+1,N+K+1)
    X1 = Set[K+1:N+K+1]
    plt.figure(figsize=(14,6))
    plt.plot(T,X1,'blue',label='Temperatura real')
    plt.plot(T,Prevision,'black',label='Temperatura prevista')
    plt.plot(T,Prevision,'#FF000000',label='R^2 ='+str(rSquared(X1,Prevision))[1:7])
    plt.plot(T,Prevision,'#FF000000',label='K = '+str(K))
    plt.title("Temperatura mínima diária em Melbourne")
    plt.ylabel("Temperatura")
    plt.xlabel("Dias")
    plt.grid(True)
    plt.legend(loc='upper right')
    plt.show()

def plotGraph(Set,Theta, Theta0):
    Y1 = []
    X = Set[0:K]
    K1 = 1000
    for i in range (K+1,K1+K+1):
        y = np.dot(X,Theta) + Theta0
        X = Set[i:K+i]
        Y1.append(y)
    T = np.arange(K+1,K1+K+1)
    X1 = Set[K+1:K1+K+1]
    plt.figure(figsize=(14,6))
    plt.plot(T,X1,'blue',label='Temperatura real')
    plt.plot(T,Y1,'red',label='Temperatura prevista')
    plt.plot(T,Y1,'#FF000000',label='R^2 ='+str(rSquared(X1,Y1))[1:7])
    plt.plot(T,Y1,'#FF000000',label='K = '+str(K))
    plt.title("Temperatura mínima diária em Melbourne")
    plt.ylabel("Temperatura")
    plt.xlabel("Dias")
    plt.grid(True)
    plt.legend(loc='upper right')
    plt.show()

filename = 'daily-minimum-temperatures.csv'
names = ['Date','Temp']
data = pd.read_csv(filename)
Time = pd.to_datetime(data.Date, format="%Y-%m-%d")
Set = data['Temp'].values.tolist()
Train = Set[0:2550]
Test = Set[2550:3650]

K = 1
N = len(Train)-K
X, Y = generateSet(Train,N,K)

Theta, Theta0 = GenericLinearModel(X,Y,K)
N = N-K

plotPrevision(Test,Theta,Theta0)