# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 12:39:25 2026

@author: Ricardo Alexandre
"""

'''
3. Leia o arquivo handel.wav e fa¸ca o que se pede nos
itens abaixo:
(a) Utilizando a fun¸c˜ao calculate_spectrum(), calcule
o espectro do sinal de ´audio.

(b) Comente os resultados obtidos.
'''

#%%
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy import signal
from scipy.io import wavfile
from pathlib import Path


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
# Usando caminho relativo para ler as arquivos em pastas paralelas
fs_handel, handel = wavfile.read('..\Arquivos_complementares\data_handel.wav')

xf, amplitude = calculate_spectrum(handel, fs_handel)

#%% Plotagem dos gráficos
figure1, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))
ax1.plot(handel)
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Amplitude")
ax1.grid(True)

ax2.plot(xf, amplitude)
ax2.set_xlabel("Frequencys (Hz)")
ax2.set_ylabel("Amplitude")
ax2.grid(True)

plt.show()
