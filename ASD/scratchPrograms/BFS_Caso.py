# BFS
def BFS(G , v):
    Init(G)
    Q = Enqueue(Q, v)
    color[v] = G
    while Q != Empty:
        (Q, v) = Head&Dequeue(Q)
        for w in Adj[v]:
            if color[w] == B:
                Enqueue(Q, w)
                color[w] = G
        color[v] == N

def Init(G, color):
    for v in V:
        color[v] = B



