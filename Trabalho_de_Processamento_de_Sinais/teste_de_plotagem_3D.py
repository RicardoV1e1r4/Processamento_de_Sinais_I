# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 20:27:23 2026

@author: Ricardo Alexandre
"""

# Modelagem e Análise de Arranjos de Sensores

import matplotlib.pyplot as plt
import numpy as np    

pi = np.pi
M = 5; d = 3

comp_total = (M)*d

sensores_x = np.arange(0, comp_total, d)
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(sensores_x, 0, 0, marker='o')

xs = [0, 2, 4]
ys = [1, 3, 5]
zs = [0, 1, 1]

ax = fig.add_subplot(projection='3d')

ax.scatter(xs, ys, zs, marker='o')

plt.show()
