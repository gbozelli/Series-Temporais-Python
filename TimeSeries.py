import numpy as np
from Regression import Regression
from matplotlib import pyplot as plt
import pandas as pd
import random

def plotGraph(boll):
    if boll == True:
        plt.plot(data.index,data.Temp)
        plt.title("Temperatura mínima diária em Melbourne de 1981 a 1990")
        plt.ylabel("Temperatura")
        plt.xlabel("Data")
        plt.grid(True)
        plt.show()
    return None

filename = 'daily-minimum-temperatures.csv'
names = ['Date','Temp']
data = pd.read_csv(filename)
data.index = pd.to_datetime(data.Date, format="%Y-%m-%d")
K = 30
Date = []
for i in range(0,3650):
    Date.append(i)

plotGraph(True)
