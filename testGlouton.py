# -*- coding: utf-8 -*-
from algorithms import AlgoDyn, AlgoGlouton
from numpy.random import randint

#Test de système de capacités
def TestGloutonCompatible(k, V):
  if k>=3:
    for s in range(V[3-1]+2,V[k-2]+V[k-1]):
      for j in range(k):
        a = AlgoGlouton(s,k,V)
        b = AlgoGlouton(s-V[j],k,V)+1
        if (V[j]<s) and (a>b):
          return False
  return True

""""
Generation de systemes de capacites
cet algorithme génère aléatoirement des vecteurs de capacités
en utilisant la fonction randint de la bibliothèque numpy.random
"""
def GenererCapacite(Pmax):
  A = []
  V = []
  for k in range(2,10):
    for j in range(1,100):      
      V = randint(2, Pmax, k)
      V = list( dict.fromkeys(V) )
      V.sort()
      V = [1] + V
      if len(V)>2:
        A.append(V)
  return A

#Question 14
def Analyse(pmax,f):
  A = GenererCapacite(pmax)
  nbGC = 0
  compatible = [] #sauvegarder les systèmes glouton-compatibles
  n_compatible=[] #sauvegarder les systèmes non glouton-compatibles
  stats = []      #sauvegarder les couples (max,avg) des ecarts calculés pour chaque systeme non g-c
  for v in A:
    k = len(v)
    if TestGloutonCompatible(k, v)==True:
      compatible.append(v)
      nbGC = nbGC + 1
    else:
      ecart = []
      for s in range(pmax, f*pmax):
        opt = AlgoDyn(s,len(v),v)
        a = AlgoGlouton(s,len(v),v)
        ecart.append(a-opt)
      stats.append((max(ecart),sum(ecart)/len(ecart)))
      n_compatible.append(v)
  return stats, compatible, n_compatible

def main():
    Pmax = 50
    A = GenererCapacite(Pmax) #Générer une liste de vecteurs de capacités
    nbGC = 0
    for v in A:
      k = len(v)
      if TestGloutonCompatible(k, v)==True:
        nbGC = nbGC + 1
    rate = round(nbGC/len(A),2)
    #Affichage des résultats
    print("Nombre de systèmes de capacités générés : ",len(A))
    print("Nombre de systèmes glouton-compatibles  : ",nbGC)
    print("La proportion des systèmes glouton-compatibles : {} ({} %)".format(rate,rate*100))
    
    
    stats, compatible, n_compatible = Analyse(200,10)
    with open("test1.txt",'w') as f:
      for el in stats:
        f.write(str(el)+"\n")
    with open("compatibles1.txt",'w') as f:
      for el in compatible:
        f.write(str(el)+"\n")
    with open("n_compatibles1.txt",'w') as f:
      for el in n_compatible:
        f.write(str(el)+"\n")
    
#
main()