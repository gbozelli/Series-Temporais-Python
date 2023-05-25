import numpy as np
from numpy import random as r
from matplotlib import pyplot as plt

def GenerateData():
    N, center, sigma, sigma_n = 100, 5, 20, 0.1  
    a,b = 0.4,1.3        
    X,n = center+sigma*r.rand(N,1),sigma_n*r.randn(N,1)       
    Y = a*X+b+n 
    return a,b,X,Y   

def BuildGraph(X,Y,T,Theta, Theta0):
    x = X
    print(Theta)
    plt.figure()
    plt.plot(Y,T,'bo')
    Ypred = np.dot(X,Theta) + Theta0
    plt.plot(T,Ypred,'red')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def DescentGradient(X,Y):
    Theta1, Theta0 = 0,0
    k,lam = 2000, 0.001
    N = len(X)
    for i in range(10):
        YPred = Theta1*X + Theta0
        Theta1 += lam*(2/N)*sum((Y-YPred)*X)
        Theta0 += lam*(2/N)*sum((Y-YPred))
        Error = 1/N*(sum((Y-YPred)**2))  
        print(Theta1)
    return Theta1, Theta0, Error

def GenericLinearModel(X,Y,K):
    N = len(Y)
    Theta = np.zeros((K,1))
    Theta0 = 0
    iterations = 5000
    lam = 0.0001
    for i in range(iterations):
        YPred = np.dot(X,Theta) + Theta0
        for k in range(1,K+1):
            D = lam*(2/N)*np.sum((X[k-1]*(Y-YPred)))
            if(D>0.000000000000000000000000000000001):
                Theta[k-1] += D
        Theta0 += lam*(2/N)*np.sum(Y-YPred)
    return Theta, Theta0

def generateSet(N,K):
    N = N - K
    X, Y, S = [], [], []
    for i in range(1,N+1):
        S.append(K+i)
        Y.append(S)
        S = []
    for i in range(1,N+1):
        for j in range(K):
            S.append(j+i)
        X.append(S)
        S = []
    return X,Y

iterations = 5000
lam = 0.00000001

