## Imports
from graph import Graph, graph_from_file, kruskal
from time import perf_counter
from numpy import mean
from random import choices


## Fonction de test des performances
def timing(f, *args):
    t1 = perf_counter()
    f(*args)
    t2 = perf_counter()
    return t2-t1


# Initialisation
data_path = "C:/Users/Bilal/Documents/ENSAE/Projet Programmation/ensae-prog23/tests/input/"
file_name = "network.1.in"
G = graph_from_file(data_path + file_name)
print(G)

# Ouverture de network.2.in -> 82s environ !!! Nous n'avons pas réussi à résoudre ce problème qui nous a handicapé pendant tout le projet

# Quelques test

print("temps d'execution pour ouvrir " + file_name + " : " + str(timing(graph_from_file, data_path+file_name)))
print("temps d'execution pour lire " + file_name + " : " + str(timing(routes_to_trajets, 2)))

print("temps d'execution pour visualiser le graphe " + file_name + " : " + str(timing(G.visualization)))
print("temps d'execution pour obtenir le plus court chemin de 1 vers 6 avec puissance de 1000 sur " + file_name + " : " + str(timing(G.get_path_with_power, 1,6,1000)))
print("temps d'execution pour obtenir la puissance minimal pour aller de 1 vers 6 sur " + file_name + " : " + str(timing(G.min_power, 1,6)))
print("temps d'execution pour obtenir le plus court chemin de 1 vers 6 (avec kruskal) sur " + file_name + " : " + str(timing(G.min_power_kruskal, 1,6)))
print("temps d'execution pour kruskal le graphe " + file_name + " : " + str(timing(kruskal,G)))
print("temps d'execution pour obtenir le plus court chemin de 1 vers 6 avec puissance de 1000 (avec kruskal) sur " + file_name + " : " + str(timing(A.get_path_with_power, 1,6,1000)))
