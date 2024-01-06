def Algo(T, p, k, visited):
    if T == NULL:
        return visited
    else:
        pos = 1 + Algo(T->sx, T, k , visited)
        visited = Algo(T->dx,T, k , pos)
        if pos % k == 0:
            if p->sx == T:
                p->sx = RimuoviNodo(T):
            else:
                p->dx = RimuoviNodo(T):
    return visited

def AlgoIterative(T, p, k, visited):
    cT = T; cP = p; cVisited = visited;
    start = True; last = NULL; stT = stP = NULL;
    while stT != NULL or start:
        if start:
            if cT != NULL:
                push(cT, stT); push(cP, stP) # manca p
                cP = cT; cT = cT -> sx
            else:
                start = False; last = cT# deve essere last = cT 

# p da mettere sullo stack 
# T da utilizzare per capire quale chiamata
