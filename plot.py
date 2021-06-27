import matplotlib.pyplot as plt
import model
import numpy as np
class Plot(model.Model):
    def __init__(self,x,y):
        super().__init__(x,y)
        
    
    def plot_line(self,x,y,label_name):
        x_max = np.max(x)
        x_min = np.min(x)

        X = np.linspace(x_max,x_min,1000)
        Y = self.get_b0(x,y) + self.get_b1(x,y)*X

        plt.plot(X,Y,color='red',label= label_name)
    
    def scatter(self,x,y):
        plt.scatter(x,y,color='green',label='Data Point')

    def x_label(self,x_label):
        plt.xlabel(x_label)

    def y_label(self,y_label):
        plt.ylabel(y_label)

    def create_plot(self):
        plt.legend()
        plt.show()
    
    # def save_fig(self,figname):
    #     plt.savefig(figname)



