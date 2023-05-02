import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

def plotGraph(boll,X,T,y):
    if boll == True:
        plt.plot(T,X,'bo')
        plt.plot(T[len(T)-1],X[len(T)-1],'or')
        plt.plot(y,X[len(T)-1],'or')
        plt.title("Temperatura mínima diária em Melbourne")
        plt.ylabel("Temperatura")
        plt.xlabel("Data")
        plt.grid(True)
        plt.show()
    return None

def findW(X,Y,K):
    S = []
    n = np.random.randint(0,3649)
    Y.append(data.Temp[n+1])
    for i in range(0,K):
        S.append(data.Temp[i+n])
    X.append(S)
    if len(Y) < K:
        findW(X,Y,K)
    else:
        W = []
        W = Regression(X,Y)
        return W

def Regression(X,Y):
    W = np.linalg.solve(X,Y)
    return W

filename = 'daily-minimum-temperatures.csv'
names = ['Date','Temp']
data = pd.read_csv(filename)
data.index = pd.to_datetime(data.Date, format="%Y-%m-%d")
K = 5
X = []
Y = []
W = []
W = (findW(X,Y,K))

X = []
Y = []
n = np.random.randint(0,3649)
T = []
for i in range(n-K,n):
    T.append(data.Date[i])
Y.append(data.Temp[n+1])
for i in range(0,K):
    X.append(data.Temp[i+n])

print(X)
y = np.dot(W,X)
plotGraph(True,X,T,y)
