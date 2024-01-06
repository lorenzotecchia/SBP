def DFS(G, v):
    (c,p) = Init(G)
    t = 0
    for v in V:
        if c(v) == bn:
            (c, p, d, f, t) = DFSVisit(G, v, c, p, d, f , t):
    return (c, d , f , p)

def DFSVisit(G, v, c, p, d , f , t):
    c(v) = gr
    d(v) t
    t = t + 1
    for w in Adj[w]:
        if c(w) = bn:
            p(w) = v
            (c, p, d, f, t) = DFSVisit(G, w , c, p, d, f, t):
    c(w) = nr; f(v) = t; t = t+1
    return (c, p , d, f, t)
    
