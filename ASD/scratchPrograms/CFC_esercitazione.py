# per il cacolo delle componenti fortemente connesse bisonga:
# 1. Eseguire l'ordinamento topologico in profondita
# 2. Calcolare il trasposto di G
# 3. Eseguire un DFS leggermente modificata G^T e sullo stack S restituito dall'ordinamento 
#    topologico

def SCC(G):
    S = TopologicalOrdering(G)
    G_T = Transpose(G)
    scc = DFS_SCC(G_T, s)
    return scc

def TopologicalOrdering(G):
    c = Init(G)
    for v in V:
        if c(v) == bn:
            s = DFSTopologicalOrdering(G, S, v, c)
    return S

def DFSTopologicalOrdering(G, S, v, c):
    c(v) = gr
    for w in Adj[v]:
        if c(v) == bn:
            DFSTopologicalOrdering(G, S, w, c)
    c(v) = nr
    s = Push(S, v)
    return S

def Transpose(G):
    Init(G_T)
    Vertix(G_T) = Vertix(G)
    for v in V:
        for w in Adj[w]:
            Edges(G_T) = Insert(Edges(G_T), (w,v))
    return (Vertix(G_T), Edges(G_T))

def DFS_SCC(G, S):
    (c, scc) = Init(G)
    while !empty(S):
        (S, v) = Top&Pop(S)
        if c(v) == bn:
            (c, scc) = DFS_SCC_Visit(G, c, scc, v, v)
    return scc

def DFS_SCC_Visit(G, c, scc, v , w):
    c(w) = gr
    scc(w) = v
    for z in Adj[w]:
        if c(z) == bn:
            (c, scc) = DFS_SCC_Visit(G, c, scc, v, z)
    c(w) = nr
    return (c, scc)
