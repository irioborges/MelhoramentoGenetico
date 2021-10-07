#!/bin/python

from __future__ import print_function
from ortools.graph import pywrapgraph
import time
import random

#Cria nós iniciais aleatórios
#Essa função não está mais sendo usada, pois foi substituida pela CriaDadosAleatorios
def CriaStartNodes(num_vacas):
  print("Começou a gerar dados de start_nodes")
  start_nodes = []
  for i in range(int(num_vacas)):
    start_nodes = start_nodes + [0]
  
  for i in range(int(num_vacas)):
    for j in range(int(num_vacas)):
      start_nodes = start_nodes + [i+1]

  
  for i in range(int(num_vacas)):
    start_nodes = start_nodes + [i+int(num_vacas)+1]

  print("Terminou de gerar dados de start_nodes")
  return start_nodes

#Cria nós finais aleatórios
#Essa função não está mais sendo usada, pois foi substituida pela CriaDadosAleatorios
def CriaEndNodes(num_vacas):
  print("Começou a gerar dados de end_nodes")
  end_nodes = []
  for i in range(int(num_vacas)):
    end_nodes = end_nodes + [i+1]
  
  for i in range(int(num_vacas)):
    for j in range(int(num_vacas)):
      end_nodes = end_nodes + [int(num_vacas)+j+1]

  for i in range(int(num_vacas)):
    end_nodes = end_nodes + [2*int(num_vacas) + 1]

  print("Terminou de gerar dados de end_nodes")
  return end_nodes

#Cria capacidades aleatórias
#Essa função não está mais sendo usada, pois foi substituida pela CriaDadosAleatorios
def CriaCapacities(num_vacas):
  print("Começou a gerar dados de capacities")
  capacities = []
  capacities = capacities + [1] * int(num_vacas)

  for i in range(int(num_vacas)):
    for j in range(int(num_vacas)):
      capacities = capacities + [1]

  for i in range(int(num_vacas)):
    capacities = capacities + [1]

  print("Terminou de gerar dados de capacities")
  return capacities

#Cria custos aleatórios
#Essa função não está mais sendo usada, pois foi substituida pela CriaDadosAleatorios
def CriaCustos(num_vacas):
  print("Começou a gerar dados de custos")
  costs = []
  for i in range(int(num_vacas)):
    costs = costs + [0]

  for i in range(int(num_vacas)):
    for j in range(int(num_vacas)):
      costs = costs + [random.randint(1, 99999)]

  for i in range(int(num_vacas)):
    costs = costs + [0]

  print("Terminou de gerar dados de custos")
  return costs

#Cria Supplies aleatórios
#Essa função não está mais sendo usada, pois foi substituida pela CriaDadosAleatorios
def CriaSupplies(num_vacas):
  supplies = []
  supplies = supplies + [int(num_vacas)]

  for i in range(int(num_vacas)):
    supplies = supplies + [0]

  for i in range(int(num_vacas)):
    supplies = supplies + [0]

  supplies = supplies + [int(num_vacas) * -1]

  return supplies

#Essa é a função que está sendo utilizada para criação de dados aleatórios!
def CriaDadosAleatorios(num_vacas):
  start_nodes = []
  end_nodes = []
  capacities = []
  costs = []
  supplies = []

  for i in range(int(num_vacas)):
    start_nodes = start_nodes + [0]
    end_nodes = end_nodes + [i+1]
    capacities = capacities + [1]
    costs = costs + [0]
    supplies = supplies + [0]
    supplies = supplies + [0]

  for i in range(int(num_vacas)):
    for j in range(int(num_vacas)):
      start_nodes = start_nodes + [i+1]
      end_nodes = end_nodes + [int(num_vacas)+j+1]
      capacities = capacities + [1]
      costs = costs + [random.randint(1, 99999)]

  for i in range(int(num_vacas)):
    start_nodes = start_nodes + [i+int(num_vacas)+1]
    end_nodes = end_nodes + [2*int(num_vacas) + 1]
    capacities = capacities + [1]
    costs = costs + [0]

  supplies = supplies + [int(num_vacas) * -1]

  return start_nodes, end_nodes, capacities, costs

