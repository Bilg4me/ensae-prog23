""" 
	La premiere ligne d'un fichier truck.x.in contient le nombre de modèle de trucks différents
	la deuxieme ligne contient des couples puissance,couts 
	La compagnie de transport possède un budget fixe B = 25 · 10^9 pour acheter des camions et souhaite
	savoir quels camions acheter pour maximiser le profit obtenu 
	
"""
from graph import Graph, graph_from_file, kruskal
data_path = "/home/brome/Documents/GitHub/ensae-prog23/tests/input/"

# Fonction lecture de fichier



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

def minimal_truck_costing(G, trajet, trucks):
	(src,dest,utility) = trajet
	min_pow = G.min_power_kruskal(src,dest)[1]
	
	acceptable = []
	for [power,cost] in trucks:
		if power >= min_pow:
			acceptable.append([power,cost])
	
	power_mtc,cost_mtc = min(acceptable, key = lambda x : x[-1])
	print(utility,cost_mtc)	
	if utility >= cost_mtc: # On couvre un trajet uniquement si le mtc augmente notre utilité
		return power_mtc,cost_mtc
		
	return None
	
def list_of_mtc(x):
	G = graph_from_file(data_path + f"network.{x}.in")
	nb_trucks,trucks = trucks_from_file(2)
	trajets = routes_to_trajets(x)
	allocations = []
	for trajet in trajets:
		mtc = minimal_truck_costing(G,trajet,trucks) 
		if mtc != None :
			allocations.append(( trajet , mtc))
		
	return allocations
	
def total_mtc_cost(allocations):
	c = 0
	
	for ( trajet, mtc ) in allocations:
		power,cost = mtc
		c += cost
		
	return c
	
	

