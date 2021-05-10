# -*- coding: utf-8 -*-
"""
Created on Sun May  9 08:34:01 2021

@author: Raza_Jutt
"""

import math
import random
import matplotlib.pyplot as plt
import numpy as np

x = []
for i in range(0,201):
    x.append(i/100)
    
y=[]
for i in x:
    y.append(math.sqrt(math.cos(i)*math.cos(i) +1 ))
    

rand_x = []
rand_y = []
for i in range(0,10000):
    rand_x.append(random.uniform(0.00,2.00))
    rand_y.append(random.uniform(1.00,1.41))
    


xpoints = np.array(x)
ypoints = np.array(y)

x_coordinates = rand_x
y_coordinates = rand_y

plt.plot(xpoints, ypoints,'r')
plt.scatter(x_coordinates, y_coordinates,s=0.1, marker="x")
plt.show()

count = 0
for i in range(0,10000):
    x=rand_x[i]
    if math.sqrt(math.cos(x)*math.cos(x) +1 ) > rand_y[i] :
        count += 1
        
print(count/10000)