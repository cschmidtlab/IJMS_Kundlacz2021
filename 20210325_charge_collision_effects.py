# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 14:49:12 2021

@author: User
"""
import sys, os
from glob import glob
import numpy as np
import matplotlib.pyplot as plt

os.chdir(r'C:\Users\User\Documents\02_experiments\16_protein_detergent_native_ms\analysis\detergent_ims\ADH_R1')

fig, axs = plt.subplots(2,2, figsize=(8,5), squeeze=False, frameon=False)

cm = plt.get_cmap('cool')

files = ['20210222_TK _ADH_80_80_CV[1-9]0_IMS1.raw_1_0_0_ms.txt',
         '20210222_TK _C8E4_ADH_80_80_CV[1-9]0_NB_IMS1.raw_1_0_0_ms.txt',
         '20210222_TK _LDAO_ADH_80_80_CV[1-9]0_NB_IMS1.raw_1_0_0_ms.txt',
         '20210222_TK _OG_ADH_80_80_CV[1-9]0_1CMC_IMS1.raw_1_0_0_ms.txt']

for ia, f in enumerate(files):
    spectra = glob(f)
    maxy = []
    for idx, s in enumerate(spectra):
        mz, intens = np.genfromtxt(s, delimiter=' ', unpack=True)
        axs[ia//2,ia%2].plot(mz, intens, color=cm(1.*idx/len(spectra)),
                             label=s.split('CV')[1].split('_')[0])
        maxy.append(intens[(mz>5000) & (mz<9000)].max())
    
    axs[ia//2,ia%2].set_xlim([5000,9000])
    axs[ia//2,ia%2].set_ylim([0, max(maxy)])
    
    axs[ia//2,ia%2].title.set_text(f.split('_')[2])
    maxy = []

plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.xlabel('m/z')
plt.ylabel('Intensity')
plt.tight_layout()
plt.savefig(r'C:\Users\User\Documents\08_publications\20210220_ijms\figureS2.png')

plt.show()