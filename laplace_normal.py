#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Solução da equação de Laplace, método das difrenaças finitas não otimizado
import numpy as np
import time


def laplace_normal():
    inicio = time.time()
    # Tamanho do Grid
    N = 100
    # Condições de contorno
    T_sup = 100
    erro = 1e-6

    # Criar os arrays para guardar o valor da temperatura
    Temp = np.zeros([N+1, N+1], float)
    Temp[0, :] = T_sup
    T_grid = np.empty([N+1, N+1], float)
    delta = 1.0

    while delta > erro:
        for i in range(N+1):
            for j in range(N+1):
                if i == 0 or i == N or j == 0 or j == N:
                    T_grid[i, j] = Temp[i, j]  # Aplicando as condições
                else:
                    T_grid[i, j] = (1/4)*(Temp[i+1, j]+Temp[i-1, j]+(Temp[i, j+1]+Temp[i, j-1]))

        # Método da relaxação
        delta = np.max(abs(Temp - T_grid))  # novo valor do delta
        Temp, T_grid = T_grid, Temp  # atualização da temperatura

    fim = time.time()
    return fim - inicio

