# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 08:52:13 2021

@author: User
"""

import matplotlib.pyplot as plt
# plt.style.use('ggplot')
from glob import glob
import os, sys
import numpy as np

sys.path.append('..')
from functions import *

os.chdir(r'C:\Users\User\Documents\08_publications\20210220_ijms\figure2')

panels = [x for x in os.listdir() if os.path.isdir(x) and not (x.startswith('.') or x.startswith('__'))]
fig, axs = plt.subplots(4,len(panels), figsize=(8,5), squeeze=False, frameon=False)

cm = plt.get_cmap('cool')

#%% Figure2: Overview of spectra

for ia, p in enumerate(panels):
    spectra = glob('{}/*.txt'.format(p))
    for ib, s in enumerate(spectra):
        mz, intens = np.genfromtxt(s, delimiter='\t', unpack=True)
        intens = 100*intens/max(intens) # relative intensity
        l  = axs[ib, ia].plot(mz, intens, color=cm(1-1.*ib/len(spectra)),
                         label=s.split('\\')[1].split('_')[0])

        axs[ib, ia].legend()
    
        # set ylabels
        if ia == 0:
            axs[ib, ia].set_xlim([4000,10000])
            if ib == 1:
                axs[ib, ia].set_ylabel('Relative Intensity [%]')
            if ib == 0:
                axs[ib, ia].title.set_text('ADH')
        else:
            if ia == 1:
                axs[ib, ia].set_xlim([1000,6000])
                if ib == 0:
                    axs[ib, ia].title.set_text('B-Lac')
            elif ia == 2:
                axs[ib, ia].set_xlim([2000,11000])
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


plt.savefig('figure2.pdf')
plt.show()

#%% Figure 2B: ADH IMS R1

subs, av = ims_plot(r'C:\Users\User\Documents\02_experiments\16_protein_detergent_native_ms\analysis\detergent_ims\ADH_R1\*ADH*.csv',
                     147000,
                     2000,
                     30,
                     "figure2B",
                     "ADH R1",
                     figsize=(4,4))

#%% Figure 2C: BSA IMS R1

subs, av= ims_plot([r'C:\Users\User\Documents\02_experiments\16_protein_detergent_native_ms\analysis\detergent_ims\BSA_R1\20210225_TK_BSA_80_80.csv',
                  r'C:\Users\User\Documents\02_experiments\16_protein_detergent_native_ms\analysis\detergent_ims\BSA_R1\20210225_TK_C8E4_BSA_80_80.csv',
                  r'C:\Users\User\Documents\02_experiments\16_protein_detergent_native_ms\analysis\detergent_ims\BSA_R1\20210225_TK_LDAO_BSA_80_80.csv',
                  r'C:\Users\User\Documents\02_experiments\16_protein_detergent_native_ms\analysis\detergent_ims\BSA_R1\20210225_TK_OG_BSA_80_80_1CMC.csv'],
                 66000,
                 2000,
                 10,
                 "figure2C",
                 "BSA R1")

#%% Fig 2D: ADH IMS R2

subs, av = ims_plot(r'C:\Users\User\Documents\02_experiments\16_protein_detergent_native_ms\analysis\detergent_ims\ADH_R2\*ADH*.csv',
                     147000,
                     2000,
                     10,
                     "figure2D",
                     "ADH R2")
