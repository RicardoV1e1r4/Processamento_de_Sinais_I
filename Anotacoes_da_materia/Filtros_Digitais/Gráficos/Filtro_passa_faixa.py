# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 21:57:52 2026

@author: Ricardo Alexandre
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

pi = np.pi

# Raio dos filtros
r = 0.95
r2 = 0.8

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


figure, eix = plt.subplots(3, 2, figsize=(8,6), layout="constrained")
# spec = figure.add_gridspec(nrows=3, ncols=2)

print(eix)

# Filtro Passa-Baixa em Rad/amostras
eix[0, 0].plot(w1, np.abs(H1))
eix[0, 0].set_xlabel(r'$\omega$ (rad/amostras)')
eix[0, 0].set_ylabel(r'$|H(e^{j\omega})|$')
eix[0, 0].grid(True)

# Filtro Passa-Alta em Rad/amostras
eix[1, 0].plot(w2, np.abs(H2), color='r')
eix[1, 0].set_xlabel(r'$\omega$ (rad/amostras)')
eix[1, 0].set_ylabel(r'$|H(e^{j\omega})|$')
eix[1, 0].grid(True)

# Soma dos filtros PB e PA em Rad/amostras
eix[2, 0].plot(w1, np.abs(H3))
eix[2, 0].set_xlabel(r'$\omega$ (rad/amostras)')
eix[2, 0].set_ylabel(r'$|H(e^{j\omega})|$')
eix[2, 0].grid(True)

# Filtro Passa-Baixa em Hertz
eix[0, 1].plot(fs*w1/(2*pi), np.abs(H1))
eix[0, 1].set_xlabel(r'$\omega/2\pi$')
eix[0, 1].set_ylabel(r'$|H(e^{j\omega})|$')
eix[0, 1].grid(True)

# Filtro Passa-Alta em Hertz
eix[1, 1].plot(fs*w2/(2*pi), np.abs(H2), color='r')
eix[1, 1].set_xlabel(r'$\omega/2\pi$')
eix[1, 1].set_ylabel(r'$|H(e^{j\omega})|$')
eix[1, 1].grid(True)

# Soma dos Filtros PB e PA em Hertz
eix[2, 1].plot(fs*w1/(2*pi), np.abs(H3))
eix[2, 1].set_xlabel(r'$\omega/2\pi$')
eix[2, 1].set_ylabel(r'$|H(e^{j\omega})|$')
eix[2, 1].grid(True)

figure.suptitle("FIltro Passa-Faixa de 2ª ordem")

plt.tight_layout()
plt.show()
