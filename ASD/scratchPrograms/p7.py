# Sia dato un grafo orientato G, rappresentato con liste d'adiacenza, un array A
# di dimensione k \leq |V|, tale che A[i] \in V per ogni i \in 1, ..., k
# e un vertice v \in V. Si scriva un algoritmo che dati in ingresso i parametri
# G, A e v, colcoli in tempo lineare sulla dimensione del grafo l'insisme di vertici Z
# \subseteq V contenente il massimo insieme di vertici di G che soddisfano la seguente
# condizione:
# - z \in Z se e solo se in G esiste un percorso da z a v che, pria di raggiungere v,
# pass per alemno un vertice di a
#

def Algo(G, A, v):
    Init(G, color1, color2)
    G_t = Transpos(G)
    color1 = DFS_Visit(G_t, v)
    for a in A:
        if color1[a] == N:
            color2 = DFS_Visit(G_t, a)
    for v in V:
        if color2[v] == N:
            Z.append(v)
    return Z
