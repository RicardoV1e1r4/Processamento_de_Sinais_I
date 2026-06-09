# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 13:16:05 2026

@author: Ricardo Alexandre
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

# parâmetros dos polos
r = 0.8

w1 = 0.25
w2 = 0.35

mb1 = -2*r*np.cos(w1)
mb2 = r**2

ma1 = -2*r*np.cos(w2)
ma2 = r**2

# coeficientes do passa baixa
num1 = [1, 2, 1]
den1 = [1, mb1, mb2]

# coeficientes do passa-alta
num2 = [1, -2, 1]
den2 = [1, ma1, ma2]

# resposta em frequência passa-baixa
w1, H1 = freqz(num1, den1, 2048)

# resposta em frequência passa-alta
w2, H2 = freqz(num2, den2, 2048)

w3, H3 = freqz(num1, den1, 2048)+freqz(num2, den2, 2048)

figure = plt.subplots(figsize=(8,7))

eix1 = plt.subplot(2, 2, 1)
eix1.plot(w1/(2*np.pi), np.abs(H1))
eix1.plot(w2/(2*np.pi), np.abs(H2))
eix1.set_xlabel(r'$\omega$ (rad/amostras)')
eix1.set_ylabel(r'$|H(e^{j\omega})|$')
eix1.set_title('Filtro Rejeita-Faixa de 2ª Ordem')
eix1.grid(True)

eix2 = plt.subplot(2, 2, 1)
eix2.plot(w3, np.abs(H3))
eix2.set_xlabel(r'$\omega$ (rad/amostras)')
eix2.set_ylabel(r'$|H(e^{j\omega})|$')
eix2.set_title('Filtro Rejeita-Faixa de 2ª Ordem')
eix2.grid(True)

eix3 = plt.subplot(2, 2, 3, projection='polar')
eix3.plot(w1/np.pi, np.abs(H1))
eix3.plot(w2/np.pi, np.abs(H2))
eix3.set_xlabel(r'$\omega/\pi$')
eix3.set_ylabel(r'$|H(e^{j\omega})|$')
eix3.grid(True)

plt.show()