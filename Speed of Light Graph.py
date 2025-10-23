#!/usr/bin/env python
# coding: utf-8

# In[24]:


import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as scpo

x = np.array([0.2100,0.4660,0.6000,0.8000,1.0000,1.2000,1.4000,1.7000,2.0000,2.3000,2.6000,2.9000,3.2000,3.5000,3.8000])
y = np.array([2.9,3.8,4.2,4.7,5.5,6.2,6.8,7.8,8.8,9.9,10.9,12.0,13.1,14.2,15.4])

xerror = 0.001
yerror = 0.2

plt.gca().set_xlim([0,4])
plt.gca().set_ylim([2,16])

def Line(x, gradient, intercept): 
    return gradient*x + intercept

actual_fit_parameters, covariance_matrix = scpo.curve_fit(Line,x,y)
fit_gradient = actual_fit_parameters[0] 
fit_intercept = actual_fit_parameters[1]
ybestfit = Line(x, fit_gradient, fit_intercept)

ytrue = (x / 299792458) * 10 ** (9) + fit_intercept

plt.figure(1)

plt.errorbar(x, y, xerr = xerror , yerr = yerror , fmt = 'none', color = "#6D6D6D",capsize=2)
plt.plot(x, ybestfit, color = "#8F8F8F")
plt.scatter(x,y,s=20,color = "#6D6D6D")

plt.xlabel("Optical Path Length ($ \mathrm{m} $)",fontsize=14)
plt.ylabel("Time Delay ($ \mathrm{ns} $)",fontsize=14)

plt.savefig('speedoflightgraph.png', dpi=1200)

plt.show()

# In[ ]:




