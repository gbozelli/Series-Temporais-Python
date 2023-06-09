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

def GenericLinearModel(X,Y,K,lam,iterations):
    N = len(Y)
    Theta = np.zeros((K,1))
    Theta0 = 0
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

def plotRsquared(Set,Theta,Theta0,K):
    Y1 = []
    X = Set[0:K]
    K1 = 1000
    for i in range (K+1,K1+K+1):
        y = np.dot(X,Theta) + Theta0
        X = Set[i:K+i]
        Y1.append(y)
    T = np.arange(K+1,K1+K+1)
    X1 = Set[K+1:K1+K+1]
    return rSquared(X1,Y1)

def rSquaredPerK(Train,Test):
    X, Y = generateSet(Train,2480,K)
    iterations = 250
    for K in range(1,30):
        if K<=5:
            lam=0.0001
        if K>5 and K<=16:
            lam=0.00001
        if K>16:
            lam=0.000001
        Theta, Theta0 = GenericLinearModel(X,Y,K,lam,iterations)
        rSquaredTrain = plotRsquared(Train,Theta,Theta0,K)
        rSquaredReal = plotRsquared(Test,Theta,Theta0,K)
        plt.plot(K,rSquaredReal,'blue',label='Teste')
        plt.plot(K,rSquaredTrain,'red',label='Treino')
    plt.ylabel("R^2")
    plt.xlabel("K")
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

rSquaredPerK(Train,Test)


