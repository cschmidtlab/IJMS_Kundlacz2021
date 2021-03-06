# -*- coding: utf-8 -*-
"""
Created on Mon May 10 15:42:16 2021

@author: User
"""
import matplotlib.pyplot as plt
# plt.style.use('ggplot')
from glob import glob
import os, sys
import numpy as np

os.chdir(r'C:\Users\User\Documents\08_publications\20210220_ijms\figure2')


sys.path.append('..')
from functions import *
panels = [x for x in os.listdir() if os.path.isdir(x) and not (x.startswith('.') or x.startswith('__'))]
fig, axs = plt.subplots(4,len(panels), figsize=(8,5), squeeze=False, frameon=False)

cm = plt.get_cmap('cool')

#%% Figure2: Overview of spectra

def group_by_sum(x):
    """
    Required as MassLync saves multiple data per m/z bin
    """
    u, idx = np.unique(x[:,0], return_inverse=True)
    s = np.bincount(idx, weights = x[:,1])
    return np.c_[u, s]

for ia, p in enumerate(panels):
    spectra = glob('{}/*.txt'.format(p))
    for ib, s in enumerate(spectra):
        d = np.genfromtxt(s, delimiter='\t', unpack=False)
        mz, intens = group_by_sum(d).T
        
        intens = 100*intens/max(intens) # relative intensity
        l  = axs[ib, ia].plot(mz, intens, color=cm(1-1.*ib/len(spectra)),
                         label=s.split('\\')[1].split('_')[0])

        axs[ib, ia].legend()
    
        # set ylabels
        if ia == 0:
            axs[ib, ia].set_xlim([1000,12000])
            if ib == 1:
                axs[ib, ia].set_ylabel('Relative Intensity [%]')
            if ib == 0:
                axs[ib, ia].title.set_text('ADH')
        else:
            if ia == 1:
                axs[ib, ia].set_xlim([1000,12000])
                if ib == 0:
                    axs[ib, ia].title.set_text('B-Lac')
            elif ia == 2:
                axs[ib, ia].set_xlim([2000,12000])
                if ib == 0:
                    axs[ib, ia].title.set_text('BSA')
            axs[ib, ia].set_ylabel(None)
            axs[ib, ia].get_yaxis().set_ticklabels([])
        
        #set xlabels
        if ib == 3:
            if ia == 1:
                axs[ib, ia].set_xlabel('m/z')
        else:
            axs[ib, ia].set_xlabel(None)
            axs[ib, ia].get_xaxis().set_ticklabels([])


plt.savefig('figure2a_sup.pdf')
plt.show()
