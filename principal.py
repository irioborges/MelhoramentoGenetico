#!/bin/python

import numpy as np
import math
from functools import reduce
from operator import mul

linha_com_zeros = [0]*10
matriz = [ linha_com_zeros ] * 5

matriz[0] = [0.0625, 7.5625, 0.5625, -1, 5.0625, 3.0625, -1, 3.0625, 1.5625, 1.5625]
matriz[1] = [3.0625, -1, 0.0625, 1.5625, -1, 7.5625, 0.5625, 0.5625, 0.0625, 5.0625] 
matriz[2] = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
matriz[3] = [0.0625, 3.0625, 3.0625, 0.5625, -1, 0.5625, 1.5625, 7.5625, 5.0625, 0.0625]
matriz[4] = [1.5625, 0.5625, 7.6525, 3.0625, 0.0625, -1, 5.0625, 14.0625, 10.5625, -1]

matriz[0] = [3.0625, 14.0625, -1, 1.5625, 10.5625, 7.5625, 0.5625, -1, -1, 5.0625]
matriz[1] = [0.5625, 7.5625, 0.5625, -1, 5.0625, 3.0625, -1, 3.0625, 1.5625, 1.5625]

#0,5625	7,5625	0,5625	-1	5,0625	3,0625	-1	3,0625	1,5625	1,5625
#3,0625	14,0625	-1	1,5625	10,5625	7,5625	0,5625	-1	-1	5,0625
#-1	-1	-1	-1	-1	-1	-1	-1	-1	-1
#0,0625	3,0625	3,0625	0,5625	-1	0,5625	1,5625	7,5625	5,0625	0,0625
#1,5625	0,5625	7,5625	3,0625	0,0625	-1	5,0625	14,0625	10,5625	-1

numero_cruzamentos = [4, 3, 0, 2, 1]
cruzamentos = [0] * 10

for i in range(5):
    for j in range(10):
        if matriz[i][j] != -1:
            matriz[i][j] = matriz[i][j] * 10000
        else:
            matriz[i][j] = math.inf
   
        
for i in range(5):
    for j in range(numero_cruzamentos[i]):
        lst = np.array(matriz[i])
        minimo = min(matriz[i])
        result = np.where(lst == minimo)

        cruzamentos[result[0][0]] = [result[0][0]]
        #print(matriz[i][result[0][0]])

        for k in range(5):
            matriz[k][result[0][0]] = math.inf

        print("Touro " + str(i) + " valor " + str(minimo) + " esta na vaca " + str(result[0][0]))       
        

