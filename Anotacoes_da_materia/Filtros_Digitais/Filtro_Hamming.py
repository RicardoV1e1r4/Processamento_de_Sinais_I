# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:52:06 2026

@author: Ricardo Alexandre
"""

import numpy as np
# import matplotlib.pyplot as plt

# Variáveis
pi = np.pi

M  = 80
wc1 = pi/4
wc2 = pi/2

Omega_c1 = 2000  #rad/s
Omega_c2 = 4000  #rad/s
Omega_s  = 10000 #rad/s

wc1 = 2*pi*(Omega_c1/Omega_s)
wc2 = 2*pi*(Omega_c2/Omega_s)

# Função h[n]
n = np.arange(0, M//2 + 1, 1)
print("Comprimento", len(n))

h0 = 1 - (wc2 - wc1)/pi

hn = np.where(n == 0, h0, (np.sin(wc1*n) - np.sin(wc2*n))/(pi*n))

# Janela de Hamming wH[n]
alpha = 0.54
wn = alpha + (1 - alpha)*np.cos((2*pi*n)/M)

# Valores arredondados
hn_round = np.round(hn, decimals=6)

wn_round = np.round(wn, decimals=6)

# Multiplicação h[n] com wH[n]
hn_linha = hn_round * wn_round

# print(n)
# print(h0)
# print("h_d[n]:", hn_round)
# print("wn:", wn_round)
# print("h_linha[n]:", hn_linha)
