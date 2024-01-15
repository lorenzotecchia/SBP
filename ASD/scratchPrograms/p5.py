# Sia dato un grafo orientato  G, rappresentato con liste di adiacenz, e un vertice s
# e due insiemi di verrtici B subseteq V e C subseteq V, rappresentati come array.
# Si scriva un algoritmo che, dati in ingresso G, s, B, C, collezioni in tempo lineare
# sulla dimensione di G in una lista L tutti i vertici v che soddisfano  entrambe
# le seguenti condizioni:
# - v appartiene a B e può raggiungere s tramite un percorso
# - esiste anche un percorso da s a v che non passa per alcun vertice di C

def Algo(G, s, B, C):
    Init(G, color)
    G_t = Transpose(G)
    color = BFS(G_t, s)
    for b in B:
        if color[b] == N:
            for c in C:
                if color[c] != N:
                    return True
    return False

def Transpose(G):
    G_t.V = G.V
    for v in G.V:
        for w in Adj[v]:
            E_t = Insert(E_t, (w, v))
    return G_t

def BFS(G, v):
    color[v] = G
    Q = Enqueue(Q, v)
    while Q != NULL:
        (Q,v) = Head&Dequeue(Q)
        for u in Adj[v]:
            if color[u] == B:
                Q = Enqueue(u)
                color[u] = G
        color[v] = N
    return color
