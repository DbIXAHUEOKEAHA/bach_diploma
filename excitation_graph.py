# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 16:52:05 2022

@author: Тиннелла о Каллинике
"""
import numpy as np
import matplotlib.pyplot as plt

T = 10

def f(t):
    return(np.exp(-t / T))

def f1(x):
    return(np.log(10 * x + 1))

stop = np.exp(1) / 10 * 1000

log = np.concatenate((np.zeros(500), f1(np.linspace(0, int(stop) / 1000, 500) / 3.05)))

t = np.linspace(0, T, 1000)
A = f(t)

periods = 1

for period in range(1, periods + 1):
    A = np.concatenate((A, A[-1000:]))
    log = np.concatenate((log, log[-1000:]))

t = np.linspace(0, T * (periods + 1), 1000 * (periods + 1))


plt.figure()
plt.plot([0, T * (periods + 1)], [1, 1], '--', color = 'red')
plt.plot([0, T * (periods + 1)], [np.min(A + log), np.min(A + log)], '--', color = 'red')
plt.plot(t, A + log, '-', lw = 3, color = 'royalblue')

#for period in range(2, periods + 2):
#    plt.plot(np.linspace(T * (period - 1) - 5, 2 * T * period, 20), f(np.linspace(T * (period - 1) - 5, 2 * T * period, 20) - (period - 2) * T), '--', color = 'red', alpha = 0.5)

plt.ylim((0.4, 1.2))
plt.xlim(0, T * (periods + 1) - T / 5)
plt.xticks([])
plt.yticks([])
plt.xlabel('t', fontsize = 20)
plt.ylabel(r'$\Delta S_{z}$', fontsize = 20)
plt.style.use('default')
plt.savefig('excitation.png', dpi = 300)


    