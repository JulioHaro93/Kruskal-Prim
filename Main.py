import graphs as grafo
from queue import Queue as que
from graphs import Grafo as Grafo
from dijkstra import dijkstra as dk
from kruskalPrim import KruskalPrim as pk
import random 

grafo = Grafo()
        
grafoMalla30 = grafo.grafoBarabasiAlbert(500,2)
for arista in grafoMalla30.aristas:
    arista.distancia = random.randint(0,100)
krusk = pk.kruskal(grafoMalla30)

grafo.generaGephi(krusk[0], "K-Grande")
print("________________________________________")
kruski = pk.kruskalInv(grafoMalla30)
grafo.generaGephi(kruski[0], "KI-Grande")
print("________________________________________")
prim = pk.prim(grafoMalla30)
#print(prim)
grafo.generaGephi(prim[0],"prim-Grande")