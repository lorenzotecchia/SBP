def Algo(T, P, k, visited):
    if T == NULL:
		return visited
    else:
		pos = 1 + Algo(T->sx, T, k, visited)
		visited = Algo(T->dx, T, k, pos)
        if pos % k == 0:
            if P->sx == T:
				P->sx = RimuoviNodo(T)
            else:
				P->dx = RimuoviNodo(T)
	    return visited

#
#
def AlgoIterative(T, P, k, visited):
    cT = T; cP = P
    stT = stP = stPos = NULL; start = True
    last = NULL; ret = NULL
    while start or stT != empty:
        if start:
            if cT == NULL:
                ret = visited
                last = cT
                start = False
            else:
                push(cT, stT); push(cP, stP);
                cP = cT; cT = cT -> sx;
        else:
            cT = top(stT); cP = top(stP);
            if last == cT -> sx: #ritorno da riga 4
                pos = 1 + ret
                if cT -> dx == NULL: # se non ho da fare la chiamata a riga 5 
                    if pos % k == 0:
                        if cP -> sx == cT:
                            cP -> sx = RimuoviNodo(cT)
                        else:
                            cP -> dx = RimuoviNodo(cT)
                    ret = visited
                    pop(stT); pop(stP); pop(stPos) #### Da controllare
                    last = cT
                else: # se ho da fare la chimata a riga 5
                     push(pos, stPos)
                    cP = cT; cT = cT -> dx; visited = pos
                    start = True
            else:# sto ritornando dalla chiamata a riga 5
                visited = ret
                if pos % k == 0:
                    if cP -> sx == cT:
                        cP -> sx = RimuoviNodo(cT)
                    else:
                        cP -> dx = RimuoviNodo(cT)
                ret = visited
                pop(stT); pop(stP); pop(stPos) #### Da controllare
                last = cT
    return ret
