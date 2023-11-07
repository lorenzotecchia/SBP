## Versione Ricorsiva
def Algo(A, p, r, L):
    x = L
    if p <= r:
        q = (p + r) / 2 
        L_1 = AllocaNodo()
        L_1 -> key = A[q]
        if A[q] % 2 == 0:
            L_1 -> next = Algo(A, q+1, r, L)
            x = Algo(A, p, q-1, r, L_1)
        else:
            L_1 -> next = Algo(A, q - 1, r, L)
            x = Algo(A, q + 1, r, L_1)
    return x


## versione Iterativa
def Algo_Iterative(A, p, r, L):
    cP = p; cR = r;cL = L
    stR = stP = stL_1= NULL
    last = NULL
    start = True
    while start or stR != NULL:
        if start:
            x = L
            if cP <= cR:
                q = (cP + cR) / 2
                L_1 = AllocaNodo()
                L_1 -> key = A[q]
                push(cP, stP); push(r, stR); push(L_1, stL_1)
                if A[q] % 2 == 0:
                    cP = q + 1
                else:
                    cP = q - 1
            else:
                start = False
                last = cR
                ret = x
        else:
            cP = top(stP); cR = top(stR); L_1 = top(stL_1)
            q = (cP + cR) / 2
            if A[q] % 2 == 0:
                if last != cR:
                    x = ret
                    last = cR
                    start = False
                    pop(stP); pop(stR); pop(stL_1)
                else:
                    L_1 -> next = ret
                    cR = q - 1
                    cL = L_1
                    start = True
            else:
                if last != cR:
                    L_1 -> next = ret
                    cP = q + 1
                    cL = L_1
                    start = True
                else:
                    x = ret; last = cR
                    start = False
                    pop(stP); pop(stR); pop(stL_1)
    return x
