## Imports
from perf_test import choices, timing, mean
from trucks import *



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
#compare_allocation(x,t,B)
