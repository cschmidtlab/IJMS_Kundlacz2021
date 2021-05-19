# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 14:06:17 2021

@author: User
"""

import matplotlib.pyplot as plt
# plt.style.use('ggplot')
import os, sys
import numpy as np

os.chdir(r'C:\Users\User\Documents\08_publications\20210220_ijms\figure3')
sys.path.append('..')
import functions

cm = plt.get_cmap('cool')

def generate_clist(NUM_COLORS):
    import pylab
    
    cm = pylab.get_cmap('cool')
    color = [cm(1-1.*i/NUM_COLORS) for i in range(NUM_COLORS)]
    
    return color

#%% figure3 Overview of spectra

spectra = ["20210303_TK_MYO_30_10_CV10__MS1_0_ms.txt",
           # "20210303_TK_MYO_80_80_M1_0_ms.txt",
           # "20210303_TK_C8E4_MYO_80_80_MS2_0_ms.txt",
            "20210303_TK_C8E4_MYO_30_10_MS1_0_ms.txt",
            "20210303_TK_LDAO_MYO_30_10_CV10_NANO_MS1_0_ms.txt",
           # "20210303_TK_LDAO_MYO_80_80_CV10_NANO_MS1_0_ms.txt",
           '20210309_TK_OG_MYO_30_10_CV10_MS1_0_ms.txt'
           # "20210303_TK_OG_MYO_80_80_CV10_1CMC_MS1_0_ms.txt"
           ]

spectra = [os.path.abspath('../data/figure3/spectra_overview/' + s) for s in spectra]

colors = generate_clist(len(spectra)+1)

zoom_1 = (500, 700)
zoom_2 = (1600, 3500)

fig, axs = plt.subplots(len(spectra),2, figsize=(4,4),
                        gridspec_kw={'width_ratios': [zoom_1[1]-zoom_1[0], zoom_2[1]-zoom_2[0]]},
                        squeeze=False, frameon=False, sharey=True, sharex='col')

for ib, s in enumerate(spectra):
    mz, intens = np.genfromtxt(s, delimiter=' ', unpack=True)
    intens = 100*intens/intens.max() # relative intensity
    axs[ib, 0].plot(mz, intens, color=colors[ib])
    axs[ib, 1].plot(mz, intens, color=colors[ib], label=os.path.split(s)[-1][-30:])

    axs[ib, 1].legend()
    axs[ib, 0].set_ylim([0,110])
    axs[ib, 0].set_xlim(zoom_1)
    axs[ib, 1].set_ylim([0,110])
    axs[ib, 1].set_xlim(zoom_2)
    
    
    # hide the spines between ax and ax2
    axs[ib, 0].spines['right'].set_visible(False)
    axs[ib, 1].spines['left'].set_visible(False)
    axs[ib, 0].yaxis.tick_left()
    # axs[ib, 0].tick_params(labeltop='off') # don't put tick labels at the top
    axs[ib, 1].yaxis.tick_right()
    
# Make the spacing between the two axes a bit smaller
plt.subplots_adjust(wspace=0.15)

plt.tight_layout()
plt.savefig('figure3.pdf')
plt.show()

#%% figure3 zoom for sup

spectra = ["20210303_TK_MYO_30_10_CV10__MS1_0_ms.txt",
           # "20210303_TK_MYO_80_80_M1_0_ms.txt",
           # "20210303_TK_C8E4_MYO_80_80_MS2_0_ms.txt",
            "20210303_TK_C8E4_MYO_30_10_MS1_0_ms.txt",
            "20210303_TK_LDAO_MYO_30_10_CV10_NANO_MS1_0_ms.txt",
           # "20210303_TK_LDAO_MYO_80_80_CV10_NANO_MS1_0_ms.txt",
           '20210309_TK_OG_MYO_30_10_CV10_MS1_0_ms.txt'
           # "20210303_TK_OG_MYO_80_80_CV10_1CMC_MS1_0_ms.txt"
           ]

spectra = [os.path.abspath('../data/figure3/spectra_overview/' + s) for s in spectra]

colors = generate_clist(len(spectra)+1)

zoom_2 = (2000, 2300)

fig, axs = plt.subplots(len(spectra),1, figsize=(4,4),
                        squeeze=False, frameon=False, sharey=True, sharex='col')

for ib, s in enumerate(spectra):
    mz, intens = np.genfromtxt(s, delimiter=' ', unpack=True)
    intens = 100*intens/intens[(mz>zoom_2[0]) & (mz < zoom_2[1])].max() # relative intensity
    axs[ib,0].plot(mz, intens, color=colors[ib], label=s.split('_')[10])

    axs[ib, 0].legend()

    axs[ib, 0].set_ylim([0,110])
    axs[ib, 0].set_xlim(zoom_2)
    
# Make the spacing between the two axes a bit smaller
plt.subplots_adjust(wspace=0.15)

plt.tight_layout()
plt.savefig('figure3_zoom.pdf')
plt.savefig('figure3_zoom.png')

plt.show()


#%% Figure 3B Myo IMS

functions.ims_plot(r'../data/figure3/MYO_R1/*MYO*.csv',
                     17550,
                     100,
                     10,
                     'figure3B',
                     ylim=(70,110),
                     # figsize=(4,2),
                     xlim=[10,90],
                     title_label="Myoglobin Heme-bound R1")

functions.ims_plot(r'../data/figure3/MYO_R1/*MYO*.csv',
                     17550,
                     100,
                     10,
                     'figure3B_z8',
                     ylim=(70,110),
                     charge=8,
                     xlim=[10,90],
                     # figsize=(4,2),
                     title_label="Myoglobin Heme-bound charge 8 R1")

#%% Figure S3 Myo R2 IMS

functions.ims_plot(r'../data/figure3/MYO_R2/*MYO*.csv',
                     17550,
                     100,
                     10,
                     'figure3Sup',
                     ylim=(70,110),
                     xlim=[10,90],
                     legend=False,
                     # figsize=(4,2),
                     title_label="Myoglobin Heme-bound R2")

functions.ims_plot(r'../data/figure3/MYO_R2/*MYO*.csv',
                     17550,
                     100,
                     10,
                     'figure3Sup_z8',
                     ylim=(70,110),
                     charge=8,
                     xlim=[10,90],
                     legend=False,
                     # figsize=(4,2),
                     title_label="Myoglobin Heme-bound charge 8 R2")

#%% Figure 2 Sup3: Drift time distributinos at 20V and 90V
from itertools import groupby

datadir = '../data/figure3/CIU_MYO_R1/'

pairs = [list(i) for j,i in groupby(os.listdir(datadir),
                                    lambda a: a[:-9])]
for p in pairs:
    fig, ax = plt.subplots(1,1, figsize=(3,3))
    for f in p:
        d = np.genfromtxt(datadir+f, delimiter='\t', unpack=True)
        #d[1] = 100*d[1]/d[1].max()
        ax.plot(d[0], d[1], label=f[-8:-4])
        
    ax.legend()
    # ax.set_title(f.split('_')[2])
    ax.set_ylabel('Intensity')
    ax.set_xlabel('Drift time [ms]')
    plt.tight_layout()
    plt.savefig(str(f[:-9]) + '_R1_plot.pdf')


datadir = '../data/figure3/CIU_MYO_R2/'

pairs = [list(i) for j,i in groupby(os.listdir(datadir),
                                    lambda a: a[:-9])]
for p in pairs:
    fig, ax = plt.subplots(1,1, figsize=(3,3))
    for f in p:
        d = np.genfromtxt(datadir+f, delimiter='\t', unpack=True)
        #d[1] = 100*d[1]/d[1].max()
        ax.plot(d[0], d[1], label=f[-8:-4])
        
    ax.legend()
    # ax.set_title(f.split('_')[2])
    ax.set_ylabel('Intensity')
    ax.set_xlabel('Drift time [ms]')
    plt.tight_layout()
    plt.savefig(str(f[:-9]) + '_R2_plot.pdf')
        