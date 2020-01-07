import numpy as np
import matplotlib.pyplot as plt


x = np.array([3.3, 5, 6.7, 8.5, 9])
y = np.array([4.3, 6.5, 5.5, 8.8, 11.4])

x_mean = x.mean()
y_mean = y.mean()

num = 0
den = 0 
for i in range(5):
    num += (x[i]-x_mean)*(y[i]-y_mean) 
    den += (x[i]-x_mean)**2
m = num/den
print(m)
c =  y_mean - m*x_mean
print(c)

r = np.linspace(3, 20, 10)
k = m*r + c

plt.plot(r, k)
plt.scatter(x, y)
plt.show
