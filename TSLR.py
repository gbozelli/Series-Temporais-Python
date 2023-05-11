import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from LinearRegression import DescentGradient as dg
from LinearRegression import GenericLinearModel as glm

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

filename = 'daily-minimum-temperatures.csv'
names = ['Date','Temp']
data = pd.read_csv(filename)
Time = pd.to_datetime(data.Date, format="%Y-%m-%d")
Set = data['Temp'].values.tolist()
Train = Set[0:2550]
Test = Set[2550:3650]
R = 42
X, T = createSet(Train, R,R+41)
Theta, Error = glm(X,Y,10)
#Theta1, Theta0, Error = TrainModel(T,X)
#print(Theta1, Theta0)
plt.show()