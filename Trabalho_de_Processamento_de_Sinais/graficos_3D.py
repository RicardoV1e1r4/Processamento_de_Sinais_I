# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 20:27:23 2026

@author: Ricardo Alexandre
"""

# Modelagem e Análise de Arranjos de Sensores

import matplotlib.pyplot as plt
import numpy as np

# Funções geradoras dos Arranjos dos Sensores
    # generate_ula(M, d)
    # generate_uca(M, R)
    # generate_upa(Mx, My, dx, dy)
    # generate_ucya(Mc, Nz, R, dz)
    
def generate_ula(M, d):
    #, eixo=coord
    
    comp_total = (M)*d
    sensores   = np.arange(0, comp_total, d)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    
    ax.scatter(sensores, 0, 0, marker='o')

plt.show()
