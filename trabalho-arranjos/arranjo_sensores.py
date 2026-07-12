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
    
    
# Variáveis globais
pi = np.pi


def generate_ula(M, d):
    position = np.zeros((M, 3))
    
    comp_total = M*d
    sensores_x = np.arange(-comp_total/2, comp_total/2, d)
    
    position[:,0] = position[:,0] + sensores_x
    return position


def generate_uca(M, R):    
    arc0 = 2*pi/M
    
    xs = np.zeros(M)
    ys = np.zeros(M)
    
    for i in np.arange(0, M, 1):
        xs[i] = R * np.cos((i*arc0))     # Posição X
        ys[i] = R * np.sin((i*arc0))     # Posição Y

    return xs, ys, 0


def generate_upa(Mx, My, dx, dy):
    x = np.arange(0, Mx*dx, dx)
    y = np.arange(0, My*dy, dy)
    
    X, Y = np.meshgrid(x, y)
    
    xs = X.flatten()
    ys = Y.flatten()
    return xs, ys, 0


def generate_ucya(Mc, Nz, R, dz):
    xs, ys, zs = generate_uca(Mc, R)
    
    xs = np.tile(xs, Nz)
    ys = np.tile(ys, Nz)
    
    zs = np.arange(0, Nz*dz, dz)
    zs = np.repeat(zs, Mc)
    return xs, ys, zs


position = generate_ula(5, 3)
# xs, ys, zs = generate_uca(6, 3)
# xs, ys, zs = generate_upa(5, 3, 1, 2)
# xs, ys, zs = generate_ucya(12, 6, 3, 1)

print(position)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(position[:,0], position[:,1], position[:,2], marker='o', color='b')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
