# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 13:09:02 2026

@author: Ricardo Alexandre
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

# parâmetros dos polos
r = 0.8
wp = 2.5

m1 = -2*r*np.cos(wp)
m2 = r**2

# coeficientes
b = [1, -2, 1]
a = [1, m1, m2]

# resposta em frequência
w, H = freqz(b, a, 2048)

plt.figure(figsize=(8,4))
plt.plot(w/np.pi, np.abs(H))
plt.grid(True)
plt.xlabel(r'$\omega/\pi$')
plt.ylabel(r'$|H(e^{j\omega})|$')
plt.title('Filtro Passa-Baixas de 2ª Ordem')
plt.show()