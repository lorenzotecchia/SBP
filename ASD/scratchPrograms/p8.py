# Algoritmo Ricorsivo
def Algo(T, h , k):
    ret = 0
    if T != NULL && h > 0:
        if T -> key < k:
            ret = Algo(T -> dx, h - 2, k)
        else:
            if T -> key % 2 == 0:
                ret = 1
            x = ret + Algo(T -> sx, h/2, k)
            ret = x + Algo(T -> dx, h -1, k)
    return ret

# Algoritmo Iterativo
def Algo(T, h, k):
    cT = T; cH = h; start = True
    stT = stH =stRet = NULL
    while start or stT != NULL:
        if start:
            ret = 0
            if cT != NULL && cH > 0:
                if cT -> key < k:
                    push(cT, stT); push(cH, stH); push(ret, stRet)
                    cT = cT -> dx; cH = cH - 2
                else:
                    if cT -> key % 2 == 0:
                        ret = 1
                    push(cT, stT); push(cH, stH); push(ret, stRet)
                    cT = cT -> sx; cH = cH / 2
            else:
                start = False
                last = cT
        else:
            cT = top(stT); ret = top(stRet); cH = top(stH)
            if cT -> key < k:
                pop(stT); pop(stH)
                ret = acc
                last = cT
            else:
                if cT -> key % 2 == 0:
                    ret = 1
                if last == cT -> sx:
                    if cT -> dx == NULL:
                        x = ret + acc
                        pop(stT); pop(stH); pop(stRet)
                        last = cT
                    else:
                        push(stT); push(stH); push(stRet)
                        cT = cT -> dx; cH = cH - 1
                        start = True
                else:
                    ret = x + acc
                    pop(stT); pop(stH); pop(stRet)
                    last = cT
    return ret

# Esercizio 3
# Idea: verificare che non esiste un percorso
def Algo(G, V1, V2):
    Init(G, color) # coloriamo tutti i nodi a bianco tranne i colori di V2 a nero
    acyclic = Acycli(G)
    return acyclic

def Acyclic(G):
    for v in V1:
        if color[v] == B:
            acyclic = DFS_Acyclic(G, v)
            if !acyclic:
                return False
    return True


def DFS_Acyclic(G, v):
    color[v] = G
    for w in Adj[v]:
        if color[w] == B:
            acyclic = DFS_Acyclic(G , w):
            if !acyclic:
                color[v] = N
                return False
        else if color[w] == G:
            return False
    color[v] = N
    return True
