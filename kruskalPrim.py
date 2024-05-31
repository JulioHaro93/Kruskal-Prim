from queuePrioridades import Queue as priority
from queuePrioridades import priorityMax as max
import random
from graphs import Grafo as Grafo
from queue import PriorityQueue
from dfs import dfs_r as dfs


class KruskalPrim:
    def __init__(self) -> None:
        pass
    def kruskal(grafo):
        grafoNuevo = priority.heapMinimum(grafo)
        grafito = Grafo()
        MST =0
        while not grafoNuevo.empty():
            nueva = grafoNuevo.get()
            for arista in grafo.aristas:
                if arista.origen == nueva[1].destino:
                    MST += nueva[0]
                    grafito.agregarArista(arista.origen, nueva[1].destino)
                    #print(str(arista)+"\nblahblahblah")
                    #print(nueva)
        #print(MST)
        return grafito, MST
    
    def kruskalInv(grafo):
        MST=0
        grafito = Grafo()
        maxim = max()
        for arista in grafo.aristas:
            maxim.push(arista, arista.distancia)
        
        while not maxim.empty():
            nueva = maxim.pop()
            #print(nueva.distancia)
            for arista in grafo.aristas:
                if arista.origen == nueva.destino:
                    #print(nueva)
                    MST += arista.distancia
                    grafito.agregarArista(arista.origen, nueva.destino)
        result = [x for x in grafo.aristas if x not in grafito.aristas]
        for arista in result:
            pass
        print(MST)
        return grafito, MST
    
    from queue import PriorityQueue

    def prim(grafo):
        MST = 0
        q = PriorityQueue()
        grafillo = Grafo()
        
        nodoInicial= grafo.obtenerNodoArbitrario(len(grafo.aristas)-1)
        nodito = grafo.aristas[nodoInicial].origen.visited = True
        
        for arista in grafo.aristas:
            #print(arista)
            if arista.origen == nodito:
                q.put(arista)
        print(grafo.aristas)
        while not q.empty():
            arista = q.get()
            if not arista.destino.visited:
                arista.destino.visited = True
                grafillo.agregarArista(arista.origen, arista.destino)
                MST += arista.distancia
                for nueva_arista in arista.destino.aristas:
                    if not nueva_arista.destino.visited:
                        q.put(nueva_arista)
        return grafillo, MST
