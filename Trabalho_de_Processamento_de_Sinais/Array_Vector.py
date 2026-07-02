# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 11:54:13 2026

@author: Ricardo Alexandre
"""

import matplotlib.pyplot as plt
import numpy as np

# Variáveis
pi = np.pi

fs = 1000
ts = 1/fs

fator = 1.5
lambd = 0.8
d = lambd*fator

# d = 0.8
# Vetores
qtd_antenas = 2
antenas = np.arange(0, qtd_antenas, 1)

# Vetor de ângulos
angles = np.arange(-pi/2, pi/2, ts)

#
psi = 2*pi*(d/lambd)*np.sin(angles)

# Vetor de pesos
w = np.ones(qtd_antenas)

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

for indice, m in enumerate(AF):
    # AF[indice] = sum(steering_vector[indice, :])
    AF[indice] = np.conj(w) @ steering_vector[indice]

# Cálculo do Ganho
AF_mod = abs(AF)
AF_mod = AF_mod/np.max(AF_mod)
AF_db = 20*np.log10(AF_mod)
    
plt.plot(180*angles/pi, AF_db)
plt.show()
