import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,1,100,endpoint=True)


returns = [3.1,9.5]
risk = [15.8,23.7]

e_returns = np.zeros((1,100))
e_risk = np.zeros((1,100))

rho = 0.5

for i in range(100):
    e_returns = x[i]*returns[0] + (1 - x[i])*returns[1]
    e_risk = (x[i]**2*risk[0]**2 + (1-x[i])**2*risk[1]**2 + 2*rho*x[i]*(1-x[i])*risk[0]*risk[1])

plt.plot(e_risk,e_returns)