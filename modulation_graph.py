# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 15:54:53 2022

@author: Тиннелла о Каллинике
"""

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('default')

'''
def f(x, x0, gamma):
    return  gamma ** 2 / ((x - x0)**2 + gamma**2) + gamma ** 2 / ((x - x0 - delta)**2 + gamma**2) + gamma ** 2 / ((x - x0 + delta)**2 + gamma**2) + gamma ** 2 / ((x - x0 - 2 * delta)**2 + gamma**2) + gamma ** 2 / ((x - x0 + 2 * delta)**2 + gamma**2)

def sinc(x, x0, delta):
    return np.sinc(2 * (x - x0) / (delta))

def theta(step):
    t = np.zeros(10000)
    for i in range(t.shape[0]):
        if i % (2*step) < step:
            t[i] = 1
    return t

t = np.linspace(-10000, 10000, 10000)
omega = 17 / 10000

fig,ax = plt.subplots(1)
ax.plot(t - 25000, np.sin(omega * t), '-', color = 'black', label = 'Рч поле')
ax.plot(t, theta(5000), '--', color = 'black', label = 'Модуляция поля')
ax.plot(t + 25000, np.sin(omega * t) * theta(5000), '-', lw = 4, color = 'black', label = 'Действие на спин')
#ax.set_yticklabels([])
ax.set_xticklabels([])
ax.tick_params(labelsize=20)
plt.text(x = -9000, y = 0, s = '*', size = 40)
plt.text(x = 11000, y = 0, s = '=', size = 40)
plt.legend(fontsize = 20)
plt.ylim((-1.3, 1.9))
#plt.savefig('modulation_rf.png', dpi = 300)

delta = 6000
gamma = 500

fig,ax = plt.subplots(1)
ax.plot(t - 25000, sinc(t - 25000, - 25000, delta), '--', color = 'black', label = 'Модуляция')
ax.plot(t, 1.1 * f(t, 0, gamma) - 0.2, '-', color = 'black', label = 'Резонансные пики')
ax.plot(t + 25000, f(t + 25000, 25000, gamma) * sinc(t + 25000, 25000, delta) - 0.05, '-', lw = 4, color = 'black', label = 'Сигнал')
ax.set_yticklabels([])
ax.set_xticklabels([])
plt.text(x = -15000, y = 0.4, s = '*', size = 40)
plt.text(x = 15000, y = 0.4, s = '=', size = 40)
plt.legend(fontsize = 20)
plt.ylim((-0.3, 1.34))
#plt.savefig('modulation_graph.png', dpi = 300)
'''

plt.figure()
for i in range(3):
    if i % 2 == 0:
        plt.plot(np.linspace(i * 2 * np.pi, (i + 1) * 2 * np.pi, 1000), np.sin(np.linspace(i * 2 * np.pi, (i + 1) * 2 * np.pi, 1000) * 2), '-', color = 'black')
    else:
        plt.plot(np.linspace(i * 2 * np.pi, (i + 1) * 2 * np.pi, 1000), np.sin(np.linspace(i * 2 * np.pi, (i + 1) * 2 * np.pi, 1000) * 2), '-', color = 'black', alpha = 0.1)
        plt.plot(np.linspace(i * 2 * np.pi, (i + 1) * 2 * np.pi, 1000), np.zeros_like(np.linspace(i * 2 * np.pi, (i + 1) * 2 * np.pi, 1000)), '-', color = 'black', label = r'Режим обычной модуляции')
plt.ylim((-1.1, 1.3))
plt.legend()
plt.savefig('modulation_mod.png', dpi = 300)

plt.figure()
for i in range(3):
    if i == 0:
        plt.plot(np.linspace(i * 2 * np.pi, (i + 1) * 2 * np.pi, 1000), np.sin(np.pi / 2 + np.linspace(i * 2 * np.pi, (i + 1) * 2 * np.pi, 1000) * 2), '-', color = 'black')
    elif i == 1:
        plt.plot(np.linspace(i * 2 * np.pi, (i + 1) * 2 * np.pi, 1000), np.sin(np.linspace(np.pi / 4 + i * 2 * np.pi, (i + 1) * 2 * np.pi, 1000) * 2), '-', color = 'black', alpha = 0.1)
        plt.plot([i * 2 * np.pi, *np.linspace(i * 2 * np.pi, (i + 1) * 2 * np.pi, 1000), (i + 1) * 2 * np.pi], [1, *np.zeros_like(np.linspace(i * 2 * np.pi, (i + 1) * 2 * np.pi, 1000)), 1], '-', color = 'black', label = r'Режим burst-модуляции')
    elif i==2:
        plt.plot(np.linspace(i * 2 * np.pi, (i + 1) * 2 * np.pi, 1000), np.sin(np.pi / 2 + np.linspace(i * 2 * np.pi, (i + 1) * 2 * np.pi, 1000) * 2), '-', color = 'black')
plt.ylim((-1.1, 1.3))
plt.legend()
plt.savefig('modulation_burst.png', dpi = 300)

plt.figure()
for i in range(2):
    if i % 2 == 0:
        plt.plot(np.linspace(0, 3 * np.pi, 1000), np.sin(np.linspace(0, 3 * np.pi, 1000) * 2), '-', color = 'black')
    else:
        plt.plot(np.linspace(3 * np.pi, 4 * np.pi, 1000), np.zeros_like(np.linspace(3 * np.pi, 4 * np.pi, 1000)), '-', color = 'black')
plt.ylim((-1.1, 1.1))
plt.savefig('modulation_duty.png', dpi = 300)

