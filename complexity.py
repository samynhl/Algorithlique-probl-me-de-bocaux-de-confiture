# -*- coding: utf-8 -*-

from algorithms import AlgoRec, AlgoDyn, AlgoGlouton
import time
import matplotlib.pyplot as plt

def SystemeExpo(d,k):
  V = []
  for i in range(1,k+1):
    V.append(d**(i-1))
  return V

"""
Analyse de complexité expérimentale
Ce programme génère des capacités différentes et calcule pour chacune
le temps d'execution par l'un des algorithme de résolution du problème
du nombre de bocaux minimum (AlgoRec,AlgoDyn,AlgoGlouton), puis
génère le graphe de complexité temporelle en fct de s (pour k donné)
"""
def plot_complexity(d,k,smax,numAlgo):
  elements = list()
  times = list()
  v = SystemeExpo(d,k)
  check = False
  for s in range(1,smax,3):
    if numAlgo==1:
        start = time.clock()
        AlgoRec(s,k,v)
        end = time.clock()
        times.append(end-start)
        elements.append(s)
        if end-start>1:  #s"arreter quand le temps d'exécution dépasse une minute
            check = True
            break
    else:
        if numAlgo==2:
            start = time.clock()
            AlgoDyn(s,k,v)
            end = time.clock()
        else:
            start = time.clock()
            AlgoGlouton(s,k,v)
            end = time.clock()
        times.append(end-start)
        elements.append(s)
  plt.xlabel('Capacity S')
  plt.ylabel('Time Complexity')
  label = "Algo {} with d = ".format(numAlgo) + str(d) + ", k = "+str(k)
  plt.plot(elements, times, label =label)
  plt.grid()
  plt.legend()
  plt.show()
  #plt.savefig("label"+".png")
  return check

#cette fonction varie S entre 2 et smax, k entre 2 et kmax, et d entre
#2 et 4 et affiche la courbe de complexité en temps d'exécution de l'algorithme
#passé en paramètre [1:Recursif,2:Dynamique, 3:Glouton]
def varier(smax,kmax, numAlgo):
    for d in range(2,5):
        for k in range(2,kmax):
            check = plot_complexity(d,k, smax,numAlgo)
            if check ==True:
                break

def main():
    #
    varier(600,9,1)
    #varier(600,9,2)
    #varier(600,9,3)

main()
