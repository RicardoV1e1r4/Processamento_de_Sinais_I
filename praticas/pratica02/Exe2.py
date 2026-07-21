# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 18:44:48 2026

@author: Ricardo Alexandre
"""

#%%
'''
2. Para um chirp com frequência inicial f0 = 500 Hz, frequência final f1 = 10000 Hz,
amostrado com fs = 44.1 kHz, faça o que se pede nos itens abaixo:
    
(a) Utilizando a função calculate_spectrum(), calcule o espectro do chirp com varreduras
de frequência lineares, quadráticas e logarítmicas.

(b) Comente os resultados obtidos.

'''
#%%
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy import signal

#%% Parâmetros
pi = np.pi

f0 = 500
f1 = 10e3

fs = 44.1e3

duracao = 5

#%% Função Calcula Espectro
def calculate_spectrum(signal, sampling_frequency, single_sided=True):
    """
    Calculates the amplitude spectrum of a signal.

    Args:
        signal (np.ndarray): The time-domain signal.
        sampling_frequency (float): The sampling frequency of the signal (Hz).
        single_sided (bool): If True, returns the single-sided spectrum (positive frequencies).
                             If False, returns the full spectrum (positive and negative frequencies).

    Returns:
        tuple: A tuple containing:
            - frequencies (np.ndarray): Array of frequencies (Hz).
            - amplitudes (np.ndarray): Array of corresponding amplitude magnitudes.
    """
    N = len(signal) # Number of sample points
    T = 1.0 / sampling_frequency # Sample spacing

    # Perform the FFT
    yf = fft(signal)

    if single_sided:
        xf = fftfreq(N, T)[:N//2] # Frequencies for the positive half of the spectrum
        # Calculate the single-sided amplitude spectrum
        # np.abs(yf[0:N//2]) gets the magnitude of the positive frequencies
        amplitudes = 1.0/N * np.abs(yf[0:N//2])
    else:
        xf = fftfreq(N, T) # All frequencies
        amplitudes = 1.0/N * np.abs(yf)

    return xf, amplitudes
#%%
time = np.linspace(0, duracao, int(fs*duracao), endpoint=False)

#%% Chirp Linear
a1 = (f1 - f0)/(pi * duracao**2)

# linear_chirp = np.cos(2*pi*(a1*time + f0)*time)
linear_chirp = signal.chirp(time, f0, duracao, f1, method='linear')

#%% Frequências do Chirp Linear

xf1, amplitude1 = calculate_spectrum(linear_chirp, fs)

#%% Plotagem dos gráficos
figure1, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))
ax1.plot(time, linear_chirp)
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Amplitude")
ax1.set_xlim((-0.1*duracao, duracao))
plt.grid(True)


ax2.plot(xf1, amplitude1)
ax2.set_xlabel("Frequencys (Hz)")
ax2.set_ylabel("Amplitude")
ax2.set_xlim((0, f1 + 100))
plt.grid(True)

plt.show()
