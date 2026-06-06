# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 17:47:08 2026

@author: Ricardo Alexandre
"""

import matplotlib.pyplot as plt
import numpy as np
#from matplotlib.widgets import Slider

# Valores iniciais do Sliders



# # Taxa de amostragem
# def taxa_amostragem():
#     return Fs
    


# # Frequência angular
# def frequencia_angular():
#     return w


# Vetor tempo
fs = 1
Ts = 1/fs
t_final = 40
t = np.arange(0, t_final, Ts)

# Sinal x[n]
x_n = np.cos(t)

# Sinal variável
h_n = np.sin(t)

# Criação dos gráficos
grafico, (linha1, linha2) = plt.subplots(2, 1, figsize=(7,7))
# Espaço extra para os botões deslizantes
plt.subplots_adjust(left=0.2, bottom=0.40, hspace=0.6)

# configuração do gráfico do sinal x[n] original
linha1.stem(t, x_n)
linha1.set_xlabel('Time [s]', size=10)
linha1.set_ylabel('Amplitude', size=10)
linha1.set_title('Sinal x[n]')
linha1.grid(True)

# Configuração do gráfico do 
linha2.stem(t, h_n)
#grafc2, = linha2.stem(t, np.cos(frequencia_angular*t), color='r')
linha2.set_xlabel('Time [s]', size=10)
linha2.set_ylabel('Amplitude', size=10)
linha2.set_title('Sinal variável')
linha2.grid(True)

###_____BOTÕES DESLIZANTES_____###
#Deslizante 1 - raio da esfera A
# f_sample = plt.axes([0.2, 0.25, 0.65, 0.03])
# slider_raioa = Slider(f_sample, 'Raio A', 0.1, 40, valinit=a)

# #Deslizante 2 - raio da esfera B
# omega = plt.axes([0.2, 0.18, 0.65, 0.03])
# slider_raiob = Slider(omega, 'Raio B', 0.1, 40, valinit=b)


# ###___Função que vai atualizar o gráfico___###
# def atualizar(val):
#     raioa = slider_raioa.val
#     raiob = slider_raiob.val
#     linha1.set_ydata(PreencheDensidade(raioa, raiob))
#     linha2.set_ydata(PreencheDensidade(raioa, raiob, True))
#     figura.canvas.draw_idle()


# # Conecta os slides à função
# slider_raioa.on_changed(atualizar)
# slider_raiob.on_changed(atualizar)

plt.show()
