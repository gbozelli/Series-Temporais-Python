import numpy as np
import numpy.matlib as mt
import matplotlib.pyplot as plt

def graphic(x,X,Y):
    x1 = np.linspace(0, 5, 100)
    fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
    ax.plot(x1, x1*x[1] + x[0], label=('',len(x)-1,'rd order'))
    ax.plot_date(X,Y)
    plt.show()
    return None

def GradientRegression(X,Y):
    Theta1 = 0
    Theta2 = 0

def Regression(X,Y):
    print(X)
    print(Y)
    W = np.linalg.solve(X,Y)
    return W

def createMatrix(m,n):
    Matrix = []
    Element = []
    for i in range(0,m+1):
        Element = []
        Matrix.append(Element)
        for j in range(0,n+1):
            Element.append(0)
    return Matrix

def valuesD(List, Sample):
    for i in range(0,len(Sample)):
        List.append(Sample[i])

def valuesMatrix(Matrix,Sample):
    m = len(Matrix)
    n = len(Matrix[0])
    Size = len(Sample)
    for i in range(0,m):
        for j in range(0,n):
            for k in range(0,Size):
                Matrix[i][j] += Sample[k]**(i+j)
    Matrix[0][0] = Size
    return Matrix

def valuesMatrixD(Matrix,Sample):
    m = len(Matrix)
    Size = len(Sample)
    for i in range(0,m):
        for k in range(0,Size):
            Matrix[i][j] = Sample[k]**(i*k)
    return Matrix

def valuesVector(Matrix,Sample):
    m = len(Matrix)
    Size = len(Sample)
    for i in range(0,m):
        for k in range(0,Size):
            Matrix[i] += Sample[k]**(i)
    return Matrix


