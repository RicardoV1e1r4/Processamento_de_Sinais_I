# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 22:14:09 2026

@author: Ricardo Alexandre
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz
import Filtros
import Funções_Janela as fj

pi = np.pi
M = 80

n = np.arange(0, M + 1, 1)

Omega_c1 = 2000
Omega_c2 = 4000
Omega_s  = 10000

wc1 = (Omega_c1*2*pi)/Omega_s
wc2 = (Omega_c2*2*pi)/Omega_s

pb = Filtros.passa_baixas(M, wc1)

pa = Filtros.passa_altas(M, wc2)

rejeita_faixa = pb + pa

window_r = fj.janela_retangular(M)
window_h = fj.janela_hamming(M)

hn_linha = rejeita_faixa * window_r

omega1, Hhamm = freqz(hn_linha, 1, 2048)

# plt.stem(n, pa)
plt.plot(Omega_s * omega1/(2 * pi), 20 * np.log10(abs(Hhamm)/max(abs(Hhamm))))

plt.show()