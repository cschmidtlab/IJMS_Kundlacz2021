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
import pandas as pd

os.chdir(r'C:\Users\User\Documents\08_publications\20210220_ijms\figure4')

datadir = '../data/figure4/'

#%%%%%%%%%% Common variables %%%%%%%%%%%%%%
def generate_clist(NUM_COLORS):
    import pylab
    
    cm = pylab.get_cmap('cool')
    color = [cm(1-1.*i/NUM_COLORS) for i in range(NUM_COLORS)]
    
    return color
#%% Figure 4A 10 POPE
spectra = ["20210302_TK_BLAC_30_10_MS_0_ms.txt",
           "20210302_TK_C8E4_15_POPE_BLAC_30_10_NB_M2_0_ms.txt",
           "20210302_TK_LDAO_15_POPE_BLAC_30_10_NB_M1_0_ms.txt",
           "20210302_TK_OG_15_POPE_BLAC_30_10_1CMC_NB_M1_0_ms.txt"]

colors = generate_clist(len(spectra))

fig, axs = plt.subplots(len(spectra),1, figsize=(6,4), squeeze=True, frameon=False, sharex=True)

for ib, s in enumerate(spectra):
        mz, intens = np.genfromtxt(datadir + s, delimiter=' ', unpack=True)
        intens = 100*intens/intens[mz>1700].max() # relative intensity
        l  = axs[ib].plot(mz, intens, color=colors[ib], label=s)

        axs[ib].legend()
        axs[ib].set_ylim([0,110])
        axs[ib].set_xlim([1700,4500])


plt.savefig(os.path.join('figure4.pdf'))
plt.show()


#%% Figure 4B: 20 POPE
spectra = ["20210302_TK_BLAC_30_10_MS_0_ms.txt",
           "20210302_TK_C8E4_25_POPE_BLAC_30_10_NB_M2_0_ms.txt",
           "20210302_TK_LDAO_25_POPE_BLAC_30_10_M1_0_ms.txt",
           "20210302_TK_OG_25_POPE_BLAC_30_10_1CMC_NB_M1_0_ms.txt"]

colors = generate_clist(len(spectra))

fig, axs = plt.subplots(len(spectra),1, figsize=(6,4), squeeze=True, frameon=False, sharex=True)

for ib, s in enumerate(spectra):
        mz, intens = np.genfromtxt(datadir + s, delimiter=' ', unpack=True)
        intens = 100*intens/intens[mz>1700].max() # relative intensity
        l  = axs[ib].plot(mz, intens, color=colors[ib], label=s)

        axs[ib].legend()
        axs[ib].set_ylim([0,110])
        axs[ib].set_xlim([1700,4500])


plt.savefig(os.path.join('figure4B.pdf'))
plt.show()


#%% Figure 4C part1

fig, ax = plt.subplots(1,1, figsize=(2,2))

spectra = ["20210302_TK_C8E4_10_POPE_BLAC_30_10_NB_MS2_0_ms.txt",
           "20210302_TK_C8E4_15_POPE_BLAC_30_10_NB_M2_0_ms.txt",
           "20210302_TK_C8E4_25_POPE_BLAC_30_10_NB_M2_0_ms.txt",
           "20210302_TK_C8E4_50_POPE_BLAC_30_10_NB_M2_0_ms.txt"]

for ib, s in enumerate(spectra):
        mz, intens = np.genfromtxt(datadir+s, delimiter=' ', unpack=True)
        intens = 100*intens/intens[mz>3500].max() # relative intensity
        l  = ax.plot(mz, intens, color=colors[ib], label=s)

ax.set_ylim([0,110])
ax.set_xlim([3500,4500])

plt.savefig(os.path.join('figure4C-1.pdf'))
plt.show()


#%% Figure 4C part2

fig, ax = plt.subplots(1,1, figsize=(2,2))

spectra = ["20210302_TK_LDAO_10_POPE_BLAC_30_10_NB_M1_0_ms.txt",
           "20210302_TK_LDAO_15_POPE_BLAC_30_10_NB_M1_0_ms.txt",
           "20210302_TK_LDAO_25_POPE_BLAC_30_10_NB_M1_0_ms.txt",
           "20210302_TK_LDAO_50_POPE_BLAC_30_10_M2_0_ms.txt"]

for ib, s in enumerate(spectra):
        mz, intens = np.genfromtxt(datadir+s, delimiter=' ', unpack=True)
        intens = 100*intens/intens[mz>3500].max() # relative intensity
        l  = ax.plot(mz, intens, color=colors[ib], label=s)

ax.set_ylim([0,110])
ax.set_xlim([3500,4500])

plt.savefig(os.path.join('figure4C-2.pdf'))
plt.show()

#%% Figure 4C part3

fig, ax = plt.subplots(1,1, figsize=(2,2))

spectra = ["20210302_TK_OG_10_POPE_BLAC_30_10_1CMC_NB_M1_0_ms.txt",
           "20210302_TK_OG_15_POPE_BLAC_30_10_1CMC_NB_M1_0_ms.txt",
           "20210302_TK_OG_25_POPE_BLAC_30_10_1CMC_NB_M1_0_ms.txt",
           "20210302_TK_OG_50_POPE_BLAC_30_10_1cmc_NB_M1_0_ms.txt"]

for ib, s in enumerate(spectra):
        mz, intens = np.genfromtxt(datadir+s, delimiter=' ', unpack=True)
        intens = 100*intens/intens[mz>3500].max() # relative intensity
        l  = ax.plot(mz, intens, color=colors[ib], label=s)

ax.set_ylim([0,110])
ax.set_xlim([3500,4500])

plt.savefig(os.path.join('figure4C-3.pdf'))
plt.show()