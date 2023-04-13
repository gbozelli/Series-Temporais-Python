import numpy as np
import numpy.matlib as mt
import matplotlib as mpl
import matplotlib.pyplot as plt

def graphic(x,X,Y):
    x1 = np.linspace(0, 5, 100)
    fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
    ax.plot(x1, x1*x[1] + x[0], label=('',len(x)-1,'rd order'))
    ax.plot_date(X,Y)
    plt.show()
    return None

def Regression(X,Y,order):
    D, r = createMatrix(len(X),order+1), createMatrix(len(Y),0)
    D = valuesMatrixD(D,X)
    r = valuesD(r,Y)
    print("Here")
    w = mt.multiply(mt.multiply(mt.invert(mt.multiply(D,mt.transpose(D))),mt.transpose(D)),r)
    print(r)
    return w

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
    n = len(Matrix[0])
    Size = len(Sample)
    for i in range(0,m):
        for j in range(0,n):
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


