# Algoritmo ricorsivo
#
def Algo(A, p, s):
	if s <= p +1:
		return 0
	else
		q = Zl(A, p, s)
		r = Zr(A, p, s)
		a = Algo(A, p, q)
		a = a - Algo(A, q, r)
		a = a + Algo(A, r, s)
		return a + (r - q)

# Algoritmo Iterativo
def AlgoIterative(A, p, s):
    cS = s; stS = stQ = stR = NULL
    last = NULL; start = True; ret = NULL
    while start or stS != empty:
        if start:
            if cS <= p + 1:
                ret = 0
                last = cS
                start = False
            else:
                cQ = Zl(A, p, cS)
                cR = ZZr(A, p, cS)
                push(cQ, stQ); push(cS, stS); push(cR, stR)
                cS = cQ
        else:
            cS = top(stS);cQ = top(stQ); cR = top(stR)
            if last == cQ:
                if cS <= p + 1:
                    pop(stS); pop(stQ)
                    a = ret
                    last = cS
                    ret = a + (r - q)
                else:
                    push(cQ, stQ); push(cS, stS); push(cR, stR)
                    p = cQ; cS = cR
                    start = True
            elif last == cR:
                if cS <= p + 1:
                    pop(stR); pop(stQ)
                    a = a - ret
                    last = cS
                    ret = a + (r - q)
                else:
                    push(cR , stR); push(cS, stS)
                    p = cR;
                    start = True
            else:
                pop(stR); pop(stS)
                a = a + ret
                last = cS
                ret = a + (r - q)
    return ret


                
