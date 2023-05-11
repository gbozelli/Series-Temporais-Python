import numpy as np
from numpy import random as r
from matplotlib import pyplot as plt

def GenerateData():
    N, center, sigma, sigma_n = 100, 5, 20, 0.1  
    a,b = 0.4,1.3        
    X,n = center+sigma*r.rand(N,1),sigma_n*r.randn(N,1)       
    Y = a*X+b+n 
    return a,b,X,Y   

def DescentGradient(X,Y):
    Theta1, Theta0 = 0,0
    k,lam = 20000, 0.001
    N = len(X)
    for i in range(k):
        YPred = Theta1*X + Theta0
        Theta1 += lam*(2/N)*sum((Y-YPred)*X)
        Theta0 += lam*(2/N)*sum((Y-YPred))
        Error = 1/N*(sum((Y-YPred)**2))  
    return Theta1, Theta0, Error

def BuildGraph(X,Y,a,b,Theta1, Theta0, Error):
    x = X
    plt.figure()
    plt.plot(X,Y,'o',alpha=0.5)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x, a*x+b, 'blue')
    plt.plot(x, Theta1*x+Theta0, 'red')
    plt.show()

def GenericLinearModel(X,Y,K):
    N = len(Y)
    Theta = np.empty(K)
    iterations = 0
    lam = 0
    for i in range(iterations):
        YPred = np.dot(Theta, X)
        for k in range(K,1,-1):
            Theta[k] += lam*(2/N)*sum((Y[i]-YPred)*X[k][i]**k)
        Theta[0] = (Y[i]-YPred)
        Error = 1/N*(sum((Y-YPred)**2))
    return Theta, Error
