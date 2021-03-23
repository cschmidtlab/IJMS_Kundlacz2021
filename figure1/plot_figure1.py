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

panels = [x for x in os.listdir() if os.path.isdir(x)]
fig, axs = plt.subplots(4,len(panels), figsize=(8,5), squeeze=False, sharex=True, sharey=True, frameon=False)

cm = plt.get_cmap('cool')

for ia, p in enumerate(panels):
    spectra = glob('{}/*.txt'.format(p))
    for ib, s in enumerate(spectra):
        mz, intens = np.genfromtxt(s, delimiter='\t', unpack=True)
        intens = 100*intens/max(intens) # relative intensity
        axs[ib, ia].plot(mz, intens, color=cm(1-1.*ib/len(spectra)),
                         label='{}-fold'.format(int(s.split('\\')[1].split('_')[0])/100))

        axs[ib, ia].legend()

plt.xlim([2000,10000])
plt.savefig('figure1.pdf')
plt.ylabel('Intensity')     
plt.xlabel('m/z')
plt.show()