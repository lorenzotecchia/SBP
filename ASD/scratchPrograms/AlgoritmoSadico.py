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
    stR = stQ = NULL
    last = NULL
    start = True
    while start or stR != NULL:

