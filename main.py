# -*- coding: utf-8 -*-
"""
Tester les algorithmes I, II et III
"""
from algorithms import AlgoRec, AlgoDyn, AlgoGlouton
#from complexity import varier

def main(path):
    with open(path,"r") as f:
      lines = f.readlines()  
      S = int(lines[0])
      k = int(lines[1])
      V = []
      for i in range(2,len(lines)):
          V.append(int(lines[i]))
          
      print("S = {}, k = {}, V = {}".format(S, k, V))
      #Test AlgoRec(s,i,v)
      print("Nombre de bocaux minimum en utilisant l'algorithme {} est : {}".format(1,AlgoRec(S,k,V)))
      
      #Test AlgoDyn(s,i,v)
      print("Nombre de bocaux minimum en utilisant l'algorithme {} est : {}".format(2,AlgoDyn(S,k,V)))
        
      #Test AlgoGlouton(s,i,v)
      print("Nombre de bocaux minimum en utilisant l'algorithme {} est : {}".format(3,AlgoGlouton(S,k,V)))
      
main("entree.txt")