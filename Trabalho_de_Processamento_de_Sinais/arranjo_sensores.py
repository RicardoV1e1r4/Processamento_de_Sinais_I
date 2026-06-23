# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 20:27:23 2026

@author: Ricardo Alexandre
"""

# Modelagem e Análise de Arranjos de Sensores

import matplotlib.pyplot as plt
import numpy as np

# Funções geradoras dos Arranjos dos Sensores
    # generate_ula(M, d)
    # generate_uca(M, R)
    # generate_upa(Mx, My, dx, dy)
    # generate_ucya(Mc, Nz, R, dz)
    
    
# Variáveis
pi = np.pi


def generate_ula(M, d):
    #, eixo=coord
    
    comp_total = (M)*d
    sensores   = np.arange(0, comp_total, d)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    
    ax.scatter(sensores, 0, 0, marker='o')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')


def generate_uca(M, R):
    #, eixo=coord
    
    comp_total = 2*pi*R
    arc0       = comp_total/M
    
    # arcs       = np.linspace(0, comp_total, M)
    
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    
    for i in np.arange(0, M, 1):
        print(i)
        xs = R*np.cos((i*arc0))
        ys = R*np.sin((i*arc0))
        ax.scatter(xs, ys, 0, marker='o')
    
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

generate_uca(5, 3)

plt.show()
