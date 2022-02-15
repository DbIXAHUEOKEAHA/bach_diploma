# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 19:27:28 2022

@author: Тиннелла о Каллинике
"""
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.cos(3*x+1)

x = np.linspace(0, 100, 1000)

enables = 4

t = []

for i in range(enables):
    num = int(1000 / (2 * enables))
    for j in range(num):
        t.append(0)
    for j in range(num):
        t.append(1)

plt.figure()
plt.plot(x, f(x)*t, color = 'royalblue')
plt.ylim((-2, 2))
plt.yticks([])
plt.xticks([])
plt.xlabel('t', fontsize = 20)
plt.ylabel('rf field', fontsize = 20)
plt.style.use('default')
plt.savefig('rf_on_off.png', dpi = 300)
