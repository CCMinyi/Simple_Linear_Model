import pandas as pd
import numpy as np
from model import Model
from plot import Plot

def main(x,y,ln_x,ln_y):
    #Model one y = bo + b1*x
    Model1 = Model(x,y)
    model_one_b0 = Model1.get_b0(x,y)
    model_one_b1 = Model1.get_b1(x,y)
    print('r_sq',Model1.get_r_sq(x,y))
    print('intercept:',model_one_b0)
    print('slope:',model_one_b1)

    #plot regression and data
    Plot1 = Plot(x,y)
    Plot1.plot_line(x,y,'y = bo + b1*x')
    Plot1.scatter(x,y)
    Plot1.x_label('x-axis')
    Plot1.y_label('y-axis')
    Plot1.create_plot()
    

    # #residual plot
    model_one_residual = Model1.get_residuals(x,y)
    Plot1 = Plot(x,model_one_residual)
    Plot1.plot_line(x,model_one_residual,'residual plot')
    Plot1.scatter(x,model_one_residual)
    Plot1.x_label('x-axis')
    Plot1.y_label('y-axis')
    Plot1.create_plot()
    

    #Model two ln(y) = bo + b1*ln(x)
    
    Model2 = Model(ln_x,ln_y)
    model_two_b0 = Model1.get_b0(ln_x,ln_y)
    model_two_b1 = Model1.get_b1(ln_x,ln_y)
    print('r_sq',Model1.get_r_sq(ln_x,ln_y))
    print('intercept:',model_two_b0)
    print('slope:',model_two_b1)

    #plot regression and data
    Plot2 = Plot(ln_x,ln_y)
    Plot2.plot_line(ln_x,ln_y,'ln(y) = bo + b1*ln(x)')
    Plot2.scatter(ln_x,ln_y)
    Plot2.x_label('ln(x)-axis')
    Plot2.y_label('ln(y)-axis')
    Plot2.create_plot()
    

    # #residual plot
    model_two_residual = Model2.get_residuals(ln_x,ln_y)
    Plot2 = Plot(ln_x,model_two_residual)
    Plot2.plot_line(ln_x,model_two_residual,'residual plot')
    Plot2.scatter(ln_x,model_two_residual)
    Plot2.x_label('ln(x)-axis')
    Plot2.y_label('ln(y)-axis')
    Plot2.create_plot()
    


df = pd.read_excel('data/北京市租金部分變量_核心區.xlsx','Sheet1')
df = df[['租金','Area']]
df['ln_租金'] = df['租金'].apply(np.log)
df['ln_Area'] = df['Area'].apply(np.log)
main(df['Area'],df['租金'],df['ln_Area'],df['ln_租金'])
#資料簡介 描述
#print(df.describe())