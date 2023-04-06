""" 
	La premiere ligne d'un fichier truck.x.in contient le nombre de modèle de trucks différents
	la deuxieme ligne contient des couples puissance,couts 
	La compagnie de transport possède un budget fixe B = 25 · 10^9 pour acheter des camions et souhaite
	savoir quels camions acheter pour maximiser le profit obtenu 
	
"""
from graph import Graph, graph_from_file, kruskal
from itertools import combinations
data_path = "C:/Users/Bilal/Documents/ENSAE/Projet Programmation/ensae-prog23/tests/input/"

# Fonction lecture de fichiers

def routes_to_trajets(x):
    with open(data_path + f"routes.{x}.in", 'r') as file:
        routes = file.readlines()
        nb_trajets = int(routes[0])

    # on va stocker les trajets de la forme (src,dest,utility)
    trajets =  [list(map(int,line.split(' '))) for line in routes[1:]]
    return trajets

	
def trucks_from_file(x):
	with open(data_path + f"truck.{x}.in", "r") as file:
		lines = file.readlines()
		nb_trucks = lines[0].strip().split(' ')[0]
	
	trucks =  [list(map(int,line.strip().split(' '))) for line in lines[1:]]
	return nb_trucks,trucks


"""Le problème est le suivant : on dispose d’un catalogue de camions, où chaque camion a une puissance p
et un coût c. On suppose que chaque modèle de camion est en stock illimité. Pour chaque camion acheté,
on peut l’affecter à un trajet au maximum, et on obtient le profit du trajet (à condition bien-sûr que la
puissance du camion soit suffisante pour couvrir le trajet). Par contre, on ne peut pas gagner plus de
profit en affectant plusieurs camions à un trajet donné.
La compagnie de transport possède un budget fixe B = 25 · 109 pour acheter des camions et souhaite
savoir quels camions acheter pour maximiser le profit obtenu.
Pour les tests, on donne plusieurs catalogues de camions dans les fichiers trucks.x.in, qui ont la
structure suivante :
— la première ligne est composée d’un entier correspondant au nombre de modèles de camions disponibles dans le catalogue ;
— les lignes suivantes représentent chacune un camion et sont composées de 2 entiers : la puissance et
le coût du camion.
Chacun des catalogues peut être utilisé pour tous les fichiers des précédentes séances network.x.in (et
les routes.x.in associés)"""

""" Chaque trajet dans la liste trajets est de la forme (source,destination,utilité) l'objectif 
est de maximiser la somme des utilités que pourra parcourir notre collection de camion sous la contrainte du budget B 
(il se peut qu'on ne puisse donc pas affecter un camion pour tous les trajets)"""


def minimal_truck_costing(G, trajet, trucks):
	(src,dest,utility) = trajet
	min_pow = G.min_power_kruskal(src,dest)[1]
	
	acceptable = []
	for [power,cost] in trucks:
		if power >= min_pow:
			acceptable.append([power,cost])
	
	power_mtc,cost_mtc = min(acceptable, key = lambda x : x[-1])
	
	return utility,cost_mtc
	
def list_of_mtc(x,t):
	G = graph_from_file(data_path + f"network.{x}.in")
	nb_trucks,trucks = trucks_from_file(t)
	trajets = routes_to_trajets(x)
	allocations = []
	for trajet in trajets:
		mtc = minimal_truck_costing(G,trajet,trucks) 
		allocations.append(( trajet , mtc))
		
	return allocations
	
def total_utility_cost(allocations):
	u,c = (0,0)
	
	for ( trajet, mtc ) in allocations:
		utility,cost = mtc
		u+=utility
		c+=cost
		
	return u,c
	
# La fonction suivante calcule le nombre maximal de trajet possible
# sous la contrainte d'un budget B, elle range les trajets dans l'ordre croissant de leur cout minimal
# puis elle les affecte au camion le moins cher possible pour autant de trajet que possible

def nombre_maximal_trajet(B, allocations):
	allocations.sort(key = lambda x : x[1][1])
	
	nb_trajet = 0
	for (trajet,mtc) in allocations:
		cost = mtc[1]
		if B >= cost:
			nb_trajet += 1
			B -= cost
		else:
			break
			
	return nb_trajet

# La fonction suivante calcule le profit maximal que l'on peut obtenir en affectant les camions

def allocation_optimale(B,x,t):
	allocations = list_of_mtc(x,t)
	nb_trajet = nombre_maximal_trajet(B,allocations)
	utility_max = 0
	alloc_opt = None
	for k in range(nb_trajet+1):
		for alloc in combinations(allocations,k): # on prend les k trajets parmi les allocations
			utility,cost = total_utility_cost(alloc)
			if utility > utility_max and cost <= B:
				utility_max = utility
				alloc_opt = alloc
	
	return total_utility_cost(alloc_opt),alloc_opt

"""La version précedente est trop lente pour les tests, on va donc utiliser un algorithme glouton"""

# La premiere idée est de trier les trajets par ordre décroissant du rapport utilité/cout et de couvrir les n trajets les plus rentables avec n le plus grand possible compte tenu de la contrainte budgétaire

def allocation_gloutonne(B,x,t):
	allocations = list_of_mtc(x,t)
	allocations.sort(key = lambda x : x[1][0]/x[1][1], reverse = True)
	
	if allocations == None:
		raise ValueError("Aucune allocation possible")

	alloc_opt = []
	cost = 0

	while cost < B:
		alloc_opt.append(allocations.pop(0))
		cost += alloc_opt[-1][1][1]
		if allocations == []:
			break

	if cost > B:
		cost -= alloc_opt[-1][1][1]
		alloc_opt.pop()

	return total_utility_cost(alloc_opt),alloc_opt

# Fonction qui décrit précisément l'allocation trouvée ainsi que le profit maximal et le cout total

def describe_allocation(x,t,B):
	(utility,cost),alloc_opt = allocation_gloutonne(B,x,t)
	print(f"Pour le réseau {x} et le catalogue {t} avec un budget de {B} \n le profit maximal est de {utility} et le cout total est de {cost}")
	print(f"L'allocation optimale est la suivante : { alloc_opt } ")
	print(f"Le nombre de trajets couverts est : { len(alloc_opt) }")
	# Donne les différents camions utilisés 
	camions = set()
	for (trajet,(u,c)) in alloc_opt:
		camions.add(c)
	print(f"Les camions utilisés sont ceux coûtants : {camions}")