# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 18:14:00 2026

@author: Ricardo Alexandre
"""

import numpy as np
import matplotlib.pyplot as plt

# Variáveis
pi = np.pi

# Resposta ao impulso

# Passa_baixas
def passa_baixas(M, wc):
    n_pos = np.arange(1, int(M/2)+1)
    
    h0 = wc/pi
    hn_pos = 1/(pi*n_pos)*np.sin(wc*n_pos)
    
    hn = np.concatenate((np.flip(hn_pos), [h0], hn_pos))
    n  = np.concatenate((np.flip(n_pos), [0], n_pos))
    return n, hn


# Passa_baixas
def passa_altas(M, wc):
    n_pos = np.arange(1, int(M/2)+1)
    
    h0 = 1 - wc/pi
    hn_pos = -1/(pi*n_pos)*np.sin(wc*n_pos)
    
    hn = np.concatenate((np.flip(hn_pos), [h0], hn_pos))
    n  = np.concatenate((np.flip(n_pos), [0], n_pos))
    return n, hn

x, y = passa_altas(8, 0.5)

# plt.stem(x, y)

plt.show()