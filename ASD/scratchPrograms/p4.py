## Algoritmo ricorsivo

def Algoritmo(T,h):
    if T == NULL:
       return Z(0, h)
    else:
        a = 0
        if T -> key % 2 == 0:
            a = a + Algoritmo(T->dx, 2h)
        if T->key % 3 == 1:
            a = a - Algoritmo(T->sx, 3h)
    return Z(T->key, a)

## Algoritmo iterativo

def AlgoIterativo(T, h):
    cT = T;cH = h; stA = stT = NULL
    start = True
    while start or stT != NULL:
        if start:
            if cT == NULL:
                ret = Z(0, h)
            else:
                a = 0
                if cT -> key % 2 == 0:
                    push(cT, stT); push(a, stA)
                    cT = cT -> dx; cH = cH * 2
                if cT -> key % 3 == 1:
                    push(cT, stT); push(a, stA)
                    cT = cT -> sx; cH = cH * 3
                ret = Z(cT -> key, a)
                start = False
                last = cT
        else:
            cT = Top(stT)
            if cT -> key % 2 == 0:
                pop(stT); pop(stA)
                last = cT
            if cT -> key % 3 == 1:
                pop(stT); pop(stA)
                last = cT
            if last = cT -> sx:
                a = a - ret
                start = True
            else:
                a = a - ret
                start = True
    return ret
