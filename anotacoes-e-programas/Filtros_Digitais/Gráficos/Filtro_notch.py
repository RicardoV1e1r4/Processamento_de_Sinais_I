# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 20:36:07 2026

@author: Ricardo Alexandre
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

# parâmetros dos polos
pi = np.pi
r = 0.95

Omega_s = 200                  #(rad/s)
fs      = Omega_s/(2*pi)       #frequência de amostragem

f1      = 10                   #Hz
Omega_1 = 2*pi*f1              #(rad/s)

wp = 2*pi*f1/fs 

m2 = r**2
m1 = -2*(m2**0.5)*np.cos(wp)
m3 = m1/(m2**0.5)

# coeficientes
b = [1, m3, 1]
a = [1, m1, m2]

# Resposta em frequência
w, H = freqz(b, a, 2048)

figure, (eix1, eix2) = plt.subplots(2, 1, figsize=(8, 6))

eix1.plot(w, np.abs(H))
eix1.set_xlabel(r'$\omega (rad/amostra)$')
eix1.set_ylabel(r'$|H(e^{j\omega})|$')
eix1.set_title('Filtro Notch de 2ª Ordem')
eix1.grid(True)

eix2.plot(w*fs/(2*pi), np.abs(H))
eix2.set_xlabel('Frequência (Hz)')
eix2.set_ylabel(r'$|H(e^{j\omega})|$')
# eix2.set_title('Filtro Passa-Baixas de 2ª Ordem')
eix2.grid(True)

plt.tight_layout()
plt.show()
