# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:52:06 2026

@author: Ricardo Alexandre
"""

import numpy as np
# import matplotlib.pyplot as plt

# Variáveis
pi = np.pi

# Janela Retangular
def janela_retangular(M):
    wr = np.ones(2 * (int(M//2)) + 1)
    return wr

# Janela Triangular
def janela_triangular(M):
    n_pos = np.arange(1, int(M/2)+1)
    
    wt0 = 1
    wt_pos = -(2 * n_pos)/(M + 2) + 1
    
    wt = np.concatenate((np.flip(wt_pos), [wt0], wt_pos))
    
    return wt

# Janelas de Hamming e de Hann
def janela_hamming(M):
    n_pos = np.arange(1, int(M//2) + 1)
    
    alpha = 0.54
    wh0 = alpha + (1 - alpha) * np.cos((2 * pi * 0)/M)
    wh_pos = alpha + (1 - alpha) * np.cos((2 * pi * n_pos)/M)
    
    wh = np.concatenate((np.flip(wh_pos), [wh0], wh_pos))
    n = np.concatenate(([0], n_pos, n_pos + 40))
    
    return n, wh
