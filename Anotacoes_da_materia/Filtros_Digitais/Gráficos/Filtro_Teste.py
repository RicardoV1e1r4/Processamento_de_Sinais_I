# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 21:57:52 2026

@author: Ricardo Alexandre
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

pi = np.pi

# parâmetros dos polos
r = 0.7

# Frequências
fs = 60000

f1 = 5000
f2 = 20000

# rad/segundos
Omega_1 = 2*pi*f1
Omega_2 = 2*pi*f2

# rad/amostras
w1 = 2*pi*(f1/fs)
w2 = 2*pi*(f2/fs)
print(w1)
print(w2)

# Passa-baixas
m_baixa1 = -2*r*np.cos(w2)
m_baixa2 = r**2
print(m_baixa1)

# Passa-alta
m_alta1 = -2*r*np.cos(w1)
m_alta2 = r**2
print(m_alta1)

# coeficientes do passa baixa
num1 = [1, 2, 1]
den1 = [1, m_baixa1, m_baixa2]

# coeficientes do passa-alta
num2 = [1, -2, 1]
den2 = [1, m_alta1, m_alta2]

# resposta em frequência passa-baixa
w1, H1 = freqz(num1, den1, 2048)

# resposta em frequência passa-alta
w2, H2 = freqz(num2, den2, 2048)

H3 = H1 + H2


figure, ax = plt.subplots(figsize=(8,6), layout="constrained")
spec = figure.add_gridspec(nrows=3, ncols=2)

# eix1 = plt.subplot(3, 2, 1)
eix1 = figure.add_subplot(spec[0, 0])
eix1.plot(w1, np.abs(H1))
# eix1.plot(w2, np.abs(H2))
eix1.set_xlabel(r'$\omega$ (rad/amostras)')
eix1.set_ylabel(r'$|H(e^{j\omega})|$')
eix1.set_title('Filtro de 2ª Ordem')
eix1.grid(True)

# eix2 = plt.subplot(3, 2, 3)
eix2 = figure.add_subplot(spec[1, 0])
eix2.plot(w2, np.abs(H2), color='r')
eix2.set_xlabel(r'$\omega$ (rad/amostras)')
eix2.set_ylabel(r'$|H(e^{j\omega})|$')
eix2.grid(True)

# eix3 = plt.subplot(3, 2, 5)
eix3 = figure.add_subplot(spec[2, 0])
eix3.plot(w1, np.abs(H3))
eix3.set_xlabel(r'$\omega$ (rad/amostras)')
eix3.set_ylabel(r'$|H(e^{j\omega})|$')
eix3.grid(True)

# eix4 = plt.subplot(3, 2, 2)
eix4 = figure.add_subplot(spec[0, 1])
eix4.plot(fs*w1/(2*pi), np.abs(H1))
# eix4.plot(w2, np.abs(H2))
eix4.set_xlabel(r'$\omega/2\pi$')
eix4.set_ylabel(r'$|H(e^{j\omega})|$')
eix4.set_title('Filtro de 2ª Ordem')
eix4.grid(True)

# eix5 = plt.subplot(3, 2, 4)
eix5 = figure.add_subplot(spec[1, 1])
eix5.plot(fs*w2/(2*pi), np.abs(H2), color='r')
eix5.set_xlabel(r'$\omega/2\pi$')
eix5.set_ylabel(r'$|H(e^{j\omega})|$')
eix5.grid(True)

# eix6 = plt.subplot(3, 2, 6)
eix6 = figure.add_subplot(spec[2, 1])
eix6.plot(fs*w1/(2*pi), np.abs(H3))
eix6.set_xlabel(r'$\omega/2\pi$')
eix6.set_ylabel(r'$|H(e^{j\omega})|$')
eix6.grid(True)

plt.show()