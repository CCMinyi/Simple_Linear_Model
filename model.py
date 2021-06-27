from typing import List
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

class Model():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def calculate(self,x,y)-> float:
        #calculate b0 and b1
        numerator = 0
        denominator = 0
        for i in range(len(x)):
            numerator += (x[i]-np.mean(x))*(y[i]-np.mean(y))
            denominator += (x[i]-np.mean(x))**2
        self.__b1 = numerator/denominator
        self.__b0 = np.mean(y)-(self.__b1*np.mean(x))

        #calculate rmse
        rsse = 0
        for i in range(len(x)):
            rsse += (y[i]-(self.__b0+self.__b1*x[i]))**2
        self.__rmse = np.sqrt(rsse/(len(x)-2))

        #calculate r_sq
        self.__suqares = []
        self.__residual_squar = []
        self.__residuals = []
        

        for i in range(len(x)):
            self.__suqares.append((y[i]-np.mean(y))**2)
            self.__residual_squar.append((y[i]-(self.__b0+self.__b1*x[i]))**2)
        self.__sum_of_suqares = sum(self.__suqares)
        self.__sum_of_residuals = sum(self.__residual_squar)

        self.__r_sq = 1 - (self.__sum_of_residuals/self.__sum_of_suqares)

        for i in range(len(x)):
            self.__residuals.append(y[i]-(self.__b0+self.__b1*x[i]))


        

    def get_b0(self,x,y)-> float:
        self.calculate(x,y)
        return self.__b0

    def get_b1(self,x,y)-> float:
        self.calculate(x,y)
        return self.__b1

    def get_mse(self,x,y)-> float:
        self.calculate(x,y)
        return self.__rmse

    def get_r_sq(self,x,y)-> float:
            self.calculate(x,y)
            return self.__r_sq
    def get_residuals(self,x,y) -> List:
        self.calculate(x,y)
        return self.__residuals
