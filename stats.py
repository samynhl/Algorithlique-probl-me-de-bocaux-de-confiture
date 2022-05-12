# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

with open("test.txt","r") as f:
    with open("n_comp.txt","r") as f1:
        lines = f.readlines()
        max_v = []
        avg_v = []
        for line in lines:  
            parts = line.split(",")
            max_v.append(int(parts[0][1:]))
            avg_v.append(round(float(parts[1][:len(parts[1])-2].strip()),2))
        lines = f1.readlines()
        """
        for i in range(len(lines)):
            print("maximum de l'écart pour le systeme {} : {}".format(lines[i],max_v[i]))
            print("moyenne de l'écart pour le systeme {} : {}".format(lines[i],avg_v[i]))
        """
        plt.hist(max_v)
        plt.title('Histogramme représentant les valeurs maximum des ecarts obtenus sur {} systèmes'.format(len(max_v)), fontsize=10)
        plt.savefig("maximum.png")
        plt.show()
        
        plt.hist(avg_v)
        plt.title('Histogramme représentant les valeurs moyennes des ecarts obtenus', fontsize=10)
        plt.savefig("average.png")
        plt.show()
        print(len(max_v))
        print(len(lines))
        print(np.median(max_v))
        print(np.median(avg_v))
        print(np.mean(max_v))
        print(np.mean(avg_v))