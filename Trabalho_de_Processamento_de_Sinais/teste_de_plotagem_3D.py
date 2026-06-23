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

ax = fig.add_subplot(projection='3d')

ax.scatter(sensores_x, 0, 0, marker='o')

plt.show()
