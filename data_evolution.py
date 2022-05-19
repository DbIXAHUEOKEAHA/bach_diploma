# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 14:18:45 2022

@author: Тиннелла о Каллинике
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.colors as colors
from os import listdir
from os.path import isfile, join, getmtime

#Path to a data
mypath = r'C:\HSE\bach_diploma\Spin_coherence\2022.04.06\results\data'

#Searching for data in 'mypath' folder
files = [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f))]
files.sort(key = getmtime)
files = np.array([f[len(mypath) + 1:] for f in files])

#Create python variable named after data-file
def create(filename):
    globals()[filename] = np.genfromtxt(join(mypath, filename), names = ('f', 'x', 'y'))
    return()

#Separation into different experimental modes (optional)
mod = []
burst = []   
percent = []
 
for file in files:
    create(file)
    if file.find('BurstFixPhase') != -1:
        burst.append(file)
    elif (file.find('perc') != -1) and ('2kRF' in file):
        percent.append(file)
    else:
        mod.append(file)
        
mod = mod[9:-5][0::2]
burst = burst[1:-7]
percent = percent[0:-3]

def find_mod(filename):
    #function to extract modulation frequency from a filename (optional)
    s = filename[filename.find('Mod') + 3: filename.find('Hz')]
    if 'k' in s:
        s = s[0:-1] + '000'
    return s


def find_burst(filename):
    #function to extract modulation frequency for a burst-mode from a filename (optional)
    s = filename[filename.find('Phase') + 5: filename.find('Hz')]
    if 'k' in s:
        s = s[0:-1] + '000'
        return s
    else:
        return int(s)
    
def find_percent(filename):
    s = filename[filename.find('perc') - 2: filename.find('perc')]
    return s

def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
    new_cmap = colors.LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(minval, maxval, n)))
    return new_cmap    

def plot_evolution_percent():
    string = 'percent'
    mode = globals()[string]
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    n = len(mode)
    colors = plt.cm.hot(np.linspace(0.1,0.4,n)[::-1])
    for a in range(0, len(mode)):
        mod = globals()[mode[a]]
        x0 = mod['f'][np.argmax(np.sqrt(mod['x']**2 + mod['y']**2))]
        x = mod['f'] - x0
        y = np.sqrt(mod['x']**2 + mod['y']**2)
        ax.plot(x, y, '.-', color = colors[a])
    ax.set_yticklabels([])
    cmap = truncate_colormap(plt.get_cmap('hot'), 0.1, 0.4, n)
    norm = mpl.colors.Normalize(vmin=40, vmax=90)
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm)
    cbar.ax.tick_params(labelsize=10)
    cbar.set_label(r'RF ratio, %', size=16)
    plt.xticks(fontsize = 14)
    plt.xlabel(r'$f_{rf} - f_o$, Hz', fontsize = 16)
    plt.ylabel(r'Spin polarization, $\Delta S_z$', fontsize = 16)
    plt.ylim((0, 60))
    plt.text(x = -1000, y = 55, s = r'B = 5.2 mT, T = 3.5 K', size = 14)
    plt.savefig(string + '_evolution.png', dpi = 300, bbox_inches='tight')

def plot_evolution_mod():
    string = 'mod'
    mode = globals()[string]
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    n = len(mode)
    colors = plt.cm.hot(np.linspace(0.1,0.4,n)[::-1])
    for a in range(0, len(mode)):
        mod = globals()[mode[a]][10:-10]
        x0 = mod['f'][np.argmax(np.sqrt(mod['x']**2 + mod['y']**2))]
        x = mod['f'] - x0
        y = np.sqrt(mod['x']**2 + mod['y']**2)
        ax.plot(x, y, '.-', color = colors[a])
        #call = globals()['find_' + string]
        #ax.text(x = -1450, y = y[0], s = call(mode[a]), color = 'black', font = 'default')
    ax.set_yticklabels([])
    cmap = truncate_colormap(plt.get_cmap('hot'), 0.1, 0.4, n)
    norm = mpl.colors.Normalize(vmin=0, vmax=50000)
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm)
    cbar.ax.tick_params(labelsize=10)
    cbar.set_label(r'$f_{mod}, Hz$', size=16)
    plt.xticks(fontsize = 14)
    plt.xlabel(r'$f_{rf} - f_o$, Hz', fontsize = 16)
    plt.ylabel(r'Spin polarization, $\Delta S_z$', fontsize = 16)
    plt.xlim((-1100, 1100))
    plt.ylim((-5, 90))
    plt.text(x = -1050, y = 80, s = r'B = 5.2 mT, T = 3.5 K', size = 14)
#    plt.savefig(string + '_evolution.png', dpi = 300, bbox_inches='tight')
    
def plot_evolution_burst():
    string = 'burst'
    mode = globals()[string]
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    n = len(mode)
    colors = plt.cm.hot(np.linspace(0.1,0.4,n))
    for a in range(0, len(mode)):
        mod = globals()[mode[a]]
        x0 = mod['f'][np.argmin(np.sqrt(mod['x']**2 + mod['y']**2))]
        x = mod['f'] - x0
        y = np.sqrt(mod['x']**2 + mod['y']**2)
        ax.plot(x, y, '.-', color = colors[a])
    ax.set_yticklabels([])
    cmap = truncate_colormap(plt.get_cmap('hot'), 0.1, 0.4, n)
    norm = mpl.colors.Normalize(vmin=200, vmax=1000)
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm)
    cbar.ax.tick_params(labelsize=10)
    cbar.set_label(r'$f_{burst}, Hz$', size=16)
    plt.xticks(fontsize = 14)
    plt.xlabel(r'$f_{rf} - f_o$, Hz', fontsize = 16)
    plt.ylabel(r'Spin polarization, $\Delta S_z$', fontsize = 16)
    plt.xlim((-1100, 1100))
    plt.ylim((150, 500))
    plt.text(x = -1050, y = 450, s = r'B = 5.2 mT, T = 3.5 K', size = 14)
    plt.savefig(string + '_evolution.png', dpi = 300, bbox_inches='tight')


plot_evolution_percent()
plot_evolution_mod()
plot_evolution_burst()

print(burst)

        
