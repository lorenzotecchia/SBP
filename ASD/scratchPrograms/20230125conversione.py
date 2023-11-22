def algoritmo(T, h):
	start = True
	cT = T; cH = h
	stT = stH = stA = NULL
	last = NULL
	while stT != NULL or start:
		a = 0
		if start:
			if cT = NULL:
				return Z(0, cH)
				start = False
			else:
			push(cT, stT); push(cH, stH)
				if cT -> key % 2 == 0:
					cT = cT -> dx; cH = cH * 2
				else:
					start = False
					ret = 0
		else: # != start
			cT = top(stT); cH = top(stH)
			if cT -> key != last:
				a = ret
				if cT -> key % 3 == 1:
					cT -> cT -> sx
					cH = cH * 3
					start = True
					stA = push(stA, a)
				else:
					stT = pop(stT)
					stH = pop(stH)
					ret = Z(cT->key, a)
					last = cT
			else:
				a = top(stA)
				a <- a - ret
				start = False
				ret = Z(cT->key, a)
				stT = pop(stT)
				stH = pop(stH)
				stA = pop(stA)
				last = cT
return ret 