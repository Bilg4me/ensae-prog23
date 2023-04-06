## Imports
from perf_test import choices, timing, mean
from trucks import *

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


## Test des fonctions d'allocation de camions
x = 1
t = 2
B = 10000

# Comparaison des deux méthodes en temps d'exécution
def compare_allocation(x,t,B):
    print(f"Allocation gloutonne pour network.{x} avec truck.{t} et {B} euros : {timing(allocation_gloutonne,B,x,t)} secondes")
    print(f"Allocation optimale pour network.{x} avec truck.{t} et {B} euros : {timing(allocation_optimale,B,x,t)} secondes")

# Test de la méthode gloutonne sur différents inputs
# X = [1]
# T = [0,1,2]
# B = [100000,200000,300000,400000,500000, 600000, 700000, 800000, 900000, 1000000]

# for x in X:
#     for t in T:
#         for b in B:
#             describe_allocation(x,t,b)

describe_allocation(x,t,B)