import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

def plotGraph(boll,W,Test):
    if boll == True:
        n = np.random.randint(0,1000-K)
        X = createX(Test,n,n+K)
        X1 = Test[n+K+1]
        Y = Test[n+K+1]
        T = data.index[2550+n:2550+n+K]
        T1 = data.index[2550+n+K+1]
        y = np.dot(W,X)
        plt.plot(T,X,'bo')
        plt.plot(T1,X1,'bo')
        plt.plot(T1,y,'or')
        if y>Y:
            plt.vlines(T1, y, Y, color='black')
        else:
            plt.vlines(T1, Y,y, color='black')
        plt.title("Temperatura mínima diária em Melbourne")
        plt.ylabel("Temperatura")
        plt.xlabel("Data")
        plt.grid(True)
        plt.show()
    return None

def fastTest(W,Set,bias,K):
    Y,Y1 = [], []
    X = createX(Set,3,3+K)
    for i in range (1,2*K):
        y = np.dot(W,X) - bias
        X = createX(Set,3+i,3+K+i)
        Y.append(abs(X[-1]-y)/X[-1])
        Y1.append(y)
    Error = sum(Y)/K
    return Error


def Regression(X,Y):
    W = []
    W = np.linalg.solve(X,Y)
    return W

def createX(Set,Inf,Sup):
    X = []
    for i in range(Inf,Sup):
        X.append(Set[i])
    return X

def TrainModel(Set,K,Test):
    Lenght = len(Set)-K
    i,j = 0,0
    X,S,Y = [],[],[]
    Error = 0.5
    W,Wp = [],[]
    biasc = 0
    while i+K+1<Lenght:
        j = i
        X,S,Y = [],[],[]
        while j<i+K:
            S = createX(Set,j,j+K)
            Y.append(Set[j+K+1])
            X.append(S)
            j += 1
        Wc = Regression(X,Y)
        n = np.random.randint(0,1000-K)
        X = createX(Test,n,n+K)
        Y = Test[n+K+1]
        biasc = -np.sqrt((np.dot(Wc,X) - Y)**2)
        i += K+1
        if fastTest(Wc,Test,biasc,K)<Error:
            Error = fastTest(Wc,Test,biasc,K)
            W = Wc  
            bias = biasc  
    return W, bias/K

def constructGraph(W,bias,Set):
    Y,Y1 = [], []
    X = createX(Set,3,3+K)
    for i in range (1,2*K):
        y = np.dot(W,X) - bias
        plt.plot(data.index[3+K-2+i],y,'bo')
        if y>X[-1]:
            plt.vlines(data.index[3+K-2+i], y, X[-1], color='black')
        else:
            plt.vlines(data.index[3+K-2+i], X[-1],y, color='black')
        X = createX(Set,3+i,3+K+i)
        Y.append(abs(X[-1]-y)/X[-1])
        Y1.append(y)
    Error = sum(Y)/K
    print(Error)
    T = data.index[3+K-1:3+3*K-2]
    X1 = createX(Set,3+K-1,3+3*K-2)
    plt.plot(T,X1,'or')
    plt.plot(T,X1,'red')
    plt.plot(T,Y1,'blue')
    plt.title("Temperatura mínima diária em Melbourne")
    plt.ylabel("Temperatura")
    plt.xlabel("Data")
    plt.grid(True)
    plt.show()
    

filename = 'daily-minimum-temperatures.csv'
names = ['Date','Temp']
data = pd.read_csv(filename)
data.index = pd.to_datetime(data.Date, format="%Y-%m-%d")
Set1 = data['Temp'].values.tolist()
Train = Set1[0:2550]
Test = Set1[2550:3650]
K = 30
W, bias = TrainModel(Set1,K,Test)
constructGraph(W,bias,Test)