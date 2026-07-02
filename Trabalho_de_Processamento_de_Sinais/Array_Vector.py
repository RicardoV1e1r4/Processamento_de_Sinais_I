# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 11:54:13 2026

@author: Ricardo Alexandre
"""

import matplotlib.pyplot as plt
import numpy as np

# Variáveis
pi = np.pi
exp = np.e

fs = 1000
ts = 1/fs

d = 0.5
lambd = 0.1

# Vetores
qtd_antenas = 2
antenas = np.arange(0, qtd_antenas, 1)

# Vetor de ângulos
angles = np.arange(-pi, pi, ts)

#
psi = 2*pi*(d/lambd)*np.sin(angles)

# Calculo do Steering Vector
steering_vector = np.zeros((len(angles), qtd_antenas), dtype=complex)
"""
    [1, e^{-j1psi}, e^{-j2psi}, ..., e^{-j(M - 1)psi}]
"""
for indice, k in enumerate(psi):
    for m in antenas:
        steering_vector[indice, m] = np.exp(-1j*m*k)

# Calculo do Array Vector
AF = np.zeros(len(angles), dtype=complex)

for indice, m in AF:
    

