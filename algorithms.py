# -*- coding: utf-8 -*-
import numpy as np
import sys


#Algorithme 1 récursif
"""
Algorithme récursif pour le calcul du nombre minimum de bocaux à remplir
par la quantité s de confiture en utilisant i cases du système de capacités v
"""
def AlgoRec(s,i,v):
  if s==0:              #si s==0 alors retourner 0
    return 0
  if i==0:              #si i==0 alors retourner l'infini
    return sys.maxsize
  if s<0:               #si s<0 alors retourner l'infini
    return sys.maxsize
  else:                 #sinon appliquer la relation de récurrence
    return min(AlgoRec(s,i-1,v), AlgoRec(s-v[i-1],i,v)+1)

#Algorithme 2 : utilisation de la matrice M
"""
algorithme iteratif AlgoDyn (en pseudo-code) qui determine le
nombre minimum de bocaux necessaires pour une quantite de confiture S
"""
def AlgoDyn(S,i, V):
  #m = math.inf
  M = np.zeros((S+1,i+1),int)
  #initialisation de la matrice M avec des valeurs infinies
  for k in range(S+1):
    M[k,0]= 10**8
  for j in range(1,i+1):
    for k in range(1,S+1):
      try:
        if k-V[j-1]<0:
          m2 =  10**9
        else:
          m2 = M[k-V[j-1],j]
        M[k,j]= min(M[k,j-1],m2+1)
      except Exception as e:
        print(e)
  return M[S,i]

#ALGORITHME 3 : méthode gloutonne
"""
Détermine les bocaux (et leur nombre) à choisir pour remplir la quantité
passée en argument.
Utilise la division euclidienne et le modulo de façon à pouvoir
traiter tous les cas.
"""
def AlgoGlouton(S: int,k, V):
    indice_capacites = k-1
    a = 0
    while indice_capacites >= 0:
        rendu = S // V[indice_capacites]
        a += rendu
        encore_a_rendre = S % V[indice_capacites]
        S = encore_a_rendre
        indice_capacites -= 1
    return a

#Algorithme 2 : utilisation de la matrice M et retourner le tableau A
"""
algorithme iteratif AlgoDyn (en pseudo-code) qui determine le
nombre minimum de bocaux necessaires pour une quantite de confiture S,
et indique le nombre de bocaux utilisés pour chaque capacité
"""
def AlgoDyn_(S,i, V):
  #m = math.inf
  M = np.zeros((S+1,i+1),int)
  #initialisation de la matrice M avec des valeurs infinies
  for k in range(S+1):
    M[k,0]= 10**9
  for j in range(1,i+1):
    for k in range(1,S+1):
      try:
        if k-V[j-1]<0:
          m2 = 10**9
        else:
          m2 = M[k-V[j-1],j]
        M[k,j]= min(M[k,j-1],m2+1)
      except:
        pass
  #retourner A
  A = []
  for t in range(len(V)):
    A.append(0)
  s1 = S
  i1 = i
  while True:
    if (s1-V[i1-1]>=0) and (M[s1,i1] == M[s1-V[i1-1], i1]+1):
      A[i1-1] = A[i1-1] + 1
      s1 = s1 - V[i1-1]
    else:
      i1 = i1-1
      if (i1<0):
        break
  return M[S,i], A