def main(start_nodes, end_nodes, capacities, costs, supplies, source, tasks, sink):
  """Solving an Assignment Problem with MinCostFlow"""

  # Instantiate a SimpleMinCostFlow solver.
  #1. Complexidade constante, conforme: /home/iriordmb/.local/lib/python3.9/site-packages/ortools/graph/pywrapgraph.py
  min_cost_flow = pywrapgraph.SimpleMinCostFlow()

  # Define the directed graph for the flow.

  touros = ['', 'Touro1', 'Touro1', 'Touro1', 'Touro2', 'Touro2', 'Touro2', 'Touro2', 'Touro4', 'Touro4', 'Touro5']
  vacas = ['', 'Vaca1', 'Vaca2', 'Vaca3', 'Vaca4', 'Vaca5', 'Vaca6', 'Vaca7', 'Vaca8', 'Vaca9', 'Vaca10']

  # Add each arc.
  # 2. Complexidade Linear
  for i in range(len(start_nodes)):
    min_cost_flow.AddArcWithCapacityAndUnitCost(start_nodes[i], end_nodes[i],
                                                capacities[i], costs[i])
  # Add node supplies.

  #3. Complexidade Linear
  for i in range(len(supplies)):
    min_cost_flow.SetNodeSupply(i, supplies[i])

  # Find the minimum cost flow between node 0 and node 10.
  #O Solve() acho que vai nesse método: SimpleMinCostFlow_Solve
  if min_cost_flow.Solve() == min_cost_flow.OPTIMAL:
    print('Variância total = ', min_cost_flow.OptimalCost())
    print()
    for arc in range(min_cost_flow.NumArcs()):

      # Can ignore arcs leading out of source or into sink.
      if min_cost_flow.Tail(arc)!=source and min_cost_flow.Head(arc)!=sink:

        # Arcs in the solution have a flow value of 1. Their start and end nodes
        # give an assignment of worker to task.

        if min_cost_flow.Flow(arc) > 0:
          if int(num_vacas) == 0:
            print('Touro %s cruzará com a vaca %s.  variância = %d' % (
                touros[min_cost_flow.Tail(arc)],
                vacas[min_cost_flow.Head(arc) - 10],
                min_cost_flow.UnitCost(arc)))
          else:
            print('Touro %s cruzará com a vaca %s.  variância = %d' % (
                min_cost_flow.Tail(arc),
                min_cost_flow.Head(arc),
                min_cost_flow.UnitCost(arc)))
  else:
    print('There was an issue with the min cost flow input.')
if __name__ == '__main__':
  
  num_vacas = input("Digite o numero de cruzamentos. Digite 0 para utilizar os dados do relatório. ")
 
  start_nodes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] + [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 
                 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 
                 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 
                 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 
                 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 
                 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 
                 10, 10, 10, 10, 10, 10, 10, 10, 10, 10] + [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


  #start_nodes = CriaStartNodes(num_vacas)

  end_nodes =   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] + [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
                 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
                 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
                 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
                 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
                 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
                 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
                 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
                 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
                 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] + [21, 21, 21, 21, 21, 21, 21, 21, 21, 21]

  #end_nodes = CriaEndNodes(num_vacas)

  capacities =  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] + [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                  1, 1, 1, 1, 1, 1, 1, 1, 1, 1] + [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

  #capacities = CriaCapacities(num_vacas)

  #Esses são os dados que estão na tabela do excel dados.xlsx
  costs      =  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] + [5625, 75625,	5625,	625,	50625,	99999999,	625,	30625,	15625,	99999999,
                  5625, 75625,	5625,	625,	50625,	99999999,	625,	30625,	15625,	99999999,
                  5625, 75625,	5625,	625,	50625,	99999999,	625,	30625,	15625,	99999999,
                  30625,	99999,	625,	15625,	99999,	75625,	5625,	5625,	625,	50625,
                  30625,	99999,	625,	15625,	99999,	75625,	5625,	5625,	625,	50625,
                  30625,	99999,	625,	15625,	99999,	75625,	5625,	5625,	625,	50625,
                  30625,	99999,	625,	15625,	99999,	75625,	5625,	5625,	625,	50625,
                  99999,	30625,	30625,	99999,	15625,	5625,	15625,	75625,	50625,	625,
                  99999,	30625,	30625,	99999,	15625,	5625,	15625,	75625,	50625,	625,
                  15625,	5625,	99999,	30625,	625, 625,	99999,	140625,	105625,	5625] + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

  # Define an array of supplies at each node.
  #costs = CriaCustos(num_vacas)
  

  supplies = [10, 
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              -10
              ]

  #supplies = CriaSupplies(num_vacas)

 
  source = 0
  tasks = 10
  sink = 21

  if int(num_vacas) != 0:
    start_nodes, end_nodes, capacities, costs = CriaDadosAleatorios(num_vacas)
    supplies = CriaSupplies(num_vacas)
    sink = (2*int(num_vacas)) + 1
    tasks = num_vacas

  start_time = time.perf_counter()
  main(start_nodes, end_nodes, capacities, costs, supplies, source, tasks, sink)
  print()
  print("Tempo =", time.perf_counter() - start_time, "segundos")