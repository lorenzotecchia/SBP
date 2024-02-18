# Si scriva un algoritmo ricorsivo che, presi in ingresso un albero binario  contenente dati interi e un intero
# positivo , restituisca il valore della massima profondità dei nodi con valore di chiave multiplo di .
# Nel caso l'insieme di tali nodi fosse vuoto, è richiesta la restituzione del valore di default -1.
# L'algoritmo dovrà essere efficiente e non far uso né di variabili globali né di parametri passati per riferimento.
# Infine, si scriva un algoritmo iterativo che simuli precisamente l'algoritmo ricorsivo di cui sopra.

# Algoritmo Ricorsivo
def Algo(T, k, h):
    Depth[] = NULL
    if T != NULL:
        h = Algo(T -> sx, k, h + 1)
        h = h + Algo(T -> dx, k, h + 1)
        if T -> key % k == 0:
            Depth.Append(h)
   return MAX(Depth)


def Algorithm(T , k, h):
    Algo(T, k, 0)

;

def MAX(A):
    if A.isempty == TRUE:
        return -1
    else:
        max_element = A[0]
        for i in A:
            if max_element <= A[i]:
                max_element = A[i]
        return max_element

# Algorimto Iterativo che simula quello Ricorsivo
def AlgoIterative(T, k, h):
    cT = T; cH = H
    stT = stH = NULL
    start = True; last = NULL
    while start or stT != NULL:
        if start:
            Depth[] = NULL
            if cT != NULL:
                push(cT , stT); push(cH, stH)
                cT = cT -> sx; cH = cH + 1
            start = False
            last = cT
        else: # start = False
            cT = top(stT); cH = top(stH)
            if last == cT -> sx: # sto tornando da riga 11
                if cT -> dx == NULL: # chiamata a riga 12 da non fare
                    cH = ret
                    last = cT
                    pop(stT); pop(stH)
                else: # chiamata a riga 12 da fare
                    push(cT, stT); push(cH, stH)
                    cT = cT -> dx; cH = cH + 1
                    start = True
            else: # sto tornando da riga 12
                cH = cH + ret
                pop(stT); pop(stH)
                last = cT
                if cT -> key % k == 0:
                    Depth.append(h)
                ret = Max(Depth)
    return ret

