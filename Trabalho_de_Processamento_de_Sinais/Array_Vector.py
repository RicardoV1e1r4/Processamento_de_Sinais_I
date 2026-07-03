# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 11:54:13 2026

@author: Ricardo Alexandre
"""

import matplotlib.pyplot as plt
import numpy as np

# Variáveis
pi = np.pi

x_lim = pi

fs = 1000
ts = 1/fs

# Parametros da antena
fator = 0.5
lambd = 1
d = lambd*fator
qtd_antenas = 2
antenas = np.arange(0, qtd_antenas, 1)

# Vetor de ângulos
angles = np.arange(-x_lim, x_lim, ts)

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


# Gráficos
# Cartesiano
plt.plot(360*angles/(2*pi), AF_db)
plt.ylim((-60, 1))
plt.xlim((-180*x_lim/(2*pi), 180*x_lim/(2*pi)))

# Polar
figura, ax = plt.subplots(subplot_kw={'projection': 'polar'})

ax.plot(angles, AF_db, label='Espiral')
ax.set_title('Gráfico Polar')

plt.tight_layout()
plt.show()
