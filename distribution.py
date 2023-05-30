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

def GenericLinearModel(X,Y,K,lam):
    N = len(Y)
    Theta = np.zeros((K,1))
    Theta0 = 0
    iterations = 500
    for i in range(iterations):
        Ypred = np.dot(X,Theta) + Theta0
        for k in range(1,K+1):
            D = lam*(2/N)*np.sum((X[k-1]*(Y-Ypred)))
            if(D>1e-30):
                Theta[k-1] += D
        Theta0 += lam*(2/N)*np.sum(Y-Ypred)
    return Theta, Theta0
  
def rSquared(Y,Ypred):
    meanY = np.sum(Y)/len(Y)
    sTotal, sResidual = 0, 0
    for i in range(len(Y)):
      sTotal += (Y[i]-meanY)**2
      sResidual += (Y[i]-Ypred[i])**2
    return 1-(sResidual/sTotal), 

def createY(Set,Theta, Theta0):
    Y1 = []
    X = Set[0:K]
    K1 = 1000
    for i in range (K+1,K1+K+1):
        y = np.dot(X,Theta) + Theta0
        X = Set[i:K+i]
        Y1.append(y[0])
    T = np.arange(K+1,K1+K+1)
    X1 = Set[K+1:K1+K+1]
    return X1, Y1
    

filename = 'daily-minimum-temperatures.csv'
names = ['Date','Temp']
data = pd.read_csv(filename)
Time = pd.to_datetime(data.Date, format="%Y-%m-%d")
Set = data['Temp'].values.tolist()
Train = Set[0:2550]
Test = Set[2550:3650]
K = 3

X, Y = generateSet(Train,2500,K)
Theta, Theta0 = GenericLinearModel(X,Y,K,0.000001)
Y1,Y2 = createY(Test,Theta, Theta0)
sResidual = []
for i in range(len(Y1)):
      sResidual.append((Y1[i]-Y2[i])**2)
N = 100

print(data.describe())
plt.xlabel("Temperatura")
plt.ylabel("Número")
plt.grid(True)
plt.hist(Set,bins=N)
plt.show()
