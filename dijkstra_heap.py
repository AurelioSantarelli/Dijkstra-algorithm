import math
import dijkstraTree
from heapq import heappop,heappush

#costo computazionale O((n+m)log(n))

#la funzione prende un grafo e un nodo sorgente(appartenente al grafo)
#il grafo è rappresentato come lista di adiacenze con ogni nodo il costo
def dijkstra(G, s):
    p = [-1] * len(G)           #inizializza lista padri a -1 ( se rimane -1 non raggiungibile)
    d = [math.inf] * len(G)     #inizializza lista costi a inf ( se rimane inf allora non raggiungibile)
    calcolato = [0] * len(G)    #inizializza lista calcolato a 0 ( se == 1 allora ci siamo stati)
    d[s] = 0                    #il costo per arrivare alla sorgente stessa è 0
    p[s] = "s"                    #il padre della sorgente è la sorgente stessa
    H = []                      #crea un heap

    #per ogni nodo adiacente ad s leggi il costo e...
    for y, costo in G[s]:
        #pushalo nel heap come(costo s->y,nodo in questione,sorgente)
        heappush(H,(costo,y,s))
        #debug
        #print(H)
    #itera finche l'heap non è vuota
    while (H):
        #pop dall'heap(il minimo costo s->y,y,padre di y)
        costo,x,padre = heappop(H)
        #debug
        #print(costo,x,padre)
        #se nella lista padre[x] == -1(significa che ancora non abbiamo modificato le liste p e d
        if(p[x] == -1):
            #aggiorna le liste padri e costi di x con rispettivi nodo padre e costo
            p[x] = padre
            d[x] = costo
            #per ogni nodo adicente ad x pusha nell'heap
            #la somma del costo per arrivare ad x + il costo per andare da x->y,
            #il nodo e il padre che sarà x
            for y, costo1 in G[x]:
                heappush(H,(d[x] + costo1,y,x))
    return d,p

#lista di adiacenze con ogni adiacenza associato il costo (nodo adiacente,costo)
G = [
        [(1, 17),(5, 4)],           #0
        [(0, 17),(4, 5),(5, 6)],    #1
        [(3, 12),(4, 10)],          #2
        [(2, 12),(4, 4),(5, 1)],    #3
        [(1, 5),(2, 10),(3, 4)],    #4
        [(0, 4),(1, 6),(3, 1)]      #5
    ]
sorgente =input("Inserisci nodo sorgente: ")
try:
    sorgente = int(sorgente)
except ValueError:
    print("Non hai inserito un numero intero valido.")

costi,padri = dijkstra(G,sorgente)
#print(f"I costi per arrivare ad ogni nodo partendo da {sorgente} sono: {costi}")
#print(f"La lista dei padri di ogni nodo partendo da {sorgente} sono: {padri}")
dijkstraTree.dijkstraTree_draw(padri,costi)