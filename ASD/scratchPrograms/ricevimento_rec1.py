# Algoritmo Ricorsivo
#
def Algo(T, h):
    if T == NULL:
        return Z(0, h)
    else:
        a = 0
        if T -> key % 2 == 0:
            a = a + Algo(T -> dx, 2 * h)
        if T -> key % 3 == 1:
            a = a - Algo(T -> sx, 3 * h)
    return Z(T -> key, a)

# Algoritmo Iterativo
def Algoritmo(T, h):
    cT = T; cH = h
    stT = stH = stA = NULL; start = True
    while start or stT !empty:
        if start:
            if cT == NULL:
                ret = Z(0,h)
                last = cT
                start = False
            else:
                a = 0
                if cT -> key % 2 == 0:
                    push(cT, stT); push(cH, stH); push(a, stA)
                    cT = cT -> dx; cH = cH * 2
                if cT -> key % 3 == 1:
                    push(cT, stT); push(cH, stH); push(a, stA)
                    cT = cT -> sxM cH = cH * 3
        else:
            cT = top(stT); cH = top(stH); a = top(stA)
            if cT -> key % 2 == 0:
                if last == cT -> dx:
                    a = a + ret
                    pop(stT); pop(stH); pop(stA)
                    last = cT
                else:
                    a = a - ret
                    pop(stT); pop(stH); pop(stA)
                    last = cT
            if cT -> key % 3 == 1:
                if last == cT -> dx:
                    a = a + ret
                    pop(stT); pop(stH); pop(stA)
                    last = cT
                else:
                    a = a - ret
                    pop(stT); pop(stH); pop(stA)
                    last = cT
            ret = Z(cT -> key, a)
    return ret
