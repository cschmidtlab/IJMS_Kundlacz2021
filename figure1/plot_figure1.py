# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 08:52:13 2021

@author: User
"""

import matplotlib.pyplot as plt
# plt.style.use('ggplot')
from glob import glob
import os
import numpy as np

os.chdir(r'C:\Users\User\Documents\08_publications\20210220_ijms\figure1')


cm = plt.get_cmap('cool')

def group_by_sum(x):
    """
    Required as MassLync saves multiple data per m/z bin
    """
    u, idx = np.unique(x[:,0], return_inverse=True)
    s = np.bincount(idx, weights = x[:,1])
    return np.c_[u, s]

#%%

spectra = glob('../data/figure1/*.txt')
fig, axs = plt.subplots(len(spectra), #nrows
                        1, #ncols
                        figsize=(8,5),
                        squeeze=False,
                        sharex=True,
                        sharey=True,
                        frameon=False)

for ib, s in enumerate(spectra):
    d = np.genfromtxt(s, delimiter='\t', unpack=False)
    mz, intens = group_by_sum(d).T
    intens = 100*intens/max(intens) # relative intensity
    axs[ib, 0].plot(mz, intens, color=cm(1-1.*ib/len(spectra)),
                     label='{}-fold'.format(int(s.split('\\')[1].split('_')[0])/100))

    axs[ib, 0].legend()

plt.xlim([2000,10000])
plt.savefig('figure1.pdf')
plt.ylabel('Intensity')     
plt.xlabel('m/z')
plt.show()