# Si scriva un algoritmo che dati un grafo G = {V, E} e due vertici s,u appartenenti a V verifichi in tempo lineare sulla dimensione del grafo se tutti i 
# percorsi infiniti che partono da s non passano infinite volte per u
#
# Esiste un percorso infinito quindi ciclico che parte da s e passa per u
#
def Algo(G, s , u):
    Init(G)
    S = DFS(G)
    G_t = Transpose(G)
    scc, color =  DFS_scc(G_t, S)
    if scc[s] == scc[u]:
        return False
    return True

def DFS1(G):
    Init(G, color)
    stackRET = NULL
    for v in V:
        if color[v] == B:
            stackRET = DFS1_Visit(G, v, stackRET)
    return stackRET

def DFS1_Visit(G, v, stackRET):
    color[v] = G
    for w in Adj[v]:
        if color[w] == B:
            stackRET = DFS_1Visit(G, w, stackRET)
    color[v] = N
    push(v, stackRET)
    return 

def Transpose(G):
    Init(G_t)
    G_t.V = G.V
    for v in V:
        for w in Adj[w]:
            E_t = Insert(E_t, (w,v))
    return G_t

def DFS_scc(G, S):
    (color, scc) = Init(G):
    while S != empty:
        (S, v) = Top&Pop(S)
        if color[v] == B:
            (c, scc) = DFS_scc_visit(G, color, scc, v, v)
    return scc, color

def DFS_scc_visit(G, color, scc, v, w):
    color[w] = G
    scc[w] = v
    for z in Adj[w]:
        if color[z] == B:
            (color, scc) = DFS_scc_visit(G, color, scc, v, z)
    color[w] = N
    return color, scc
