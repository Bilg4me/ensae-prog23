## Imports
from graph import Graph, graph_from_file
from time import perf_counter
from numpy import mean
from random import choices

## Initialisation
data_path = "c:/Users/Bilal/Documents/ENSAE/Projet Programmation/ensae-prog23/tests/input/"
file_name = "network.1.in"
G = graph_from_file(data_path + file_name)

## Fonction de test des performances
def timing(f, *args):
    t1 = perf_counter()
    f(*args)
    t2 = perf_counter()
    return t2-t1

## Quelques test

# timing(lambda x : graph_from_file(x), data_path+file_name)
# timing(G.visualization)
# timing(G.get_path_with_power, 1,6,1000)
# Ouverture de network.2.in -> 82s environ !!!

## Ouverture du fichier routes.1.in

with open(data_path + "routes.1.in", 'r') as file:
    routes = file.readlines()
    nb_trajets = int(routes[0])

# on va stocker les trajets de la formes (src,dest,utility) en ne prenant que 50 trajets

trajets =  [list(map(int,line.split(' '))) for line in choices(routes[1:], k=50)]

perf_trajets_gpwp = [timing(G.get_path_with_power,src,dest,utility) for (src,dest,utility) in trajets]
perf_trajets_mp = [timing(G.min_power,src,dest) for (src,dest,utility) in trajets]


print("temps d'execution moyen de get_path_with_power:", mean(perf_trajets_gpwp))
print("temps d'execution moyen de min_power:", mean(perf_trajets_mp))


#Résoudre le problème : ModuleNotFoundError: No module named 'graph' (Existe uniquement sur Vscode)