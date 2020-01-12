import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

data = pd.read_csv('C:\\Users\\dmcut\\OneDrive\\Documents\\AI_ML_DL_training\\Advertising.csv')
x = data.TV
y = data.sales
print(x)
x_mean = x.mean()
y_mean = y.mean()

num = 0
den = 0 

for i in range(200):
    num += (x[i]-x_mean)*(y[i]-y_mean) 
    den += (x[i]-x_mean)**2
    
m = num/den
print(m)
c =  y_mean - m*x_mean
print(c)

r = np.linspace(0, 350, 10)
k = m*r + c

plt.plot(r, k)
plt.scatter(x, y)
plt.show

