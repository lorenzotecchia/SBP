## Algoritmo Ricorsivo
def Algo(T, k):
    ret = NULL
    if T != NULL:
        if T->key > k:
            b = T
            ret = BEST(Algo(T->sx, k), b, k)
        elif T->key < k:
            a = T
            ret = BEST(a, Algo(T->dx, k), k)
        else:
            a = Algo(T->sx, k)
            b = Algo(T->dx, k)
            ret = BEST(a, b, k)
    return ret


## Algoritmo Iterativo
def AlgoIterative(T,k):
    cT = T; 
    stT = stA = NULL; start = True
    while start or stT != NULL:
        if start:
            ret = NULL
            if cT != NULL:
                    push(cT, stT)
                if cT -> key > k:
                    # b = T
                    cT = cT -> sx
                elif cT->key < k:
                    # a = T
                    cT = cT -> dx
                else:
                   cT = cT -> sx
            else:
                start = False
                last = cT
        else:
            cT = top(stT)
            if cT -> key > k:
                ret = BEST(ret, cT, k)
                top(stT)
                last = cT
            elif cT -> key < k:
                ret = BEST(cT, ret, k)
                top(stT)
                last = cT
            else:
                if last == cT -> sx:
                    if cT -> dx == NULL:
                        BEST(ret, NULL, k)
                        pop(stT)
                        last = cT
                    else:
                        a = ret
                        push(a, stA)
                        cT = cT -> dx
                        start = True
                else:
                    a = top(stA)
                    ret = BEST(a, ret, k)
                    pop(stT); pop(stA)
                    last = cT
    return ret

