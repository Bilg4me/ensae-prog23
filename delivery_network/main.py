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

# Fonction lecture de fichier

def routes_to_trajets(x):
    with open(data_path + "routes.{}.in".format(x), 'r') as file:
        routes = file.readlines()
        nb_trajets = int(routes[0])

    # on va stocker les trajets de la forme (src,dest,utility)
    trajets =  [list(map(int,line.split(' '))) for line in routes[1:]]
    return trajets

## Initialisation
data_path = "c:/Users/Bilal/Documents/ENSAE/Projet Programmation/ensae-prog23/tests/input/"
file_name = "network.2.in"
G = graph_from_file(data_path + file_name)
print(G)
# Ouverture de network.2.in -> 82s environ !!!

## Quelques test

#print("temps d'execution pour ouvrir " + file_name + " : " + str(timing(graph_from_file, data_path+file_name)))
#print("temps d'execution pour lire " + file_name + " : " + str(timing(routes_to_trajets, 2)))

# print("temps d'execution pour visualiser le graphe " + file_name + " : " + str(timing(G.visualization)))
# print("temps d'execution pour obtenir le plus court chemin de 1 vers 6 avec puissance de 1000 sur " + file_name + " : " + str(timing(G.get_path_with_power, 1,6,1000)))
# print("temps d'execution pour obtenir la puissance minimal pour aller de 1 vers 6 sur " + file_name + " : " + str(timing(G.min_power, 1,6)))
# print("temps d'execution pour obtenir le plus court chemin de 1 vers 6 (avec kruskal) sur " + file_name + " : " + str(timing(G.min_power_kruskal, 1,6)))
# print("temps d'execution pour kruskal le graphe " + file_name + " : " + str(timing(kruskal,G)))
# print("temps d'execution pour obtenir le plus court chemin de 1 vers 6 avec puissance de 1000 (avec kruskal) sur " + file_name + " : " + str(timing(A.get_path_with_power, 1,6,1000)))

def output_routes(x):

    ## Lecture du graphe
    file_name = "network.{}.in".format(x)
    G = graph_from_file(data_path + file_name)

    ## Ouverture du fichier routes.x.in

    with open(data_path + "routes.{}.in".format(x), 'r') as file:
        routes = file.readlines()
        nb_trajets = int(routes[0])

    # on va stocker les trajets de la forme (src,dest,utility) en ne prenant que k trajets

    trajets =  [list(map(int,line.split(' '))) for line in choices(routes[1:], k=50)]

    #perf_trajets_gpwp = [timing(G.get_path_with_power,src,dest,utility) for (src,dest,utility) in trajets]
    perf_trajets_mp = [timing(G.min_power,src,dest) for (src,dest,utility) in trajets]


    #print("temps d'execution moyen de get_path_with_power sur network.{}:".format(x), mean(perf_trajets_gpwp))
    print("temps d'execution moyen de min_power sur network.{}:".format(x) , mean(perf_trajets_mp))

    ## Création du fichier routes.x.out
    tous_les_trajets = [list(map(int,line.split(' '))) for line in routes[1:]]
    with open(data_path + "output/routes.{}.out".format(x), 'w') as file:
        text_lines = [ str(G.min_power_kruskal(src,dest)[1]) + "\n" for (src,dest,utility) in tous_les_trajets] 
        file.writelines(text_lines)

