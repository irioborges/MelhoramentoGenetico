#!/bin/python

import numpy as np
import math
from functools import reduce
from operator import mul

linha_com_zeros = [0]*10
matriz = [ linha_com_zeros ] * 5

matriz[1] = [3.0625, -1, 0.0625, 1.5625, -1, 7.5625, 0.5625, 0.5625, 0.0625, 5.0625] 
matriz[0] = [0.0625, 7.5625, 0.5625, -1, 5.0625, 3.0625, -1, 3.0625, 1.5625, 1.5625]
matriz[3] = [0.0625, 3.0625, 3.0625, 0.5625, -1, 0.5625, 1.5625, 7.5625, 5.0625, 0.0625]
matriz[4] = [1.5625, 0.5625, 7.6525, 3.0625, 0.0625, -1, 5.0625, 14.0625, 10.5625, -1]
matriz[2] = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

numero_cruzamentos = [3, 4, 0, 2, 1]

#print(matriz[0][4])

for touros in matriz:

    for vacas in touros:
        int(vacas * 10000)
        #print(vacas)
        
            
        

for touros in matriz:
#    lst = np.array(touros)
#    minimo = min(touros)
#    result = np.where(lst == minimo)
    #touros.replace(-1, math.inf)
    print(min(touros))